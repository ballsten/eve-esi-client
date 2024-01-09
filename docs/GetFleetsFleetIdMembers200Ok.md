# GetFleetsFleetIdMembers200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character_id** | **int** | character_id integer | 
**join_time** | **datetime** | join_time string | 
**role** | **str** | Member’s role in fleet | 
**role_name** | **str** | Localized role names | 
**ship_type_id** | **int** | ship_type_id integer | 
**solar_system_id** | **int** | Solar system the member is located in | 
**squad_id** | **int** | ID of the squad the member is in. If not applicable, will be set to -1 | 
**station_id** | **int** | Station in which the member is docked in, if applicable | [optional] 
**takes_fleet_warp** | **bool** | Whether the member take fleet warps | 
**wing_id** | **int** | ID of the wing the member is in. If not applicable, will be set to -1 | 

## Example

```python
from esi_client.models.get_fleets_fleet_id_members200_ok import GetFleetsFleetIdMembers200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetFleetsFleetIdMembers200Ok from a JSON string
get_fleets_fleet_id_members200_ok_instance = GetFleetsFleetIdMembers200Ok.from_json(json)
# print the JSON string representation of the object
print GetFleetsFleetIdMembers200Ok.to_json()

# convert the object into a dict
get_fleets_fleet_id_members200_ok_dict = get_fleets_fleet_id_members200_ok_instance.to_dict()
# create an instance of GetFleetsFleetIdMembers200Ok from a dict
get_fleets_fleet_id_members200_ok_form_dict = get_fleets_fleet_id_members200_ok.from_dict(get_fleets_fleet_id_members200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


