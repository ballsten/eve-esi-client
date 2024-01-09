# PutFleetsFleetIdNewSettings

new_settings object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_free_move** | **bool** | Should free-move be enabled in the fleet | [optional] 
**motd** | **str** | New fleet MOTD in CCP flavoured HTML | [optional] 

## Example

```python
from esi_client.models.put_fleets_fleet_id_new_settings import PutFleetsFleetIdNewSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PutFleetsFleetIdNewSettings from a JSON string
put_fleets_fleet_id_new_settings_instance = PutFleetsFleetIdNewSettings.from_json(json)
# print the JSON string representation of the object
print PutFleetsFleetIdNewSettings.to_json()

# convert the object into a dict
put_fleets_fleet_id_new_settings_dict = put_fleets_fleet_id_new_settings_instance.to_dict()
# create an instance of PutFleetsFleetIdNewSettings from a dict
put_fleets_fleet_id_new_settings_form_dict = put_fleets_fleet_id_new_settings.from_dict(put_fleets_fleet_id_new_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


