# GetFwLeaderboardsCharactersOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kills** | [**GetFwLeaderboardsCharactersKills**](GetFwLeaderboardsCharactersKills.md) |  | 
**victory_points** | [**GetFwLeaderboardsCharactersVictoryPoints**](GetFwLeaderboardsCharactersVictoryPoints.md) |  | 

## Example

```python
from esi_client.models.get_fw_leaderboards_characters_ok import GetFwLeaderboardsCharactersOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetFwLeaderboardsCharactersOk from a JSON string
get_fw_leaderboards_characters_ok_instance = GetFwLeaderboardsCharactersOk.from_json(json)
# print the JSON string representation of the object
print GetFwLeaderboardsCharactersOk.to_json()

# convert the object into a dict
get_fw_leaderboards_characters_ok_dict = get_fw_leaderboards_characters_ok_instance.to_dict()
# create an instance of GetFwLeaderboardsCharactersOk from a dict
get_fw_leaderboards_characters_ok_form_dict = get_fw_leaderboards_characters_ok.from_dict(get_fw_leaderboards_characters_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


