# Managing drive arrays

Drives are iSCSI based block devices attached to servers at runtime. They can be operating system drives or unformatted drives.

**Drive arrays** are collections of identical drives that users can control as a single entity.

## Creating a drive array using the UI
There are multiple ways to create a drive array from the **Infrastructure Editor**:
1. Click on on an instance array and go to the **DriveArrays** tab
2. Click on **Create DriveArray** button

![](/assets/guides/managing_drive_arrays1.png)

 
## Listing drive arrays of an instance array using the UI

1. Click on on an instance array and go to the **DriveArrays** tab

![](/assets/guides/managing_drive_arrays2.png)

## Adding a new drive

 1.In the Bigstep Infrastructure Editor, click on the **Infrastructure** button on the left bar and select Drive Array.  
![](/assets/guides/drive_management_1.png)  
2.The new Drive Array will now be visible in the interface.  
![](/assets/guides/drive_management_2.png)  
3. Click on the new Drive Array, in order to customize it. You can tweak the size, storage type, operating system template, file system and block size, as well as attach it to an existing Instance Array or Container Array. You can also attach it to an array by simply dragging and dropping it in the interface.  
  
![](/assets/guides/drive_management_3.png)  
4. An alternative way to create a Drive Array is from the Instance Array overview, in the **DriveArrays** tab. Click on **Create DriveArray** and a new one will be attached to the server, with default settings. You can customize the Drive Array by clicking on its icon in the interface.  
  
![](/assets/guides/drive_management_4.png)  
5.After configuring and attaching the drive, click on **Deploy Changes** in order to make it active.  
![](/assets/guides/drive_management_5.png)  
  
6.The new disk will be attached to your server after the deploy. A server reboot might be needed, as well as additional configuration from your operating system, before it can be used.  
  
 ## Removing a drive

 1.In order to delete an existing Drive Array, click on its icon in the infrastructure editor.  
![](/assets/guides/drive_management_6.png)  
2.Click on **Delete DriveArray**.  
![](/assets/guides/drive_management_7.png)  
3.Confirm that you want to delete the drive.  
![](/assets/guides/drive_management_8.png)  
4.Click on **Deploy Changes** in the infrastructure editor.

 5.As a safety measure, you will be warned about data loss. In order to confirm your option, manually type *destroydata* before the actual deploy starts.  
![](/assets/guides/drive_management_9.png)  
6.The drive will be deleted at the end of the deploy.

 ## Expanding disk size

 1.From the infrastructure editor, click on the DriveArray you want to change the Drive size of. This opens the DriveArray overview panel.  
![](/assets/guides/drive_management_10.png)

 2.Drag the **Default drive size** slider in order to increase its capacity, or simply type the desired size in GB. It is not possible to reduce the size of a drive, since this is a very risky operation on most operating systems.  
![](/assets/guides/drive_management_11.png)  
  
3.Click on **Save**, then on **Deploy changes**.

 4.Resizing a disk requires that the server is powered off. If any affected servers in the infrastructure are still powered on, you will be prompted to **Hard power off** or **Soft power off** them before the deploy. We recommend the **Soft power off** option.  
![](/assets/guides/drive_management_12.png)

 5.The resized disk will be available after the deploy. Depending on the operating system on your server, additional configuration might be required.



## Creating a drive array using the CLI

```bash
metalcloud-cli drive-array create -ia gold -infra complex-demo -size 100000 -label da
```

In order for a drive array to be accessible you need to push the **Deploy changes** button in the UI, or run the following metalcloud-cli command:

```
metalcloud-cli infrastructure deploy -id complex-demo
```
or
```
metalcloud-cli infrastructure deploy -id complex-demo -autoconfirm
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
All the drive arrays with status ordered are not yet accessible.

## Deleting a drive array via the CLI
To delete a drive array use
```bash
metalcloud-cli drive-array delete -id 47859
```

## Manually logging into the iscsi target

Most of the time the drives will simply appear in the operating system at a reboot. However sometimes manual intervention is required. Reffer to [Manually managing iSCSI connections](/advanced/manually_managing_iscsi_connections.md) for more information.