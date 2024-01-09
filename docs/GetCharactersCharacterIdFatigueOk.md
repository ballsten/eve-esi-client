# GetCharactersCharacterIdFatigueOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jump_fatigue_expire_date** | **datetime** | Character&#39;s jump fatigue expiry | [optional] 
**last_jump_date** | **datetime** | Character&#39;s last jump activation | [optional] 
**last_update_date** | **datetime** | Character&#39;s last jump update | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_fatigue_ok import GetCharactersCharacterIdFatigueOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdFatigueOk from a JSON string
get_characters_character_id_fatigue_ok_instance = GetCharactersCharacterIdFatigueOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdFatigueOk.to_json()

# convert the object into a dict
get_characters_character_id_fatigue_ok_dict = get_characters_character_id_fatigue_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdFatigueOk from a dict
get_characters_character_id_fatigue_ok_form_dict = get_characters_character_id_fatigue_ok.from_dict(get_characters_character_id_fatigue_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


