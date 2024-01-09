# GetCharactersCharacterIdBlueprints200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | Unique ID for this item. | 
**location_flag** | **str** | Type of the location_id | 
**location_id** | **int** | References a station, a ship or an item_id if this blueprint is located within a container. If the return value is an item_id, then the Character AssetList API must be queried to find the container using the given item_id to determine the correct location of the Blueprint. | 
**material_efficiency** | **int** | Material Efficiency Level of the blueprint. | 
**quantity** | **int** | A range of numbers with a minimum of -2 and no maximum value where -1 is an original and -2 is a copy. It can be a positive integer if it is a stack of blueprint originals fresh from the market (e.g. no activities performed on them yet). | 
**runs** | **int** | Number of runs remaining if the blueprint is a copy, -1 if it is an original. | 
**time_efficiency** | **int** | Time Efficiency Level of the blueprint. | 
**type_id** | **int** | type_id integer | 

## Example

```python
from esi_client.models.get_characters_character_id_blueprints200_ok import GetCharactersCharacterIdBlueprints200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdBlueprints200Ok from a JSON string
get_characters_character_id_blueprints200_ok_instance = GetCharactersCharacterIdBlueprints200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdBlueprints200Ok.to_json()

# convert the object into a dict
get_characters_character_id_blueprints200_ok_dict = get_characters_character_id_blueprints200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdBlueprints200Ok from a dict
get_characters_character_id_blueprints200_ok_form_dict = get_characters_character_id_blueprints200_ok.from_dict(get_characters_character_id_blueprints200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


