# GetAlliancesAllianceIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator_corporation_id** | **int** | ID of the corporation that created the alliance | 
**creator_id** | **int** | ID of the character that created the alliance | 
**date_founded** | **datetime** | date_founded string | 
**executor_corporation_id** | **int** | the executor corporation ID, if this alliance is not closed | [optional] 
**faction_id** | **int** | Faction ID this alliance is fighting for, if this alliance is enlisted in factional warfare | [optional] 
**name** | **str** | the full name of the alliance | 
**ticker** | **str** | the short name of the alliance | 

## Example

```python
from esi_client.models.get_alliances_alliance_id_ok import GetAlliancesAllianceIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetAlliancesAllianceIdOk from a JSON string
get_alliances_alliance_id_ok_instance = GetAlliancesAllianceIdOk.from_json(json)
# print the JSON string representation of the object
print GetAlliancesAllianceIdOk.to_json()

# convert the object into a dict
get_alliances_alliance_id_ok_dict = get_alliances_alliance_id_ok_instance.to_dict()
# create an instance of GetAlliancesAllianceIdOk from a dict
get_alliances_alliance_id_ok_form_dict = get_alliances_alliance_id_ok.from_dict(get_alliances_alliance_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


