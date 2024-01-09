# GetCharactersCharacterIdPlanets200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_update** | **datetime** | last_update string | 
**num_pins** | **int** | num_pins integer | 
**owner_id** | **int** | owner_id integer | 
**planet_id** | **int** | planet_id integer | 
**planet_type** | **str** | planet_type string | 
**solar_system_id** | **int** | solar_system_id integer | 
**upgrade_level** | **int** | upgrade_level integer | 

## Example

```python
from esi_client.models.get_characters_character_id_planets200_ok import GetCharactersCharacterIdPlanets200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdPlanets200Ok from a JSON string
get_characters_character_id_planets200_ok_instance = GetCharactersCharacterIdPlanets200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdPlanets200Ok.to_json()

# convert the object into a dict
get_characters_character_id_planets200_ok_dict = get_characters_character_id_planets200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdPlanets200Ok from a dict
get_characters_character_id_planets200_ok_form_dict = get_characters_character_id_planets200_ok.from_dict(get_characters_character_id_planets200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


