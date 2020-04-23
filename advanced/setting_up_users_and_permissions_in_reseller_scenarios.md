# Setting up users and permissions in reseller scenarios

In reseller scenarios such as when a development agency uses the Metal Cloud to handle the infrastructure of its clients the user configuration must be setup to allow both client access and billing in a manner that matches the business model of the reseller.

There are primarly two types of business models:

1. When the MetalCloud has a direct contract with the End-User (Referral scenario)

    ![](/assets/advanced/setting_up_users_and_permissions_in_reseller_scenarios_2.svg)

2. When the MetalCloud has a direct contract with the Reseller (Reseller scenario)

    ![](/assets/advanced/setting_up_users_and_permissions_in_reseller_scenarios_3.svg)


## Setting up users and permissions in a referral scenario when end-users own the infrastructures

In some situations resellers preffer to only provide certain services such as manage an infrastructure owned by a 3rd party company (called here end-user).

Typically the reseller wants to be able to:
* Manage all infrastructures of all clients form a single location
* Ensure security segregation between all clients

To achieve the above, the end-clients would setup the relationships like this:

![](/assets/advanced/setting_up_users_and_permissions_in_reseller_scenarios_5.svg)



1. An ops account of **Company 1** creates **client1 infra 1** and **client1 infra 2** (just the infrastructures without the servers).

2. The same ops account of **Company 1** adds **ops@resller.com** account as an infrastructure delegate for infrastructures: **client1 infra 1** and **client1 infra 2**

3. An ops account of **Company 2** creates **client2 infrastructure1 **
2. The same ops account of **Company 2** adds **ops@resller.com** account as an infrastructure delegate for infrastructures: **client 2 infra 1**

3. The reseller ops account (ops@reseller.com) can now manage all 3 infrastructures.
4. The billing user (or the ops user depending on the situation) of both Company 1 and Company 2 will then receive invoices for their respective utilizations. 


## Setting up users and permissions in a fully managed reseller scenario

Most resellers preffer to have a direct business relationship with the end client. In fully managed scenario the end-users do not have access to the MetalCloud environment.

Typically the reseller wants to be able to:
* Receive a single invoice for all services
* Manage all infrastructures of all clients form a single location
* Ensure security segregation between all clients
* Retrieve the on-demand utilization of each end-client in order to issue invoices to the respective clients (manually or programatically).

To achieve the above, a reseller would setup the relationships like this:

![](/assets/advanced/setting_up_users_and_permissions_in_reseller_scenarios_4.svg)

1. **A billing account** (finance@reseller.com) is created using an email that will reach the department in charge with paying the invoices. The department will not actualy manage infrastructures but will receive invoices.
2. **An OPS account** (ops@reseller.com) is added by the finance department as an account delegate of the finance account. 
4. The ops account is now able to create infrastructures for each individual client.
5. The billing user will then be able to [retrieve the on-demand utilization report](/guides/retrieving_the_utilization_report) on a per infrastructure basis and issue separate invoices for each client.


## Setting up users and permissions in a reseller scenario when end-users have access to infrastructures

In some situations resellers preffer to maintain a direct commercial relationship while also allowing their clients to access the MetalCloud in order to retrieve access credentials or even manage infrastructures directly.

Typically the reseller wants to be able to:
* Receive a single invoice for all services
* Manage all infrastructures of all clients form a single location
* Ensure security segregation between all clients
* Retrieve the on-demand utilization of each end-client in order to issue invoices to the respective clients (manually or programatically).
* Allow users from individual clients to access certain infrastructures but not others

To achieve the above, a reseller would setup the relationships like this:

![](/assets/advanced/setting_up_users_and_permissions_in_reseller_scenarios_1.svg)

1. **A billing account** (finance@reseller.com) is created using an email that will reach the department in charge with payments. The department will not actualy manage infrastructures but will receive invoices.
2. **An OPS account** (ops@reseller.com) is added by the finance department as an account delegate of the finance account. 
4. The ops account is now able to create infrastructures for each individual client.
5. The ops account will now invite ops@company1.com to manage the two infrastructures of company 1.
6. The ops account will also invite ops@company2.com to manage the infrastructure of company 1.
7. The billing user will then be able to [retrieve the on-demand utilization report](/guides/retrieving_the_utilization_report) on a per infrastructure basis and issue separate invoices for each client.

Where to go from here:
* [Managing users and permissions](/guides/managing_users_and_permissions)
* [Managing billing information](/guides/managing_billing_information)
* [Retrieving the utilization report](/guides/retrieving_the_utilization_report)