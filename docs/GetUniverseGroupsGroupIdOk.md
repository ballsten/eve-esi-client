# GetUniverseGroupsGroupIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **int** | category_id integer | 
**group_id** | **int** | group_id integer | 
**name** | **str** | name string | 
**published** | **bool** | published boolean | 
**types** | **List[int]** | types array | 

## Example

```python
from esi_client.models.get_universe_groups_group_id_ok import GetUniverseGroupsGroupIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseGroupsGroupIdOk from a JSON string
get_universe_groups_group_id_ok_instance = GetUniverseGroupsGroupIdOk.from_json(json)
# print the JSON string representation of the object
print GetUniverseGroupsGroupIdOk.to_json()

# convert the object into a dict
get_universe_groups_group_id_ok_dict = get_universe_groups_group_id_ok_instance.to_dict()
# create an instance of GetUniverseGroupsGroupIdOk from a dict
get_universe_groups_group_id_ok_form_dict = get_universe_groups_group_id_ok.from_dict(get_universe_groups_group_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


