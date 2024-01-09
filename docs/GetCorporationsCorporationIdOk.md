# GetCorporationsCorporationIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alliance_id** | **int** | ID of the alliance that corporation is a member of, if any | [optional] 
**ceo_id** | **int** | ceo_id integer | 
**creator_id** | **int** | creator_id integer | 
**date_founded** | **datetime** | date_founded string | [optional] 
**description** | **str** | description string | [optional] 
**faction_id** | **int** | faction_id integer | [optional] 
**home_station_id** | **int** | home_station_id integer | [optional] 
**member_count** | **int** | member_count integer | 
**name** | **str** | the full name of the corporation | 
**shares** | **int** | shares integer | [optional] 
**tax_rate** | **float** | tax_rate number | 
**ticker** | **str** | the short name of the corporation | 
**url** | **str** | url string | [optional] 
**war_eligible** | **bool** | war_eligible boolean | [optional] 

## Example

```python
from esi_client.models.get_corporations_corporation_id_ok import GetCorporationsCorporationIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdOk from a JSON string
get_corporations_corporation_id_ok_instance = GetCorporationsCorporationIdOk.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdOk.to_json()

# convert the object into a dict
get_corporations_corporation_id_ok_dict = get_corporations_corporation_id_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdOk from a dict
get_corporations_corporation_id_ok_form_dict = get_corporations_corporation_id_ok.from_dict(get_corporations_corporation_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


