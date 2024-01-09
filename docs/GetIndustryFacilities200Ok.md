# GetIndustryFacilities200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_id** | **int** | ID of the facility | 
**owner_id** | **int** | Owner of the facility | 
**region_id** | **int** | Region ID where the facility is | 
**solar_system_id** | **int** | Solar system ID where the facility is | 
**tax** | **float** | Tax imposed by the facility | [optional] 
**type_id** | **int** | Type ID of the facility | 

## Example

```python
from esi_client.models.get_industry_facilities200_ok import GetIndustryFacilities200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetIndustryFacilities200Ok from a JSON string
get_industry_facilities200_ok_instance = GetIndustryFacilities200Ok.from_json(json)
# print the JSON string representation of the object
print GetIndustryFacilities200Ok.to_json()

# convert the object into a dict
get_industry_facilities200_ok_dict = get_industry_facilities200_ok_instance.to_dict()
# create an instance of GetIndustryFacilities200Ok from a dict
get_industry_facilities200_ok_form_dict = get_industry_facilities200_ok.from_dict(get_industry_facilities200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


