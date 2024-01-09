# GetCharactersCharacterIdCalendar200Ok

event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_date** | **datetime** | event_date string | [optional] 
**event_id** | **int** | event_id integer | [optional] 
**event_response** | **str** | event_response string | [optional] 
**importance** | **int** | importance integer | [optional] 
**title** | **str** | title string | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_calendar200_ok import GetCharactersCharacterIdCalendar200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdCalendar200Ok from a JSON string
get_characters_character_id_calendar200_ok_instance = GetCharactersCharacterIdCalendar200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdCalendar200Ok.to_json()

# convert the object into a dict
get_characters_character_id_calendar200_ok_dict = get_characters_character_id_calendar200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdCalendar200Ok from a dict
get_characters_character_id_calendar200_ok_form_dict = get_characters_character_id_calendar200_ok.from_dict(get_characters_character_id_calendar200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


