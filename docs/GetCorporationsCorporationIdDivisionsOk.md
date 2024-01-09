# GetCorporationsCorporationIdDivisionsOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hangar** | [**List[GetCorporationsCorporationIdDivisionsHangarHangar]**](GetCorporationsCorporationIdDivisionsHangarHangar.md) | hangar array | [optional] 
**wallet** | [**List[GetCorporationsCorporationIdDivisionsWalletWallet]**](GetCorporationsCorporationIdDivisionsWalletWallet.md) | wallet array | [optional] 

## Example

```python
from esi_client.models.get_corporations_corporation_id_divisions_ok import GetCorporationsCorporationIdDivisionsOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdDivisionsOk from a JSON string
get_corporations_corporation_id_divisions_ok_instance = GetCorporationsCorporationIdDivisionsOk.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdDivisionsOk.to_json()

# convert the object into a dict
get_corporations_corporation_id_divisions_ok_dict = get_corporations_corporation_id_divisions_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdDivisionsOk from a dict
get_corporations_corporation_id_divisions_ok_form_dict = get_corporations_corporation_id_divisions_ok.from_dict(get_corporations_corporation_id_divisions_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


