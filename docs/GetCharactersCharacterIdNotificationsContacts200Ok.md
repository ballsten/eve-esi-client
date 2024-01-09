# GetCharactersCharacterIdNotificationsContacts200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | message string | 
**notification_id** | **int** | notification_id integer | 
**send_date** | **datetime** | send_date string | 
**sender_character_id** | **int** | sender_character_id integer | 
**standing_level** | **float** | A number representing the standing level the receiver has been added at by the sender. The standing levels are as follows: -10 -&gt; Terrible | -5 -&gt; Bad |  0 -&gt; Neutral |  5 -&gt; Good |  10 -&gt; Excellent | 

## Example

```python
from esi_client.models.get_characters_character_id_notifications_contacts200_ok import GetCharactersCharacterIdNotificationsContacts200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdNotificationsContacts200Ok from a JSON string
get_characters_character_id_notifications_contacts200_ok_instance = GetCharactersCharacterIdNotificationsContacts200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdNotificationsContacts200Ok.to_json()

# convert the object into a dict
get_characters_character_id_notifications_contacts200_ok_dict = get_characters_character_id_notifications_contacts200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdNotificationsContacts200Ok from a dict
get_characters_character_id_notifications_contacts200_ok_form_dict = get_characters_character_id_notifications_contacts200_ok.from_dict(get_characters_character_id_notifications_contacts200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


