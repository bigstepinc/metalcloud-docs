# Release notes

### R4.1 - 21 April 2020
This is a minor release that was focused on improving usability. Here are the highlights:

1. **New instance array create form**

    This new form is not just easier to understand for new users but also supports local install better. Moving forward the templates will be depending on the server type selected meaning some templates, especially Windows templates which are hardware dependent will only be available to some server types and this form supports this approach. This will avoid some corner cases where specific hardware are incopatible with certain templates and the user was allowed to proceed with the deploy.

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