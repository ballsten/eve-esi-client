# GetUniverseBloodlines200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bloodline_id** | **int** | bloodline_id integer | 
**charisma** | **int** | charisma integer | 
**corporation_id** | **int** | corporation_id integer | 
**description** | **str** | description string | 
**intelligence** | **int** | intelligence integer | 
**memory** | **int** | memory integer | 
**name** | **str** | name string | 
**perception** | **int** | perception integer | 
**race_id** | **int** | race_id integer | 
**ship_type_id** | **int** | ship_type_id integer | 
**willpower** | **int** | willpower integer | 

## Example

```python
from esi_client.models.get_universe_bloodlines200_ok import GetUniverseBloodlines200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseBloodlines200Ok from a JSON string
get_universe_bloodlines200_ok_instance = GetUniverseBloodlines200Ok.from_json(json)
# print the JSON string representation of the object
print GetUniverseBloodlines200Ok.to_json()

# convert the object into a dict
get_universe_bloodlines200_ok_dict = get_universe_bloodlines200_ok_instance.to_dict()
# create an instance of GetUniverseBloodlines200Ok from a dict
get_universe_bloodlines200_ok_form_dict = get_universe_bloodlines200_ok.from_dict(get_universe_bloodlines200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


