# Manually managing iSCSI connections 

Most iscsi related operations are automaticbut there are situations where manual intervention is necessary. This guide describes how to retrieve iscsi credentials, login into targets, format drives, mount them etc.

## Retriving iscsi access credentials using the CLI

Typically drive arrays that are part of the same target as other drives that are mounted in the operating system automatically. However if you need to manually mount a drive use the following:

This is the LUN that you will need to mount:
```bash
$ metalcloud-cli drive-array get -id drive-array-45929 -show-credentials
Drive Array #45929 attached to instance array 35517 has the following drives:
+-------+-------------------------------+-----------+-----------+-----------+-------------------------------+--------------------------+--------------------------+-----------------------------------------------------------------------------------------------------+
| ID    | LABEL                         | STATUS    | SIZE (MB) | TYPE      | ATTACHED TO                   | TEMPLATE                 | DETAILS                  | CREDENTIALS                                                                                         |
+-------+-------------------------------+-----------+-----------+-----------+-------------------------------+--------------------------+--------------------------+-----------------------------------------------------------------------------------------------------+
| 71587 | drive-71587                   | active    | 40960     | iscsi_ssd | instance-56008                | CentOS 7.4(#78)          | CentOS  none             | Target: 100.96.0.12 Port:3260 IQN:iqn.2013-01.com.bigstep:storage.dd.6fjo87t.dd LUN ID:33 |
+-------+-------------------------------+-----------+-----------+-----------+-------------------------------+--------------------------+-----------------------
```
This are the initiator credentials. These should already be configured on the instance but if they are not use the following to retrieve them:
```bash
$ metalcloud-cli instance-array get -id workers -show-iscsi-credentials
Instances of instance array workers (#35516) of infrastructure complex-demo (#25524):
+-------+---------------------------+--------------+----------------+--------+----------------------------------------------------------------------------------------------------------------+
| ID    | SUBDOMAIN                 | WAN_IP       | DETAILS        | STATUS | ISCSI                                                                                                          |
+-------+---------------------------+--------------+----------------+--------+----------------------------------------------------------------------------------------------------------------+
| 56006 | instance-56006.bigstep.io | 84.40.60.226 | M.8.32 (#123)  | active | Initiator IQN: iqn.2019-03.com.bigstep.storage.instance-56006 Username: asdads Password: dd  |
| 56007 | instance-56007.bigstep.io | 84.40.60.227 | M.8.32 (#124)  | active | Initiator IQN: iqn.2019-03.com.bigstep.storage.instance-56007 Username: asd Password: dd  |
+-------+---------------------------+--------------+----------------+--------+----------------------------------------------------------------------------------------------------------------+
Total: 2 Instances
```

## Logging into the iSCSI target from Linux (CentOS/Redhat)

This process is operating system version but in general lines it requires a user to configure it's iscsi initiator (the server) and login into the target (the storage).

1. Install iscsi support

    ```bash
    yum install iscsi-initiator-utils
    ```

2. Set node.startup to automatic.

    ```bash
    vi /etc/iscsi/iscsid.conf

    [...]
    node.startup = automatic
    [...]
    ```

3. Start the iSCSI discovery

    ```bash
    iscsiadm -m discovery -t st -p 100.96.0.12
    iscsiadm -m node
    ```
4. Login the iSCSI target. Notice the .33 at the end of the IQN. That's the LUN ID from the drive array's credentials.

    ```bash
    iscsiadm -m node --targetname "iqn.2013-01.com.bigstep:storage.dd.6fjo87t.dd.33" --portal "100.96.0.12:3260" --login
    ```

5. Identifying the drive by looking at dmesg

    ```bash
    $ dmesg
    ```

5. Formatting & mounting the drive
The drive is now visible in the OS just like any other drive:

    ```bash
    $ mkfs.ext3 /dev/sdb1
    $ mount /dev/sdb1 /mnt
    $ ls -l
    ```

## Logging into a drive on Windows using PowerShell

1. Set iSCSI Initiator service to started and automatic
    ```bash
    Set-Service msiscsi -startuptype "automatic"
    Start-Service msiscsi
    ```

2. Check iSCSI Initiator Configuration Initiator Name
    ```bash
    (Get-WmiObject -Namespace root\wmi -Class MSiSCSIInitiator_MethodClass).iSCSINodeName
    ```

