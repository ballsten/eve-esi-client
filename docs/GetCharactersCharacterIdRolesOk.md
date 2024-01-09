# GetCharactersCharacterIdRolesOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | **List[str]** | roles array | [optional] 
**roles_at_base** | **List[str]** | roles_at_base array | [optional] 
**roles_at_hq** | **List[str]** | roles_at_hq array | [optional] 
**roles_at_other** | **List[str]** | roles_at_other array | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_roles_ok import GetCharactersCharacterIdRolesOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdRolesOk from a JSON string
get_characters_character_id_roles_ok_instance = GetCharactersCharacterIdRolesOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdRolesOk.to_json()

# convert the object into a dict
get_characters_character_id_roles_ok_dict = get_characters_character_id_roles_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdRolesOk from a dict
get_characters_character_id_roles_ok_form_dict = get_characters_character_id_roles_ok.from_dict(get_characters_character_id_roles_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


