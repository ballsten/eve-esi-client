# PostUniverseIdsSystem

system object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id integer | [optional] 
**name** | **str** | name string | [optional] 

## Example

```python
from esi_client.models.post_universe_ids_system import PostUniverseIdsSystem

# TODO update the JSON string below
json = "{}"
# create an instance of PostUniverseIdsSystem from a JSON string
post_universe_ids_system_instance = PostUniverseIdsSystem.from_json(json)
# print the JSON string representation of the object
print PostUniverseIdsSystem.to_json()

# convert the object into a dict
post_universe_ids_system_dict = post_universe_ids_system_instance.to_dict()
# create an instance of PostUniverseIdsSystem from a dict
post_universe_ids_system_form_dict = post_universe_ids_system.from_dict(post_universe_ids_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


