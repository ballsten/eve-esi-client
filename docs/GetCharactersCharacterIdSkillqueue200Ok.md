# GetCharactersCharacterIdSkillqueue200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finish_date** | **datetime** | Date on which training of the skill will complete. Omitted if the skill queue is paused. | [optional] 
**finished_level** | **int** | finished_level integer | 
**level_end_sp** | **int** | level_end_sp integer | [optional] 
**level_start_sp** | **int** | Amount of SP that was in the skill when it started training it&#39;s current level. Used to calculate % of current level complete. | [optional] 
**queue_position** | **int** | queue_position integer | 
**skill_id** | **int** | skill_id integer | 
**start_date** | **datetime** | start_date string | [optional] 
**training_start_sp** | **int** | training_start_sp integer | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_skillqueue200_ok import GetCharactersCharacterIdSkillqueue200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdSkillqueue200Ok from a JSON string
get_characters_character_id_skillqueue200_ok_instance = GetCharactersCharacterIdSkillqueue200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdSkillqueue200Ok.to_json()

# convert the object into a dict
get_characters_character_id_skillqueue200_ok_dict = get_characters_character_id_skillqueue200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdSkillqueue200Ok from a dict
get_characters_character_id_skillqueue200_ok_form_dict = get_characters_character_id_skillqueue200_ok.from_dict(get_characters_character_id_skillqueue200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