3. Set iSCSI Initiator Configuration Initiator Name.
    Note -NewNodeAddress is retrieved from the CLI by running metalcloud-cli instance-array get -id workers -show-iscsi-credentials
    ```bash
    $AddInP = (Get-InitiatorPort)
    $AddInP | Select NodeAddress
    Set-InitiatorPort -NodeAddress $AddInP.NodeAddress -NewNodeAddress "iqn.2020-03.com.bigstep.storage:instance-0000"
    ```

4. Add a new portal
    ```bash
    New-IscsiTargetPortal -TargetPortalAddress "100.96.0.192" -AuthenticationType OneWayCHAP -ChapUsername "ss" -ChapSecret "ss"
    ```

5. Add a new target
    ```bash
    $GIT = Get-IscsiTarget | Where-Object {$_.IsConnected -like "False"}
    ```

6. Connect to the new target (disconnect if already connected)
    ```bash
    Disconnect-IscsiTarget -NodeAddress $GIT.NodeAddress -Confirm:$false
    Connect-IscsiTarget -nodeaddress $GIT.NodeAddress
    ```

7. Make persistent
    You can skip this step or set the -IsPersistent to false if reconnect not required at reboot
    ```bash
    Connect-IscsiTarget -nodeaddress $GIT.NodeAddress -IsPersistent $True
    ```

8. Connect to the target
    ```bash
    Connect-IscsiTarget -nodeaddress $GIT.NodeAddress -IsPersistent $False -AsJob
    ```



## Prepare and format disk in Powershell

To make all attached disks online
```bash
Get-Disk | Where-Object IsOffline –Eq $True | Set-Disk –IsOffline $False
```

To Initialize all raw disks.  This will initialize the disks and create new partitions and format the drive without confirmation.
```bash
Get-Disk | Where-Object Partitionstyle -eq ‘RAW’ | Initialize-Disk -PartitionStyle GPT -PassThru | New-Partition -AssignDriveLetter -UseMaximumSize | Format-Volume -FileSystem NTFS -Confirm:$false
```

## Disconnect from all iscsi targets in Windows using Powershell Or Just disconnect Offline target

To disconnect all connections. You may receive an error if there are files open on the associated drive. This will disconnect without confirmation
```bash
$GIT = Get-IscsiTarget | Where-Object {$_.IsConnected -like "True"}
Disconnect-IscsiTarget -NodeAddress $GIT.NodeAddress -Confirm:$false
```
Or you can use the below.  This will disconnect without confirmation
```bash
Get-IscsiTarget | Where-Object IsConnected -Eq $True | Disconnect-IscsiTarget -Confirm:$false
```
Warning, the above two will disconnect ALL iSCSI drives.  If your operating system is on iSCSI, it is safer to use the below two commands

Offline disks which are not Boot
```bash
Get-Disk | Where-Object IsBoot -Eq $False | Set-Disk -IsOffline $True
```
Disconnect iSCSI connection of offline disk 
```bash
Get-Disk | Where-Object -FilterScript {($_.BusType -Eq "iSCSI") -and ($_.IsOffline -Eq $True)} | Get-IscsiSession | Get-IscsiTarget | Disconnect-IscsiTarget -Confirm:$false
```


## Deleting a drive array via the CLI
To delete a drive array use
```bash
metalcloud-cli drive-array delete -id 47859
```

## Disable indexing on a drive in Powershell

To disable indexing on a drive, you must first create a function
```bash
function Disable-Indexing{
Param($Drive)
$obj = Get-WmiObject -Class Win32_Volume -Filter "DriveLetter='$Drive'"
$indexing = $obj.IndexingEnabled
if("$indexing" -eq $True){
write-host "Disabling indexing of drive $Drive"
$obj | Set-WmiInstance -Arguments @{IndexingEnabled=$False} | Out-Null
}
}
```

To save as a function
Go to C:\Program Files\WindowsPowerShell\Modules and create a folder called Indexing
Save it in C:\Program Files\WindowsPowerShell\Modules\Indexing and save it as Indexing.psm1 as a script

Usage
```bash
Disable-Indexing "d:" 
where "d:" is the drive
```
