# GetMarketsPrices200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_price** | **float** | adjusted_price number | [optional] 
**average_price** | **float** | average_price number | [optional] 
**type_id** | **int** | type_id integer | 

## Example

```python
from esi_client.models.get_markets_prices200_ok import GetMarketsPrices200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarketsPrices200Ok from a JSON string
get_markets_prices200_ok_instance = GetMarketsPrices200Ok.from_json(json)
# print the JSON string representation of the object
print GetMarketsPrices200Ok.to_json()

# convert the object into a dict
get_markets_prices200_ok_dict = get_markets_prices200_ok_instance.to_dict()
# create an instance of GetMarketsPrices200Ok from a dict
get_markets_prices200_ok_form_dict = get_markets_prices200_ok.from_dict(get_markets_prices200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


