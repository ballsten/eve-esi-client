# GetFleetsFleetIdWings200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id integer | 
**name** | **str** | name string | 
**squads** | [**List[GetFleetsFleetIdWingsSquad]**](GetFleetsFleetIdWingsSquad.md) | squads array | 

## Example

```python
from esi_client.models.get_fleets_fleet_id_wings200_ok import GetFleetsFleetIdWings200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetFleetsFleetIdWings200Ok from a JSON string
get_fleets_fleet_id_wings200_ok_instance = GetFleetsFleetIdWings200Ok.from_json(json)
# print the JSON string representation of the object
print GetFleetsFleetIdWings200Ok.to_json()

# convert the object into a dict
get_fleets_fleet_id_wings200_ok_dict = get_fleets_fleet_id_wings200_ok_instance.to_dict()
# create an instance of GetFleetsFleetIdWings200Ok from a dict
get_fleets_fleet_id_wings200_ok_form_dict = get_fleets_fleet_id_wings200_ok.from_dict(get_fleets_fleet_id_wings200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


