# PostCharactersCharacterIdMailRecipient

recipient object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **int** | recipient_id integer | 
**recipient_type** | **str** | recipient_type string | 

## Example

```python
from esi_client.models.post_characters_character_id_mail_recipient import PostCharactersCharacterIdMailRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of PostCharactersCharacterIdMailRecipient from a JSON string
post_characters_character_id_mail_recipient_instance = PostCharactersCharacterIdMailRecipient.from_json(json)
# print the JSON string representation of the object
print PostCharactersCharacterIdMailRecipient.to_json()

# convert the object into a dict
post_characters_character_id_mail_recipient_dict = post_characters_character_id_mail_recipient_instance.to_dict()
# create an instance of PostCharactersCharacterIdMailRecipient from a dict
post_characters_character_id_mail_recipient_form_dict = post_characters_character_id_mail_recipient.from_dict(post_characters_character_id_mail_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


