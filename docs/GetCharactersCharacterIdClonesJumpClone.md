# GetCharactersCharacterIdClonesJumpClone

jump_clone object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**implants** | **List[int]** | implants array | 
**jump_clone_id** | **int** | jump_clone_id integer | 
**location_id** | **int** | location_id integer | 
**location_type** | **str** | location_type string | 
**name** | **str** | name string | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_clones_jump_clone import GetCharactersCharacterIdClonesJumpClone

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdClonesJumpClone from a JSON string
get_characters_character_id_clones_jump_clone_instance = GetCharactersCharacterIdClonesJumpClone.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdClonesJumpClone.to_json()

# convert the object into a dict
get_characters_character_id_clones_jump_clone_dict = get_characters_character_id_clones_jump_clone_instance.to_dict()
# create an instance of GetCharactersCharacterIdClonesJumpClone from a dict
get_characters_character_id_clones_jump_clone_form_dict = get_characters_character_id_clones_jump_clone.from_dict(get_characters_character_id_clones_jump_clone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


