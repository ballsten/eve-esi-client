# GetCorporationsCorporationIdStructures200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporation_id** | **int** | ID of the corporation that owns the structure | 
**fuel_expires** | **datetime** | Date on which the structure will run out of fuel | [optional] 
**name** | **str** | The structure name | [optional] 
**next_reinforce_apply** | **datetime** | The date and time when the structure&#39;s newly requested reinforcement times (e.g. next_reinforce_hour and next_reinforce_day) will take effect | [optional] 
**next_reinforce_hour** | **int** | The requested change to reinforce_hour that will take effect at the time shown by next_reinforce_apply | [optional] 
**profile_id** | **int** | The id of the ACL profile for this citadel | 
**reinforce_hour** | **int** | The hour of day that determines the four hour window when the structure will randomly exit its reinforcement periods and become vulnerable to attack against its armor and/or hull. The structure will become vulnerable at a random time that is +/- 2 hours centered on the value of this property | [optional] 
**services** | [**List[GetCorporationsCorporationIdStructuresService]**](GetCorporationsCorporationIdStructuresService.md) | Contains a list of service upgrades, and their state | [optional] 
**state** | **str** | state string | 
**state_timer_end** | **datetime** | Date at which the structure will move to it&#39;s next state | [optional] 
**state_timer_start** | **datetime** | Date at which the structure entered it&#39;s current state | [optional] 
**structure_id** | **int** | The Item ID of the structure | 
**system_id** | **int** | The solar system the structure is in | 
**type_id** | **int** | The type id of the structure | 
**unanchors_at** | **datetime** | Date at which the structure will unanchor | [optional] 

## Example

```python
from esi_client.models.get_corporations_corporation_id_structures200_ok import GetCorporationsCorporationIdStructures200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdStructures200Ok from a JSON string
get_corporations_corporation_id_structures200_ok_instance = GetCorporationsCorporationIdStructures200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdStructures200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_structures200_ok_dict = get_corporations_corporation_id_structures200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdStructures200Ok from a dict
get_corporations_corporation_id_structures200_ok_form_dict = get_corporations_corporation_id_structures200_ok.from_dict(get_corporations_corporation_id_structures200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


