# Authenticating to the DataLake using kerberos utilities

The DataLake service uses kerberos to vierify identity of users. The DataLake CLI performs this step automatically but if the WebHDFS is used using CURL, preliminary kerberos authentication is required.

Kerberos credentials can be obtained from the infrastructure editor at [cloud.bigstep.com](https://cloud.bigstep.com) and an utility called `kinit` is used to obtain an authentication **ticket**.

![](/assets/guides/managing_datalake_permissions.png)

## Installing kerberos utilities in MacOS X

Already built into the operating system

## Installing kerberos utilities in CentOS/Redhat
```bash
yum -y install krb5-workstation
```
## Installing kerberos utilities in Ubuntu
```bash
apt-get install krb5-user
```

`kinit` requires a file called `krb5.conf`, containing the Kerberos server address, the ticket defaults, and other configuration information. The configuration information is also retrieved from the Bigstep Infrastructure editor.

Place this file into the `/etc` directory on your system.

```bash
$ kinit k233
k233@api.bigstep.com's Password: 
```

```bash
$ klist
Credentials cache: API:3625966A-C8BA-4DA4-A17D-A5F22E328F2D
Principal: k233@api.bigstep.com


Issued                Expires               Principal
Jun 18 17:22:43 2015  Jun 19 17:22:36 2015  krbtgt/ikrb.bigstepcloud.com@krb.bigstepcloud.com
```

## Creating a keytab

Tickets are stored in the client OS's system-wide cache and can be used by multiple applications simultaneously. 
 
To avoid entering the password each time `kinit` is used (for instance in a script), a keytab file can be provided. It stores the hash of the password that is sent to the server to retrieve the ticket.

Creating a keytab file depends on the operating system used, however it should be fairly straightforward. 
Multiple hashes with different hashing algorithms can be used (created with different encryption types), for maximum compatibility.

As tickets expire after a while, they can be renewed without entering the password by issuing either `kinit -R` or by using a daemon called `k5start`.

## Destroying a Kerberos ticket

The tickets can be destroyed by using kdestroy:

```bash
$ kdestroy
```

Destroying the tickets will not close browser/CURL active sessions. The user must manually delete all the cookies or cookie jars associated with these sessions.
