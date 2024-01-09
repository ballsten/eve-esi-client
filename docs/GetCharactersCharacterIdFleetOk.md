# GetCharactersCharacterIdFleetOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleet_id** | **int** | The character&#39;s current fleet ID | 
**role** | **str** | Member’s role in fleet | 
**squad_id** | **int** | ID of the squad the member is in. If not applicable, will be set to -1 | 
**wing_id** | **int** | ID of the wing the member is in. If not applicable, will be set to -1 | 

## Example

```python
from esi_client.models.get_characters_character_id_fleet_ok import GetCharactersCharacterIdFleetOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdFleetOk from a JSON string
get_characters_character_id_fleet_ok_instance = GetCharactersCharacterIdFleetOk.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdFleetOk.to_json()

# convert the object into a dict
get_characters_character_id_fleet_ok_dict = get_characters_character_id_fleet_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdFleetOk from a dict
get_characters_character_id_fleet_ok_form_dict = get_characters_character_id_fleet_ok.from_dict(get_characters_character_id_fleet_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


