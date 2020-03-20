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


## Deleting a drive array via the CLI
To delete a drive array use
```bash
metalcloud-cli drive-array delete -id 47859
```

## Manually logging into the iscsi target

Most of the time the drives will simply appear in the operating system at a reboot. However sometimes manual intervention is required. Reffer to [Manually managing iSCSI connections](/advanced/manually_managing_iscsi_connections.md) for more information.