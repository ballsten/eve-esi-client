# GetFwLeaderboardsCharactersVictoryPoints

Top 100 rankings of pilots by victory points from yesterday, last week and in total

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_total** | [**List[GetFwLeaderboardsCharactersActiveTotalActiveTotal1]**](GetFwLeaderboardsCharactersActiveTotalActiveTotal1.md) | Top 100 ranking of pilots active in faction warfare by total victory points. A pilot is considered \&quot;active\&quot; if they have participated in faction warfare in the past 14 days | 
**last_week** | [**List[GetFwLeaderboardsCharactersLastWeekLastWeek1]**](GetFwLeaderboardsCharactersLastWeekLastWeek1.md) | Top 100 ranking of pilots by victory points in the past week | 
**yesterday** | [**List[GetFwLeaderboardsCharactersYesterdayYesterday1]**](GetFwLeaderboardsCharactersYesterdayYesterday1.md) | Top 100 ranking of pilots by victory points in the past day | 

## Example

```python
from esi_client.models.get_fw_leaderboards_characters_victory_points import GetFwLeaderboardsCharactersVictoryPoints

# TODO update the JSON string below
json = "{}"
# create an instance of GetFwLeaderboardsCharactersVictoryPoints from a JSON string
get_fw_leaderboards_characters_victory_points_instance = GetFwLeaderboardsCharactersVictoryPoints.from_json(json)
# print the JSON string representation of the object
print GetFwLeaderboardsCharactersVictoryPoints.to_json()

# convert the object into a dict
get_fw_leaderboards_characters_victory_points_dict = get_fw_leaderboards_characters_victory_points_instance.to_dict()
# create an instance of GetFwLeaderboardsCharactersVictoryPoints from a dict
get_fw_leaderboards_characters_victory_points_form_dict = get_fw_leaderboards_characters_victory_points.from_dict(get_fw_leaderboards_characters_victory_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


