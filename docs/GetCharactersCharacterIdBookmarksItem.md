# GetCharactersCharacterIdBookmarksItem

Optional object that is returned if a bookmark was made on a particular item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | item_id integer | 
**type_id** | **int** | type_id integer | 

## Example

```python
from esi_client.models.get_characters_character_id_bookmarks_item import GetCharactersCharacterIdBookmarksItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdBookmarksItem from a JSON string
get_characters_character_id_bookmarks_item_instance = GetCharactersCharacterIdBookmarksItem.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdBookmarksItem.to_json()

# convert the object into a dict
get_characters_character_id_bookmarks_item_dict = get_characters_character_id_bookmarks_item_instance.to_dict()
# create an instance of GetCharactersCharacterIdBookmarksItem from a dict
get_characters_character_id_bookmarks_item_form_dict = get_characters_character_id_bookmarks_item.from_dict(get_characters_character_id_bookmarks_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


