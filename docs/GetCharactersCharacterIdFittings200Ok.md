# GetCharactersCharacterIdFittings200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description string | 
**fitting_id** | **int** | fitting_id integer | 
**items** | [**List[GetCharactersCharacterIdFittingsItem]**](GetCharactersCharacterIdFittingsItem.md) | items array | 
**name** | **str** | name string | 
**ship_type_id** | **int** | ship_type_id integer | 

## Example

```python
from esi_client.models.get_characters_character_id_fittings200_ok import GetCharactersCharacterIdFittings200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdFittings200Ok from a JSON string
get_characters_character_id_fittings200_ok_instance = GetCharactersCharacterIdFittings200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdFittings200Ok.to_json()

# convert the object into a dict
get_characters_character_id_fittings200_ok_dict = get_characters_character_id_fittings200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdFittings200Ok from a dict
get_characters_character_id_fittings200_ok_form_dict = get_characters_character_id_fittings200_ok.from_dict(get_characters_character_id_fittings200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


