# GetCorporationsCorporationIdAlliancehistory200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alliance_id** | **int** | alliance_id integer | [optional] 
**is_deleted** | **bool** | True if the alliance has been closed | [optional] 
**record_id** | **int** | An incrementing ID that can be used to canonically establish order of records in cases where dates may be ambiguous | 
**start_date** | **datetime** | start_date string | 

## Example

```python
from esi_client.models.get_corporations_corporation_id_alliancehistory200_ok import GetCorporationsCorporationIdAlliancehistory200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdAlliancehistory200Ok from a JSON string
get_corporations_corporation_id_alliancehistory200_ok_instance = GetCorporationsCorporationIdAlliancehistory200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdAlliancehistory200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_alliancehistory200_ok_dict = get_corporations_corporation_id_alliancehistory200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdAlliancehistory200Ok from a dict
get_corporations_corporation_id_alliancehistory200_ok_form_dict = get_corporations_corporation_id_alliancehistory200_ok.from_dict(get_corporations_corporation_id_alliancehistory200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


