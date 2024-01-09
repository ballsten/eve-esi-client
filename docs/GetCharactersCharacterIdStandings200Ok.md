# GetCharactersCharacterIdStandings200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_id** | **int** | from_id integer | 
**from_type** | **str** | from_type string | 
**standing** | **float** | standing number | 

## Example

```python
from esi_client.models.get_characters_character_id_standings200_ok import GetCharactersCharacterIdStandings200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdStandings200Ok from a JSON string
get_characters_character_id_standings200_ok_instance = GetCharactersCharacterIdStandings200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdStandings200Ok.to_json()

# convert the object into a dict
get_characters_character_id_standings200_ok_dict = get_characters_character_id_standings200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdStandings200Ok from a dict
get_characters_character_id_standings200_ok_form_dict = get_characters_character_id_standings200_ok.from_dict(get_characters_character_id_standings200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


