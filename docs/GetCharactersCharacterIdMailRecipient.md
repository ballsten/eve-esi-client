# GetCharactersCharacterIdMailRecipient

recipient object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **int** | recipient_id integer | 
**recipient_type** | **str** | recipient_type string | 

## Example

```python
from esi_client.models.get_characters_character_id_mail_recipient import GetCharactersCharacterIdMailRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdMailRecipient from a JSON string
get_characters_character_id_mail_recipient_instance = GetCharactersCharacterIdMailRecipient.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdMailRecipient.to_json()

# convert the object into a dict
get_characters_character_id_mail_recipient_dict = get_characters_character_id_mail_recipient_instance.to_dict()
# create an instance of GetCharactersCharacterIdMailRecipient from a dict
get_characters_character_id_mail_recipient_form_dict = get_characters_character_id_mail_recipient.from_dict(get_characters_character_id_mail_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


