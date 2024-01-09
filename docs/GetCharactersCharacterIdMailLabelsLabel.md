# GetCharactersCharacterIdMailLabelsLabel

label object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | color string | [optional] [default to '#ffffff']
**label_id** | **int** | label_id integer | [optional] 
**name** | **str** | name string | [optional] 
**unread_count** | **int** | unread_count integer | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_mail_labels_label import GetCharactersCharacterIdMailLabelsLabel

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdMailLabelsLabel from a JSON string
get_characters_character_id_mail_labels_label_instance = GetCharactersCharacterIdMailLabelsLabel.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdMailLabelsLabel.to_json()

# convert the object into a dict
get_characters_character_id_mail_labels_label_dict = get_characters_character_id_mail_labels_label_instance.to_dict()
# create an instance of GetCharactersCharacterIdMailLabelsLabel from a dict
get_characters_character_id_mail_labels_label_form_dict = get_characters_character_id_mail_labels_label.from_dict(get_characters_character_id_mail_labels_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


