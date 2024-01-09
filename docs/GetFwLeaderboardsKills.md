# GetFwLeaderboardsKills

Top 4 rankings of factions by number of kills from yesterday, last week and in total

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_total** | [**List[GetFwLeaderboardsActiveTotalActiveTotal]**](GetFwLeaderboardsActiveTotalActiveTotal.md) | Top 4 ranking of factions active in faction warfare by total kills. A faction is considered \&quot;active\&quot; if they have participated in faction warfare in the past 14 days | 
**last_week** | [**List[GetFwLeaderboardsLastWeekLastWeek]**](GetFwLeaderboardsLastWeekLastWeek.md) | Top 4 ranking of factions by kills in the past week | 
**yesterday** | [**List[GetFwLeaderboardsYesterdayYesterday]**](GetFwLeaderboardsYesterdayYesterday.md) | Top 4 ranking of factions by kills in the past day | 

## Example

```python
from esi_client.models.get_fw_leaderboards_kills import GetFwLeaderboardsKills

# TODO update the JSON string below
json = "{}"
# create an instance of GetFwLeaderboardsKills from a JSON string
get_fw_leaderboards_kills_instance = GetFwLeaderboardsKills.from_json(json)
# print the JSON string representation of the object
print GetFwLeaderboardsKills.to_json()

# convert the object into a dict
get_fw_leaderboards_kills_dict = get_fw_leaderboards_kills_instance.to_dict()
# create an instance of GetFwLeaderboardsKills from a dict
get_fw_leaderboards_kills_form_dict = get_fw_leaderboards_kills.from_dict(get_fw_leaderboards_kills_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


