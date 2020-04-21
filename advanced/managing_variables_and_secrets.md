# Managing variables and secrets

Variables and Secrets have many uses. They allow the user to provide dynamic assets during deploy and provide means to change the way stage definitions behave. A stage definition can change a variable and another stage definition can use it. 

### Referencing variables
The variables and secrets are referenced by name in various places including in assets such as `{{MY_VAR_NAME}}`. Variables are read-write and they can be altered at any time.

### Referencing secrets
Secrets are identical to variables except they are write only. They can be replaced at any time but they cannot be retrieved and are encrypted.

### Creating a variable from console input

This will ask the user for the variable content to be inputed on the command line.

```bash
metalcloud-cli variable create -name test2 
Variable content:
```

### Creating a variable using a pipe

This will create a variable using the echo's output as content:
```bash
echo "https://172.17.108.75/" | metalcloud-cli  variable create -name vcenter -pipe
```

### Creating a secret from user input
The following will read the content from console but it will mask the user's input. No output will be shown but the content will be read.

```bash
metalcloud-cli secret create -name test3
Secret content:
```

### Creating a secret from pipe

```bash 
echo "Basic YWRtaW5pc3RyYXRvckB2c3BoZXJlLmxvY2FsOkRlbGxSMGNrcyE=" | metalcloud-cli secret create -name vcenter_creds -pipe
```



