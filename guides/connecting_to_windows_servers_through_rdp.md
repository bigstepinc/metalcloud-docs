# Connecting to Windows servers through RDP

As soon as the deploy of an infrastructure is completed, the servers are powered up and you can connect to them remotely using the Remote Desktop protocol.

 Depending on the operating system on your computer, there are multiple ways to use RDP. While Windows includes a Remote Desktop Connection client, Linux users may need to install a 3rd party Remote Desktop Connection client (either search your package store for the console based rdesktop or search your package store for a GUI based application). MacOS users can download the Microsoft provided Remote Desktop Connection client from the app store, just search for Microsoft Remote Desktop.

 ## Locating access credentials

 1.In the Bigstep Infrastructure Editor, click on the Instance Array widget of the instance you want to connect to.  
![](/assets/guides/connecting_to_windows_servers_through_rdp_1.png)

 2.This opens the Instance Array overview window, with a list of the servers (instances) in the array.  
  
![](/assets/guides/connecting_to_windows_servers_through_rdp_2.png)

 3.If you have an RDP application configured, you can click on the RDP **Access link** and it will download the RDP file. Just click on this and it should launch your default RDP application file.  
  
![](/assets/guides/connecting_to_windows_servers_through_rdp_3.png)

 Alternatively, you can click on the instance name and below that click on **Network interfaces** and copy the IPv4 Address and paste this directly into your client.

 ![](/assets/guides/connecting_to_windows_servers_through_rdp_4.png)

 4.The initial RDP password for the root account is found in the column to the right.

 ![](/assets/guides/connecting_to_windows_servers_through_rdp_5.png)

 5.If you copy the IP address rather than opening the file, paste the IP address from the **Network interfaces**c olumn into the application's Computer field. Leave the other settings unchanged and click **Open**.

 ![](/assets/guides/connecting_to_windows_servers_through_rdp_6.png)

 6. When prompted for the username in the terminal emulator, enter Administrator.

 7. Copy the initial password and paste it when asked.

 8. You are now connected to the server with Administrator privileges and you can administrate it remotely.

 We would always recommend you restrict access to RDP by IP address in the Windows Firewall. If this is not possible you can change the port for RDP in the registry (<https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/change-listening-port>) .

 Restrict RDP Access by IP Address

 If you would like to restrict Remote Desktop access to your Dedicated server to an IP address or range of IP addresses, youcan do so by following the instructions below.

 Edit Existing Firewall Rule

 ## Connect to your server via RDP.

 Open Windows Firewall with Advanced Security

 Click on `Inbound Rules` in the left pane.

 ## Locate your RDP Rule

 Right click the rule, go toProperties, switch to theScopetab.  

 ![](/assets/guides/connecting_to_windows_servers_through_rdp_7.png)

 ## Creating Your IP Restrictions

 The Scope tab is where you will add the IP addresses and ranges you want to access your server.

 In the Scope tab. edit the Remote IP Address section

 Click the radio button next toThese IP Addresses

 Then click Add...

 If using a single IP Address,simply type it in the top text field, then click **OK**.

 For every additional single IP Address, repeat Steps 3 & 4.

 If you need to add an IP Range, click the radio button next toThis IP range

 Type the start of the range in the **From** field, and the end of the range in the **To** field.
 
 For every additional range, repeat Steps 6 & 7.  
   
 ![](/assets/guides/connecting_to_windows_servers_through_rdp_8.png)

 After adding every desired IP Address, click the OK button to finalize the changes.

 Once you finalize the changes, you can test the rule by attempting to RDP to the server using an IP outside of the desired ranges. If it fails to connect, then the rule is successful.

