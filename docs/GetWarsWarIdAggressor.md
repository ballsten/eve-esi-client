# GetWarsWarIdAggressor

The aggressor corporation or alliance that declared this war, only contains either corporation_id or alliance_id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alliance_id** | **int** | Alliance ID if and only if the aggressor is an alliance | [optional] 
**corporation_id** | **int** | Corporation ID if and only if the aggressor is a corporation | [optional] 
**isk_destroyed** | **float** | ISK value of ships the aggressor has destroyed | 
**ships_killed** | **int** | The number of ships the aggressor has killed | 

## Example

```python
from esi_client.models.get_wars_war_id_aggressor import GetWarsWarIdAggressor

# TODO update the JSON string below
json = "{}"
# create an instance of GetWarsWarIdAggressor from a JSON string
get_wars_war_id_aggressor_instance = GetWarsWarIdAggressor.from_json(json)
# print the JSON string representation of the object
print GetWarsWarIdAggressor.to_json()

# convert the object into a dict
get_wars_war_id_aggressor_dict = get_wars_war_id_aggressor_instance.to_dict()
# create an instance of GetWarsWarIdAggressor from a dict
get_wars_war_id_aggressor_form_dict = get_wars_war_id_aggressor.from_dict(get_wars_war_id_aggressor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


