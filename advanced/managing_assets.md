# Managing assets

Assets are files that are served at appropriate times via the DHCP, TFTP and HTTP mechanisms during PXE or ONIE.

There are 3 types of assets:
1. text files stored in the DB (size limited to 4MB). These can also hold references to [variables or secrets](/advanced/managing_variables_and_secrets). MIME type: `text/plain`
2. binary files stored in the DB (size limited to 64MB). MIME type: `application/octet-stream`
3. external files referenced as an URL. MIME type: `text/plain`, `application/octet-stream`

## Using text assets as file templates

If enabled, text files stored in the db can act as a template. When they need to be served t the user via HTTP or TFTP a search_and_replace will be executed for strings matching the provided list of params with the format `{{<VARIABLE_NODE>}}`.

See [Managing Variables and Secrets](/advanced/managing_variables_and_secrets) for more details.

## Creating an URL asset

```bash
metalcloud-cli asset create -url "%repoURL%/.tftp/boot/uefi-windows/bootx64.efi" -filename "bootx64.efi" -mime "application/octet-stream" -usage "bootloader" -return-id
```

## Creating a text asset

Creating an asset from a pipe:

```bash
echo "test" | metalcloud-cli asset create -filename "test.xxx" -mime "text/plain" -pipe -return-id
```

## Creating a binary asset from pipe

```bash
cat data.bin | metalcloud-cli asset create -filename "data.bin" -mime "application/octet-stream" -pipe -return-id
```


## Associating assets with templates

Before assets can be used they need to be associated with a specific OS template. Associating an asset with a template at a specific path (`/bootx64.efi`). 

```bash
metalcloud-cli asset associate -id "bootx64.efi" -template-id windows2019 -path "/bootx64.efi"
```

During the install process, the fill be accesible at `{{HTTP_SERVER_ENDPOINT}}/bootx64.efi`. For more information visit [Creating a local install os template](/advanced/creating_a_local_install_os_template)

## List assets
```bash
metalcloud-cli  asset list
```

## Deleting an asset

```bash
metalcloud-cli  asset delete -id 10023
```
