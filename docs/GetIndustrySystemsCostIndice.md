# GetIndustrySystemsCostIndice

cost_indice object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | **str** | activity string | 
**cost_index** | **float** | cost_index number | 

## Example

```python
from esi_client.models.get_industry_systems_cost_indice import GetIndustrySystemsCostIndice

# TODO update the JSON string below
json = "{}"
# create an instance of GetIndustrySystemsCostIndice from a JSON string
get_industry_systems_cost_indice_instance = GetIndustrySystemsCostIndice.from_json(json)
# print the JSON string representation of the object
print GetIndustrySystemsCostIndice.to_json()

# convert the object into a dict
get_industry_systems_cost_indice_dict = get_industry_systems_cost_indice_instance.to_dict()
# create an instance of GetIndustrySystemsCostIndice from a dict
get_industry_systems_cost_indice_form_dict = get_industry_systems_cost_indice.from_dict(get_industry_systems_cost_indice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


