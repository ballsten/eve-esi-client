# GetCorporationsCorporationIdCustomsOffices200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alliance_tax_rate** | **float** | Only present if alliance access is allowed | [optional] 
**allow_access_with_standings** | **bool** | standing_level and any standing related tax rate only present when this is true | 
**allow_alliance_access** | **bool** | allow_alliance_access boolean | 
**bad_standing_tax_rate** | **float** | bad_standing_tax_rate number | [optional] 
**corporation_tax_rate** | **float** | corporation_tax_rate number | [optional] 
**excellent_standing_tax_rate** | **float** | Tax rate for entities with excellent level of standing, only present if this level is allowed, same for all other standing related tax rates | [optional] 
**good_standing_tax_rate** | **float** | good_standing_tax_rate number | [optional] 
**neutral_standing_tax_rate** | **float** | neutral_standing_tax_rate number | [optional] 
**office_id** | **int** | unique ID of this customs office | 
**reinforce_exit_end** | **int** | reinforce_exit_end integer | 
**reinforce_exit_start** | **int** | Together with reinforce_exit_end, marks a 2-hour period where this customs office could exit reinforcement mode during the day after initial attack | 
**standing_level** | **str** | Access is allowed only for entities with this level of standing or better | [optional] 
**system_id** | **int** | ID of the solar system this customs office is located in | 
**terrible_standing_tax_rate** | **float** | terrible_standing_tax_rate number | [optional] 

## Example

```python
from esi_client.models.get_corporations_corporation_id_customs_offices200_ok import GetCorporationsCorporationIdCustomsOffices200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdCustomsOffices200Ok from a JSON string
get_corporations_corporation_id_customs_offices200_ok_instance = GetCorporationsCorporationIdCustomsOffices200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdCustomsOffices200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_customs_offices200_ok_dict = get_corporations_corporation_id_customs_offices200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdCustomsOffices200Ok from a dict
get_corporations_corporation_id_customs_offices200_ok_form_dict = get_corporations_corporation_id_customs_offices200_ok.from_dict(get_corporations_corporation_id_customs_offices200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


