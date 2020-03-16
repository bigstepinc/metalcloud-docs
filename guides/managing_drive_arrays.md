# Managing drive arrays

Drives are iSCSI based block devices attached to servers at runtime. They can be operating system drives or unformatted drives.

**Drive arrays** are collections of identical drives that users can control as a single entity.

## Creating a drive array using the UI
There are multiple was to create a drive array from the **Infrastructure Editor**:
1. Click on on an instance array and go to the **DriveArray** tabs
2. Click on Create **DriveArray** button

![](/assets/guides/managing_drive_arrays1.png)

## Listing drive arrays of an instance array using the UI

1. Click on on an instance array and go to the **DriveArray** tabs

![](/assets/guides/managing_drive_arrays2.png)

## Retrieving the drive array's connection details from the UI

1. Click on on an instance array and go to the **DriveArray** tabs
2. Select one of the drive arrays
3. Click on **Show Drives**
4. Scroll down to **iSCSI credentials**

![](/assets/guides/managing_drive_arrays3.png)

## Creating a drive array using the CLI

```bash
$ metalcloud-cli drive-array create -ia gold -infra complex-demo -size 100000 -label da
```

Typically drive arrays will expand with their instance array. To stop that from happening use `-no-expand-with-ia`

## Listing drive arrays of an infrastructure using the CLI

```bash
$ metalcloud-cli drive-array list -infra  complex-demo
Drive Arrays I have access to as user alex.@d.com:
+-------+-------------------------------+-----------+-----------+-----------+-------------------------------+-----------+--------------------------+
| ID    | LABEL                         | STATUS    | SIZE (MB) | TYPE      | ATTACHED TO                   | DRV_CNT   | TEMPLATE                 |
+-------+-------------------------------+-----------+-----------+-----------+-------------------------------+-----------+--------------------------+
| 47859 | da                            | ordered   | 100000    | iscsi_ssd | gold (#37135)                 | 1         |                          |
| 45928 | drive-array-45928             | active    | 40960     | iscsi_ssd | workers (#35516)              | 2         | CentOS 7.4 (#78)         |
| 45929 | drive-array-45929             | active    | 40960     | iscsi_ssd | master (#35517)               | 1         | CentOS 7.4 (#78)         |
| 47799 | gold-da                       | ordered   | 100000    | iscsi_ssd | gold (#37135)                 | 1         |                          |
| 47858 | test                          | ordered   | 40960     | iscsi_ssd |                               | 1         |                          |
+-------+-------------------------------+-----------+-----------+-----------+-------------------------------+-----------+--------------------------+
Total: 5 Drive Arrays


```

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

## Logging into the target on Windows
Using powershell:
1. Add a new portal

        ```bash
        New-IscsiTargetPortal -TargetPortalAddress "100.96.0.192" -AuthenticationType OneWayCHAP -ChapUsername "ss" -ChapSecret "ss"
        ```
2. Add a new target

        ```bash
        $GIT = Get-IscsiTarget | Where-Object {$_.IsConnected -like "False"}
        ```

3. Connect to the new target (disconnect if already connected)

    ```bash
    Disconnect-IscsiTarget -NodeAddress $GIT.NodeAddress -Confirm:$false
    Connect-IscsiTarget -nodeaddress $GIT.NodeAddress
    ```
4. Make persistent

    You can skip this step or set the -IsPersistent to false if reconnect not required at reboot

    ```bash
    Connect-IscsiTarget -nodeaddress $GIT.NodeAddress -IsPersistent $True
    ```
5. Connect to the target

    ```bash
    Connect-IscsiTarget -nodeaddress $GIT.NodeAddress -IsPersistent $False -AsJob
    ```

## Disconnected from all iscsi targets in Windows

To disconnect all connections:

    ```bash
    $GIT = Get-IscsiTarget | Where-Object {$_.IsConnected -like "True"}
    Disconnect-IscsiTarget -NodeAddress $GIT.NodeAddress -Confirm:$false
    ```


## Deleting a drive array via the CLI
To delete a drive array use:

```bash
metalcloud-cli drive-array delete -id 47859
```

