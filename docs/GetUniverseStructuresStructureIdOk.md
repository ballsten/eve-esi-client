# GetUniverseStructuresStructureIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The full name of the structure | 
**owner_id** | **int** | The ID of the corporation who owns this particular structure | 
**position** | [**GetUniverseStructuresStructureIdPosition**](GetUniverseStructuresStructureIdPosition.md) |  | [optional] 
**solar_system_id** | **int** | solar_system_id integer | 
**type_id** | **int** | type_id integer | [optional] 

## Example

```python
from esi_client.models.get_universe_structures_structure_id_ok import GetUniverseStructuresStructureIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseStructuresStructureIdOk from a JSON string
get_universe_structures_structure_id_ok_instance = GetUniverseStructuresStructureIdOk.from_json(json)
# print the JSON string representation of the object
print GetUniverseStructuresStructureIdOk.to_json()

# convert the object into a dict
get_universe_structures_structure_id_ok_dict = get_universe_structures_structure_id_ok_instance.to_dict()
# create an instance of GetUniverseStructuresStructureIdOk from a dict
get_universe_structures_structure_id_ok_form_dict = get_universe_structures_structure_id_ok.from_dict(get_universe_structures_structure_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


