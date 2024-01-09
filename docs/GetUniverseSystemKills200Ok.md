# GetUniverseSystemKills200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**npc_kills** | **int** | Number of NPC ships killed in this system | 
**pod_kills** | **int** | Number of pods killed in this system | 
**ship_kills** | **int** | Number of player ships killed in this system | 
**system_id** | **int** | system_id integer | 

## Example

```python
from esi_client.models.get_universe_system_kills200_ok import GetUniverseSystemKills200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseSystemKills200Ok from a JSON string
get_universe_system_kills200_ok_instance = GetUniverseSystemKills200Ok.from_json(json)
# print the JSON string representation of the object
print GetUniverseSystemKills200Ok.to_json()

# convert the object into a dict
get_universe_system_kills200_ok_dict = get_universe_system_kills200_ok_instance.to_dict()
# create an instance of GetUniverseSystemKills200Ok from a dict
get_universe_system_kills200_ok_form_dict = get_universe_system_kills200_ok.from_dict(get_universe_system_kills200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


