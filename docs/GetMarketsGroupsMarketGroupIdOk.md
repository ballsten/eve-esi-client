# GetMarketsGroupsMarketGroupIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description string | 
**market_group_id** | **int** | market_group_id integer | 
**name** | **str** | name string | 
**parent_group_id** | **int** | parent_group_id integer | [optional] 
**types** | **List[int]** | types array | 

## Example

```python
from esi_client.models.get_markets_groups_market_group_id_ok import GetMarketsGroupsMarketGroupIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarketsGroupsMarketGroupIdOk from a JSON string
get_markets_groups_market_group_id_ok_instance = GetMarketsGroupsMarketGroupIdOk.from_json(json)
# print the JSON string representation of the object
print GetMarketsGroupsMarketGroupIdOk.to_json()

# convert the object into a dict
get_markets_groups_market_group_id_ok_dict = get_markets_groups_market_group_id_ok_instance.to_dict()
# create an instance of GetMarketsGroupsMarketGroupIdOk from a dict
get_markets_groups_market_group_id_ok_form_dict = get_markets_groups_market_group_id_ok.from_dict(get_markets_groups_market_group_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


