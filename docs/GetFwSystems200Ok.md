# GetFwSystems200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contested** | **str** | contested string | 
**occupier_faction_id** | **int** | occupier_faction_id integer | 
**owner_faction_id** | **int** | owner_faction_id integer | 
**solar_system_id** | **int** | solar_system_id integer | 
**victory_points** | **int** | victory_points integer | 
**victory_points_threshold** | **int** | victory_points_threshold integer | 

## Example

```python
from esi_client.models.get_fw_systems200_ok import GetFwSystems200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetFwSystems200Ok from a JSON string
get_fw_systems200_ok_instance = GetFwSystems200Ok.from_json(json)
# print the JSON string representation of the object
print GetFwSystems200Ok.to_json()

# convert the object into a dict
get_fw_systems200_ok_dict = get_fw_systems200_ok_instance.to_dict()
# create an instance of GetFwSystems200Ok from a dict
get_fw_systems200_ok_form_dict = get_fw_systems200_ok.from_dict(get_fw_systems200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


