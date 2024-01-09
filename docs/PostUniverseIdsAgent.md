# PostUniverseIdsAgent

agent object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id integer | [optional] 
**name** | **str** | name string | [optional] 

## Example

```python
from esi_client.models.post_universe_ids_agent import PostUniverseIdsAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PostUniverseIdsAgent from a JSON string
post_universe_ids_agent_instance = PostUniverseIdsAgent.from_json(json)
# print the JSON string representation of the object
print PostUniverseIdsAgent.to_json()

# convert the object into a dict
post_universe_ids_agent_dict = post_universe_ids_agent_instance.to_dict()
# create an instance of PostUniverseIdsAgent from a dict
post_universe_ids_agent_form_dict = post_universe_ids_agent.from_dict(post_universe_ids_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


