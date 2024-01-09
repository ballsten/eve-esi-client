# GetCharactersCharacterIdContracts200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptor_id** | **int** | Who will accept the contract | 
**assignee_id** | **int** | ID to whom the contract is assigned, can be alliance, corporation or character ID | 
**availability** | **str** | To whom the contract is available | 
**buyout** | **float** | Buyout price (for Auctions only) | [optional] 
**collateral** | **float** | Collateral price (for Couriers only) | [optional] 
**contract_id** | **int** | contract_id integer | 
**date_accepted** | **datetime** | Date of confirmation of contract | [optional] 
**date_completed** | **datetime** | Date of completed of contract | [optional] 
**date_expired** | **datetime** | Expiration date of the contract | 
**date_issued** | **datetime** | Сreation date of the contract | 
**days_to_complete** | **int** | Number of days to perform the contract | [optional] 
**end_location_id** | **int** | End location ID (for Couriers contract) | [optional] 
**for_corporation** | **bool** | true if the contract was issued on behalf of the issuer&#39;s corporation | 
**issuer_corporation_id** | **int** | Character&#39;s corporation ID for the issuer | 
**issuer_id** | **int** | Character ID for the issuer | 
**price** | **float** | Price of contract (for ItemsExchange and Auctions) | [optional] 
**reward** | **float** | Remuneration for contract (for Couriers only) | [optional] 
**start_location_id** | **int** | Start location ID (for Couriers contract) | [optional] 
**status** | **str** | Status of the the contract | 
**title** | **str** | Title of the contract | [optional] 
**type** | **str** | Type of the contract | 
**volume** | **float** | Volume of items in the contract | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_contracts200_ok import GetCharactersCharacterIdContracts200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdContracts200Ok from a JSON string
get_characters_character_id_contracts200_ok_instance = GetCharactersCharacterIdContracts200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdContracts200Ok.to_json()

# convert the object into a dict
get_characters_character_id_contracts200_ok_dict = get_characters_character_id_contracts200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdContracts200Ok from a dict
get_characters_character_id_contracts200_ok_form_dict = get_characters_character_id_contracts200_ok.from_dict(get_characters_character_id_contracts200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


