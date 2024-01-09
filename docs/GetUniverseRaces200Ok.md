# GetUniverseRaces200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alliance_id** | **int** | The alliance generally associated with this race | 
**description** | **str** | description string | 
**name** | **str** | name string | 
**race_id** | **int** | race_id integer | 

## Example

```python
from esi_client.models.get_universe_races200_ok import GetUniverseRaces200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseRaces200Ok from a JSON string
get_universe_races200_ok_instance = GetUniverseRaces200Ok.from_json(json)
# print the JSON string representation of the object
print GetUniverseRaces200Ok.to_json()

# convert the object into a dict
get_universe_races200_ok_dict = get_universe_races200_ok_instance.to_dict()
# create an instance of GetUniverseRaces200Ok from a dict
get_universe_races200_ok_form_dict = get_universe_races200_ok.from_dict(get_universe_races200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


