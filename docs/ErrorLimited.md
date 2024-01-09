# ErrorLimited

Error limited model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error limited message | 

## Example

```python
from esi_client.models.error_limited import ErrorLimited

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorLimited from a JSON string
error_limited_instance = ErrorLimited.from_json(json)
# print the JSON string representation of the object
print ErrorLimited.to_json()

# convert the object into a dict
error_limited_dict = error_limited_instance.to_dict()
# create an instance of ErrorLimited from a dict
error_limited_form_dict = error_limited.from_dict(error_limited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


