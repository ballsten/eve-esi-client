# GetUniverseSchematicsSchematicIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_time** | **int** | Time in seconds to process a run | 
**schematic_name** | **str** | schematic_name string | 

## Example

```python
from esi_client.models.get_universe_schematics_schematic_id_ok import GetUniverseSchematicsSchematicIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseSchematicsSchematicIdOk from a JSON string
get_universe_schematics_schematic_id_ok_instance = GetUniverseSchematicsSchematicIdOk.from_json(json)
# print the JSON string representation of the object
print GetUniverseSchematicsSchematicIdOk.to_json()

# convert the object into a dict
get_universe_schematics_schematic_id_ok_dict = get_universe_schematics_schematic_id_ok_instance.to_dict()
# create an instance of GetUniverseSchematicsSchematicIdOk from a dict
get_universe_schematics_schematic_id_ok_form_dict = get_universe_schematics_schematic_id_ok.from_dict(get_universe_schematics_schematic_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


