# GetCharactersCharacterIdPlanetsPlanetIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[GetCharactersCharacterIdPlanetsPlanetIdLink]**](GetCharactersCharacterIdPlanetsPlanetIdLink.md) | links array | 
**pins** | [**List[GetCharactersCharacterIdPlanetsPlanetIdPin]**](GetCharactersCharacterIdPlanetsPlanetIdPin.md) | pins array | 
**routes** | [**List[GetCharactersCharacterIdPlanetsPlanetIdRoute]**](GetCharactersCharacterIdPlanetsPlanetIdRoute.md) | routes array | 

## Example

```python
from esi_client.models.get_characters_character_id_planets_planet_id_ok import GetCharactersCharacterIdPlanetsPlanetIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdPlanetsPlanetIdOk from a JSON string
get_characters_character_id_planets_planet_id_ok_instance = GetCharactersCharacterIdPlanetsPlanetIdOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdPlanetsPlanetIdOk.to_json()

# convert the object into a dict
get_characters_character_id_planets_planet_id_ok_dict = get_characters_character_id_planets_planet_id_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdPlanetsPlanetIdOk from a dict
get_characters_character_id_planets_planet_id_ok_form_dict = get_characters_character_id_planets_planet_id_ok.from_dict(get_characters_character_id_planets_planet_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


