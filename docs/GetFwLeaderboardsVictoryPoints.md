# GetFwLeaderboardsVictoryPoints

Top 4 rankings of factions by victory points from yesterday, last week and in total

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_total** | [**List[GetFwLeaderboardsActiveTotalActiveTotal1]**](GetFwLeaderboardsActiveTotalActiveTotal1.md) | Top 4 ranking of factions active in faction warfare by total victory points. A faction is considered \&quot;active\&quot; if they have participated in faction warfare in the past 14 days | 
**last_week** | [**List[GetFwLeaderboardsLastWeekLastWeek1]**](GetFwLeaderboardsLastWeekLastWeek1.md) | Top 4 ranking of factions by victory points in the past week | 
**yesterday** | [**List[GetFwLeaderboardsYesterdayYesterday1]**](GetFwLeaderboardsYesterdayYesterday1.md) | Top 4 ranking of factions by victory points in the past day | 

## Example

```python
from esi_client.models.get_fw_leaderboards_victory_points import GetFwLeaderboardsVictoryPoints

# TODO update the JSON string below
json = "{}"
# create an instance of GetFwLeaderboardsVictoryPoints from a JSON string
get_fw_leaderboards_victory_points_instance = GetFwLeaderboardsVictoryPoints.from_json(json)
# print the JSON string representation of the object
print GetFwLeaderboardsVictoryPoints.to_json()

# convert the object into a dict
get_fw_leaderboards_victory_points_dict = get_fw_leaderboards_victory_points_instance.to_dict()
# create an instance of GetFwLeaderboardsVictoryPoints from a dict
get_fw_leaderboards_victory_points_form_dict = get_fw_leaderboards_victory_points.from_dict(get_fw_leaderboards_victory_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


