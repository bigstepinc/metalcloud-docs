# Managing drive arrays

Drives are iSCSI based block devices attached to servers at runtime. They can be operating system drives or unformatted drives.

**Drive arrays** are collections of identical drives that users can control as a single entity.

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
```
This are the initiator credentials. These should already be configured on the instance but if they are not use the following to retrieve them:
```bash
$ metalcloud-cli instance-array get -id workers -show-iscsi-credentials
```

## Deleting a drive array via the CLI

To delete a drive array use:
```bash
metalcloud-cli drive-array delete -id 47859
```