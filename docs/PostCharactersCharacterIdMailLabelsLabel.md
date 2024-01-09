# PostCharactersCharacterIdMailLabelsLabel

label object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | Hexadecimal string representing label color, in RGB format | [optional] [default to '#ffffff']
**name** | **str** | name string | 

## Example

```python
from esi_client.models.post_characters_character_id_mail_labels_label import PostCharactersCharacterIdMailLabelsLabel

# TODO update the JSON string below
json = "{}"
# create an instance of PostCharactersCharacterIdMailLabelsLabel from a JSON string
post_characters_character_id_mail_labels_label_instance = PostCharactersCharacterIdMailLabelsLabel.from_json(json)
# print the JSON string representation of the object
print PostCharactersCharacterIdMailLabelsLabel.to_json()

# convert the object into a dict
post_characters_character_id_mail_labels_label_dict = post_characters_character_id_mail_labels_label_instance.to_dict()
# create an instance of PostCharactersCharacterIdMailLabelsLabel from a dict
post_characters_character_id_mail_labels_label_form_dict = post_characters_character_id_mail_labels_label.from_dict(post_characters_character_id_mail_labels_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


