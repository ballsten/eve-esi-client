# GetIncursions200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constellation_id** | **int** | The constellation id in which this incursion takes place | 
**faction_id** | **int** | The attacking faction&#39;s id | 
**has_boss** | **bool** | Whether the final encounter has boss or not | 
**infested_solar_systems** | **List[int]** | A list of infested solar system ids that are a part of this incursion | 
**influence** | **float** | Influence of this incursion as a float from 0 to 1 | 
**staging_solar_system_id** | **int** | Staging solar system for this incursion | 
**state** | **str** | The state of this incursion | 
**type** | **str** | The type of this incursion | 

## Example

```python
from esi_client.models.get_incursions200_ok import GetIncursions200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetIncursions200Ok from a JSON string
get_incursions200_ok_instance = GetIncursions200Ok.from_json(json)
# print the JSON string representation of the object
print GetIncursions200Ok.to_json()

# convert the object into a dict
get_incursions200_ok_dict = get_incursions200_ok_instance.to_dict()
# create an instance of GetIncursions200Ok from a dict
get_incursions200_ok_form_dict = get_incursions200_ok.from_dict(get_incursions200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


