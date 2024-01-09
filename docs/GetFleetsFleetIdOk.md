# GetFleetsFleetIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_free_move** | **bool** | Is free-move enabled | 
**is_registered** | **bool** | Does the fleet have an active fleet advertisement | 
**is_voice_enabled** | **bool** | Is EVE Voice enabled | 
**motd** | **str** | Fleet MOTD in CCP flavoured HTML | 

## Example

```python
from esi_client.models.get_fleets_fleet_id_ok import GetFleetsFleetIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetFleetsFleetIdOk from a JSON string
get_fleets_fleet_id_ok_instance = GetFleetsFleetIdOk.from_json(json)
# print the JSON string representation of the object
print GetFleetsFleetIdOk.to_json()

# convert the object into a dict
get_fleets_fleet_id_ok_dict = get_fleets_fleet_id_ok_instance.to_dict()
# create an instance of GetFleetsFleetIdOk from a dict
get_fleets_fleet_id_ok_form_dict = get_fleets_fleet_id_ok.from_dict(get_fleets_fleet_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


