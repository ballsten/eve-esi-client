# GatewayTimeout

Gateway timeout model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Gateway timeout message | 
**timeout** | **int** | number of seconds the request was given | [optional] 

## Example

```python
from esi_client.models.gateway_timeout import GatewayTimeout

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayTimeout from a JSON string
gateway_timeout_instance = GatewayTimeout.from_json(json)
# print the JSON string representation of the object
print GatewayTimeout.to_json()

# convert the object into a dict
gateway_timeout_dict = gateway_timeout_instance.to_dict()
# create an instance of GatewayTimeout from a dict
gateway_timeout_form_dict = gateway_timeout.from_dict(gateway_timeout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


