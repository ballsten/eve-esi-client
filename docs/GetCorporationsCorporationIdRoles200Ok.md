# GetCorporationsCorporationIdRoles200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character_id** | **int** | character_id integer | 
**grantable_roles** | **List[str]** | grantable_roles array | [optional] 
**grantable_roles_at_base** | **List[str]** | grantable_roles_at_base array | [optional] 
**grantable_roles_at_hq** | **List[str]** | grantable_roles_at_hq array | [optional] 
**grantable_roles_at_other** | **List[str]** | grantable_roles_at_other array | [optional] 
**roles** | **List[str]** | roles array | [optional] 
**roles_at_base** | **List[str]** | roles_at_base array | [optional] 
**roles_at_hq** | **List[str]** | roles_at_hq array | [optional] 
**roles_at_other** | **List[str]** | roles_at_other array | [optional] 

## Example

```python
from esi_client.models.get_corporations_corporation_id_roles200_ok import GetCorporationsCorporationIdRoles200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdRoles200Ok from a JSON string
get_corporations_corporation_id_roles200_ok_instance = GetCorporationsCorporationIdRoles200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdRoles200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_roles200_ok_dict = get_corporations_corporation_id_roles200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdRoles200Ok from a dict
get_corporations_corporation_id_roles200_ok_form_dict = get_corporations_corporation_id_roles200_ok.from_dict(get_corporations_corporation_id_roles200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


