# GetCorporationsCorporationIdRolesHistory200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_at** | **datetime** | changed_at string | 
**character_id** | **int** | The character whose roles are changed | 
**issuer_id** | **int** | ID of the character who issued this change | 
**new_roles** | **List[str]** | new_roles array | 
**old_roles** | **List[str]** | old_roles array | 
**role_type** | **str** | role_type string | 

## Example

```python
from esi_client.models.get_corporations_corporation_id_roles_history200_ok import GetCorporationsCorporationIdRolesHistory200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdRolesHistory200Ok from a JSON string
get_corporations_corporation_id_roles_history200_ok_instance = GetCorporationsCorporationIdRolesHistory200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdRolesHistory200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_roles_history200_ok_dict = get_corporations_corporation_id_roles_history200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdRolesHistory200Ok from a dict
get_corporations_corporation_id_roles_history200_ok_form_dict = get_corporations_corporation_id_roles_history200_ok.from_dict(get_corporations_corporation_id_roles_history200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


