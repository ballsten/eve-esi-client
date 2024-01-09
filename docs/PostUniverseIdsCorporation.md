# PostUniverseIdsCorporation

corporation object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id integer | [optional] 
**name** | **str** | name string | [optional] 

## Example

```python
from esi_client.models.post_universe_ids_corporation import PostUniverseIdsCorporation

# TODO update the JSON string below
json = "{}"
# create an instance of PostUniverseIdsCorporation from a JSON string
post_universe_ids_corporation_instance = PostUniverseIdsCorporation.from_json(json)
# print the JSON string representation of the object
print PostUniverseIdsCorporation.to_json()

# convert the object into a dict
post_universe_ids_corporation_dict = post_universe_ids_corporation_instance.to_dict()
# create an instance of PostUniverseIdsCorporation from a dict
post_universe_ids_corporation_form_dict = post_universe_ids_corporation.from_dict(post_universe_ids_corporation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


