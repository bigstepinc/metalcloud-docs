# Managing networks

MetalSoft networks are designed around performance and isolation. Each network is an isolated layer 2 broadcast domain. Since there is no router or virtual switch between user's servers, the latency is minimal users being able to achieve bare metal line rate performance.

There are 3 types of networks:
1. LAN - This is a pure L2 network. MetalSoft does not allocate IPs in this network and users are free to allocate any IP range they see fit. Each network is isolated from each other. (The isolation is done using either VLANs, MPLS, VXLAN etc.)
2. WAN - This is identical to the LAN network with the exception that is features a gateway L3 interface (SVI). This gateway provides internet access to the hosts. At the same time we provide DHCP service within this network and allocate ips from a subnet configured at the infrastructure level.
3. SAN - This is a special network dedicated for SAN traffic, only present if drives are attached to server instances.



Networks are connected to server instance arrays which in turn will propagate the network configuration to all of the underlying server instances. 

## Creating a LAN network

1. Option #1
In the infrastructure editor, to create a network that connects two instance arrays CLICK AND HOLD on the circles on the top of the instance arrays and DRAG to the other desired port (circle) on the target instance array and RELEASE.

Press Deploy to effect the changes.

![](/assets/guides/network_create.gif)

2. Option #2
In the infrastructure editor, click on any of the ports and using the form select the Networks tab and input a name for the network and click Create LAN network button.

![](/assets/guides/network_create_03.png)

In the infrastructure editor, click on any of the ports (the circles on the top of instance arrays) and using the form select the network in which the respective port must be connected.

![](/assets/guides/network_create_2.png)

Press Deploy to effect the changes.

## Joining an existing network


1. Option #1

In the infrastructure editor, to join an existing network that connects two SEPARATE instance arrays click on any of the the circles that are connected with the network that you want to join and DRAG to the other desired port (circle) on the target instance array and RELEASE. Note that if you want to connect only servers within the same instance array option #2 must be used.

![](/assets/guides/network_join.gif)

Press Deploy to effect the changes.

2. Option #2

In the infrastructure editor, click on any of the ports (the circles on the top of instance arrays) and using the form select the network in which the respective port must be connected.

![](/assets/guides/network_create_2.png)

Press Deploy to effect the changes.


## Adding more IPs

MetalSoft allocates entire subnets to infrastructures not just individual IPs. By default a /29 IPv4 block is allocated that is automatically expanded (to a /28, /27 etc if more IPs are needed) or a new subnet is automatically created.

If additional ips are required (for example for Kubernetes services via MetalLB) they can be ordered via the infrastructure editor.

To configure MetalSoft to route additional IPs to your WAN network click on the Internet network icon:

![](/assets/guides/add_more_ips.png)

Then, click on add subnet and select the subnet range that you want to allocate:

![](/assets/guides/add_subnet_01.png)

![](/assets/guides/add_subnet_02.png)

