# Delegating access to an infrastructure

This article details how primary users (billable account owners) can grant other users administrative privileges over their infrastructures or revoke them.

 This can be done on an infrastructure by infrastructure basis or as a global action, delegating a user with administrative access over all already existing infrastructures, as well as all infrastructures that will be created in the future.

 A delegated user or a user with administrative rights over an infrastructure can deploy, create, edit and delete operations for infrastructure elements and can access all resources as their own. All on demand use is billed to the user who owns the infrastructure, not to the invested users.

 The granting of administrative privileges is a one-way process. Users who grant other users administrative rights will not receive any rights on those users' infrastructures, for security reasons.

 Once a user has been added as a delegate or has been granted privileges on a single infrastructure, that user's list of public SSH keys will be added to all newly provisioned drives. Existing active drives will not be affected, and users will have to manually add those keys should they wish to use them.

 Privileges can be revoked from the same interface pages with a simple click. Please note that any SSH keys copied to drives during provisioning while those users had administrative privileges are not automatically removed, and it is recommended to manually remove them from all active drives for security reasons.

 **Grant a user administrative rights over all your infrastructures**

 1. From the Bigstep infrastructure editor, click on the arrow next to your account name in the top right, then select **Account Settings**.

 ![](/assets/guides/user_management_1.png)

 2.In the next window, click on **Account sharing**.

 ![](/assets/guides/user_management_2.png)

 3.In the **Delegate children** section, enter the Bigstep login email address of the user whom you want to grant administrative privileges to. Users who don't already have a Bigstep account will have one created for them automatically, and an activation email will be sent to the provided address.

 ![](/assets/guides/user_management_3.png)

 4.The user has now been added as an administrator over all your existing as well as any future infrastructures. An activation email has been sent to the provided email address, and once the user clicks the link in the message he will be able to create, edit, and deploy elements on your infrastructures.

 ![](/assets/guides/user_management_4.png)

 The user is also visible in the Delegate children section, and you can remove him anytime if you wish.

  **Grant a user administrative rights over a single infrastructure**

 1. From the infrastructure editor, click on the wheel settings button to open the **Infrastructure properties** menu.

 ![](/assets/guides/user_management_5.png)

 2.Open the **Sharing** tab.

 ![](/assets/guides/user_management_6.png)

 3.Enter the Bigstep login email address of the user whom you want to grant administrative privileges to, then click on **Grant access**.

 ![](/assets/guides/user_management_7.png)

 If there is no user account associated with the email address, you can create one automatically by clicking on **Send invite**.

 ![](/assets/guides/user_management_8.png)

 An activation email has been sent to the provided email address, and once the user clicks the link in the message, he will be able to create, edit, and deploy elements on your infrastructure.

 Please note that he will only have administrative privileges over this particular infrastructure, and will not be able to access any other infrastructures that you might have or create in the future.

 Users with access on all of your infrastructures through account-level sharing are also visible in this tab.

 ![](/assets/guides/user_management_9.png)

See [Managing users and permissions](/guides/managing_users_and_permissions) for more details.