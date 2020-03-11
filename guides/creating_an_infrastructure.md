# Creating an infrastructure

Instance Arrays are collections of identical servers used as a single entity.

## Creating an infrastructure using the UI

1. In the infrastructure selector on the very top of the editor select **Create an infrastructure**

![](/assets/guides/creating_an_infrastructure1.png)


2. Add the name and select your datacenter.


![](/assets/guides/creating_an_infrastructure2.png)


3. Click **Create**

## Creating an infrastructure using the CLI

This tutorial uses the CLI. Visit [using the CLI](/guides/using_the_cli) for more details.


 ```bash
 metalcloud-cli new infra -label test1
 ```

## Listing infrastructures using the CLI

Check if your infrastructure has been created:

 ```bash
metalcloud-cli ls infra
Infrastructures I have access to (as alex.bordei@bigstep.com) in datacenter uk-reading

+-------+-------------------------------+----------------------------------+-----------+---------+--------------+
| ID    | LABEL                         | OWNER                            | REL.      | STATUS  | DATACENTER   |
+-------+-------------------------------+----------------------------------+-----------+---------+--------------+
| 26356 | test4444                      | alex.d@d.com                     | OWNER     | ordered | uk-reading   |
| 26358 | test44443                     | alex.d@d.com                     | OWNER     | ordered | uk-reading   |
| 26359 | test1                         | alex.d@d.com                     | OWNER     | ordered | uk-reading   |
+-------+-------------------------------+----------------------------------+-----------+---------+--------------+
Total: 3 Infrastructures
 ```


Where to go from here:
1. [Creating an InstanceArray](/guides/creating_an_instance_array)
