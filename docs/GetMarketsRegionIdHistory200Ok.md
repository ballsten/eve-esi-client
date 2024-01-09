# GetMarketsRegionIdHistory200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average** | **float** | average number | 
**var_date** | **date** | The date of this historical statistic entry | 
**highest** | **float** | highest number | 
**lowest** | **float** | lowest number | 
**order_count** | **int** | Total number of orders happened that day | 
**volume** | **int** | Total | 

## Example

```python
from esi_client.models.get_markets_region_id_history200_ok import GetMarketsRegionIdHistory200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarketsRegionIdHistory200Ok from a JSON string
get_markets_region_id_history200_ok_instance = GetMarketsRegionIdHistory200Ok.from_json(json)
# print the JSON string representation of the object
print GetMarketsRegionIdHistory200Ok.to_json()

# convert the object into a dict
get_markets_region_id_history200_ok_dict = get_markets_region_id_history200_ok_instance.to_dict()
# create an instance of GetMarketsRegionIdHistory200Ok from a dict
get_markets_region_id_history200_ok_form_dict = get_markets_region_id_history200_ok.from_dict(get_markets_region_id_history200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


