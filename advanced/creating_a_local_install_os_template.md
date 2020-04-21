# Creating a custom local install OS template

Operating systems are central to the utilization of servers by end-users. Operating System templates ar provided out of the box (CentOS, Ubuntu, Windows) but users to create new 'templates' by customizing the provided template's bootloader, bootloader config files and any other asset pulled from the TFTP server during the servers' install or regular boot process.

Users will see the new "custom template" in the list of templates associated to a drive.

> Note: Only local install templates are customizable this way. iSCSI volume templates use copy on write which is a separate mechanism. Reffer to [creating an ISCSI OS template](/advanced/creating_an_iscsi_os_template) for more details.

OS templates provide a mechanism to fully customize the deployment and boot process of a server by:
1. Providing a series of special assets such as a bootloader and a bootloader config assets
2. Providing a list of assets to be served
3. Providing a list of secrets & variables

The OS template is a property that can be used instead of a volume_template of an instance or as a special OS Install stage in the Workflow system.

### An example install process

The following is a custom install process, based on kickstart, with no utility OS booted that is possible:
![an example install process](/assets/advanced/os_templates_1.svg)


### Creating a new OS template using the CLI


1. Download the ISO and upload the files to the repo

2. Create a new asset for the bootloader (as an URL):
```bash
metalcloud-cli asset create -url "https://repointegration.bigstepcloud.com/.tftp/boot/uefi-esxi/bootx64.efi" -filename "esxi.efi" -mime "application/octet-stream" -usage "bootloader"

```

3. Create a new `boot.cfg` file to configure the bootloader

```bash
bootstate=0
title=Loading ESXi installer
timeout=5
prefix=/images/ESXi
kernel=b.b00
kernelopt=ks=http://172.17.107.2/tftp8069/ks-01-mac.cfg ip=dhcp
modules=jumpstrt.gz --- useropts.gz --- features.gz --- k.b00 --- chardevs.b00 --- user.b00 --- procfs.b00 --- uc_intel.b00 --- uc_amd.b00 --- uc_hygon.b00 --- vmx.v00 --- vim.v00 --- sb.v00 --- s.v00 --- ata_liba.v00 --- ata_pata.v00 --- ata_pata.v01 --- ata_pata.v02 --- ata_pata.v03 --- ata_pata.v04 --- ata_pata.v05 --- ata_pata.v06 --- ata_pata.v07 --- block_cc.v00 --- bnxtnet.v00 --- bnxtroce.v00 --- brcmfcoe.v00 --- char_ran.v00 --- ehci_ehc.v00 --- elxiscsi.v00 --- elxnet.v00 --- hid_hid.v00 --- i40en.v00 --- iavmd.v00 --- igbn.v00 --- ima_qla4.v00 --- ipmi_ipm.v00 --- ipmi_ipm.v01 --- ipmi_ipm.v02 --- iser.v00 --- ixgben.v00 --- lpfc.v00 --- lpnic.v00 --- lsi_mr3.v00 --- lsi_msgp.v00 --- lsi_msgp.v01 --- lsi_msgp.v02 --- misc_cni.v00 --- misc_dri.v00 --- mtip32xx.v00 --- ne1000.v00 --- nenic.v00 --- net_bnx2.v00 --- net_bnx2.v01 --- net_cdc_.v00 --- net_cnic.v00 --- net_e100.v00 --- net_e100.v01 --- net_enic.v00 --- net_fcoe.v00 --- net_forc.v00 --- net_igb.v00 --- net_ixgb.v00 --- net_libf.v00 --- net_mlx4.v00 --- net_mlx4.v01 --- net_nx_n.v00 --- net_tg3.v00 --- net_usbn.v00 --- net_vmxn.v00 --- nfnic.v00 --- nhpsa.v00 --- nmlx4_co.v00 --- nmlx4_en.v00 --- nmlx4_rd.v00 --- nmlx5_co.v00 --- nmlx5_rd.v00 --- ntg3.v00 --- nvme.v00 --- nvmxnet3.v00 --- nvmxnet3.v01 --- ohci_usb.v00 --- pvscsi.v00 --- qcnic.v00 --- qedentv.v00 --- qfle3.v00 --- qfle3f.v00 --- qfle3i.v00 --- qflge.v00 --- sata_ahc.v00 --- sata_ata.v00 --- sata_sat.v00 --- sata_sat.v01 --- sata_sat.v02 --- sata_sat.v03 --- sata_sat.v04 --- scsi_aac.v00 --- scsi_adp.v00 --- scsi_aic.v00 --- scsi_bnx.v00 --- scsi_bnx.v01 --- scsi_fni.v00 --- scsi_hps.v00 --- scsi_ips.v00 --- scsi_isc.v00 --- scsi_lib.v00 --- scsi_meg.v00 --- scsi_meg.v01 --- scsi_meg.v02 --- scsi_mpt.v00 --- scsi_mpt.v01 --- scsi_mpt.v02 --- scsi_qla.v00 --- sfvmk.v00 --- shim_isc.v00 --- shim_isc.v01 --- shim_lib.v00 --- shim_lib.v01 --- shim_lib.v02 --- shim_lib.v03 --- shim_lib.v04 --- shim_lib.v05 --- shim_vmk.v00 --- shim_vmk.v01 --- shim_vmk.v02 --- smartpqi.v00 --- uhci_usb.v00 --- usb_stor.v00 --- usbcore_.v00 --- vmkata.v00 --- vmkfcoe.v00 --- vmkplexe.v00 --- vmkusb.v00 --- vmw_ahci.v00 --- xhci_xhc.v00 --- elx_esx_.v00 --- btldr.t00 --- esx_dvfi.v00 --- esx_ui.v00 --- esxupdt.v00 --- weaselin.t00 --- lsu_hp_h.v00 --- lsu_inte.v00 --- lsu_lsi_.v00 --- lsu_lsi_.v01 --- lsu_lsi_.v02 --- lsu_lsi_.v03 --- lsu_lsi_.v04 --- lsu_smar.v00 --- native_m.v00 --- qlnative.v00 --- rste.v00 --- vmware_e.v00 --- vsan.v00 --- vsanheal.v00 --- vsanmgmt.v00 --- tools.t00 --- xorg.v00 --- imgdb.tgz --- imgpayld.tgz
build=
updated=0
```

