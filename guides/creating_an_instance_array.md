# Creating an instance array

This is how Servers This is often the very first step in using the Metal Cloud.
Make sure you have created an account with us by signing up [here](http://bigstep.com)

### CCreating an instance array using the Infrastructure Editor

In the MetalCloud servers (called **Instances**) are groupped in **InstanceArrays**. By default an infrastructure is created for you called "my-infrastructure" in a datacenter geographically close to you.

1. Click on the `Create your first InstanceArray`

![](/assets/guides/getting_started3.png)


2. Select your configuration, number of servers, operating system, drive size and boot type. 

Certain servers types support deploying the operating system on a local drive (or a collection of local drives in an RAID 0 array). Local drives do not allow switching the server but are less expensive and carry higher capacities and, if using local NVMes higher performance.

![](/assets/guides/getting_started5.png)

3. Alter firewall rules

By default all traffic is blocked except if it originates from what our systems detects as being your IP. You need to explicitly enable additional IPs or ports before you deploy.

![](/assets/guides/getting_started41.png)

4. Deploy the infrastructure

Operations in the MetalCloud are not immediatelly deployed. In fact they can be reverted until the infrastructure is "Deployed".
Click on the big "Deploy" button from the bottom of the screen.
![](/assets/guides/getting_started61.png)

### Creating an instance array using the CLI

This tutorial uses the CLI. Visit [using the CLI](/guides/using_the_cli) for more details.

1. List available templates

```bash
$ metalcloud-cli ls volume_templates
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
$ metalcloud-cli create instance_array -boot pxe_iscsi -firewall_management_disabled -infra demo -instance_count 1 -label gold
```
3. Add a drive array to the instance

Use the ID of the template, for instance **18** for CentOS 7.1

```bash
$ metalcloud-cli create da -ia gold -infra demo -size 100000 -label gold-da -template 18
```

4. Deploy the infrastructure
```bash
$ metalcloud-cli deploy infra -id demo
```

5. Login or connect to the server and perform required modifications, test etc.
```bash
$ metalcloud-cli show ia -id gold -show_credentials
```
