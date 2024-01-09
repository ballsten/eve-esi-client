# GetWarsWarIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggressor** | [**GetWarsWarIdAggressor**](GetWarsWarIdAggressor.md) |  | 
**allies** | [**List[GetWarsWarIdAlly]**](GetWarsWarIdAlly.md) | allied corporations or alliances, each object contains either corporation_id or alliance_id | [optional] 
**declared** | **datetime** | Time that the war was declared | 
**defender** | [**GetWarsWarIdDefender**](GetWarsWarIdDefender.md) |  | 
**finished** | **datetime** | Time the war ended and shooting was no longer allowed | [optional] 
**id** | **int** | ID of the specified war | 
**mutual** | **bool** | Was the war declared mutual by both parties | 
**open_for_allies** | **bool** | Is the war currently open for allies or not | 
**retracted** | **datetime** | Time the war was retracted but both sides could still shoot each other | [optional] 
**started** | **datetime** | Time when the war started and both sides could shoot each other | [optional] 

## Example

```python
from esi_client.models.get_wars_war_id_ok import GetWarsWarIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetWarsWarIdOk from a JSON string
get_wars_war_id_ok_instance = GetWarsWarIdOk.from_json(json)
# print the JSON string representation of the object
print GetWarsWarIdOk.to_json()

# convert the object into a dict
get_wars_war_id_ok_dict = get_wars_war_id_ok_instance.to_dict()
# create an instance of GetWarsWarIdOk from a dict
get_wars_war_id_ok_form_dict = get_wars_war_id_ok.from_dict(get_wars_war_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


