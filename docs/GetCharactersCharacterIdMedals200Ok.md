# GetCharactersCharacterIdMedals200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporation_id** | **int** | corporation_id integer | 
**var_date** | **datetime** | date string | 
**description** | **str** | description string | 
**graphics** | [**List[GetCharactersCharacterIdMedalsGraphic]**](GetCharactersCharacterIdMedalsGraphic.md) | graphics array | 
**issuer_id** | **int** | issuer_id integer | 
**medal_id** | **int** | medal_id integer | 
**reason** | **str** | reason string | 
**status** | **str** | status string | 
**title** | **str** | title string | 

## Example

```python
from esi_client.models.get_characters_character_id_medals200_ok import GetCharactersCharacterIdMedals200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdMedals200Ok from a JSON string
get_characters_character_id_medals200_ok_instance = GetCharactersCharacterIdMedals200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdMedals200Ok.to_json()

# convert the object into a dict
get_characters_character_id_medals200_ok_dict = get_characters_character_id_medals200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdMedals200Ok from a dict
get_characters_character_id_medals200_ok_form_dict = get_characters_character_id_medals200_ok.from_dict(get_characters_character_id_medals200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


