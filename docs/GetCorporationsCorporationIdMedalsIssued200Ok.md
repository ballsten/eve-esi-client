# GetCorporationsCorporationIdMedalsIssued200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character_id** | **int** | ID of the character who was rewarded this medal | 
**issued_at** | **datetime** | issued_at string | 
**issuer_id** | **int** | ID of the character who issued the medal | 
**medal_id** | **int** | medal_id integer | 
**reason** | **str** | reason string | 
**status** | **str** | status string | 

## Example

```python
from esi_client.models.get_corporations_corporation_id_medals_issued200_ok import GetCorporationsCorporationIdMedalsIssued200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdMedalsIssued200Ok from a JSON string
get_corporations_corporation_id_medals_issued200_ok_instance = GetCorporationsCorporationIdMedalsIssued200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdMedalsIssued200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_medals_issued200_ok_dict = get_corporations_corporation_id_medals_issued200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdMedalsIssued200Ok from a dict
get_corporations_corporation_id_medals_issued200_ok_form_dict = get_corporations_corporation_id_medals_issued200_ok.from_dict(get_corporations_corporation_id_medals_issued200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


