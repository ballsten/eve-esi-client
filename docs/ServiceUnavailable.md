# ServiceUnavailable

Service unavailable model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Service unavailable message | 

## Example

```python
from esi_client.models.service_unavailable import ServiceUnavailable

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUnavailable from a JSON string
service_unavailable_instance = ServiceUnavailable.from_json(json)
# print the JSON string representation of the object
print ServiceUnavailable.to_json()

# convert the object into a dict
service_unavailable_dict = service_unavailable_instance.to_dict()
# create an instance of ServiceUnavailable from a dict
service_unavailable_form_dict = service_unavailable.from_dict(service_unavailable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


