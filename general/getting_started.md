# Getting started with the Metal Cloud

Metalcloud is very easy to operate but it does have some unique concepts. This short introductory tutorial will walk you through deploying a server and retrieving access credentials while also explaining the various Metalcloud concepts.

Before you start make sure you have created an account with us by signing up [here](https://my.bigstep.com/en/signup?redirect_url=https://cloud.bigstep.com/en/infrastructure/diagram)

### Creating an instance array using the Infrastructure Editor

In the MetalCloud servers (called **Instances**) are groupped in **InstanceArrays**. By default an infrastructure is created for you called "my-infrastructure" in a datacenter geographically close to you.

1. Click on the `Create your first InstanceArray`

    ![](/assets/guides/getting_started3.png)

2. Select your configuration, number of servers, operating system, drive size and boot type. The server will not be deployed now but rather will wait for the Deploy button to be clicked. (step #5)

    Certain servers types support deploying the operating system on a local drive (or a collection of local drives in an RAID 0 array). Local drives do not allow switching the server but are less expensive and carry higher capacities and, if using local NVMes higher performance.

    ![](/assets/guides/getting_started5.png)

    You will notice that a structure has been created on your UI:

    ![](/assets/guides/getting_started7.png)

    it Includes both an instance array and a drive array both with a count of 1. That is normal. If you want to perform further modifications such as firewall rules or selecting another configuration by click on it.

3. Select firewall configuration

    By default all traffic is blocked except if it originates from what our systems detects as being your IP. You need to explicitly enable additional IPs or ports before you deploy.

    ![](/assets/guides/getting_started41.png)

4. Deploy the infrastructure

    Operations in the Metal Cloud are not immediatelly deployed. In fact they can be reverted until the infrastructure is "Deployed".
    Click on the big "Deploy" button from the bottom of the screen.
    ![](/assets/guides/getting_started61.png)

    The deploy operation should take between 3 and 10 minutes. At the end of it the *instance array* will be in an `active` state.

5. After the deploy the *instance array* is in "active" state. Click on the instance array:

    ![](/assets/guides/managing_instance_arrays1.png)

    This will pop-up the access credentials window:

    ![](/assets/guides/managing_instance_arrays2.png)

    Here you can find, for each instance (server):
    1. the quick ssh access link
    2. root password

    >Note: It is recommended that you register your public SSH key in the **Account settings** section so that it gets automatically added on the hosts at deploy time.

Where to go from here:
1. [A short 5 minute introductory video](https://www.youtube.com/watch?v=vcVxZgc82D0&t=8s)
2. [Managing infrastructures](/guides/managing_infrastructures)
3. [Managing instance arrays](/guides/managing_instance_arrays)
