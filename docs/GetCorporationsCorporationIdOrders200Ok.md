# GetCorporationsCorporationIdOrders200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | Number of days for which order is valid (starting from the issued date). An order expires at time issued + duration | 
**escrow** | **float** | For buy orders, the amount of ISK in escrow | [optional] 
**is_buy_order** | **bool** | True if the order is a bid (buy) order | [optional] 
**issued** | **datetime** | Date and time when this order was issued | 
**issued_by** | **int** | The character who issued this order | 
**location_id** | **int** | ID of the location where order was placed | 
**min_volume** | **int** | For buy orders, the minimum quantity that will be accepted in a matching sell order | [optional] 
**order_id** | **int** | Unique order ID | 
**price** | **float** | Cost per unit for this order | 
**range** | **str** | Valid order range, numbers are ranges in jumps | 
**region_id** | **int** | ID of the region where order was placed | 
**type_id** | **int** | The type ID of the item transacted in this order | 
**volume_remain** | **int** | Quantity of items still required or offered | 
**volume_total** | **int** | Quantity of items required or offered at time order was placed | 
**wallet_division** | **int** | The corporation wallet division used for this order. | 

## Example

```python
from esi_client.models.get_corporations_corporation_id_orders200_ok import GetCorporationsCorporationIdOrders200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdOrders200Ok from a JSON string
get_corporations_corporation_id_orders200_ok_instance = GetCorporationsCorporationIdOrders200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdOrders200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_orders200_ok_dict = get_corporations_corporation_id_orders200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdOrders200Ok from a dict
get_corporations_corporation_id_orders200_ok_form_dict = get_corporations_corporation_id_orders200_ok.from_dict(get_corporations_corporation_id_orders200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


