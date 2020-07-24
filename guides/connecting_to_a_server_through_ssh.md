# Connecting to a server through SSH
As soon as the deploy of an infrastructure is completed, the servers are powered up and you can connect to them remotely using the SSH protocol.

 Depending on the operating system on your computer, there are multiple ways to use SSH. While Linux and MacOS systems already include a terminal, Windows users must install an emulator unless they have the Linux Bash Shell already configured. The most popular Windows terminal emulator is PuTTY, a free application that can be downloaded from [here](https://www.putty.org/).

 ## Locating access credentials and connecting

 1.In the Bigstep Infrastructure Editor, click on the Instance Array widget of the instance you want to connect to.  
  
![](/assets/guides/connecting_to_a_server_through_ssh_1.png)

 2.This opens the Instance Array overview window, with a list of the servers (instances) in the array.  
  
![](/assets/guides/connecting_to_a_server_through_ssh_2.png)  
3.If you have a terminal application configured, you can click on the SSH **Access link **and it will open directly.   
  
![](/assets/guides/connecting_to_a_server_through_ssh_3.png)

 4.The initial SSH password for the root account is found in the column to the right.  
  
![](/assets/guides/connecting_to_a_server_through_ssh_4.png)  
5.If you use PuTTY, copy and paste the IP address from the **Access link** column into the application's "Hostname (or IP address)" field. Leave the other settings unchanged and click **Open**.  
  
![](/assets/guides/connecting_to_a_server_through_ssh_5.png)  
  
6.When prompted for the username in the terminal emulator, enter root.  
  
7.Copy the initial password and paste it when asked. In PuTTY, you can paste text by right clicking.  
  
8. You are now connected to the server with root privileges and you can administrate it remotely.

 9. Another option is to use the HTML5 SSH console. From the Instance Array overview window, click on **Browser SSH client** next to the server that you want to access.  
  
![](/assets/guides/connecting_to_a_server_through_ssh_6.png)

 10. This feature requires two factor authentication, as a safety measure. If you didn't configure an authenticator on your account, do so now, and then paste the generated code and click **Connect**.

 ![](/assets/guides/connecting_to_a_server_through_ssh_7.png)

 11. You are now logged in as root in the HTML5 console.

 ![](/assets/guides/connecting_to_a_server_through_ssh_8.png)

