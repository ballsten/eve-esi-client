# GetCorporationsCorporationIdFwStatsOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enlisted_on** | **datetime** | The enlistment date of the given corporation into faction warfare. Will not be included if corporation is not enlisted in faction warfare | [optional] 
**faction_id** | **int** | The faction the given corporation is enlisted to fight for. Will not be included if corporation is not enlisted in faction warfare | [optional] 
**kills** | [**GetCorporationsCorporationIdFwStatsKills**](GetCorporationsCorporationIdFwStatsKills.md) |  | 
**pilots** | **int** | How many pilots the enlisted corporation has. Will not be included if corporation is not enlisted in faction warfare | [optional] 
**victory_points** | [**GetCorporationsCorporationIdFwStatsVictoryPoints**](GetCorporationsCorporationIdFwStatsVictoryPoints.md) |  | 

## Example

```python
from esi_client.models.get_corporations_corporation_id_fw_stats_ok import GetCorporationsCorporationIdFwStatsOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdFwStatsOk from a JSON string
get_corporations_corporation_id_fw_stats_ok_instance = GetCorporationsCorporationIdFwStatsOk.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdFwStatsOk.to_json()

# convert the object into a dict
get_corporations_corporation_id_fw_stats_ok_dict = get_corporations_corporation_id_fw_stats_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdFwStatsOk from a dict
get_corporations_corporation_id_fw_stats_ok_form_dict = get_corporations_corporation_id_fw_stats_ok.from_dict(get_corporations_corporation_id_fw_stats_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


