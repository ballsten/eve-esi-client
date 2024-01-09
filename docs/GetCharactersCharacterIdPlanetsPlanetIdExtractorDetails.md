# GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails

extractor_details object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_time** | **int** | in seconds | [optional] 
**head_radius** | **float** | head_radius number | [optional] 
**heads** | [**List[GetCharactersCharacterIdPlanetsPlanetIdHead]**](GetCharactersCharacterIdPlanetsPlanetIdHead.md) | heads array | 
**product_type_id** | **int** | product_type_id integer | [optional] 
**qty_per_cycle** | **int** | qty_per_cycle integer | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_planets_planet_id_extractor_details import GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails from a JSON string
get_characters_character_id_planets_planet_id_extractor_details_instance = GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.to_json()

# convert the object into a dict
get_characters_character_id_planets_planet_id_extractor_details_dict = get_characters_character_id_planets_planet_id_extractor_details_instance.to_dict()
# create an instance of GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails from a dict
get_characters_character_id_planets_planet_id_extractor_details_form_dict = get_characters_character_id_planets_planet_id_extractor_details.from_dict(get_characters_character_id_planets_planet_id_extractor_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


