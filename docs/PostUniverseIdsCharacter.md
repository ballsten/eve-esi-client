# PostUniverseIdsCharacter

character object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id integer | [optional] 
**name** | **str** | name string | [optional] 

## Example

```python
from esi_client.models.post_universe_ids_character import PostUniverseIdsCharacter

# TODO update the JSON string below
json = "{}"
# create an instance of PostUniverseIdsCharacter from a JSON string
post_universe_ids_character_instance = PostUniverseIdsCharacter.from_json(json)
# print the JSON string representation of the object
print PostUniverseIdsCharacter.to_json()

# convert the object into a dict
post_universe_ids_character_dict = post_universe_ids_character_instance.to_dict()
# create an instance of PostUniverseIdsCharacter from a dict
post_universe_ids_character_form_dict = post_universe_ids_character.from_dict(post_universe_ids_character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


