# GetCharactersCharacterIdContractsContractIdItems200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_included** | **bool** | true if the contract issuer has submitted this item with the contract, false if the isser is asking for this item in the contract | 
**is_singleton** | **bool** | is_singleton boolean | 
**quantity** | **int** | Number of items in the stack | 
**raw_quantity** | **int** | -1 indicates that the item is a singleton (non-stackable). If the item happens to be a Blueprint, -1 is an Original and -2 is a Blueprint Copy | [optional] 
**record_id** | **int** | Unique ID for the item | 
**type_id** | **int** | Type ID for item | 

## Example

```python
from esi_client.models.get_characters_character_id_contracts_contract_id_items200_ok import GetCharactersCharacterIdContractsContractIdItems200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdContractsContractIdItems200Ok from a JSON string
get_characters_character_id_contracts_contract_id_items200_ok_instance = GetCharactersCharacterIdContractsContractIdItems200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdContractsContractIdItems200Ok.to_json()

# convert the object into a dict
get_characters_character_id_contracts_contract_id_items200_ok_dict = get_characters_character_id_contracts_contract_id_items200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdContractsContractIdItems200Ok from a dict
get_characters_character_id_contracts_contract_id_items200_ok_form_dict = get_characters_character_id_contracts_contract_id_items200_ok.from_dict(get_characters_character_id_contracts_contract_id_items200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


