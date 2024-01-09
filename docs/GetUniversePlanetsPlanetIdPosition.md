# GetUniversePlanetsPlanetIdPosition

position object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** | x number | 
**y** | **float** | y number | 
**z** | **float** | z number | 

## Example

```python
from esi_client.models.get_universe_planets_planet_id_position import GetUniversePlanetsPlanetIdPosition

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniversePlanetsPlanetIdPosition from a JSON string
get_universe_planets_planet_id_position_instance = GetUniversePlanetsPlanetIdPosition.from_json(json)
# print the JSON string representation of the object
print GetUniversePlanetsPlanetIdPosition.to_json()

# convert the object into a dict
get_universe_planets_planet_id_position_dict = get_universe_planets_planet_id_position_instance.to_dict()
# create an instance of GetUniversePlanetsPlanetIdPosition from a dict
get_universe_planets_planet_id_position_form_dict = get_universe_planets_planet_id_position.from_dict(get_universe_planets_planet_id_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


