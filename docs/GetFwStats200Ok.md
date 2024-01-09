# GetFwStats200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faction_id** | **int** | faction_id integer | 
**kills** | [**GetFwStatsKills**](GetFwStatsKills.md) |  | 
**pilots** | **int** | How many pilots fight for the given faction | 
**systems_controlled** | **int** | The number of solar systems controlled by the given faction | 
**victory_points** | [**GetFwStatsVictoryPoints**](GetFwStatsVictoryPoints.md) |  | 

## Example

```python
from esi_client.models.get_fw_stats200_ok import GetFwStats200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetFwStats200Ok from a JSON string
get_fw_stats200_ok_instance = GetFwStats200Ok.from_json(json)
# print the JSON string representation of the object
print GetFwStats200Ok.to_json()

# convert the object into a dict
get_fw_stats200_ok_dict = get_fw_stats200_ok_instance.to_dict()
# create an instance of GetFwStats200Ok from a dict
get_fw_stats200_ok_form_dict = get_fw_stats200_ok.from_dict(get_fw_stats200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


