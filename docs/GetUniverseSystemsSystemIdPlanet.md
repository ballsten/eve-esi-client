# GetUniverseSystemsSystemIdPlanet

planet object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asteroid_belts** | **List[int]** | asteroid_belts array | [optional] 
**moons** | **List[int]** | moons array | [optional] 
**planet_id** | **int** | planet_id integer | 

## Example

```python
from esi_client.models.get_universe_systems_system_id_planet import GetUniverseSystemsSystemIdPlanet

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseSystemsSystemIdPlanet from a JSON string
get_universe_systems_system_id_planet_instance = GetUniverseSystemsSystemIdPlanet.from_json(json)
# print the JSON string representation of the object
print GetUniverseSystemsSystemIdPlanet.to_json()

# convert the object into a dict
get_universe_systems_system_id_planet_dict = get_universe_systems_system_id_planet_instance.to_dict()
# create an instance of GetUniverseSystemsSystemIdPlanet from a dict
get_universe_systems_system_id_planet_form_dict = get_universe_systems_system_id_planet.from_dict(get_universe_systems_system_id_planet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


