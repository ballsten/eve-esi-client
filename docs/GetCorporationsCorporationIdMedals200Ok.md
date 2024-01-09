# GetCorporationsCorporationIdMedals200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | created_at string | 
**creator_id** | **int** | ID of the character who created this medal | 
**description** | **str** | description string | 
**medal_id** | **int** | medal_id integer | 
**title** | **str** | title string | 

## Example

```python
from esi_client.models.get_corporations_corporation_id_medals200_ok import GetCorporationsCorporationIdMedals200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdMedals200Ok from a JSON string
get_corporations_corporation_id_medals200_ok_instance = GetCorporationsCorporationIdMedals200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdMedals200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_medals200_ok_dict = get_corporations_corporation_id_medals200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdMedals200Ok from a dict
get_corporations_corporation_id_medals200_ok_form_dict = get_corporations_corporation_id_medals200_ok.from_dict(get_corporations_corporation_id_medals200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


