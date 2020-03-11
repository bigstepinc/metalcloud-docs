# Using the Terraform provider

This is a terraform plugin for controlling Bigstep Metalcloud resources.

## Terraform provider requirements


-	[Terraform](https://www.terraform.io/downloads.html) 0.12.x


## Using the Provider

A terraform `main.tf` template file, for an infrastructure with a single server would look something like this:

```javascript
provider "metalcloud" {
   user_email = var.user_email
   api_key = var.api_key 
   endpoint = var.endpoint
}

data "metalcloud_volume_template" "centos76" {
  volume_template_label = "centos7-6"
}

resource "metalcloud_infrastructure" "my-infra216" {
  
  infrastructure_label = "my-terraform-infra216"
  datacenter_name = var.datacenter
  
  prevent_deploy = true

  network{
    network_type = "san"
    network_label = "san"
  }

  network{
    network_type = "wan"
    network_label = "internet"
  }

  network{
    network_type = "lan"
    network_label = "private"
  }


  instance_array {
    instance_array_label = "exmaple-master"
    instance_array_instance_count = 2
    instance_array_ram_gbytes = 8
    instance_array_processor_count = 1
    instance_array_processor_core_count = 8

    interface{
        interface_index = 0
        network_label = "san"
    }

    interface{
        interface_index = 1
        network_label = "internet"
    }

    interface{
        interface_index = 2
        network_label = "private"
    }
    
    drive_array{
      drive_array_label = "example-master-os-drive"
      drive_array_storage_type = "iscsi_hdd"
      drive_size_mbytes_default = 49000
      volume_template_id = tonumber(data.metalcloud_volume_template.centos76.id)
    }

    firewall_rule {
      firewall_rule_description = "test fw rule"
      firewall_rule_port_range_start = 22
      firewall_rule_port_range_end = 22
      firewall_rule_source_ip_address_range_start="0.0.0.0"
      firewall_rule_source_ip_address_range_end="0.0.0.0"
      firewall_rule_protocol="tcp"
      firewall_rule_ip_address_type="ipv4"
    }
  }

  instance_array {
    instance_array_label = "example-slave"  
    instance_array_instance_count = 1
    instance_array_ram_gbytes = 8
    instance_array_processor_count = 1
    instance_array_processor_core_count = 8

    drive_array{
      drive_array_label = "example-slave-os-drive"
      drive_array_storage_type = "iscsi_hdd"
      drive_size_mbytes_default = 49000
      volume_template_id = tonumber(data.metalcloud_volume_template.centos76.id)
    }

    firewall_rule {
      firewall_rule_description = "test fw rule"
      firewall_rule_port_range_start = 22
      firewall_rule_port_range_end = 22
      firewall_rule_source_ip_address_range_start="0.0.0.0"
      firewall_rule_source_ip_address_range_end="0.0.0.0"
      firewall_rule_protocol="tcp"
      firewall_rule_ip_address_type="ipv4"
    }
  }
}


```


Initialize the provider with your API key and the api endpoint either by using environment variables or -var.

```bash
export TF_VAR_api_key="<yourkey>"
export TF_VAR_user="test@test.com"
export TF_VAR_endpoint="https://api.bigstep.com/metal-cloud"
export TF_VAR_datacenter="uk-reading"
```

Initialize the provider:
```bash
terraform init
```

To deploy this infrastructure export the following variables (or use -var):

The plan phase:
```bash
terraform plan
```

The apply phase:
```bash
terraform apply
```

To delete the infrastrucure:
```bash
terraform destroy
```
