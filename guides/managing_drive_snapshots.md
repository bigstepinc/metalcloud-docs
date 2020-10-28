# Managing drive snapshots

You can create snapshots of your drives at any time and revert then when needed, with just a few clicks from the Bigstep infrastructure editor.

 Creating a snapshot or reverting to a snapshot are performed instantaneously and do not require an infrastructure deploy operation.

 However, there are a few caveats. Each Drive can have a maximum of 5 snapshots at any given time. After that, whenever a new snapshot is created the oldest one is automatically deleted. After a successful rollback, any snapshots newer than the one selected for the rollback are automatically deleted.

 Some servers have local disks that are not automatically managed. Those disks are not displayed in the graphical user interface and can only be interacted with at the OS level or using iLO. The information in this document does not apply to those drives, but only to drives in DriveArrays, to which the servers connect through iSCSI.

  **Creating a snapshot**

 1. From the infrastructure editor, click on the DriveArray that the Drive you want to create a snapshot of belongs to.

 ![](/assets/guides/drive_snapshot_management_1.png)

 2.This opens the DriveArray overview panel. Click on the **Drives** tab.

 ![](/assets/guides/drive_snapshot_management_2.png)

 3.You can now click on the Drive you want to create a snapshot of, to open the Drive overview panel.

 ![](/assets/guides/drive_snapshot_management_3.png)

 4.Click the **Snapshots** tab. Any existing Drive snapshots related to the selected Drive will be displayed there.

 ![](/assets/guides/drive_snapshot_management_4.png)

 5.Click the **Create snapshot** button. The snapshot is created instantaneously (copy on write).

 ![](/assets/guides/drive_snapshot_management_5.png)

 6.After the snapshot is created, it will be visible in the list.

 ![](/assets/guides/drive_snapshot_management_6.png)

  **Rolling back a snapshot**

 In order to ensure data consistency, the server connected to the Drive undertaking the operation must be powered off.

 1. Click on the InstanceArray connected to the DriveArray that the Drive belongs to.

 ![](/assets/guides/drive_snapshot_management_7.png)

 2.This opens the InstanceArray overview panel. Select the instance that you want to poweroff, then click on the **Soft Shutdown** button.

 ![](/assets/guides/drive_snapshot_management_8.png)

 3.After the server shuts down, go back to the infrastructure editor and click on the DriveArray that the Drive you want to rollback a snapshot of belongs to. Click on the Drive and then on the **Snapshots** tab.

 4.Click the **Revert** button next to the Drive snapshot you want to rollback to. This restores the Drive to its previous state and deletes any snapshots newer than the selected one. The interface will warn you about this behavior.

 ![](/assets/guides/drive_snapshot_management_9.png)

 ![](/assets/guides/drive_snapshot_management_10.png)

 5.You can now go back to the InstanceArray overview panel and power on your server.

 