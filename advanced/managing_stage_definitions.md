# Managing stage definitions

>Note: Support for workflows is experimental and subject to change

Stage definitions describe a stage that can be added in to one or many workflows.

There are several types of stage types:

1. HTTPRequest
2. AnsibleBundle
3. WorkflowReference

In addition we provide several out of the box stages that allow the users to build fully custom provisioning workflows.


### Creating a new stage definition

A programmatic example on how to create your own HTTP Request stage:


### HTTP Request stages

HTTP Requests stage definitions are very powerful and they provide a more or less universal mechanism that can be used to issue API calls, retrieve assets etc.

Any of the fields in stage_definition, such as the URL or 'Authentication' header field can be references to variables or secrets so that the stage can be parametrized for each situation in which it is used such as Authorization or Cookie fields.

```bash
$ metalcloud-cli new stage_def -label "vcenter-login" -title "vcenter-login" -type "HTTPRequest" -http_request_method GET -http_request_url='{{vcenter}}/rest/com/vmware/cis/session' -vars "vcenter"
```

#### HTTPRequest cookie jar

The system maintains a "cookie jar" so that an login HTTP request ca be followed by subsequent HTTP Requests that reuse an auth token stored in a cooke.




### Ansible Bundle stages

Ansible is a very powerful tool to effect changes on one or more hosts via SSH. This stage can affect multiple hosts at the same time if the Workflow has been attached to an infrastructure.

An StageDefinition.stage_definition holds a .zip file which contains an Ansible project's files. The root directory of the .zip file must have a main.yml file as the only execution entry point.

The projects in the .zip files must not contain the variables, private keys or inventory files. They are provided automatically when executing the Ansible project.

Ansible Bundle projects can be executed in the context of an infrastructure. 
When executed:
the variables.json file is created automatically (no need to provide one in your Ansible project)

To create a new ansible stage using the cli:
```bash
$ metalcloud-cli new stage_def -label "ansible1" -title "ansible1" -type "AnsibleBundle" -ansible_bundle_filename "/test/bundle1.zip"
```
 
#### Ansible Bundle inventory file 
The inventory file is created automatically with all active servers at the moment of execution (`instance_array_label` as group key and with `instance_label` as server key).
 
the private keys necessary for SSH provisioning for all the servers are added to the bundle as individual files


The variables file is populated with secrets() where the secret_label is used as variable name.

When the stage is executed "pre_deploy" then these variables are also available:
* `will_be_removed_instance_hostnames`
* `will_be_added_instance_hostnames`
* `will_be_active_instance_hostnames`


When the stage is executed "post_deploy" then these variables are also available:
* `removed_instance_hostnames`
* `added_instance_hostnames`


The instances_hostnames variable is always populated with the currently active instances' subdomains.


The generated inventory file is similar to this example:
```ini
[instance-array-48]
instance-36	ansible_ssh_user='root' ansible_ssh_host='192.168.138.130' ansible_ssh_private_key_file='instance-36.bigstep.local.io.private.key' host_fqdn='instance-36.bigstep.local.io' instance_ipv4='192.168.138.130' instance_ipv4_cidr='192.168.138.130/30' instance_ipv4_subnet_mask='255.255.255.252' instance_subdomain_permanent='instance-36.bigstep.local.io' 

[instance-array-49]
instance-39	ansible_ssh_user='root' ansible_ssh_host='192.168.138.131' ansible_ssh_private_key_file='instance-39.bigstep.local.io.private.key' host_fqdn='instance-39.bigstep.local.io' instance_ipv4='192.168.138.131' instance_ipv4_cidr='192.168.138.130/30' instance_ipv4_subnet_mask='255.255.255.252' instance_subdomain_permanent='instance-39.bigstep.local.io' 
instance-37	ansible_ssh_user='root' ansible_ssh_host='192.168.138.132' ansible_ssh_private_key_file='instance-37.bigstep.local.io.private.key' host_fqdn='instance-37.bigstep.local.io' instance_ipv4='192.168.138.132' instance_ipv4_cidr='192.168.138.130/30' instance_ipv4_subnet_mask='255.255.255.252' instance_subdomain_permanent='instance-37.bigstep.local.io' 
```

### WorkflowReference stages

This is an utility stage that allows an workflow to call another workflow allowying you to build a tree fo workflows.

```bash
$ metalcloud-cli new stage_def -type WorkflowReference -title "call test workflow" -label callwf1 -workflow test
```

### Listing stages
To list stage definitions available to the current user:
```bash
$ metalcloud-cli list stages
Stage Definitions I have access to as user alex.d@bigdstep.com:
+-------+-------------------+------------------+-------------+-------------+-----------------------------------------------------+----------------------------------------------------------------+----------------------+----------------------+
| ID    | LABEL             | TITLE            | DESCRIPTION | TYPE        | VARS_REQUIRED                                       | DEF.                                                           | CREATED              | UPDATED              |
+-------+-------------------+------------------+-------------+-------------+-----------------------------------------------------+----------------------------------------------------------------+----------------------+----------------------+
| 322   | vcenter-login     | vcenter-login    |             | HTTPRequest | vcenter                                             | HTTP Request URI: {{vcenter}}/rest/com/vmware/cis/session     | 2020-01-31T15:26:03Z | 2020-01-31T15:26:03Z |
| 328   | vcenter-host-add  | vcenter-host-add |             | HTTPRequest | vcenter,vcenter_creds,vmware_ipv4_0                 | HTTP Request URI: {{vcenter}}/rest/vcenter/host               | 2020-01-31T16:19:35Z | 2020-01-31T16:19:35Z |
| 332   | vcenter-login2    | vcenter-login2   |             | HTTPRequest | vcenterhost                                         | HTTP Request URI: {{vcenterhost}}/rest/com/vmware/cis/session | 2020-01-31T17:52:59Z | 2020-01-31T17:52:59Z |
| 336   | vcenter-host-add3 | vcenter-host-add |             | HTTPRequest | vcenterhost,vcenter_creds2,vmware_ipv4__address_0_0 | HTTP Request URI: {{vcenter}}/rest/vcenter/host               | 2020-01-31T18:14:01Z | 2020-01-31T18:14:01Z |
+-------+-------------------+------------------+-------------+-------------+-----------------------------------------------------+----------------------------------------------------------------+----------------------+----------------------+
Total: 4 Stage Definitions
```