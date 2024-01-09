# GetCharactersCharacterIdCalendarEventIdOk

Full details of a specific event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | date string | 
**duration** | **int** | Length in minutes | 
**event_id** | **int** | event_id integer | 
**importance** | **int** | importance integer | 
**owner_id** | **int** | owner_id integer | 
**owner_name** | **str** | owner_name string | 
**owner_type** | **str** | owner_type string | 
**response** | **str** | response string | 
**text** | **str** | text string | 
**title** | **str** | title string | 

## Example

```python
from esi_client.models.get_characters_character_id_calendar_event_id_ok import GetCharactersCharacterIdCalendarEventIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdCalendarEventIdOk from a JSON string
get_characters_character_id_calendar_event_id_ok_instance = GetCharactersCharacterIdCalendarEventIdOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdCalendarEventIdOk.to_json()

# convert the object into a dict
get_characters_character_id_calendar_event_id_ok_dict = get_characters_character_id_calendar_event_id_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdCalendarEventIdOk from a dict
get_characters_character_id_calendar_event_id_ok_form_dict = get_characters_character_id_calendar_event_id_ok.from_dict(get_characters_character_id_calendar_event_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


