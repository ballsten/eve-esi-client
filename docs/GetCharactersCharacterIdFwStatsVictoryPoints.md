# GetCharactersCharacterIdFwStatsVictoryPoints

Summary of victory points gained by the given character for the enlisted faction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_week** | **int** | Last week&#39;s victory points gained by the given character | 
**total** | **int** | Total victory points gained since the given character enlisted | 
**yesterday** | **int** | Yesterday&#39;s victory points gained by the given character | 

## Example

```python
from esi_client.models.get_characters_character_id_fw_stats_victory_points import GetCharactersCharacterIdFwStatsVictoryPoints

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdFwStatsVictoryPoints from a JSON string
get_characters_character_id_fw_stats_victory_points_instance = GetCharactersCharacterIdFwStatsVictoryPoints.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdFwStatsVictoryPoints.to_json()

# convert the object into a dict
get_characters_character_id_fw_stats_victory_points_dict = get_characters_character_id_fw_stats_victory_points_instance.to_dict()
# create an instance of GetCharactersCharacterIdFwStatsVictoryPoints from a dict
get_characters_character_id_fw_stats_victory_points_form_dict = get_characters_character_id_fw_stats_victory_points.from_dict(get_characters_character_id_fw_stats_victory_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


