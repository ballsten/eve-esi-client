# GetFwLeaderboardsCorporationsOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kills** | [**GetFwLeaderboardsCorporationsKills**](GetFwLeaderboardsCorporationsKills.md) |  | 
**victory_points** | [**GetFwLeaderboardsCorporationsVictoryPoints**](GetFwLeaderboardsCorporationsVictoryPoints.md) |  | 

## Example

```python
from esi_client.models.get_fw_leaderboards_corporations_ok import GetFwLeaderboardsCorporationsOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetFwLeaderboardsCorporationsOk from a JSON string
get_fw_leaderboards_corporations_ok_instance = GetFwLeaderboardsCorporationsOk.from_json(json)
# print the JSON string representation of the object
print GetFwLeaderboardsCorporationsOk.to_json()

# convert the object into a dict
get_fw_leaderboards_corporations_ok_dict = get_fw_leaderboards_corporations_ok_instance.to_dict()
# create an instance of GetFwLeaderboardsCorporationsOk from a dict
get_fw_leaderboards_corporations_ok_form_dict = get_fw_leaderboards_corporations_ok.from_dict(get_fw_leaderboards_corporations_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


