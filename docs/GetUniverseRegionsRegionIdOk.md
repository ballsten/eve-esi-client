# GetUniverseRegionsRegionIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constellations** | **List[int]** | constellations array | 
**description** | **str** | description string | [optional] 
**name** | **str** | name string | 
**region_id** | **int** | region_id integer | 

## Example

```python
from esi_client.models.get_universe_regions_region_id_ok import GetUniverseRegionsRegionIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseRegionsRegionIdOk from a JSON string
get_universe_regions_region_id_ok_instance = GetUniverseRegionsRegionIdOk.from_json(json)
# print the JSON string representation of the object
print GetUniverseRegionsRegionIdOk.to_json()

# convert the object into a dict
get_universe_regions_region_id_ok_dict = get_universe_regions_region_id_ok_instance.to_dict()
# create an instance of GetUniverseRegionsRegionIdOk from a dict
get_universe_regions_region_id_ok_form_dict = get_universe_regions_region_id_ok.from_dict(get_universe_regions_region_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


