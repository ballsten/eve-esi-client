# GetWarsWarIdAlly

ally object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alliance_id** | **int** | Alliance ID if and only if this ally is an alliance | [optional] 
**corporation_id** | **int** | Corporation ID if and only if this ally is a corporation | [optional] 

## Example

```python
from esi_client.models.get_wars_war_id_ally import GetWarsWarIdAlly

# TODO update the JSON string below
json = "{}"
# create an instance of GetWarsWarIdAlly from a JSON string
get_wars_war_id_ally_instance = GetWarsWarIdAlly.from_json(json)
# print the JSON string representation of the object
print GetWarsWarIdAlly.to_json()

# convert the object into a dict
get_wars_war_id_ally_dict = get_wars_war_id_ally_instance.to_dict()
# create an instance of GetWarsWarIdAlly from a dict
get_wars_war_id_ally_form_dict = get_wars_war_id_ally.from_dict(get_wars_war_id_ally_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


