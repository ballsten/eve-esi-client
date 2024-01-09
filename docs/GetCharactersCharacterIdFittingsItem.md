# GetCharactersCharacterIdFittingsItem

item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flag** | **str** | flag string | 
**quantity** | **int** | quantity integer | 
**type_id** | **int** | type_id integer | 

## Example

```python
from esi_client.models.get_characters_character_id_fittings_item import GetCharactersCharacterIdFittingsItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdFittingsItem from a JSON string
get_characters_character_id_fittings_item_instance = GetCharactersCharacterIdFittingsItem.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdFittingsItem.to_json()

# convert the object into a dict
get_characters_character_id_fittings_item_dict = get_characters_character_id_fittings_item_instance.to_dict()
# create an instance of GetCharactersCharacterIdFittingsItem from a dict
get_characters_character_id_fittings_item_form_dict = get_characters_character_id_fittings_item.from_dict(get_characters_character_id_fittings_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


