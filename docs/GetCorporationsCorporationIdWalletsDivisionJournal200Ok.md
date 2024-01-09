# GetCorporationsCorporationIdWalletsDivisionJournal200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of ISK given or taken from the wallet as a result of the given transaction. Positive when ISK is deposited into the wallet and negative when ISK is withdrawn | [optional] 
**balance** | **float** | Wallet balance after transaction occurred | [optional] 
**context_id** | **int** | An ID that gives extra context to the particular transaction. Because of legacy reasons the context is completely different per ref_type and means different things. It is also possible to not have a context_id | [optional] 
**context_id_type** | **str** | The type of the given context_id if present | [optional] 
**var_date** | **datetime** | Date and time of transaction | 
**description** | **str** | The reason for the transaction, mirrors what is seen in the client | 
**first_party_id** | **int** | The id of the first party involved in the transaction. This attribute has no consistency and is different or non existant for particular ref_types. The description attribute will help make sense of what this attribute means. For more info about the given ID it can be dropped into the /universe/names/ ESI route to determine its type and name | [optional] 
**id** | **int** | Unique journal reference ID | 
**reason** | **str** | The user stated reason for the transaction. Only applies to some ref_types | [optional] 
**ref_type** | **str** | \&quot;The transaction type for the given. transaction. Different transaction types will populate different attributes. Note: If you have an existing XML API application that is using ref_types, you will need to know which string ESI ref_type maps to which integer. You can look at the following file to see string-&gt;int mappings: https://github.com/ccpgames/eve-glue/blob/master/eve_glue/wallet_journal_ref.py\&quot; | 
**second_party_id** | **int** | The id of the second party involved in the transaction. This attribute has no consistency and is different or non existant for particular ref_types. The description attribute will help make sense of what this attribute means. For more info about the given ID it can be dropped into the /universe/names/ ESI route to determine its type and name | [optional] 
**tax** | **float** | Tax amount received. Only applies to tax related transactions | [optional] 
**tax_receiver_id** | **int** | The corporation ID receiving any tax paid. Only applies to tax related transactions | [optional] 

## Example

```python
from esi_client.models.get_corporations_corporation_id_wallets_division_journal200_ok import GetCorporationsCorporationIdWalletsDivisionJournal200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdWalletsDivisionJournal200Ok from a JSON string
get_corporations_corporation_id_wallets_division_journal200_ok_instance = GetCorporationsCorporationIdWalletsDivisionJournal200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdWalletsDivisionJournal200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_wallets_division_journal200_ok_dict = get_corporations_corporation_id_wallets_division_journal200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdWalletsDivisionJournal200Ok from a dict
get_corporations_corporation_id_wallets_division_journal200_ok_form_dict = get_corporations_corporation_id_wallets_division_journal200_ok.from_dict(get_corporations_corporation_id_wallets_division_journal200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


