# GetMarketsStructuresStructureId200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | duration integer | 
**is_buy_order** | **bool** | is_buy_order boolean | 
**issued** | **datetime** | issued string | 
**location_id** | **int** | location_id integer | 
**min_volume** | **int** | min_volume integer | 
**order_id** | **int** | order_id integer | 
**price** | **float** | price number | 
**range** | **str** | range string | 
**type_id** | **int** | type_id integer | 
**volume_remain** | **int** | volume_remain integer | 
**volume_total** | **int** | volume_total integer | 

## Example

```python
from esi_client.models.get_markets_structures_structure_id200_ok import GetMarketsStructuresStructureId200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarketsStructuresStructureId200Ok from a JSON string
get_markets_structures_structure_id200_ok_instance = GetMarketsStructuresStructureId200Ok.from_json(json)
# print the JSON string representation of the object
print GetMarketsStructuresStructureId200Ok.to_json()

# convert the object into a dict
get_markets_structures_structure_id200_ok_dict = get_markets_structures_structure_id200_ok_instance.to_dict()
# create an instance of GetMarketsStructuresStructureId200Ok from a dict
get_markets_structures_structure_id200_ok_form_dict = get_markets_structures_structure_id200_ok.from_dict(get_markets_structures_structure_id200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


