# GetCharactersCharacterIdClonesHomeLocation

home_location object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **int** | location_id integer | [optional] 
**location_type** | **str** | location_type string | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_clones_home_location import GetCharactersCharacterIdClonesHomeLocation

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdClonesHomeLocation from a JSON string
get_characters_character_id_clones_home_location_instance = GetCharactersCharacterIdClonesHomeLocation.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdClonesHomeLocation.to_json()

# convert the object into a dict
get_characters_character_id_clones_home_location_dict = get_characters_character_id_clones_home_location_instance.to_dict()
# create an instance of GetCharactersCharacterIdClonesHomeLocation from a dict
get_characters_character_id_clones_home_location_form_dict = get_characters_character_id_clones_home_location.from_dict(get_characters_character_id_clones_home_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


