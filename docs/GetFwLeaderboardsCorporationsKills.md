# GetFwLeaderboardsCorporationsKills

Top 10 rankings of corporations by number of kills from yesterday, last week and in total

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_total** | [**List[GetFwLeaderboardsCorporationsActiveTotalActiveTotal]**](GetFwLeaderboardsCorporationsActiveTotalActiveTotal.md) | Top 10 ranking of corporations active in faction warfare by total kills. A corporation is considered \&quot;active\&quot; if they have participated in faction warfare in the past 14 days | 
**last_week** | [**List[GetFwLeaderboardsCorporationsLastWeekLastWeek]**](GetFwLeaderboardsCorporationsLastWeekLastWeek.md) | Top 10 ranking of corporations by kills in the past week | 
**yesterday** | [**List[GetFwLeaderboardsCorporationsYesterdayYesterday]**](GetFwLeaderboardsCorporationsYesterdayYesterday.md) | Top 10 ranking of corporations by kills in the past day | 

## Example

```python
from esi_client.models.get_fw_leaderboards_corporations_kills import GetFwLeaderboardsCorporationsKills

# TODO update the JSON string below
json = "{}"
# create an instance of GetFwLeaderboardsCorporationsKills from a JSON string
get_fw_leaderboards_corporations_kills_instance = GetFwLeaderboardsCorporationsKills.from_json(json)
# print the JSON string representation of the object
print GetFwLeaderboardsCorporationsKills.to_json()

# convert the object into a dict
get_fw_leaderboards_corporations_kills_dict = get_fw_leaderboards_corporations_kills_instance.to_dict()
# create an instance of GetFwLeaderboardsCorporationsKills from a dict
get_fw_leaderboards_corporations_kills_form_dict = get_fw_leaderboards_corporations_kills.from_dict(get_fw_leaderboards_corporations_kills_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


