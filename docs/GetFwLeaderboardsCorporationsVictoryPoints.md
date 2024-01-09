# GetFwLeaderboardsCorporationsVictoryPoints

Top 10 rankings of corporations by victory points from yesterday, last week and in total

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_total** | [**List[GetFwLeaderboardsCorporationsActiveTotalActiveTotal1]**](GetFwLeaderboardsCorporationsActiveTotalActiveTotal1.md) | Top 10 ranking of corporations active in faction warfare by total victory points. A corporation is considered \&quot;active\&quot; if they have participated in faction warfare in the past 14 days | 
**last_week** | [**List[GetFwLeaderboardsCorporationsLastWeekLastWeek1]**](GetFwLeaderboardsCorporationsLastWeekLastWeek1.md) | Top 10 ranking of corporations by victory points in the past week | 
**yesterday** | [**List[GetFwLeaderboardsCorporationsYesterdayYesterday1]**](GetFwLeaderboardsCorporationsYesterdayYesterday1.md) | Top 10 ranking of corporations by victory points in the past day | 

## Example

```python
from esi_client.models.get_fw_leaderboards_corporations_victory_points import GetFwLeaderboardsCorporationsVictoryPoints

# TODO update the JSON string below
json = "{}"
# create an instance of GetFwLeaderboardsCorporationsVictoryPoints from a JSON string
get_fw_leaderboards_corporations_victory_points_instance = GetFwLeaderboardsCorporationsVictoryPoints.from_json(json)
# print the JSON string representation of the object
print GetFwLeaderboardsCorporationsVictoryPoints.to_json()

# convert the object into a dict
get_fw_leaderboards_corporations_victory_points_dict = get_fw_leaderboards_corporations_victory_points_instance.to_dict()
# create an instance of GetFwLeaderboardsCorporationsVictoryPoints from a dict
get_fw_leaderboards_corporations_victory_points_form_dict = get_fw_leaderboards_corporations_victory_points.from_dict(get_fw_leaderboards_corporations_victory_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


