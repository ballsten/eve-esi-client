# GetCorporationsCorporationIdContainersLogs200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | action string | 
**character_id** | **int** | ID of the character who performed the action. | 
**container_id** | **int** | ID of the container | 
**container_type_id** | **int** | Type ID of the container | 
**location_flag** | **str** | location_flag string | 
**location_id** | **int** | location_id integer | 
**logged_at** | **datetime** | Timestamp when this log was created | 
**new_config_bitmask** | **int** | new_config_bitmask integer | [optional] 
**old_config_bitmask** | **int** | old_config_bitmask integer | [optional] 
**password_type** | **str** | Type of password set if action is of type SetPassword or EnterPassword | [optional] 
**quantity** | **int** | Quantity of the item being acted upon | [optional] 
**type_id** | **int** | Type ID of the item being acted upon | [optional] 

## Example

```python
from esi_client.models.get_corporations_corporation_id_containers_logs200_ok import GetCorporationsCorporationIdContainersLogs200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdContainersLogs200Ok from a JSON string
get_corporations_corporation_id_containers_logs200_ok_instance = GetCorporationsCorporationIdContainersLogs200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdContainersLogs200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_containers_logs200_ok_dict = get_corporations_corporation_id_containers_logs200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdContainersLogs200Ok from a dict
get_corporations_corporation_id_containers_logs200_ok_form_dict = get_corporations_corporation_id_containers_logs200_ok.from_dict(get_corporations_corporation_id_containers_logs200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


