# Managing users and permissions

Security and access control is a very important aspect of any infrastructure.  The MetalCloud supports many scenarios but might be a bit atypical in the way it handles users and permissions, relying heavily on a concept called Delegation.

## User accounts

All who interact with the MetalCloud must have an "account" identified by email and password, API key and - if enabled - protected by 2FA.

Users can have multiple roles assciated with them:
* Account delegate of another user
* Infrastructure delegate


## Example scenario

To help understand the various options available consier the following scenario:
1. **A billing account** (finance@company.com) is created using an email that will reach the department in charge with paying the invoices. The department will not actualy manage infrastructures but will receive invoices.
2. **An OPS account** (ops@company.com) is added by the finance department as an account delegate of the finance account. 
4. The ops account is now able to create infrastructures: **A Web Infrastructure** for the marketing department, a **Hadoop infrastructure** for the BI department and an **ERP infrastructure** for the Logistics department
5. The Ops user then invites user mktg@company.com form the marketing department to the Web infrastructure using infrastructure delegation.
6. The Ops user also invites user logistics@company.com form the logstics department to the ERP infrastructure using infrastructure delegation.
7. Lastly, the Ops user invites user bi@company.com form the BI department to the Hadoop and the ERP infrastructures using infrastructure delegation.

![](/assets/guides/managing_users_and_permissions_1.svg)


The result of this setup is that:
* OPS has the ability to oversee and manage all infrastructures
* Marketing and logistics departments each manage their own infrastructures only
* BI team has access to it's infrastructure (the hadoop infrastructure) but also to the ERP infrastructure
* The Finance team then receives invoices for all infrastructures.

* The detailed infratructure utilization report will provide a breakdown of consumtion for each individual department which enables chargeback to the respective departments. 



## The "Billable" account

Only infrastructures that are owned by a "Billable" account can be deployed.

Normally in an organization only one account will have Billing activated such as by adding a credit card.

Invoices for all infrastructures owned by this user will be issued on the company or individual information listed on this account.

For more information on how to enable billing on an account see the [Managing billing information](/guides/managing_billing_information) section.

## Managing account delegation

Many organizations opt to have a finance/procurement department user as the billable user and have a second user as the technical user that actually performs operations "on-behalf-of" the organization. This relationship is called "account delegation".

If enabled this second user will have all rights that the owner of the infrastructures has.

Any number of users can be account delegates.

To add an account delegate access **Account Settings** (Infrastructure Editor > Account Settings)

![](/assets/guides/managing_users_and_permissions_2.png)

Click on **Account sharing** (Infrastructure Editor > Account Settings > Account Sharing)

![](/assets/guides/managing_users_and_permissions_3.png)

Add the email address of the delegated user that the user uses to login to manage the Metalcloud.

![](/assets/guides/managing_users_and_permissions_4.png)

As a delegated account, from this page you can also **Impersonate**  a user in order to perform payments or change credit card information on his/hers behalf.

This mechanism can be used if the primary account is a technical one somebody else needs to perform manual payment, download invoices etc.

## Managing infrastructure delegation

A user can be "invited" by an owner or account delegate of an infrastructure to have access only to that respective infrastructure. This is used in situations where internal users or clients of a company reselling MetalCloud services need to have access to a specific infrastructure. 

Users will have full access to manage that infrastructure but the billable account that is the ower of the infrastructure will receive the invoices.

To add a delegate on an infrastructure access the **Infrastructure properties** dialog by clicking the the cogwheel:

![](/assets/guides/managing_users_and_permissions_5.png)

Click on the **Sharing** tab and enter the login email of the user that is to be granted permissions.  The user will receive an invite email on that address.

![](/assets/guides/managing_users_and_permissions_6.png)

If the user doesn't have a MetalCloud account he will be invited to create one but no CC information will be required.


Where to go from here:
* [Retrieving the utilization report](/guides/retrieving_the_utilization_report)
* [Managing billing information](/guides/managing_billing_information)

