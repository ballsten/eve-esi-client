# GetCorporationCorporationIdMiningObservers200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated** | **date** | last_updated string | 
**observer_id** | **int** | The entity that was observing the asteroid field when it was mined.  | 
**observer_type** | **str** | The category of the observing entity | 

## Example

```python
from esi_client.models.get_corporation_corporation_id_mining_observers200_ok import GetCorporationCorporationIdMiningObservers200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationCorporationIdMiningObservers200Ok from a JSON string
get_corporation_corporation_id_mining_observers200_ok_instance = GetCorporationCorporationIdMiningObservers200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationCorporationIdMiningObservers200Ok.to_json()

# convert the object into a dict
get_corporation_corporation_id_mining_observers200_ok_dict = get_corporation_corporation_id_mining_observers200_ok_instance.to_dict()
# create an instance of GetCorporationCorporationIdMiningObservers200Ok from a dict
get_corporation_corporation_id_mining_observers200_ok_form_dict = get_corporation_corporation_id_mining_observers200_ok.from_dict(get_corporation_corporation_id_mining_observers200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


