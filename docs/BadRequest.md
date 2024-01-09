# BadRequest

Bad request model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Bad request message | 

## Example

```python
from esi_client.models.bad_request import BadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequest from a JSON string
bad_request_instance = BadRequest.from_json(json)
# print the JSON string representation of the object
print BadRequest.to_json()

# convert the object into a dict
bad_request_dict = bad_request_instance.to_dict()
# create an instance of BadRequest from a dict
bad_request_form_dict = bad_request.from_dict(bad_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


