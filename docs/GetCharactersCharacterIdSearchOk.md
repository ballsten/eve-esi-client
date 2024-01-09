# GetCharactersCharacterIdSearchOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | **List[int]** | agent array | [optional] 
**alliance** | **List[int]** | alliance array | [optional] 
**character** | **List[int]** | character array | [optional] 
**constellation** | **List[int]** | constellation array | [optional] 
**corporation** | **List[int]** | corporation array | [optional] 
**faction** | **List[int]** | faction array | [optional] 
**inventory_type** | **List[int]** | inventory_type array | [optional] 
**region** | **List[int]** | region array | [optional] 
**solar_system** | **List[int]** | solar_system array | [optional] 
**station** | **List[int]** | station array | [optional] 
**structure** | **List[int]** | structure array | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_search_ok import GetCharactersCharacterIdSearchOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdSearchOk from a JSON string
get_characters_character_id_search_ok_instance = GetCharactersCharacterIdSearchOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdSearchOk.to_json()

# convert the object into a dict
get_characters_character_id_search_ok_dict = get_characters_character_id_search_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdSearchOk from a dict
get_characters_character_id_search_ok_form_dict = get_characters_character_id_search_ok.from_dict(get_characters_character_id_search_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


