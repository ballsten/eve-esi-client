# GetUniverseConstellationsConstellationIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constellation_id** | **int** | constellation_id integer | 
**name** | **str** | name string | 
**position** | [**GetUniverseConstellationsConstellationIdPosition**](GetUniverseConstellationsConstellationIdPosition.md) |  | 
**region_id** | **int** | The region this constellation is in | 
**systems** | **List[int]** | systems array | 

## Example

```python
from esi_client.models.get_universe_constellations_constellation_id_ok import GetUniverseConstellationsConstellationIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseConstellationsConstellationIdOk from a JSON string
get_universe_constellations_constellation_id_ok_instance = GetUniverseConstellationsConstellationIdOk.from_json(json)
# print the JSON string representation of the object
print GetUniverseConstellationsConstellationIdOk.to_json()

# convert the object into a dict
get_universe_constellations_constellation_id_ok_dict = get_universe_constellations_constellation_id_ok_instance.to_dict()
# create an instance of GetUniverseConstellationsConstellationIdOk from a dict
get_universe_constellations_constellation_id_ok_form_dict = get_universe_constellations_constellation_id_ok.from_dict(get_universe_constellations_constellation_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


