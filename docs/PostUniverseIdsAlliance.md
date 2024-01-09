# PostUniverseIdsAlliance

alliance object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id integer | [optional] 
**name** | **str** | name string | [optional] 

## Example

```python
from esi_client.models.post_universe_ids_alliance import PostUniverseIdsAlliance

# TODO update the JSON string below
json = "{}"
# create an instance of PostUniverseIdsAlliance from a JSON string
post_universe_ids_alliance_instance = PostUniverseIdsAlliance.from_json(json)
# print the JSON string representation of the object
print PostUniverseIdsAlliance.to_json()

# convert the object into a dict
post_universe_ids_alliance_dict = post_universe_ids_alliance_instance.to_dict()
# create an instance of PostUniverseIdsAlliance from a dict
post_universe_ids_alliance_form_dict = post_universe_ids_alliance.from_dict(post_universe_ids_alliance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


