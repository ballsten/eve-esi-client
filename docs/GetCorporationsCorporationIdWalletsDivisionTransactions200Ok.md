# GetCorporationsCorporationIdWalletsDivisionTransactions200Ok

wallet transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** | client_id integer | 
**var_date** | **datetime** | Date and time of transaction | 
**is_buy** | **bool** | is_buy boolean | 
**journal_ref_id** | **int** | -1 if there is no corresponding wallet journal entry | 
**location_id** | **int** | location_id integer | 
**quantity** | **int** | quantity integer | 
**transaction_id** | **int** | Unique transaction ID | 
**type_id** | **int** | type_id integer | 
**unit_price** | **float** | Amount paid per unit | 

## Example

```python
from esi_client.models.get_corporations_corporation_id_wallets_division_transactions200_ok import GetCorporationsCorporationIdWalletsDivisionTransactions200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdWalletsDivisionTransactions200Ok from a JSON string
get_corporations_corporation_id_wallets_division_transactions200_ok_instance = GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_wallets_division_transactions200_ok_dict = get_corporations_corporation_id_wallets_division_transactions200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdWalletsDivisionTransactions200Ok from a dict
get_corporations_corporation_id_wallets_division_transactions200_ok_form_dict = get_corporations_corporation_id_wallets_division_transactions200_ok.from_dict(get_corporations_corporation_id_wallets_division_transactions200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


