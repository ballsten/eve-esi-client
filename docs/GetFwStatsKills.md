# GetFwStatsKills

Summary of kills against an enemy faction for the given faction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_week** | **int** | Last week&#39;s total number of kills against enemy factions | 
**total** | **int** | Total number of kills against enemy factions since faction warfare began | 
**yesterday** | **int** | Yesterday&#39;s total number of kills against enemy factions | 

## Example

```python
from esi_client.models.get_fw_stats_kills import GetFwStatsKills

# TODO update the JSON string below
json = "{}"
# create an instance of GetFwStatsKills from a JSON string
get_fw_stats_kills_instance = GetFwStatsKills.from_json(json)
# print the JSON string representation of the object
print GetFwStatsKills.to_json()

# convert the object into a dict
get_fw_stats_kills_dict = get_fw_stats_kills_instance.to_dict()
# create an instance of GetFwStatsKills from a dict
get_fw_stats_kills_form_dict = get_fw_stats_kills.from_dict(get_fw_stats_kills_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


