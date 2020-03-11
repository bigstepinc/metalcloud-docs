# Creating an instance array using the infrastructure editor

Instance Arrays are collections of identical servers used as a single entity.

### Creating an infrastructure using the CLI

 ```bash
 metalcloud-cli new infra -label test1
 ```

 ### Listing infrastructures using the CLI
 ```bash
metalcloud-cli ls infra
Infrastructures I have access to (as alex.bordei@bigstep.com) in datacenter uk-reading

+-------+-------------------------------+----------------------------------+-----------+---------+--------------+
| ID    | LABEL                         | OWNER                            | REL.      | STATUS  | DATACENTER   |
+-------+-------------------------------+----------------------------------+-----------+---------+--------------+
| 26356 | test4444                      | alex.d@d.com                     | OWNER     | ordered | uk-reading   |
| 26358 | test44443                     | alex.d@d.com                     | OWNER     | ordered | uk-reading   |
| 26359 | my-test22                     | alex.d@d.com                     | OWNER     | ordered | uk-reading   |
+-------+-------------------------------+----------------------------------+-----------+---------+--------------+
Total: 3 Infrastructures
 ```

