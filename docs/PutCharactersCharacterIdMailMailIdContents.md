# PutCharactersCharacterIdMailMailIdContents

contents object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[int]** | Labels to assign to the mail. Pre-existing labels are unassigned. | [optional] 
**read** | **bool** | Whether the mail is flagged as read | [optional] 

## Example

```python
from esi_client.models.put_characters_character_id_mail_mail_id_contents import PutCharactersCharacterIdMailMailIdContents

# TODO update the JSON string below
json = "{}"
# create an instance of PutCharactersCharacterIdMailMailIdContents from a JSON string
put_characters_character_id_mail_mail_id_contents_instance = PutCharactersCharacterIdMailMailIdContents.from_json(json)
# print the JSON string representation of the object
print PutCharactersCharacterIdMailMailIdContents.to_json()

# convert the object into a dict
put_characters_character_id_mail_mail_id_contents_dict = put_characters_character_id_mail_mail_id_contents_instance.to_dict()
# create an instance of PutCharactersCharacterIdMailMailIdContents from a dict
put_characters_character_id_mail_mail_id_contents_form_dict = put_characters_character_id_mail_mail_id_contents.from_dict(put_characters_character_id_mail_mail_id_contents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


