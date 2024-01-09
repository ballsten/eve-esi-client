# GetCharactersCharacterIdContractsContractIdBids200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount bid, in ISK | 
**bid_id** | **int** | Unique ID for the bid | 
**bidder_id** | **int** | Character ID of the bidder | 
**date_bid** | **datetime** | Datetime when the bid was placed | 

## Example

```python
from esi_client.models.get_characters_character_id_contracts_contract_id_bids200_ok import GetCharactersCharacterIdContractsContractIdBids200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdContractsContractIdBids200Ok from a JSON string
get_characters_character_id_contracts_contract_id_bids200_ok_instance = GetCharactersCharacterIdContractsContractIdBids200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdContractsContractIdBids200Ok.to_json()

# convert the object into a dict
get_characters_character_id_contracts_contract_id_bids200_ok_dict = get_characters_character_id_contracts_contract_id_bids200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdContractsContractIdBids200Ok from a dict
get_characters_character_id_contracts_contract_id_bids200_ok_form_dict = get_characters_character_id_contracts_contract_id_bids200_ok.from_dict(get_characters_character_id_contracts_contract_id_bids200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


