# PostCharactersCharacterIdMailMail

mail object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved_cost** | **int** | approved_cost integer | [optional] [default to 0]
**body** | **str** | body string | 
**recipients** | [**List[PostCharactersCharacterIdMailRecipient]**](PostCharactersCharacterIdMailRecipient.md) | recipients array | 
**subject** | **str** | subject string | 

## Example

```python
from esi_client.models.post_characters_character_id_mail_mail import PostCharactersCharacterIdMailMail

# TODO update the JSON string below
json = "{}"
# create an instance of PostCharactersCharacterIdMailMail from a JSON string
post_characters_character_id_mail_mail_instance = PostCharactersCharacterIdMailMail.from_json(json)
# print the JSON string representation of the object
print PostCharactersCharacterIdMailMail.to_json()

# convert the object into a dict
post_characters_character_id_mail_mail_dict = post_characters_character_id_mail_mail_instance.to_dict()
# create an instance of PostCharactersCharacterIdMailMail from a dict
post_characters_character_id_mail_mail_form_dict = post_characters_character_id_mail_mail.from_dict(post_characters_character_id_mail_mail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


