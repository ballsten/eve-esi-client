# PostFleetsFleetIdMembersInvitation

invitation object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character_id** | **int** | The character you want to invite | 
**role** | **str** | If a character is invited with the &#x60;fleet_commander&#x60; role, neither &#x60;wing_id&#x60; or &#x60;squad_id&#x60; should be specified. If a character is invited with the &#x60;wing_commander&#x60; role, only &#x60;wing_id&#x60; should be specified. If a character is invited with the &#x60;squad_commander&#x60; role, both &#x60;wing_id&#x60; and &#x60;squad_id&#x60; should be specified. If a character is invited with the &#x60;squad_member&#x60; role, &#x60;wing_id&#x60; and &#x60;squad_id&#x60; should either both be specified or not specified at all. If they aren’t specified, the invited character will join any squad with available positions. | 
**squad_id** | **int** | squad_id integer | [optional] 
**wing_id** | **int** | wing_id integer | [optional] 

## Example

```python
from esi_client.models.post_fleets_fleet_id_members_invitation import PostFleetsFleetIdMembersInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of PostFleetsFleetIdMembersInvitation from a JSON string
post_fleets_fleet_id_members_invitation_instance = PostFleetsFleetIdMembersInvitation.from_json(json)
# print the JSON string representation of the object
print PostFleetsFleetIdMembersInvitation.to_json()

# convert the object into a dict
post_fleets_fleet_id_members_invitation_dict = post_fleets_fleet_id_members_invitation_instance.to_dict()
# create an instance of PostFleetsFleetIdMembersInvitation from a dict
post_fleets_fleet_id_members_invitation_form_dict = post_fleets_fleet_id_members_invitation.from_dict(post_fleets_fleet_id_members_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


