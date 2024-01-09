# GetFwLeaderboardsOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kills** | [**GetFwLeaderboardsKills**](GetFwLeaderboardsKills.md) |  | 
**victory_points** | [**GetFwLeaderboardsVictoryPoints**](GetFwLeaderboardsVictoryPoints.md) |  | 

## Example

```python
from esi_client.models.get_fw_leaderboards_ok import GetFwLeaderboardsOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetFwLeaderboardsOk from a JSON string
get_fw_leaderboards_ok_instance = GetFwLeaderboardsOk.from_json(json)
# print the JSON string representation of the object
print GetFwLeaderboardsOk.to_json()

# convert the object into a dict
get_fw_leaderboards_ok_dict = get_fw_leaderboards_ok_instance.to_dict()
# create an instance of GetFwLeaderboardsOk from a dict
get_fw_leaderboards_ok_form_dict = get_fw_leaderboards_ok.from_dict(get_fw_leaderboards_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


