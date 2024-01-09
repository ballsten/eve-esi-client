# GetUniverseFactions200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporation_id** | **int** | corporation_id integer | [optional] 
**description** | **str** | description string | 
**faction_id** | **int** | faction_id integer | 
**is_unique** | **bool** | is_unique boolean | 
**militia_corporation_id** | **int** | militia_corporation_id integer | [optional] 
**name** | **str** | name string | 
**size_factor** | **float** | size_factor number | 
**solar_system_id** | **int** | solar_system_id integer | [optional] 
**station_count** | **int** | station_count integer | 
**station_system_count** | **int** | station_system_count integer | 

## Example

```python
from esi_client.models.get_universe_factions200_ok import GetUniverseFactions200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseFactions200Ok from a JSON string
get_universe_factions200_ok_instance = GetUniverseFactions200Ok.from_json(json)
# print the JSON string representation of the object
print GetUniverseFactions200Ok.to_json()

# convert the object into a dict
get_universe_factions200_ok_dict = get_universe_factions200_ok_instance.to_dict()
# create an instance of GetUniverseFactions200Ok from a dict
get_universe_factions200_ok_form_dict = get_universe_factions200_ok.from_dict(get_universe_factions200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


