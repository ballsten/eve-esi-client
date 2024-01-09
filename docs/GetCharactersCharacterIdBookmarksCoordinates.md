# GetCharactersCharacterIdBookmarksCoordinates

Optional object that is returned if a bookmark was made on a planet or a random location in space.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** | x number | 
**y** | **float** | y number | 
**z** | **float** | z number | 

## Example

```python
from esi_client.models.get_characters_character_id_bookmarks_coordinates import GetCharactersCharacterIdBookmarksCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdBookmarksCoordinates from a JSON string
get_characters_character_id_bookmarks_coordinates_instance = GetCharactersCharacterIdBookmarksCoordinates.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdBookmarksCoordinates.to_json()

# convert the object into a dict
get_characters_character_id_bookmarks_coordinates_dict = get_characters_character_id_bookmarks_coordinates_instance.to_dict()
# create an instance of GetCharactersCharacterIdBookmarksCoordinates from a dict
get_characters_character_id_bookmarks_coordinates_form_dict = get_characters_character_id_bookmarks_coordinates.from_dict(get_characters_character_id_bookmarks_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


