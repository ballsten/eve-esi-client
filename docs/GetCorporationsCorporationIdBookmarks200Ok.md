# GetCorporationsCorporationIdBookmarks200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmark_id** | **int** | bookmark_id integer | 
**coordinates** | [**GetCorporationsCorporationIdBookmarksCoordinates**](GetCorporationsCorporationIdBookmarksCoordinates.md) |  | [optional] 
**created** | **datetime** | created string | 
**creator_id** | **int** | creator_id integer | 
**folder_id** | **int** | folder_id integer | [optional] 
**item** | [**GetCorporationsCorporationIdBookmarksItem**](GetCorporationsCorporationIdBookmarksItem.md) |  | [optional] 
**label** | **str** | label string | 
**location_id** | **int** | location_id integer | 
**notes** | **str** | notes string | 

## Example

```python
from esi_client.models.get_corporations_corporation_id_bookmarks200_ok import GetCorporationsCorporationIdBookmarks200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdBookmarks200Ok from a JSON string
get_corporations_corporation_id_bookmarks200_ok_instance = GetCorporationsCorporationIdBookmarks200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdBookmarks200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_bookmarks200_ok_dict = get_corporations_corporation_id_bookmarks200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdBookmarks200Ok from a dict
get_corporations_corporation_id_bookmarks200_ok_form_dict = get_corporations_corporation_id_bookmarks200_ok.from_dict(get_corporations_corporation_id_bookmarks200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


