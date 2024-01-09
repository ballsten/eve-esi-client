# GetLoyaltyStoresCorporationIdOffers200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ak_cost** | **int** | Analysis kredit cost | [optional] 
**isk_cost** | **int** | isk_cost integer | 
**lp_cost** | **int** | lp_cost integer | 
**offer_id** | **int** | offer_id integer | 
**quantity** | **int** | quantity integer | 
**required_items** | [**List[GetLoyaltyStoresCorporationIdOffersRequiredItem]**](GetLoyaltyStoresCorporationIdOffersRequiredItem.md) | required_items array | 
**type_id** | **int** | type_id integer | 

## Example

```python
from esi_client.models.get_loyalty_stores_corporation_id_offers200_ok import GetLoyaltyStoresCorporationIdOffers200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoyaltyStoresCorporationIdOffers200Ok from a JSON string
get_loyalty_stores_corporation_id_offers200_ok_instance = GetLoyaltyStoresCorporationIdOffers200Ok.from_json(json)
# print the JSON string representation of the object
print GetLoyaltyStoresCorporationIdOffers200Ok.to_json()

# convert the object into a dict
get_loyalty_stores_corporation_id_offers200_ok_dict = get_loyalty_stores_corporation_id_offers200_ok_instance.to_dict()
# create an instance of GetLoyaltyStoresCorporationIdOffers200Ok from a dict
get_loyalty_stores_corporation_id_offers200_ok_form_dict = get_loyalty_stores_corporation_id_offers200_ok.from_dict(get_loyalty_stores_corporation_id_offers200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


