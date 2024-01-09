# GetCharactersCharacterIdSkillsSkill

skill object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_skill_level** | **int** | active_skill_level integer | 
**skill_id** | **int** | skill_id integer | 
**skillpoints_in_skill** | **int** | skillpoints_in_skill integer | 
**trained_skill_level** | **int** | trained_skill_level integer | 

## Example

```python
from esi_client.models.get_characters_character_id_skills_skill import GetCharactersCharacterIdSkillsSkill

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdSkillsSkill from a JSON string
get_characters_character_id_skills_skill_instance = GetCharactersCharacterIdSkillsSkill.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdSkillsSkill.to_json()

# convert the object into a dict
get_characters_character_id_skills_skill_dict = get_characters_character_id_skills_skill_instance.to_dict()
# create an instance of GetCharactersCharacterIdSkillsSkill from a dict
get_characters_character_id_skills_skill_form_dict = get_characters_character_id_skills_skill.from_dict(get_characters_character_id_skills_skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


