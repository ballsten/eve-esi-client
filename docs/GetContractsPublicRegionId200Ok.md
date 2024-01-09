# GetContractsPublicRegionId200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyout** | **float** | Buyout price (for Auctions only) | [optional] 
**collateral** | **float** | Collateral price (for Couriers only) | [optional] 
**contract_id** | **int** | contract_id integer | 
**date_expired** | **datetime** | Expiration date of the contract | 
**date_issued** | **datetime** | Сreation date of the contract | 
**days_to_complete** | **int** | Number of days to perform the contract | [optional] 
**end_location_id** | **int** | End location ID (for Couriers contract) | [optional] 
**for_corporation** | **bool** | true if the contract was issued on behalf of the issuer&#39;s corporation | [optional] 
**issuer_corporation_id** | **int** | Character&#39;s corporation ID for the issuer | 
**issuer_id** | **int** | Character ID for the issuer | 
**price** | **float** | Price of contract (for ItemsExchange and Auctions) | [optional] 
**reward** | **float** | Remuneration for contract (for Couriers only) | [optional] 
**start_location_id** | **int** | Start location ID (for Couriers contract) | [optional] 
**title** | **str** | Title of the contract | [optional] 
**type** | **str** | Type of the contract | 
**volume** | **float** | Volume of items in the contract | [optional] 

## Example

```python
from esi_client.models.get_contracts_public_region_id200_ok import GetContractsPublicRegionId200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetContractsPublicRegionId200Ok from a JSON string
get_contracts_public_region_id200_ok_instance = GetContractsPublicRegionId200Ok.from_json(json)
# print the JSON string representation of the object
print GetContractsPublicRegionId200Ok.to_json()

# convert the object into a dict
get_contracts_public_region_id200_ok_dict = get_contracts_public_region_id200_ok_instance.to_dict()
# create an instance of GetContractsPublicRegionId200Ok from a dict
get_contracts_public_region_id200_ok_form_dict = get_contracts_public_region_id200_ok.from_dict(get_contracts_public_region_id200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


