# Forbidden

Forbidden model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Forbidden message | 
**sso_status** | **int** | status code received from SSO | [optional] 

## Example

```python
from esi_client.models.forbidden import Forbidden

# TODO update the JSON string below
json = "{}"
# create an instance of Forbidden from a JSON string
forbidden_instance = Forbidden.from_json(json)
# print the JSON string representation of the object
print Forbidden.to_json()

# convert the object into a dict
forbidden_dict = forbidden_instance.to_dict()
# create an instance of Forbidden from a dict
forbidden_form_dict = forbidden.from_dict(forbidden_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


