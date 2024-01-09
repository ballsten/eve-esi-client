# GetCharactersCharacterIdLocationOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solar_system_id** | **int** | solar_system_id integer | 
**station_id** | **int** | station_id integer | [optional] 
**structure_id** | **int** | structure_id integer | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_location_ok import GetCharactersCharacterIdLocationOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdLocationOk from a JSON string
get_characters_character_id_location_ok_instance = GetCharactersCharacterIdLocationOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdLocationOk.to_json()

# convert the object into a dict
get_characters_character_id_location_ok_dict = get_characters_character_id_location_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdLocationOk from a dict
get_characters_character_id_location_ok_form_dict = get_characters_character_id_location_ok.from_dict(get_characters_character_id_location_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


