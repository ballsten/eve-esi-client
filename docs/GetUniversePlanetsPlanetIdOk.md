# GetUniversePlanetsPlanetIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name string | 
**planet_id** | **int** | planet_id integer | 
**position** | [**GetUniversePlanetsPlanetIdPosition**](GetUniversePlanetsPlanetIdPosition.md) |  | 
**system_id** | **int** | The solar system this planet is in | 
**type_id** | **int** | type_id integer | 

## Example

```python
from esi_client.models.get_universe_planets_planet_id_ok import GetUniversePlanetsPlanetIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniversePlanetsPlanetIdOk from a JSON string
get_universe_planets_planet_id_ok_instance = GetUniversePlanetsPlanetIdOk.from_json(json)
# print the JSON string representation of the object
print GetUniversePlanetsPlanetIdOk.to_json()

# convert the object into a dict
get_universe_planets_planet_id_ok_dict = get_universe_planets_planet_id_ok_instance.to_dict()
# create an instance of GetUniversePlanetsPlanetIdOk from a dict
get_universe_planets_planet_id_ok_form_dict = get_universe_planets_planet_id_ok.from_dict(get_universe_planets_planet_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


