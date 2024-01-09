# PostCharactersCharacterIdFittingsItem

item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flag** | **str** | Fitting location for the item. Entries placed in &#39;Invalid&#39; will be discarded. If this leaves the fitting with nothing, it will cause an error. | 
**quantity** | **int** | quantity integer | 
**type_id** | **int** | type_id integer | 

## Example

```python
from esi_client.models.post_characters_character_id_fittings_item import PostCharactersCharacterIdFittingsItem

# TODO update the JSON string below
json = "{}"
# create an instance of PostCharactersCharacterIdFittingsItem from a JSON string
post_characters_character_id_fittings_item_instance = PostCharactersCharacterIdFittingsItem.from_json(json)
# print the JSON string representation of the object
print PostCharactersCharacterIdFittingsItem.to_json()

# convert the object into a dict
post_characters_character_id_fittings_item_dict = post_characters_character_id_fittings_item_instance.to_dict()
# create an instance of PostCharactersCharacterIdFittingsItem from a dict
post_characters_character_id_fittings_item_form_dict = post_characters_character_id_fittings_item.from_dict(post_characters_character_id_fittings_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


