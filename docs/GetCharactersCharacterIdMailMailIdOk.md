# GetCharactersCharacterIdMailMailIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Mail&#39;s body | [optional] 
**var_from** | **int** | From whom the mail was sent | [optional] 
**labels** | **List[int]** | Labels attached to the mail | [optional] 
**read** | **bool** | Whether the mail is flagged as read | [optional] 
**recipients** | [**List[GetCharactersCharacterIdMailMailIdRecipient]**](GetCharactersCharacterIdMailMailIdRecipient.md) | Recipients of the mail | [optional] 
**subject** | **str** | Mail subject | [optional] 
**timestamp** | **datetime** | When the mail was sent | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_mail_mail_id_ok import GetCharactersCharacterIdMailMailIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdMailMailIdOk from a JSON string
get_characters_character_id_mail_mail_id_ok_instance = GetCharactersCharacterIdMailMailIdOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdMailMailIdOk.to_json()

# convert the object into a dict
get_characters_character_id_mail_mail_id_ok_dict = get_characters_character_id_mail_mail_id_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdMailMailIdOk from a dict
get_characters_character_id_mail_mail_id_ok_form_dict = get_characters_character_id_mail_mail_id_ok.from_dict(get_characters_character_id_mail_mail_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


