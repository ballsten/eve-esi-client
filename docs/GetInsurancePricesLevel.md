# GetInsurancePricesLevel

level object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** | cost number | 
**name** | **str** | Localized insurance level | 
**payout** | **float** | payout number | 

## Example

```python
from esi_client.models.get_insurance_prices_level import GetInsurancePricesLevel

# TODO update the JSON string below
json = "{}"
# create an instance of GetInsurancePricesLevel from a JSON string
get_insurance_prices_level_instance = GetInsurancePricesLevel.from_json(json)
# print the JSON string representation of the object
print GetInsurancePricesLevel.to_json()

# convert the object into a dict
get_insurance_prices_level_dict = get_insurance_prices_level_instance.to_dict()
# create an instance of GetInsurancePricesLevel from a dict
get_insurance_prices_level_form_dict = get_insurance_prices_level.from_dict(get_insurance_prices_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


