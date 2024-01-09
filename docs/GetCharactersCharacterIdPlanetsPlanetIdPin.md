# GetCharactersCharacterIdPlanetsPlanetIdPin

pin object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | [**List[GetCharactersCharacterIdPlanetsPlanetIdContent]**](GetCharactersCharacterIdPlanetsPlanetIdContent.md) | contents array | [optional] 
**expiry_time** | **datetime** | expiry_time string | [optional] 
**extractor_details** | [**GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails**](GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.md) |  | [optional] 
**factory_details** | [**GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails**](GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails.md) |  | [optional] 
**install_time** | **datetime** | install_time string | [optional] 
**last_cycle_start** | **datetime** | last_cycle_start string | [optional] 
**latitude** | **float** | latitude number | 
**longitude** | **float** | longitude number | 
**pin_id** | **int** | pin_id integer | 
**schematic_id** | **int** | schematic_id integer | [optional] 
**type_id** | **int** | type_id integer | 

## Example

```python
from esi_client.models.get_characters_character_id_planets_planet_id_pin import GetCharactersCharacterIdPlanetsPlanetIdPin

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdPlanetsPlanetIdPin from a JSON string
get_characters_character_id_planets_planet_id_pin_instance = GetCharactersCharacterIdPlanetsPlanetIdPin.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdPlanetsPlanetIdPin.to_json()

# convert the object into a dict
get_characters_character_id_planets_planet_id_pin_dict = get_characters_character_id_planets_planet_id_pin_instance.to_dict()
# create an instance of GetCharactersCharacterIdPlanetsPlanetIdPin from a dict
get_characters_character_id_planets_planet_id_pin_form_dict = get_characters_character_id_planets_planet_id_pin.from_dict(get_characters_character_id_planets_planet_id_pin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


