# GetWarsWarIdDefender

The defending corporation or alliance that declared this war, only contains either corporation_id or alliance_id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alliance_id** | **int** | Alliance ID if and only if the defender is an alliance | [optional] 
**corporation_id** | **int** | Corporation ID if and only if the defender is a corporation | [optional] 
**isk_destroyed** | **float** | ISK value of ships the defender has killed | 
**ships_killed** | **int** | The number of ships the defender has killed | 

## Example

```python
from esi_client.models.get_wars_war_id_defender import GetWarsWarIdDefender

# TODO update the JSON string below
json = "{}"
# create an instance of GetWarsWarIdDefender from a JSON string
get_wars_war_id_defender_instance = GetWarsWarIdDefender.from_json(json)
# print the JSON string representation of the object
print GetWarsWarIdDefender.to_json()

# convert the object into a dict
get_wars_war_id_defender_dict = get_wars_war_id_defender_instance.to_dict()
# create an instance of GetWarsWarIdDefender from a dict
get_wars_war_id_defender_form_dict = get_wars_war_id_defender.from_dict(get_wars_war_id_defender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


