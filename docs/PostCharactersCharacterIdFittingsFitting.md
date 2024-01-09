# PostCharactersCharacterIdFittingsFitting

fitting object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description string | 
**items** | [**List[PostCharactersCharacterIdFittingsItem]**](PostCharactersCharacterIdFittingsItem.md) | items array | 
**name** | **str** | name string | 
**ship_type_id** | **int** | ship_type_id integer | 

## Example

```python
from esi_client.models.post_characters_character_id_fittings_fitting import PostCharactersCharacterIdFittingsFitting

# TODO update the JSON string below
json = "{}"
# create an instance of PostCharactersCharacterIdFittingsFitting from a JSON string
post_characters_character_id_fittings_fitting_instance = PostCharactersCharacterIdFittingsFitting.from_json(json)
# print the JSON string representation of the object
print PostCharactersCharacterIdFittingsFitting.to_json()

# convert the object into a dict
post_characters_character_id_fittings_fitting_dict = post_characters_character_id_fittings_fitting_instance.to_dict()
# create an instance of PostCharactersCharacterIdFittingsFitting from a dict
post_characters_character_id_fittings_fitting_form_dict = post_characters_character_id_fittings_fitting.from_dict(post_characters_character_id_fittings_fitting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


