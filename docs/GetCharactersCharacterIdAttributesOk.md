# GetCharactersCharacterIdAttributesOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrued_remap_cooldown_date** | **datetime** | Neural remapping cooldown after a character uses remap accrued over time | [optional] 
**bonus_remaps** | **int** | Number of available bonus character neural remaps | [optional] 
**charisma** | **int** | charisma integer | 
**intelligence** | **int** | intelligence integer | 
**last_remap_date** | **datetime** | Datetime of last neural remap, including usage of bonus remaps | [optional] 
**memory** | **int** | memory integer | 
**perception** | **int** | perception integer | 
**willpower** | **int** | willpower integer | 

## Example

```python
from esi_client.models.get_characters_character_id_attributes_ok import GetCharactersCharacterIdAttributesOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdAttributesOk from a JSON string
get_characters_character_id_attributes_ok_instance = GetCharactersCharacterIdAttributesOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdAttributesOk.to_json()

# convert the object into a dict
get_characters_character_id_attributes_ok_dict = get_characters_character_id_attributes_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdAttributesOk from a dict
get_characters_character_id_attributes_ok_form_dict = get_characters_character_id_attributes_ok.from_dict(get_characters_character_id_attributes_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


