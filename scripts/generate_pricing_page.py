import requests
from jinja2 import Environment, FileSystemLoader
from collections import OrderedDict
import os 

PRICES_URL='https://api.bigstep.com/metal-cloud/?rpc-method=prices'

dir_path = os.path.dirname(os.path.realpath(__file__))
TEMPLATES_DIR=os.path.join(dir_path,"templates")
OUTPUT_DIR=os.path.join(os.path.join(dir_path,".."),"general")

PRICING_PAGE_NAME="metalcloud_pricing.md"
PRICING_PAGE_TEMPLATE=PRICING_PAGE_NAME+".tmpl"

BLACKLIST=["M.20.128", "M.10.128","M.40.384.12D","M.4.32.1G"]

##retrive the data
try:

  response=requests.get(PRICES_URL)

  response.raise_for_status()

except HTTPError as http_err:
  print('HTTP error occurred: '+http_err)
except Exception as err:
  print('Other error occurred: '+err)


prices=response.json()["result"]

instances={}
drives={}
datalake={}
ips={}
networks={}

for franchise in prices.keys():
  for datacenter in prices[franchise]["datacenters"].keys():
    for instance,v in prices[franchise]["datacenters"][datacenter]["instance"]["server_types"].items():

      if "server_class" in v.keys() and v["server_class"]=="bigdata" and not v["server_type_is_experimental"]:
          if instance in BLACKLIST:
            continue

          if instance not in instances.keys():
            instances[instance]={}

            for k in ["server_ram_gbytes", 
            "server_processor_name", 
            "server_disk_type", 
            "server_disk_count", 
            "server_disk_size_mbytes", 
            "server_processor_count", 
            "server_processor_core_mhz",
            "server_processor_core_count", 
            "server_type_is_experimental", 
            "server_network_total_capacity_mbps"]:
              instances[instance][k]=v[k]
          
          currency=v["demand"]["resource_utilization_price_currency"]  

          instances[instance]["on_demand_"+currency]=v["demand"]["resource_utilization_price"]
          instances[instance]["reservation_"+currency]=v["reservation"]["resource_reservation_price"]

    for drive,v in prices[franchise]["datacenters"][datacenter]["drive"].items():
      
          if drive not in drives.keys():
                drives[drive]={}

          currency=v["resource_utilization_price_currency"]  
          #this price is per month
          drives[drive]["price_"+currency]=v["resource_utilization_price"]

    if "data_lake" in prices[franchise]["datacenters"][datacenter].keys():
        v=prices[franchise]["datacenters"][datacenter]["data_lake"]
        currency=v["resource_utilization_price_currency"]  
        datalake["price_"+currency]=v["resource_utilization_price"] 

    for ip_type,v in prices[franchise]["datacenters"][datacenter]["subnet"]["wan"].items():
    
        if ip_type not in ips.keys():
              ips[ip_type]={}

        currency=v["resource_utilization_price_currency"]  
        ips[ip_type]["price_"+currency]=v["resource_utilization_price"]

    for network,v in prices[franchise]["datacenters"][datacenter]["network"]["wan"].items():
    
        if network not in networks.keys():
              networks[network]={}

        currency=v["resource_utilization_price_currency"]  
        networks[network]["price_"+currency]=v["resource_utilization_price"]
           
instances = OrderedDict(sorted(instances.items(), key=lambda (k,v): v['server_ram_gbytes']))

#generate the files
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
template = env.get_template(PRICING_PAGE_TEMPLATE)
output = template.render(
  prices=prices, 
  instances=instances, 
  drives=drives, 
  datalake=datalake, 
  ips=ips,
  networks=networks
)

with open(os.path.join(OUTPUT_DIR,PRICING_PAGE_NAME), "w") as fh:
    fh.write(output.encode('utf-8'))

