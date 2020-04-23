# Retrieving the utilization report

Metered utilization is relatively straightforward in the MetalCloud. All resources are utilized on-demand. Some on-demand utilization charges can be overriten by subscriptions such as server subscriptions (rezervations) which lower costs in sustanined utilization scenarios.

To access the report access the **Billing section** (infrastructure Editor > Billing):

![](/assets/guides/managing_billing_information_2.png)

Click on the **Utilization Report** (infrastructure Editor > Billing > Utilization report)

![](/assets/guides/the_utilization_report_2.png)

This opens up the utilization report for the current billable account and by default shows totals for all of the infrastructures of the billable user.

![](/assets/guides/the_utilization_report_1.png)

## The Detailed utilization report

To drill-down to see more information about each infrastructure in particular click on **Detailed utilization report** infrastructure Editor > Billing > Detailed Utilization report)

Select the **Infrastructure owner** from the dropdown to view the infrastructures billed to that user. The dropdown is populated with aditional users to which the current user is added as delegate. This allows a single finance department or in reseller situations, a single company to have access to multiple utilization reports of multiple commercial entities.

![](/assets/guides/the_detailed_utilization_report_2.png)

Select the time interval by clicking ont he dates below and scroll to the desired infrastructure.

![](/assets/guides/the_detailed_utilization_report_3.png)

This report shows the exact utilization of each on-demand asset. Instances can be covered by "rezervations" which are not shown here.

If a server configuration has changed at any given time there will be separate lines for the same instance name. 

# Viewing server subscriptions (reservations)

To view which **Subscriptions** apply click on the **Utilization Report** (infrastructure Editor > Billing > Utilization report) and then on the **Server Subscriptions**. (infrastructure Editor > Billing > Utilization report> Server Subscriptions)

![](/assets/guides/understanding_the_utilization_report_4.png)

These subscriptions will override the pricing of the on-demand instances they match. For example this subscription will be valid for a period of one year and will automatically renew at the end of that year. Every month a separate charge will be added to the invoice. 

![](/assets/guides/understanding_the_utilization_report_4.png)

The price will depending on the rezervation pricing in place at the time of the creation of the reservation. Rezervations are not affected by on demand pricing changes. See [Metalcloud Pricing](/general/metalcloud_pricing) for more details.

## Automating chargeback or billing in reselling scenarios

