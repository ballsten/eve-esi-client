# GetCharactersCharacterIdPlanetsPlanetIdRoute

route object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type_id** | **int** | content_type_id integer | 
**destination_pin_id** | **int** | destination_pin_id integer | 
**quantity** | **float** | quantity number | 
**route_id** | **int** | route_id integer | 
**source_pin_id** | **int** | source_pin_id integer | 
**waypoints** | **List[int]** | list of pin ID waypoints | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_planets_planet_id_route import GetCharactersCharacterIdPlanetsPlanetIdRoute

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdPlanetsPlanetIdRoute from a JSON string
get_characters_character_id_planets_planet_id_route_instance = GetCharactersCharacterIdPlanetsPlanetIdRoute.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdPlanetsPlanetIdRoute.to_json()

# convert the object into a dict
get_characters_character_id_planets_planet_id_route_dict = get_characters_character_id_planets_planet_id_route_instance.to_dict()
# create an instance of GetCharactersCharacterIdPlanetsPlanetIdRoute from a dict
get_characters_character_id_planets_planet_id_route_form_dict = get_characters_character_id_planets_planet_id_route.from_dict(get_characters_character_id_planets_planet_id_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


