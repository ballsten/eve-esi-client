# GetFwLeaderboardsCharactersKills

Top 100 rankings of pilots by number of kills from yesterday, last week and in total

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_total** | [**List[GetFwLeaderboardsCharactersActiveTotalActiveTotal]**](GetFwLeaderboardsCharactersActiveTotalActiveTotal.md) | Top 100 ranking of pilots active in faction warfare by total kills. A pilot is considered \&quot;active\&quot; if they have participated in faction warfare in the past 14 days | 
**last_week** | [**List[GetFwLeaderboardsCharactersLastWeekLastWeek]**](GetFwLeaderboardsCharactersLastWeekLastWeek.md) | Top 100 ranking of pilots by kills in the past week | 
**yesterday** | [**List[GetFwLeaderboardsCharactersYesterdayYesterday]**](GetFwLeaderboardsCharactersYesterdayYesterday.md) | Top 100 ranking of pilots by kills in the past day | 

## Example

```python
from esi_client.models.get_fw_leaderboards_characters_kills import GetFwLeaderboardsCharactersKills

# TODO update the JSON string below
json = "{}"
# create an instance of GetFwLeaderboardsCharactersKills from a JSON string
get_fw_leaderboards_characters_kills_instance = GetFwLeaderboardsCharactersKills.from_json(json)
# print the JSON string representation of the object
print GetFwLeaderboardsCharactersKills.to_json()

# convert the object into a dict
get_fw_leaderboards_characters_kills_dict = get_fw_leaderboards_characters_kills_instance.to_dict()
# create an instance of GetFwLeaderboardsCharactersKills from a dict
get_fw_leaderboards_characters_kills_form_dict = get_fw_leaderboards_characters_kills.from_dict(get_fw_leaderboards_characters_kills_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