To automate the chargeback or billing in a reseller scenario use the [`resource_utilization_detailed()`](https://api.bigstep.com/metal-cloud#resource_utilization_detailed) API function to retrive the utilization report in a JSON format.

Users can also retrieve the current pricing using the [`prices()`](https://api.bigstep.com/metal-cloud#prices) function.

Reffer to the [API](https://api.bigstep.com/metal-cloud#resource_utilization_summary) for more information.

Example detailed utilization summary json:

```javascript
{
	"detailed_report": {
		"3668": {
			"data_lake": [
				{
					"cost": "0.00000000",
					"cost_currency": "GBP",
					"cost_per_unit": "0.00000000",
					"end_timestamp": "2016-02-01T14:21:05Z",
					"is_reservation": "0",
					"measurement_period": "2592000",
					"measurement_unit": "seconds",
					"product_id": 8,
					"product_label": "data-lake-8",
					"product_subdomain": "data-lake-8.d-lake.1.integration.bigstep.io",
					"quantity": "4261",
					"resource_utilization_gbytes": 0,
					"start_timestamp": "2016-02-01T13:10:05Z"
				}
			],
			"shared_drive":[
				{
					"cost": "0.23354152",
					"cost_currency": "GBP",
					"cost_per_unit": "0.00347222",
					"end_timestamp": "2016-01-25T09:54:39Z",
					"is_reservation": "0",
					"measurement_period": 3600,
					"measurement_unit": "seconds",
					"product_id": 779,
					"product_label": "new-shared-drive",
					"product_subdomain": "new-shared-drive.test.1.integration.bigstep.io",
					"quantity: "242136",
					"shared_drive_size_mbytes": 51200,
					"start_timestamp": "2016-01-22T14:39:04Z"

				}
			],
			"drive": [
				{
					"cost": "1.11383813",
					"cost_currency": "GBP",
					"cost_per_unit": "0.01601563",
					"drive_size_mbytes": 41000,
					"end_timestamp": "2016-02-04T10:31:03Z",
					"is_reservation": "0",
					"measurement_period": "3600",
					"measurement_unit": "seconds",
					"product_id": 3727,
					"product_label": "drive-3727",
					"product_subdomain": "drive-3727.new-drive-array.d-lake.1.integration.bigstep.io",
					"quantity": "250369",
					"start_timestamp": "2016-02-01T12:58:15Z"
				}
			],
			"instance": [
				{
					"cost": "7.25925278",
					"cost_currency": "GBP",
					"cost_per_unit": "0.31000000",
					"end_timestamp": "2016-02-02T12:23:00Z",
					"is_reservation": "0",
					"measurement_period": "3600",
					"measurement_unit": "seconds",
					"product_id": 2416,
					"product_label": "instance-2416",
					"product_subdomain": "instance-2416.new-instance-array.d-lake.1.integration.bigstep.io",
					"quantity": "84301",
					"server_type_id": null,
					"start_timestamp": "2016-02-01T12:58:00Z"
				}
			],
			"subnet": [
				{
					"cost": "0.00000000",
					"cost_currency": "GBP",
					"cost_per_unit": "0.00000000",
					"end_timestamp": "2016-02-04T10:30:53Z",
					"is_reservation": "0",
					"measurement_period": "3600",
					"measurement_unit": "seconds",
					"product_id": 6378,
					"product_label": "subnet-6378",
					"product_subdomain": "subnet-6378.wan.d-lake.1.integration.bigstep.io",
					"quantity": "250376",
					"start_timestamp": "2016-02-01T12:57:58Z",
					"subnet_prefix_size": 64,
					"subnet_type": "ipv6"
				}
			]
	},
	"network_report": {
		"3688": {
			"data_lake": {
				"download": {
					"cost": 0,
					"cost_currency": "GBP",
					"measurement_unit": "gbytes",
					"quantity": 0,
					"metered_waypoints": [
						{
							"cost": "0.00000000",
							"cost_currency": "GBP",
							"cost_per_unit": "0.00000000",
							"end_timestamp": "2016-02-09T08:11:39Z",
							"is_reservation": "0",
							"measurement_period": "3600",
							"measurement_unit": "gbytes",
							"product_id": 8,
							"product_label": "data-lake-8",
							"product_subdomain": "data-lake-8.d-lake.1.integration.bigstep.io",
							"quantity": "0.0000",
							"start_timestamp": "2016-02-01T13:10:05Z"
						}
					]
				},
				"upload": {
					"cost": 0,
					"cost_currency": "GBP",
					"measurement_unit": "gbytes",
					"quantity": 0,
					"metered_waypoints": [
						{
							"cost": "0.00000000",
							"cost_currency": "GBP",
							"cost_per_unit": "0.06000000",
							"end_timestamp": "2016-02-09T08:11:39Z",
							"is_reservation": "0",
							"measurement_period": "3600",
							"measurement_unit": "gbytes",
							"product_id": 8,
							"product_label": "data-lake-8",
							"product_subdomain": "data-lake-8.d-lake.1.integration.bigstep.io",
							"quantity": "0.0000",
							"start_timestamp": "2016-02-01T13:10:06Z"
						}
					]
				}
			},
			"network": {
				"download": {
					"cost": 0,
					"cost_currency": "GBP",
					"measurement_unit": "gbytes",
					"quantity": 0,
					"metered_waypoints": [
						{
							"cost": "0.00000000",
							"cost_currency": "GBP",
							"cost_per_unit": "0.00000000",
							"end_timestamp": "2016-02-04T10:30:54Z",
							"is_reservation": "0",
							"measurement_period": "10800",
							"measurement_unit": "gbytes",
							"product_id": 8381,
							"product_label": "wan",
							"product_subdomain": "wan.d-lake.1.integration.bigstep.io",
							"quantity": "0.0000",
							"start_timestamp": "2016-02-01T12:57:59Z"
						}
					]
				},
				"upload": {
					"cost": 0,
					"cost_currency": "GBP",
					"measurement_unit": "gbytes",
					"quantity": 0,
					"metered_waypoints": [
						{
							"cost": "0.00000000",
							"cost_currency": "GBP",
							"cost_per_unit": "0.06000000",
							"end_timestamp": "2016-02-04T10:30:54Z",
							"is_reservation": "0",
							"measurement_period": "10800",
							"measurement_unit": "gbytes",
							"product_id": 8381,
							"product_label": "wan",
							"product_subdomain": "wan.d-lake.1.integration.bigstep.io",
							"quantity": "0.0000",
							"start_timestamp": "2016-02-01T12:57:59Z"
						}
					]
				}
			}
		}
	},
	"reservation_installments": {
		"server_types": [
			{
				"cost": 119.81,
				"cost_currency": "GBP",
				"created_timestamp": "2016-02-09T11:17:39Z",
				"end_timestamp": "2016-03-09T11:17:38Z",
				"server_type_name": "FMCI 4.8",
				"server_type_reservation_id": 60,
				"start_timestamp": "2016-02-09T11:17:39Z"
			}
		]
	},
	"infrastructures": {
		"3688": {
			"infrastructure_id": 3688,
			"infrastructure_label": "d-lake",
			"infrastructure_service_status": "deleted"
		}
	},
	"end_timestamp": "2016-11-01T00:00:00Z",
	"start_timestamp": "2015-01-01T00:00:00Z"
}
```