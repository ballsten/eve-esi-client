# GetCharactersCharacterIdOnlineOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_login** | **datetime** | Timestamp of the last login | [optional] 
**last_logout** | **datetime** | Timestamp of the last logout | [optional] 
**logins** | **int** | Total number of times the character has logged in | [optional] 
**online** | **bool** | If the character is online | 

## Example

```python
from esi_client.models.get_characters_character_id_online_ok import GetCharactersCharacterIdOnlineOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdOnlineOk from a JSON string
get_characters_character_id_online_ok_instance = GetCharactersCharacterIdOnlineOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdOnlineOk.to_json()

# convert the object into a dict
get_characters_character_id_online_ok_dict = get_characters_character_id_online_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdOnlineOk from a dict
get_characters_character_id_online_ok_form_dict = get_characters_character_id_online_ok.from_dict(get_characters_character_id_online_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


