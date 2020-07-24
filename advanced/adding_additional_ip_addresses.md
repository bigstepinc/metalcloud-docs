# Adding additional IP addresses
Additional IPv4 addresses or subnets can be added or deleted easily directly from the Bigstep infrastructure editor. In this article, we will walk you through the process.

 **Adding a subnet**

 1.Click on the **Internet** widget in your infrastructure editor.  
![](/assets/guides/adding_additional_ip_addresses_1.png)  
2.When a server is deployed, one IPv4 subnet and one IPv6 subnet are already configured. Click on **Add subnet** if you need more IP addresses.   
  
![](/assets/guides/adding_additional_ip_addresses_2.png)  
3.In the next window, you can configure your subnet. Choose a label for easier identification, then a subnet type and size.  
  
![](/assets/guides/adding_additional_ip_addresses_3.png)  
4.Available IPv4 subnets range between the smallest /30 (a single usable IP) and the largest/27 (30 usable IP addresses). Keep in mind that is cheaper to use a larger subnet instead of several smaller ones that provide the same total number of IPs.  
  
![](/assets/guides/adding_additional_ip_addresses_4.png)  
  
5.For IPv6 networking, you can only add /64 subnets.

 ![](/assets/guides/adding_additional_ip_addresses_5.png)

 6.After selecting your options, click on **Create subnet**, then on **Save**.

 ![](/assets/guides/adding_additional_ip_addresses_6.png)

 7.The changes must be deployed from the infrastructure editor. Click on **Deploy changes**.

 ![](/assets/guides/adding_additional_ip_addresses_7.png)

 8.The new subnet will be usable after the deploy and is now visible in the **Internet** tab.

 ![](/assets/guides/adding_additional_ip_addresses_8.png)

 9.Click on the subnet in order to see information such as the gateway or the last usable address.

 ![](/assets/guides/adding_additional_ip_addresses_9.png)

 **Deleting a subnet**

 1.Click on the **Internet** tab of the infrastructure editor and select the subnet that you want to delete. Please note that the initial IPv4 and IPv6 subnets cant be deleted.

 ![](/assets/guides/adding_additional_ip_addresses_10.png)

 2.Click on **Delete subnet **and then** Save**.

 ![](/assets/guides/adding_additional_ip_addresses_11.png)

 3.Click on **Deploy changes** in the infrastructure editor, the subnet will be deleted at the end of the deploy.

