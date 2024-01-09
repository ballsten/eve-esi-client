# GetContractsPublicItemsContractId200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_blueprint_copy** | **bool** | is_blueprint_copy boolean | [optional] 
**is_included** | **bool** | true if the contract issuer has submitted this item with the contract, false if the isser is asking for this item in the contract | 
**item_id** | **int** | Unique ID for the item being sold. Not present if item is being requested by contract rather than sold with contract | [optional] 
**material_efficiency** | **int** | Material Efficiency Level of the blueprint | [optional] 
**quantity** | **int** | Number of items in the stack | 
**record_id** | **int** | Unique ID for the item, used by the contract system | 
**runs** | **int** | Number of runs remaining if the blueprint is a copy, -1 if it is an original | [optional] 
**time_efficiency** | **int** | Time Efficiency Level of the blueprint | [optional] 
**type_id** | **int** | Type ID for item | 

## Example

```python
from esi_client.models.get_contracts_public_items_contract_id200_ok import GetContractsPublicItemsContractId200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetContractsPublicItemsContractId200Ok from a JSON string
get_contracts_public_items_contract_id200_ok_instance = GetContractsPublicItemsContractId200Ok.from_json(json)
# print the JSON string representation of the object
print GetContractsPublicItemsContractId200Ok.to_json()

# convert the object into a dict
get_contracts_public_items_contract_id200_ok_dict = get_contracts_public_items_contract_id200_ok_instance.to_dict()
# create an instance of GetContractsPublicItemsContractId200Ok from a dict
get_contracts_public_items_contract_id200_ok_form_dict = get_contracts_public_items_contract_id200_ok.from_dict(get_contracts_public_items_contract_id200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


