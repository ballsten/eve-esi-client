# GetCharactersCharacterIdShipOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ship_item_id** | **int** | Item id&#39;s are unique to a ship and persist until it is repackaged. This value can be used to track repeated uses of a ship, or detect when a pilot changes into a different instance of the same ship type. | 
**ship_name** | **str** | ship_name string | 
**ship_type_id** | **int** | ship_type_id integer | 

## Example

```python
from esi_client.models.get_characters_character_id_ship_ok import GetCharactersCharacterIdShipOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdShipOk from a JSON string
get_characters_character_id_ship_ok_instance = GetCharactersCharacterIdShipOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdShipOk.to_json()

# convert the object into a dict
get_characters_character_id_ship_ok_dict = get_characters_character_id_ship_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdShipOk from a dict
get_characters_character_id_ship_ok_form_dict = get_characters_character_id_ship_ok.from_dict(get_characters_character_id_ship_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


