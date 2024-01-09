# GetCharactersCharacterIdMail200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** | From whom the mail was sent | [optional] 
**is_read** | **bool** | is_read boolean | [optional] 
**labels** | **List[int]** | labels array | [optional] 
**mail_id** | **int** | mail_id integer | [optional] 
**recipients** | [**List[GetCharactersCharacterIdMailRecipient]**](GetCharactersCharacterIdMailRecipient.md) | Recipients of the mail | [optional] 
**subject** | **str** | Mail subject | [optional] 
**timestamp** | **datetime** | When the mail was sent | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_mail200_ok import GetCharactersCharacterIdMail200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdMail200Ok from a JSON string
get_characters_character_id_mail200_ok_instance = GetCharactersCharacterIdMail200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdMail200Ok.to_json()

# convert the object into a dict
get_characters_character_id_mail200_ok_dict = get_characters_character_id_mail200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdMail200Ok from a dict
get_characters_character_id_mail200_ok_form_dict = get_characters_character_id_mail200_ok.from_dict(get_characters_character_id_mail200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


