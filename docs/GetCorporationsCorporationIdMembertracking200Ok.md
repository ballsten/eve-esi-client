# GetCorporationsCorporationIdMembertracking200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_id** | **int** | base_id integer | [optional] 
**character_id** | **int** | character_id integer | 
**location_id** | **int** | location_id integer | [optional] 
**logoff_date** | **datetime** | logoff_date string | [optional] 
**logon_date** | **datetime** | logon_date string | [optional] 
**ship_type_id** | **int** | ship_type_id integer | [optional] 
**start_date** | **datetime** | start_date string | [optional] 

## Example

```python
from esi_client.models.get_corporations_corporation_id_membertracking200_ok import GetCorporationsCorporationIdMembertracking200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdMembertracking200Ok from a JSON string
get_corporations_corporation_id_membertracking200_ok_instance = GetCorporationsCorporationIdMembertracking200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdMembertracking200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_membertracking200_ok_dict = get_corporations_corporation_id_membertracking200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdMembertracking200Ok from a dict
get_corporations_corporation_id_membertracking200_ok_form_dict = get_corporations_corporation_id_membertracking200_ok.from_dict(get_corporations_corporation_id_membertracking200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


