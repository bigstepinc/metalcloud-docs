# Managing Operating System deployment options

Starting with version 4.10 MetalSoft introduced support for Virtual Media based Operating system deployments. 

This has many advantages over the legacy PXE mechanism:
1. Faster provisioning due to no transient deployment (Quarantine) network being required.
2. No need for bridging to the in-band network enabling air-gapped management networks. 
3. No need for internet access or a repository with the operating system binaries.
4. No need for DHCP relay setups on switches

The legacy PXE-based mechanism is still supported. A server registration process will determine if a server supports virtual media based deployments and will mark the server as such.

> Note: A different server type is required to enable virtual media on a server. This new server type will be created automatically upon registration if BMC based registration is used to register a server. For example if a server is registered via the legacy "BDK"-based mechanism is to be used with virtual media, a new v2 server type will be created if the server is re-registered using the "BMC"-based mechanism.

If a server does not support virtual media based deployments and the legacy system is activated the system will use the legacy deployment mechanism. 

Note however that operating system templates are not compatible across modes. A virtual media template is not compatible with PXE deployment and vice-versa. 

### Enabling the virtual media based deploy mechanism and configuring it as default

1. Navigate to **Datacenters** > **Datacenter** > **Configuration** > **Show more**:
2. Select **Enable legacy server operations**
3. Set the default deployment mechanism to **Virtual Media**
4. Set the default cleanup and registration mechanism to **BMC**

![](/assets/advanced/managing_operating_system_deployment_options_01.png)



### Enabling the legacy PXE-based deploy mechanism and configuring it as default.

1. Navigate to **Datacenters** > **Datacenter** > **Configuration** > **Show more**:
2. Select **Enable legacy server operations**
3. Set the default deployment mechanism to **PXE**
4. Set the "default cleanup and registration mechanism" to **BDK**

![](/assets/advanced/managing_operating_system_deployment_options_02.png)

