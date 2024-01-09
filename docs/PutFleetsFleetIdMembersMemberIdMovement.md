# PutFleetsFleetIdMembersMemberIdMovement

movement object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | If a character is moved to the &#x60;fleet_commander&#x60; role, neither &#x60;wing_id&#x60; or &#x60;squad_id&#x60; should be specified. If a character is moved to the &#x60;wing_commander&#x60; role, only &#x60;wing_id&#x60; should be specified. If a character is moved to the &#x60;squad_commander&#x60; role, both &#x60;wing_id&#x60; and &#x60;squad_id&#x60; should be specified. If a character is moved to the &#x60;squad_member&#x60; role, both &#x60;wing_id&#x60; and &#x60;squad_id&#x60; should be specified. | 
**squad_id** | **int** | squad_id integer | [optional] 
**wing_id** | **int** | wing_id integer | [optional] 

## Example

```python
from esi_client.models.put_fleets_fleet_id_members_member_id_movement import PutFleetsFleetIdMembersMemberIdMovement

# TODO update the JSON string below
json = "{}"
# create an instance of PutFleetsFleetIdMembersMemberIdMovement from a JSON string
put_fleets_fleet_id_members_member_id_movement_instance = PutFleetsFleetIdMembersMemberIdMovement.from_json(json)
# print the JSON string representation of the object
print PutFleetsFleetIdMembersMemberIdMovement.to_json()

# convert the object into a dict
put_fleets_fleet_id_members_member_id_movement_dict = put_fleets_fleet_id_members_member_id_movement_instance.to_dict()
# create an instance of PutFleetsFleetIdMembersMemberIdMovement from a dict
put_fleets_fleet_id_members_member_id_movement_form_dict = put_fleets_fleet_id_members_member_id_movement.from_dict(put_fleets_fleet_id_members_member_id_movement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


