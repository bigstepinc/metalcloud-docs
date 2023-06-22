# Configure Okta for SAML authentication

The whole process can be divided in 2 steps:
1.	Configuring Okta.
2.	Configuring Metalsoft App to use Okta, configured in step 1 “Configuring Okta”.


Step 1. Configuring Okta
1.	Create an app in Okta
![](/assets/guides/create_a_new_app_integration_okta.png)
![](/assets/guides/create_saml_integration_okta_1.png)
![](/assets/guides/create_saml_integration_okta_2.png)

Single sign-on URL should be https://<<domain>>/cloudv1/en/login?saml_auth=1 

Audience URI (SP Entity ID) may be any, can be used https://<<domain>> 

![](/assets/guides/okta_attribute_statements.png)

It is mandatory to have attributes in Attribute Statements (optional) section as on the example above.

The Metalsoft app expects the following attributes in the left column email, role, objecGUID, sAMAccountName . However, the values in the right column may differ from the example.

email - This attribute represents the email address that will be used in the Metalsoft app.

role - This attribute indicates the user's role in the Metalsoft app (e.g., root, user, full_admin, etc.).

objecGUID - This attribute should be a unique value associated with the user. In the given example, the custom attribute 'user.objectGUID' is used, but it can be mapped to any unique attribute associated with the user.

sAMAccountName - This attribute represents the user's username. For example, if the user's email is 'john.doe@domain.com', the corresponding username could be 'John Doe'. In the example above, sAMAccountName is mapped to 'user.sAMAccountName', but it can be mapped to any attribute that corresponds to the username.

![](/assets/guides/create_a_new_app_integration_okta_2.png)
![](/assets/guides/create_a_new_app_integration_okta_3.png)

After pressing “Finish“ the app will be created.

2. Assign a user to the app
![](/assets/guides/assign_user_to_okta_app_1.png)
![](/assets/guides/assign_user_to_okta_app_2.png)
![](/assets/guides/assign_user_to_okta_app_3.png)
![](/assets/guides/assign_user_to_okta_app_4.png)
![](/assets/guides/assign_user_to_okta_app_5.png)
![](/assets/guides/assign_user_to_okta_app_6.png)

Step 2. Configuring Metalsoft App for using Okta configuration.

In step 1, we created an app named "saml-test." For step 2, it is necessary to integrate Okta's app with the Metalsoft app. Okta will provide the configuration data required by the Metalsoft app. Please follow the steps below:

![](/assets/guides/okta_configuration_1.png)
![](/assets/guides/okta_configuration_2.png)
![](/assets/guides/okta_configuration_3.png)
![](/assets/guides/okta_configuration_4.png)

Identity Provider Single Sign-On URL, Identity Provider Issuer, X.509 Certificate will be used in the Metalsoft app.

![](/assets/guides/ms_okta_config_1.png)

In the Metalsoft app go to Global configuration → Authentication
![](/assets/guides/ms_okta_config_2.png)

Enable Enable SAML Authentication.

<<Metalsoft app prop>> = <<okta provides>>

SAML entrypoint URL = Identity Provider Single Sign-On URL

SAML Issuer URL = Identity Provider Issuer

SAML Callback URL = https://<<domain>>/en/login 

SAML Logout URL = don’t know how to get it in Okta (can be used https://<<domain>> as placeholder, because can’t be empty)

SAML Certificate = X.509 Certificate

SAML Allowed domains = The domains of email addresses that will be subjected to SAML treatment on the login page. (eg. domain.com, gmail.com)
![](/assets/guides/ms_okta_config_3.png)

After saving config, SAML should work. You may try to login.
![](/assets/guides/ms_okta_config_4.png)
![](/assets/guides/ms_okta_config_5.png)
![](/assets/guides/ms_okta_config_6.png)

If the SAML Logout URL is not configured properly in the Metalsoft app or if a placeholder is passed, the Single Log Out functionality will not work correctly. Simply logging out from the Metalsoft app will not be sufficient for a complete logout. To achieve a full logout, it is also necessary to log out from Okta.

