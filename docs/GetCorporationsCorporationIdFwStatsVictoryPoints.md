# GetCorporationsCorporationIdFwStatsVictoryPoints

Summary of victory points gained by the given corporation for the enlisted faction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_week** | **int** | Last week&#39;s victory points gained by members of the given corporation | 
**total** | **int** | Total victory points gained since the given corporation enlisted | 
**yesterday** | **int** | Yesterday&#39;s victory points gained by members of the given corporation | 

## Example

```python
from esi_client.models.get_corporations_corporation_id_fw_stats_victory_points import GetCorporationsCorporationIdFwStatsVictoryPoints

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdFwStatsVictoryPoints from a JSON string
get_corporations_corporation_id_fw_stats_victory_points_instance = GetCorporationsCorporationIdFwStatsVictoryPoints.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdFwStatsVictoryPoints.to_json()

# convert the object into a dict
get_corporations_corporation_id_fw_stats_victory_points_dict = get_corporations_corporation_id_fw_stats_victory_points_instance.to_dict()
# create an instance of GetCorporationsCorporationIdFwStatsVictoryPoints from a dict
get_corporations_corporation_id_fw_stats_victory_points_form_dict = get_corporations_corporation_id_fw_stats_victory_points.from_dict(get_corporations_corporation_id_fw_stats_victory_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


