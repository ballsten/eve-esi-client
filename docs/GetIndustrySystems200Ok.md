# GetIndustrySystems200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_indices** | [**List[GetIndustrySystemsCostIndice]**](GetIndustrySystemsCostIndice.md) | cost_indices array | 
**solar_system_id** | **int** | solar_system_id integer | 

## Example

```python
from esi_client.models.get_industry_systems200_ok import GetIndustrySystems200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetIndustrySystems200Ok from a JSON string
get_industry_systems200_ok_instance = GetIndustrySystems200Ok.from_json(json)
# print the JSON string representation of the object
print GetIndustrySystems200Ok.to_json()

# convert the object into a dict
get_industry_systems200_ok_dict = get_industry_systems200_ok_instance.to_dict()
# create an instance of GetIndustrySystems200Ok from a dict
get_industry_systems200_ok_form_dict = get_industry_systems200_ok.from_dict(get_industry_systems200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


