# PostUniverseIdsRegion

region object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id integer | [optional] 
**name** | **str** | name string | [optional] 

## Example

```python
from esi_client.models.post_universe_ids_region import PostUniverseIdsRegion

# TODO update the JSON string below
json = "{}"
# create an instance of PostUniverseIdsRegion from a JSON string
post_universe_ids_region_instance = PostUniverseIdsRegion.from_json(json)
# print the JSON string representation of the object
print PostUniverseIdsRegion.to_json()

# convert the object into a dict
post_universe_ids_region_dict = post_universe_ids_region_instance.to_dict()
# create an instance of PostUniverseIdsRegion from a dict
post_universe_ids_region_form_dict = post_universe_ids_region.from_dict(post_universe_ids_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


