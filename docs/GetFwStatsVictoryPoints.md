# GetFwStatsVictoryPoints

Summary of victory points gained for the given faction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_week** | **int** | Last week&#39;s victory points gained | 
**total** | **int** | Total victory points gained since faction warfare began | 
**yesterday** | **int** | Yesterday&#39;s victory points gained | 

## Example

```python
from esi_client.models.get_fw_stats_victory_points import GetFwStatsVictoryPoints

# TODO update the JSON string below
json = "{}"
# create an instance of GetFwStatsVictoryPoints from a JSON string
get_fw_stats_victory_points_instance = GetFwStatsVictoryPoints.from_json(json)
# print the JSON string representation of the object
print GetFwStatsVictoryPoints.to_json()

# convert the object into a dict
get_fw_stats_victory_points_dict = get_fw_stats_victory_points_instance.to_dict()
# create an instance of GetFwStatsVictoryPoints from a dict
get_fw_stats_victory_points_form_dict = get_fw_stats_victory_points.from_dict(get_fw_stats_victory_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