4. Create a new asset with the bootloader config file `boot.cfg` file (as a text file). You can name th asset's filename in any way you see fit. It will be mapped to the proper path later.
```bash
cat boot.cfg | metalcloud-cli asset create -filename "esxiboot.cfg" -mime "text/plain" -pipe
```
5. Create a new secret to hold the password of the template

```bash 
echo "Basic YWRtaW5pc3RyYXRvckB2c3BoZXJlLmxvY2FsOkRlbGxSMGNrcyE=" | metalcloud-cli secret create -name rootpw -pipe
```

6. Create a new file to configure the install process: `ks-01-mac.cfg`
```bash
#### Tested with: ESXi 6.7

### Accept the VMware End User License Agreement
vmaccepteula

# Set the root password
rootpw {{rootpw}}

# Clear paritions and install
clearpart --firstdisk --overwritevmfs
install --firstdisk --overwritevmfs

# Set the network to DHCP on the first network adapter
network --bootproto=dhcp --device=vmnic0

### Reboot ESXi Host
reboot --noeject

%firstboot --interpreter=busybox

# enable & start SSH
vim-cmd hostsvc/enable_ssh
vim-cmd hostsvc/start_ssh

# enable & start ESXi Shell
vim-cmd hostsvc/enable_esx_shell
vim-cmd hostsvc/start_esx_shell

# Suppress ESXi Shell warning
esxcli system settings advanced set -o /UserVars/SuppressShellWarning -i 1

%post --interpreter=python --ignorefailure=true
import time
stampFile = open('/finished.stamp', mode='w')
stampFile.write( time.asctime() )
```

7. Create new asset (as a text file):
```bash
cat ks-01-mac.cfg | metalcloud-cli  asset create -filename "ks-01-mac.cfg" -mime "text/plain" -pipe
```

8. Create an OS template for ESXI.
```bash
metalcloud-cli os-template create -label esxi -name esxi -initial-password 'Setup00!' -template-architecture uefi -os-architecture x86 -os-type ESXi -os-version 1  -description "installs esxi" -initial-user "root"  -initial-ssh-port 22 -boot-type uefi-only -local-disk-supported
```

9. Associate all assets to the template with their respective paths
```bash
metalcloud-cli  asset associate -id 'bootx64.efi' -template_id esxi -path '/bootx64.efi'
metalcloud-cli asset associate -id 'esxiboot.cfg' -template_id esxi -path '/boot.cfg'
metalcloud-cli asset associate -id 'ks-01-mac.cfg' -template_id esxi -path '/ks-01-mac.cfg'
```

### Choosing an architecture

Since multiple types of servers and architectures need to be supported, the [PXE protocol RFC4578](https://tools.ietf.org/html/rfc4578) provides mechanisms for distinguishing between a request made by an EFI system or a x86 system.

Excerpt from the RFC4578:
As of the writing of this document, the following pre-boot architecture types have been requested:

            Type   Architecture Name
            ----   -----------------
              0    Intel x86PC
              1    NEC/PC98
              2    EFI Itanium
              3    DEC Alpha
              4    Arc x86
              5    Intel Lean Client
              6    EFI IA32
              7    EFI BC
              8    EFI Xscale
              9    EFI x86-64

The property `volume_template_architecture` receives one of the above. The most important ones are 0 (Intel x86PC) which is the default and 7 (EFI BC) which is the default for EFI servers.

If the server does not boot using the OS template you are building check the DHCP packet log and identify the value sent in the `Client System Architecture (DHCP option 93)` field. 

### Specifying a bootloader and config file

You can specify any asset in the `os_asset_id_bootloader` field as long as the binary is in the right architecture.

### Specifying a custom config for iPXE

Some bootloaders (namely `iPXE`) request config via DHCP by making a request with a specific `User Class (DHCP option 77)` matching `^iPXE$`. Specify the config file to be returned by setting the `os_asset_usage` property to `ipxe_config_local_install` or `ipxe_config_os_boot` depending on where is the asset to be used.

### Associating assets with OS Templates

Before use assets need to be associated with a template which in effect creates a mapping between a path  (eg: `/vmlinuz`) and an asset in the context of an OS template. Use the UI's OS template assets tab to add an asset to an OS template. If you are using the API use the `os_template_os_asset` function to perform this association.

See the [Managing assets](/advanced/managing_assets) section for more details.

### Important variables

A special variable is part of the execution context `{{HTTP_SERVER_ENDPOINT}}` and points to the closest **tftp/http** agent.
More details on variables can be found at [managing variables and secrets](/advanced/managing_variables_and_secrets).