# GetCorporationsCorporationIdStructuresService

service object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name string | 
**state** | **str** | state string | 

## Example

```python
from esi_client.models.get_corporations_corporation_id_structures_service import GetCorporationsCorporationIdStructuresService

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdStructuresService from a JSON string
get_corporations_corporation_id_structures_service_instance = GetCorporationsCorporationIdStructuresService.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdStructuresService.to_json()

# convert the object into a dict
get_corporations_corporation_id_structures_service_dict = get_corporations_corporation_id_structures_service_instance.to_dict()
# create an instance of GetCorporationsCorporationIdStructuresService from a dict
get_corporations_corporation_id_structures_service_form_dict = get_corporations_corporation_id_structures_service.from_dict(get_corporations_corporation_id_structures_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


