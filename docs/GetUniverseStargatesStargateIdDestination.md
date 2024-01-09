# GetUniverseStargatesStargateIdDestination

destination object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stargate_id** | **int** | The stargate this stargate connects to | 
**system_id** | **int** | The solar system this stargate connects to | 

## Example

```python
from esi_client.models.get_universe_stargates_stargate_id_destination import GetUniverseStargatesStargateIdDestination

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseStargatesStargateIdDestination from a JSON string
get_universe_stargates_stargate_id_destination_instance = GetUniverseStargatesStargateIdDestination.from_json(json)
# print the JSON string representation of the object
print GetUniverseStargatesStargateIdDestination.to_json()

# convert the object into a dict
get_universe_stargates_stargate_id_destination_dict = get_universe_stargates_stargate_id_destination_instance.to_dict()
# create an instance of GetUniverseStargatesStargateIdDestination from a dict
get_universe_stargates_stargate_id_destination_form_dict = get_universe_stargates_stargate_id_destination.from_dict(get_universe_stargates_stargate_id_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


