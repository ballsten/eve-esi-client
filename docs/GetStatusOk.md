# GetStatusOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**players** | **int** | Current online player count | 
**server_version** | **str** | Running version as string | 
**start_time** | **datetime** | Server start timestamp | 
**vip** | **bool** | If the server is in VIP mode | [optional] 

## Example

```python
from esi_client.models.get_status_ok import GetStatusOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusOk from a JSON string
get_status_ok_instance = GetStatusOk.from_json(json)
# print the JSON string representation of the object
print GetStatusOk.to_json()

# convert the object into a dict
get_status_ok_dict = get_status_ok_instance.to_dict()
# create an instance of GetStatusOk from a dict
get_status_ok_form_dict = get_status_ok.from_dict(get_status_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


