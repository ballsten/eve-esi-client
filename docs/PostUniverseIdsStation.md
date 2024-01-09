# PostUniverseIdsStation

station object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id integer | [optional] 
**name** | **str** | name string | [optional] 

## Example

```python
from esi_client.models.post_universe_ids_station import PostUniverseIdsStation

# TODO update the JSON string below
json = "{}"
# create an instance of PostUniverseIdsStation from a JSON string
post_universe_ids_station_instance = PostUniverseIdsStation.from_json(json)
# print the JSON string representation of the object
print PostUniverseIdsStation.to_json()

# convert the object into a dict
post_universe_ids_station_dict = post_universe_ids_station_instance.to_dict()
# create an instance of PostUniverseIdsStation from a dict
post_universe_ids_station_form_dict = post_universe_ids_station.from_dict(post_universe_ids_station_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


