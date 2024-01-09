# GetCorporationsCorporationIdTitles200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grantable_roles** | **List[str]** | grantable_roles array | [optional] 
**grantable_roles_at_base** | **List[str]** | grantable_roles_at_base array | [optional] 
**grantable_roles_at_hq** | **List[str]** | grantable_roles_at_hq array | [optional] 
**grantable_roles_at_other** | **List[str]** | grantable_roles_at_other array | [optional] 
**name** | **str** | name string | [optional] 
**roles** | **List[str]** | roles array | [optional] 
**roles_at_base** | **List[str]** | roles_at_base array | [optional] 
**roles_at_hq** | **List[str]** | roles_at_hq array | [optional] 
**roles_at_other** | **List[str]** | roles_at_other array | [optional] 
**title_id** | **int** | title_id integer | [optional] 

## Example

```python
from esi_client.models.get_corporations_corporation_id_titles200_ok import GetCorporationsCorporationIdTitles200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdTitles200Ok from a JSON string
get_corporations_corporation_id_titles200_ok_instance = GetCorporationsCorporationIdTitles200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdTitles200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_titles200_ok_dict = get_corporations_corporation_id_titles200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdTitles200Ok from a dict
get_corporations_corporation_id_titles200_ok_form_dict = get_corporations_corporation_id_titles200_ok.from_dict(get_corporations_corporation_id_titles200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


