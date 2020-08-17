# Release notes

### R4.5 - 12 August 2020
This is a minor release that was focused on bug fixes and to add basic variable support. Here are the highlights:

1. **UI Improvements**

   We fixed a range of bugs in the Servers page, Storages page, Storage Templates page, Variables pages, Workflow page 
	and a few more other bugs in the Multi-server enclosures pages. 
2. **Metalcoud CLI**

   We added variables to OS assets and missing shared drive functions. 
   Support for subnets and switches is now possible from the CLI. Also the CLI now has updated yaml format configuration for all commands.
3. **Monitoring agent updates**

   The new improved monitoring agent will be released, with enhancements for data measurements and SNMP pooling. The new implementation allows
better monitoring capabilities and more exact SFLOW measurements.
4. **Switch provisioning**

   We continued the work on the switch provisioning from the previous release.We improved the switch provisioning layer to always use the caching layer, that would provide improved speed in switch provisioning operations. We also removed reconnects for HP switches which improves deploy time.
   
5. **OS Template API improvement**
 
   The OS template API has now the ability to use variables for templates.


### R4.4 - 9 July 2020
This is a minor release that was focused on improving deploy speed and fix bugs. Here are the highlights:

1. **Improve deploy speed for Windows**

   This new deploy method improves boot times for Windows images and provides the fixes needed to boot the image fast.If the server is already powered up then we also added some time optimisations.

2. **DC agent stability fixes and performance optimisations for very high latency networks**

   We have introduced performance optimisations in very high latency environments and in environments that have 1000+ VLANs. The system is able to perform well under these 
   special conditions and agents are able to fully manage this kind of environments. We also fixed some stability issues for DC agents triggered by the high latency environments.

3. **Workflow UI improvements and improved usage reports**

    We improved the Workflow UI interface with correct sort options, adding a Run now button and by adding confirmations for delete and fixing new stage form. We improved the usage reports with fixes for Windows usage.

4. **Monitoring agent improvements**

    The monitoring agent has a new time series database implementation that will add the ability to display additional details in the monitoring tab and will improve monitoring in general. The monitoring agent implementation was improved and the agent will be able to also add metadata to data. 

5. **Subnet pools, storage pools and search API**

    We added UI and API fixes to subnet pools and enhanced the storage pools create APIs. We also improved the search API functionality for all search APIs in all forms.  

### R4.1 - 21 April 2020
This is a minor release that was focused on improving usability. Here are the highlights:

1. **New instance array create form**

    This new form is not just easier to understand for new users but also supports local install better. Moving forward the templates will be depending on the server type selected meaning some templates, especially Windows templates which are hardware dependent will only be available to some server types and this form supports this approach. This will avoid some corner cases where specific hardware are incompatible with certain templates and the user was allowed to proceed with the deploy.

2. **New GPU Instances**

    We are introducing new GPU instances: the M.4.16.1G and the M.8.32.1G. These feature a NVidia Tesla T4 16GB GPU. They are currently available only to beta customers but if you are interested get in touch with us. We are also able to source NVIDIA GRIDD Drivers which enable many scenarios such as VDI or power workstation.

3. **Boot customization support**

    We are now introducing a new mechanism that allows users to automate boot processes which can be used to perform custom OS installs such as perform unattended Gentoo deployment on local drives. This is currently possible only via the CLI. See [Creating a local install os template](/advanced/creating_a_local_install_os_template) for more details.

4. **CLI updated**

    The CLI, now at 1.5.5 is now fully features and can perform all actions possible via the UI and more.

5. **Windows 2019 template available**

    This new Windows template is currently only available for **M.8.8**, **M.8.16**, **M.8.32 (v1)**, **M.4.16.1G**, **M.8.32.1G** server types and only for diskless setups.


### R4.0 - 12 March 2020

This is a major release that was focused on improving reliability. Here are the highlights:

1. **Support for local install**

    We now have very extensive support for local install. Users are now able to select the "install on local disks" option which has a separate set of templates.

2. **Support for pre and post deploy workflows**

    Users can now attach Anisble tasks to infrastructures which are executed when the infrastructures are updated (deployed). This allows users to perform tasks such as updating loadbalancing configurations upon instance array expand, or install pre-requisite software on nodes when the nodes are deployed.

3. **Many bug fixes and improvements**

    This release was focused on improving reliability and ease of use and many bugs specially around networking provisioning has been addressed.


