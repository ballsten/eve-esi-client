# Unauthorized

Unauthorized model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Unauthorized message | 

## Example

```python
from esi_client.models.unauthorized import Unauthorized

# TODO update the JSON string below
json = "{}"
# create an instance of Unauthorized from a JSON string
unauthorized_instance = Unauthorized.from_json(json)
# print the JSON string representation of the object
print Unauthorized.to_json()

# convert the object into a dict
unauthorized_dict = unauthorized_instance.to_dict()
# create an instance of Unauthorized from a dict
unauthorized_form_dict = unauthorized.from_dict(unauthorized_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


