# GetCharactersCharacterIdFwStatsOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_rank** | **int** | The given character&#39;s current faction rank | [optional] 
**enlisted_on** | **datetime** | The enlistment date of the given character into faction warfare. Will not be included if character is not enlisted in faction warfare | [optional] 
**faction_id** | **int** | The faction the given character is enlisted to fight for. Will not be included if character is not enlisted in faction warfare | [optional] 
**highest_rank** | **int** | The given character&#39;s highest faction rank achieved | [optional] 
**kills** | [**GetCharactersCharacterIdFwStatsKills**](GetCharactersCharacterIdFwStatsKills.md) |  | 
**victory_points** | [**GetCharactersCharacterIdFwStatsVictoryPoints**](GetCharactersCharacterIdFwStatsVictoryPoints.md) |  | 

## Example

```python
from esi_client.models.get_characters_character_id_fw_stats_ok import GetCharactersCharacterIdFwStatsOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdFwStatsOk from a JSON string
get_characters_character_id_fw_stats_ok_instance = GetCharactersCharacterIdFwStatsOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdFwStatsOk.to_json()

# convert the object into a dict
get_characters_character_id_fw_stats_ok_dict = get_characters_character_id_fw_stats_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdFwStatsOk from a dict
get_characters_character_id_fw_stats_ok_form_dict = get_characters_character_id_fw_stats_ok.from_dict(get_characters_character_id_fw_stats_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


