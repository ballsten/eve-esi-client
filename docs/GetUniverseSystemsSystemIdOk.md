# GetUniverseSystemsSystemIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constellation_id** | **int** | The constellation this solar system is in | 
**name** | **str** | name string | 
**planets** | [**List[GetUniverseSystemsSystemIdPlanet]**](GetUniverseSystemsSystemIdPlanet.md) | planets array | [optional] 
**position** | [**GetUniverseSystemsSystemIdPosition**](GetUniverseSystemsSystemIdPosition.md) |  | 
**security_class** | **str** | security_class string | [optional] 
**security_status** | **float** | security_status number | 
**star_id** | **int** | star_id integer | [optional] 
**stargates** | **List[int]** | stargates array | [optional] 
**stations** | **List[int]** | stations array | [optional] 
**system_id** | **int** | system_id integer | 

## Example

```python
from esi_client.models.get_universe_systems_system_id_ok import GetUniverseSystemsSystemIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseSystemsSystemIdOk from a JSON string
get_universe_systems_system_id_ok_instance = GetUniverseSystemsSystemIdOk.from_json(json)
# print the JSON string representation of the object
print GetUniverseSystemsSystemIdOk.to_json()

# convert the object into a dict
get_universe_systems_system_id_ok_dict = get_universe_systems_system_id_ok_instance.to_dict()
# create an instance of GetUniverseSystemsSystemIdOk from a dict
get_universe_systems_system_id_ok_form_dict = get_universe_systems_system_id_ok.from_dict(get_universe_systems_system_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


