# GetCharactersCharacterIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alliance_id** | **int** | The character&#39;s alliance ID | [optional] 
**birthday** | **datetime** | Creation date of the character | 
**bloodline_id** | **int** | bloodline_id integer | 
**corporation_id** | **int** | The character&#39;s corporation ID | 
**description** | **str** | description string | [optional] 
**faction_id** | **int** | ID of the faction the character is fighting for, if the character is enlisted in Factional Warfare | [optional] 
**gender** | **str** | gender string | 
**name** | **str** | name string | 
**race_id** | **int** | race_id integer | 
**security_status** | **float** | security_status number | [optional] 
**title** | **str** | The individual title of the character | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_ok import GetCharactersCharacterIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdOk from a JSON string
get_characters_character_id_ok_instance = GetCharactersCharacterIdOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdOk.to_json()

# convert the object into a dict
get_characters_character_id_ok_dict = get_characters_character_id_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdOk from a dict
get_characters_character_id_ok_form_dict = get_characters_character_id_ok.from_dict(get_characters_character_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


