# GetCorporationsCorporationIdStandings200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_id** | **int** | from_id integer | 
**from_type** | **str** | from_type string | 
**standing** | **float** | standing number | 

## Example

```python
from esi_client.models.get_corporations_corporation_id_standings200_ok import GetCorporationsCorporationIdStandings200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdStandings200Ok from a JSON string
get_corporations_corporation_id_standings200_ok_instance = GetCorporationsCorporationIdStandings200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdStandings200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_standings200_ok_dict = get_corporations_corporation_id_standings200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdStandings200Ok from a dict
get_corporations_corporation_id_standings200_ok_form_dict = get_corporations_corporation_id_standings200_ok.from_dict(get_corporations_corporation_id_standings200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


