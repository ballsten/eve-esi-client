# GetUniverseGraphicsGraphicIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collision_file** | **str** | collision_file string | [optional] 
**graphic_file** | **str** | graphic_file string | [optional] 
**graphic_id** | **int** | graphic_id integer | 
**icon_folder** | **str** | icon_folder string | [optional] 
**sof_dna** | **str** | sof_dna string | [optional] 
**sof_fation_name** | **str** | sof_fation_name string | [optional] 
**sof_hull_name** | **str** | sof_hull_name string | [optional] 
**sof_race_name** | **str** | sof_race_name string | [optional] 

## Example

```python
from esi_client.models.get_universe_graphics_graphic_id_ok import GetUniverseGraphicsGraphicIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseGraphicsGraphicIdOk from a JSON string
get_universe_graphics_graphic_id_ok_instance = GetUniverseGraphicsGraphicIdOk.from_json(json)
# print the JSON string representation of the object
print GetUniverseGraphicsGraphicIdOk.to_json()

# convert the object into a dict
get_universe_graphics_graphic_id_ok_dict = get_universe_graphics_graphic_id_ok_instance.to_dict()
# create an instance of GetUniverseGraphicsGraphicIdOk from a dict
get_universe_graphics_graphic_id_ok_form_dict = get_universe_graphics_graphic_id_ok.from_dict(get_universe_graphics_graphic_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


