# GetCharactersCharacterIdMailMailIdRecipient

recipient object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **int** | recipient_id integer | 
**recipient_type** | **str** | recipient_type string | 

## Example

```python
from esi_client.models.get_characters_character_id_mail_mail_id_recipient import GetCharactersCharacterIdMailMailIdRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdMailMailIdRecipient from a JSON string
get_characters_character_id_mail_mail_id_recipient_instance = GetCharactersCharacterIdMailMailIdRecipient.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdMailMailIdRecipient.to_json()

# convert the object into a dict
get_characters_character_id_mail_mail_id_recipient_dict = get_characters_character_id_mail_mail_id_recipient_instance.to_dict()
# create an instance of GetCharactersCharacterIdMailMailIdRecipient from a dict
get_characters_character_id_mail_mail_id_recipient_form_dict = get_characters_character_id_mail_mail_id_recipient.from_dict(get_characters_character_id_mail_mail_id_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


