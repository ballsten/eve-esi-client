# GetCorporationsCorporationIdFwStatsKills

Summary of kills done by the given corporation against enemy factions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_week** | **int** | Last week&#39;s total number of kills by members of the given corporation against enemy factions | 
**total** | **int** | Total number of kills by members of the given corporation against enemy factions since the corporation enlisted | 
**yesterday** | **int** | Yesterday&#39;s total number of kills by members of the given corporation against enemy factions | 

## Example

```python
from esi_client.models.get_corporations_corporation_id_fw_stats_kills import GetCorporationsCorporationIdFwStatsKills

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdFwStatsKills from a JSON string
get_corporations_corporation_id_fw_stats_kills_instance = GetCorporationsCorporationIdFwStatsKills.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdFwStatsKills.to_json()

# convert the object into a dict
get_corporations_corporation_id_fw_stats_kills_dict = get_corporations_corporation_id_fw_stats_kills_instance.to_dict()
# create an instance of GetCorporationsCorporationIdFwStatsKills from a dict
get_corporations_corporation_id_fw_stats_kills_form_dict = get_corporations_corporation_id_fw_stats_kills.from_dict(get_corporations_corporation_id_fw_stats_kills_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


