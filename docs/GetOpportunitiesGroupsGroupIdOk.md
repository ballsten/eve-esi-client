# GetOpportunitiesGroupsGroupIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_groups** | **List[int]** | The groups that are connected to this group on the opportunities map | 
**description** | **str** | description string | 
**group_id** | **int** | group_id integer | 
**name** | **str** | name string | 
**notification** | **str** | notification string | 
**required_tasks** | **List[int]** | Tasks need to complete for this group | 

## Example

```python
from esi_client.models.get_opportunities_groups_group_id_ok import GetOpportunitiesGroupsGroupIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpportunitiesGroupsGroupIdOk from a JSON string
get_opportunities_groups_group_id_ok_instance = GetOpportunitiesGroupsGroupIdOk.from_json(json)
# print the JSON string representation of the object
print GetOpportunitiesGroupsGroupIdOk.to_json()

# convert the object into a dict
get_opportunities_groups_group_id_ok_dict = get_opportunities_groups_group_id_ok_instance.to_dict()
# create an instance of GetOpportunitiesGroupsGroupIdOk from a dict
get_opportunities_groups_group_id_ok_form_dict = get_opportunities_groups_group_id_ok.from_dict(get_opportunities_groups_group_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


