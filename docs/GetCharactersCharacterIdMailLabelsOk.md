# GetCharactersCharacterIdMailLabelsOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**List[GetCharactersCharacterIdMailLabelsLabel]**](GetCharactersCharacterIdMailLabelsLabel.md) | labels array | [optional] 
**total_unread_count** | **int** | total_unread_count integer | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_mail_labels_ok import GetCharactersCharacterIdMailLabelsOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdMailLabelsOk from a JSON string
get_characters_character_id_mail_labels_ok_instance = GetCharactersCharacterIdMailLabelsOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdMailLabelsOk.to_json()

# convert the object into a dict
get_characters_character_id_mail_labels_ok_dict = get_characters_character_id_mail_labels_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdMailLabelsOk from a dict
get_characters_character_id_mail_labels_ok_form_dict = get_characters_character_id_mail_labels_ok.from_dict(get_characters_character_id_mail_labels_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


