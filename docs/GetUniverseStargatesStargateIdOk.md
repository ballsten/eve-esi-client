# GetUniverseStargatesStargateIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | [**GetUniverseStargatesStargateIdDestination**](GetUniverseStargatesStargateIdDestination.md) |  | 
**name** | **str** | name string | 
**position** | [**GetUniverseStargatesStargateIdPosition**](GetUniverseStargatesStargateIdPosition.md) |  | 
**stargate_id** | **int** | stargate_id integer | 
**system_id** | **int** | The solar system this stargate is in | 
**type_id** | **int** | type_id integer | 

## Example

```python
from esi_client.models.get_universe_stargates_stargate_id_ok import GetUniverseStargatesStargateIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseStargatesStargateIdOk from a JSON string
get_universe_stargates_stargate_id_ok_instance = GetUniverseStargatesStargateIdOk.from_json(json)
# print the JSON string representation of the object
print GetUniverseStargatesStargateIdOk.to_json()

# convert the object into a dict
get_universe_stargates_stargate_id_ok_dict = get_universe_stargates_stargate_id_ok_instance.to_dict()
# create an instance of GetUniverseStargatesStargateIdOk from a dict
get_universe_stargates_stargate_id_ok_form_dict = get_universe_stargates_stargate_id_ok.from_dict(get_universe_stargates_stargate_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


