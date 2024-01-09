# GetCorporationCorporationIdMiningExtractions200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_arrival_time** | **datetime** | The time at which the chunk being extracted will arrive and can be fractured by the moon mining drill.  | 
**extraction_start_time** | **datetime** | The time at which the current extraction was initiated.  | 
**moon_id** | **int** | moon_id integer | 
**natural_decay_time** | **datetime** | The time at which the chunk being extracted will naturally fracture if it is not first fractured by the moon mining drill.  | 
**structure_id** | **int** | structure_id integer | 

## Example

```python
from esi_client.models.get_corporation_corporation_id_mining_extractions200_ok import GetCorporationCorporationIdMiningExtractions200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationCorporationIdMiningExtractions200Ok from a JSON string
get_corporation_corporation_id_mining_extractions200_ok_instance = GetCorporationCorporationIdMiningExtractions200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationCorporationIdMiningExtractions200Ok.to_json()

# convert the object into a dict
get_corporation_corporation_id_mining_extractions200_ok_dict = get_corporation_corporation_id_mining_extractions200_ok_instance.to_dict()
# create an instance of GetCorporationCorporationIdMiningExtractions200Ok from a dict
get_corporation_corporation_id_mining_extractions200_ok_form_dict = get_corporation_corporation_id_mining_extractions200_ok.from_dict(get_corporation_corporation_id_mining_extractions200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


