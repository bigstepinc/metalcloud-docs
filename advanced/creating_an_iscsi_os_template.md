# Creating an iSCSI OS template

Custom iSCSI templates allow users to build their own images. Typically a user would start from a standard Metalcloud template and modify it:

![](/assets/advanced/creating_custom_template1.svg)

This tutorial uses the CLI. Visit [using the CLI](/guides/using_the_cli) for more details.

## Creating a "golden" drive

1. List available templates

	```bash
	$ metalcloud-cli volume-template list
	Volume templates I have access to as user alex.d@d.com:
	+-------+-----------------------------------------+----------------------------------+-------+---------------------------+-----------+
	| ID    | LABEL                                   | NAME                             | SIZE  | STATUS                    | FLAGS     |
	+-------+-----------------------------------------+----------------------------------+-------+---------------------------+-----------+
	| 6     | ubuntu-12-04                            | Ubuntu-12.04                     | 40960 | deprecated_deny_provision |           |
	| 13    | centos6-5                               | CentOS6.5                        | 40960 | deprecated_allow_expand   |           |
	| 14    | centos6-6                               | CentOS6.6                        | 41000 | deprecated_allow_expand   |           |
	| 18    | centos71v1                              | CentOS 7.1                       | 40960 | deprecated_allow_expand   |           |
	+-------+-----------------------------------------+----------------------------------+-------+---------------------------+-----------+
	Total: 4 Volume templates
	```

2. Provision an Instance 


	```bash
	$ metalcloud-cli  instance-array create -boot pxe_iscsi -firewall-management-disabled -infra demo -instance-count 1 -label gold
	```
3. Add a drive array to the instance

	Use the ID of the template, for instance **18** for CentOS 7.1

	```bash
	$ metalcloud-cli drive-array create  -ia gold -infra demo -size 100000 -label gold-da -template 18
	```

4. Deploy the infrastructure

	```bash
	$ metalcloud-cli infrastructure deploy -id demo
	```

5. Login or connect to the server and perform required modifications, test etc.

	```bash
	$ metalcloud-cli instance-array get -id gold -show-credentials
	```

6. Shutdown the server to avoid in-flight data from not being serialized
	```bash
	$  metalcloud-cli instance power-control  -id 58413 -operation soft
	```

7. List the drives of the **gold-da** drive array

	```bash
	$ metalcloud-cli drive-array get -id gold-da
	Drive Array #47799 attached to instance array 37135 has the following drives:
	+-------+-------------------------------+-----------+-----------+-----------+-------------------------------+--------------------------+--------------------------+
	| ID    | LABEL                         | STATUS    | SIZE (MB) | TYPE      | ATTACHED TO                   | TEMPLATE                 | DETAILS                  |
	+-------+-------------------------------+-----------+-----------+-----------+-------------------------------+--------------------------+--------------------------+
	| 74270 | drive-74270                   | active   | 100000    | iscsi_ssd | instance-58413                |                          | none  none               |
	+-------+-------------------------------+-----------+-----------+-----------+-------------------------------+--------------------------+--------------------------+
	Total: 1 Drives
	```


## Creating a a volume template from the golden drive

1. Create a template from the first drive

	```bash
	$ metalcloud-cli volume-template create  -id 74270 -boot-methods-supported pxe_iscsi -boot-type hybrid -label "centos7.1-custom" -description "Custom 7.1 template" -name "Custom Centos 7.1"
	```

	The "create volume_template" operation takes the following arguments:
	```bash
	$ ./metalcloud-cli volume-template create -h
	Command: volume-template create    Create volume templates (alternatively use "new vt")
		-boot-methods-supported    The boot_methods_supported of the volume template. Defaults to 'pxe_iscsi'.
		-boot-type                 (Required) The boot_type of the volume template. Possible values: 'uefi_only','legacy_only','hybrid' 
		-deprecated                (Flag) set to true if this template is deprecated
		-description               (Required) The description of the volume template
		-id                        (Required) The id of the drive to create the volume template from
		-label                     (Required) The label of the volume template
		-name                      (Required) The display name of the volume template
		-return-id                 (Optional) Will print the ID of the created Drive Array. Useful for automating tasks.
		-tags                      The tags of the volume template, comma separated.
		-h                         Show command help and exit.
	```
	Notes on server boot methods:
	* -boot-methods-supported reffers to the type of mechanism emplyed to boot this template. For iSCSi drives use `pxe_iscsi`.
	* -boot-type reffers to the boot process of the server which can be either legacy BIOS or EFI. Hybrid reffers to templates that support both mechanisms.

2. Check that the volume template has been created

	```bash
	$ metalcloud-cli volume-template list
	Volume templates I have access to as user alex.d@d.com:
	+-------+-----------------------------------------+----------------------------------+-------+---------------------------+-----------+
	| ID    | LABEL                                   | NAME                             | SIZE  | STATUS                    | FLAGS     |
	+-------+-----------------------------------------+----------------------------------+-------+---------------------------+-----------+
	| 6     | ubuntu-12-04                            | Ubuntu-12.04                     | 40960 | deprecated_deny_provision |           |
	| 13    | centos6-5                               | CentOS6.5                        | 40960 | deprecated_allow_expand   |           |
	| 14    | centos6-6                               | CentOS6.6                        | 41000 | deprecated_allow_expand   |           |
	| 18    | centos71v1                              | CentOS 7.1                       | 40960 | deprecated_allow_expand   |           |
	| 19    | centos71-custom                         | CustomCentOS 7.1                 | 40960 | deprecated_allow_expand   |           |
	+-------+-----------------------------------------+----------------------------------+-------+---------------------------+-----------+
	Total: 5 Volume templates
	```
	> Please note that the volume template is a private template meaning only it's owner has access to it.

	Now the template can be used as any other template.

	```bash
	$ metalcloud-cli drive-array create -ia gold -infra demo -size 100000 -label gold-da -template 19
	```
