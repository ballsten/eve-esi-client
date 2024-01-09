# GetCharactersCharacterIdAssets200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_blueprint_copy** | **bool** | is_blueprint_copy boolean | [optional] 
**is_singleton** | **bool** | is_singleton boolean | 
**item_id** | **int** | item_id integer | 
**location_flag** | **str** | location_flag string | 
**location_id** | **int** | location_id integer | 
**location_type** | **str** | location_type string | 
**quantity** | **int** | quantity integer | 
**type_id** | **int** | type_id integer | 

## Example

```python
from esi_client.models.get_characters_character_id_assets200_ok import GetCharactersCharacterIdAssets200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdAssets200Ok from a JSON string
get_characters_character_id_assets200_ok_instance = GetCharactersCharacterIdAssets200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdAssets200Ok.to_json()

# convert the object into a dict
get_characters_character_id_assets200_ok_dict = get_characters_character_id_assets200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdAssets200Ok from a dict
get_characters_character_id_assets200_ok_form_dict = get_characters_character_id_assets200_ok.from_dict(get_characters_character_id_assets200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


