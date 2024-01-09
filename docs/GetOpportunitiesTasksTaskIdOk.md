# GetOpportunitiesTasksTaskIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description string | 
**name** | **str** | name string | 
**notification** | **str** | notification string | 
**task_id** | **int** | task_id integer | 

## Example

```python
from esi_client.models.get_opportunities_tasks_task_id_ok import GetOpportunitiesTasksTaskIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpportunitiesTasksTaskIdOk from a JSON string
get_opportunities_tasks_task_id_ok_instance = GetOpportunitiesTasksTaskIdOk.from_json(json)
# print the JSON string representation of the object
print GetOpportunitiesTasksTaskIdOk.to_json()

# convert the object into a dict
get_opportunities_tasks_task_id_ok_dict = get_opportunities_tasks_task_id_ok_instance.to_dict()
# create an instance of GetOpportunitiesTasksTaskIdOk from a dict
get_opportunities_tasks_task_id_ok_form_dict = get_opportunities_tasks_task_id_ok.from_dict(get_opportunities_tasks_task_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


