# GetCharactersCharacterIdSkillsOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skills** | [**List[GetCharactersCharacterIdSkillsSkill]**](GetCharactersCharacterIdSkillsSkill.md) | skills array | 
**total_sp** | **int** | total_sp integer | 
**unallocated_sp** | **int** | Skill points available to be assigned | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_skills_ok import GetCharactersCharacterIdSkillsOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdSkillsOk from a JSON string
get_characters_character_id_skills_ok_instance = GetCharactersCharacterIdSkillsOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdSkillsOk.to_json()

# convert the object into a dict
get_characters_character_id_skills_ok_dict = get_characters_character_id_skills_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdSkillsOk from a dict
get_characters_character_id_skills_ok_form_dict = get_characters_character_id_skills_ok.from_dict(get_characters_character_id_skills_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


