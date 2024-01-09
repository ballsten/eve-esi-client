# GetSovereigntyMap200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alliance_id** | **int** | alliance_id integer | [optional] 
**corporation_id** | **int** | corporation_id integer | [optional] 
**faction_id** | **int** | faction_id integer | [optional] 
**system_id** | **int** | system_id integer | 

## Example

```python
from esi_client.models.get_sovereignty_map200_ok import GetSovereigntyMap200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetSovereigntyMap200Ok from a JSON string
get_sovereignty_map200_ok_instance = GetSovereigntyMap200Ok.from_json(json)
# print the JSON string representation of the object
print GetSovereigntyMap200Ok.to_json()

# convert the object into a dict
get_sovereignty_map200_ok_dict = get_sovereignty_map200_ok_instance.to_dict()
# create an instance of GetSovereigntyMap200Ok from a dict
get_sovereignty_map200_ok_form_dict = get_sovereignty_map200_ok.from_dict(get_sovereignty_map200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


