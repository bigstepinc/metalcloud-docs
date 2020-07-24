# Using the infrastructure firewall
The Bigstep platform includes a firewall that allows users to control traffic permissions on their Infrastructures remotely, at the Cluster, InstanceArray, or ContainerPlatform level, without needing to manually configure each underlying machine.

 While the infrastructure firewall is a very convenient tool, it is important to understand the way it operates, in order to use it effectively.

 First of all, the firewall is compatible only with Linux operating systems. If you run a version of Windows on your server, the firewall tab will still be present in the infrastructure, but the rules do not apply.

 Another very important aspect that you have to consider is that only one firewall should be active on a server at any time.

 If you want to install and configure your own firewall at operating system level, you should disable the one in the infrastructure, in order to avoid conflicts. For example, any deploy activity will re-apply the infrastructure firewall rules and delete other firewall settings. This might break server functionality, like blocking SAN traffic.

 The firewall is enabled by default and enforces a standard set of rules that allow only IPv4 private subnets, ICMP traffic on both IPv4 and IPv6 protocols, as well as several hidden rules that open traffic from Bigsteps provisioning systems and inside the infrastructure.

 ![](/assets/guides/using_the_infrastructure_firewall_1.png)

 All ports of newly created instances are closed to any outside traffic by default, to increase security. In order to be able to access any service, you will need to whitelist your IP addresses or open the ports to the world.

 For example, if you want to connect to your servers using SSH, a custom firewall rule must be created. For your convenience, your external IP address is displayed in the top right corner of the window and several common predefined rules to allow SSH, RDP and SNMP traffic are pre-defined and can be activated with a single click.

 Disabling automatic firewall management erases all the iptables rules present on all the servers belonging to the affected Infrastructure element. Enabling it again installs the provided rules (the ones visible in the interface) back on the servers.

 The Metal Cloud service automatically provisions some additional firewall rules at the OS level, as well as a SSH key that allows our systems to securely access the servers.

 The firewall on each machine needs to open ports 67 and 68 through UDP and allow traffic from the 100.64.0.0/16, 185.90.48.54, and 84.40.58.54 subnets.

 If you configure a supplementary firewall from the OS, please open the above-mentioned ports and allow access from the above-mentioned subnets.

  Lets see how you can **Create a New Firewall Rule**

 1. In the Bigstep Infrastructure Editor, click the icon of the Cluster for which you want to create custom firewall rules. This opens the Cluster overview panel.

 ![](/assets/guides/using_the_infrastructure_firewall_overview.png)

 2.Click on the **Firewall** tab, in order to open the rule management panel.

 ![](/assets/guides/using_the_infrastructure_firewall_rules_panel.png)

 3.If the firewall is disabled, click on the **Enable firewall management** checkbox. Keep in mind that enabling or disabling the automatic firewall management feature removes any iptables rules present on the servers. In order to keep any existing rules you have to add them to the Bigstep firewall manager.

 4.Click **Add rule** and a new one will be added on the bottom of the list.

 5.Click on the settings wheel button in order to edit the new rule.

 ![](/assets/guides/using_the_infrastructure_firewall_edit_rule.png)

 6. Enter the desired firewall rule values, protocol and type. 

 The first field can be used to specify a custom label that makes it easy to identify the purpose of the rule. The source address specifies the IP address of the computer that initiates communication. Leaving this blank accepts communication from any IP address.   
   
 The destination address must be one of the IP addresses of the instances on the cluster. Leaving this blank accepts communication directed at any IP address.   
   
 The two port fields specify the port range that is available for communication. Leaving this blank opens all ports.  
   
 After editing the rule, click **Save**.

 ![](/assets/guides/using_the_infrastructure_firewall_rule_save.png)

 7.Click on the **Deploy** button at the top, keep in mind that firewall changes only become active once deployed. You can review the changes in the deploy overview panel.

 8.After the deploy is complete, the new firewall rules are automatically added to all the Instances on the selected Cluster.

 