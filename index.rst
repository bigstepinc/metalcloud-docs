.. Metalcloud Documentation documentation master file, created by
   sphinx-quickstart on Tue Mar 10 22:28:54 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



Welcome to Metalcloud's documentation!
====================================================

.. image:: /assets/bigstep-logo.svg
   :align: left
   :width: 100

The Bigstep Metalcloud is an IaaS service focused on offering low latency and high performance compute and storage services.  The service offers the same level of flexibility that is typical from a cloud provider but using only bare metal.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   general/introduction
   general/getting_started
   general/metalcloud_instances
   general/metalcloud_pricing
   general/datalake_overview
   general/glossary

.. toctree::
   :maxdepth: 2
   :caption: Guides:
   
   guides/connecting_to_a_server_through_ssh
   guides/connecting_to_windows_servers_through_rdp
   guides/using_the_infrastructure_firewall
   guides/managing_infrastructures
   guides/managing_instance_arrays
   guides/managing_drive_arrays
   guides/managing_networks
   guides/managing_drive_snapshots
   guides/managing_billing_information
   guides/managing_users_and_permissions
   
   guides/delegating_access_to_an_infrastructure
   guides/retrieving_the_utilization_report
   guides/using_the_cli
   guides/using_the_terraform_provider
   guides/using_the_datalake_command_line_tool
   guides/managing_datalake_files_using_curl
   guides/authenticating_to_the_datalake_using_kerberos
   guides/configure_okta_for_saml_authentication
   guides/add_boot_and_install_drivers_to_a_repository_windows_iso
   
   

.. toctree::
   :maxdepth: 2
   :caption: Advanced:

   advanced/adding_additional_ip_addresses
   advanced/creating_an_iscsi_os_template
   advanced/creating_a_local_install_os_template
   advanced/manually_managing_iscsi_connections
   advanced/enabling_two_factor_authentication
   advanced/managing_assets
   advanced/managing_variables_and_secrets
   advanced/managing_stage_definitions
   advanced/setting_up_users_and_permissions_in_reseller_scenarios
   advanced/deploying_and_managing_kubernetes_cluster

.. toctree::
   :maxdepth: 2
   :caption: Others:

   general/additional_resources
   general/release_notes

Additional resources
--------------------
- `Terraform Provider <https://www.terraform.io/docs/providers/metalcloud/index.html>`_
- `CLI <https://github.com/bigstepinc/metalcloud-cli>`_
- `GO SDK <https://github.com/bigstepinc/metal-cloud-sdk-go>`_
- `User API Documentation <https://api.bigstep.com/metal-cloud>`_
- `Additional SDKs <https://api.bigstep.com/metal-cloud#api-clients>`_

