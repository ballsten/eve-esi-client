# PostUniverseIdsOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[PostUniverseIdsAgent]**](PostUniverseIdsAgent.md) | agents array | [optional] 
**alliances** | [**List[PostUniverseIdsAlliance]**](PostUniverseIdsAlliance.md) | alliances array | [optional] 
**characters** | [**List[PostUniverseIdsCharacter]**](PostUniverseIdsCharacter.md) | characters array | [optional] 
**constellations** | [**List[PostUniverseIdsConstellation]**](PostUniverseIdsConstellation.md) | constellations array | [optional] 
**corporations** | [**List[PostUniverseIdsCorporation]**](PostUniverseIdsCorporation.md) | corporations array | [optional] 
**factions** | [**List[PostUniverseIdsFaction]**](PostUniverseIdsFaction.md) | factions array | [optional] 
**inventory_types** | [**List[PostUniverseIdsInventoryType]**](PostUniverseIdsInventoryType.md) | inventory_types array | [optional] 
**regions** | [**List[PostUniverseIdsRegion]**](PostUniverseIdsRegion.md) | regions array | [optional] 
**stations** | [**List[PostUniverseIdsStation]**](PostUniverseIdsStation.md) | stations array | [optional] 
**systems** | [**List[PostUniverseIdsSystem]**](PostUniverseIdsSystem.md) | systems array | [optional] 

## Example

```python
from esi_client.models.post_universe_ids_ok import PostUniverseIdsOk

# TODO update the JSON string below
json = "{}"
# create an instance of PostUniverseIdsOk from a JSON string
post_universe_ids_ok_instance = PostUniverseIdsOk.from_json(json)
# print the JSON string representation of the object
print PostUniverseIdsOk.to_json()

# convert the object into a dict
post_universe_ids_ok_dict = post_universe_ids_ok_instance.to_dict()
# create an instance of PostUniverseIdsOk from a dict
post_universe_ids_ok_form_dict = post_universe_ids_ok.from_dict(post_universe_ids_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


