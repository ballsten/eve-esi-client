# GetCharactersCharacterIdNotifications200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_read** | **bool** | is_read boolean | [optional] 
**notification_id** | **int** | notification_id integer | 
**sender_id** | **int** | sender_id integer | 
**sender_type** | **str** | sender_type string | 
**text** | **str** | text string | [optional] 
**timestamp** | **datetime** | timestamp string | 
**type** | **str** | type string | 

## Example

```python
from esi_client.models.get_characters_character_id_notifications200_ok import GetCharactersCharacterIdNotifications200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdNotifications200Ok from a JSON string
get_characters_character_id_notifications200_ok_instance = GetCharactersCharacterIdNotifications200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdNotifications200Ok.to_json()

# convert the object into a dict
get_characters_character_id_notifications200_ok_dict = get_characters_character_id_notifications200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdNotifications200Ok from a dict
get_characters_character_id_notifications200_ok_form_dict = get_characters_character_id_notifications200_ok.from_dict(get_characters_character_id_notifications200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


