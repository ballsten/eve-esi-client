# GetSovereigntyCampaignsParticipant

participant object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alliance_id** | **int** | alliance_id integer | 
**score** | **float** | score number | 

## Example

```python
from esi_client.models.get_sovereignty_campaigns_participant import GetSovereigntyCampaignsParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of GetSovereigntyCampaignsParticipant from a JSON string
get_sovereignty_campaigns_participant_instance = GetSovereigntyCampaignsParticipant.from_json(json)
# print the JSON string representation of the object
print GetSovereigntyCampaignsParticipant.to_json()

# convert the object into a dict
get_sovereignty_campaigns_participant_dict = get_sovereignty_campaigns_participant_instance.to_dict()
# create an instance of GetSovereigntyCampaignsParticipant from a dict
get_sovereignty_campaigns_participant_form_dict = get_sovereignty_campaigns_participant.from_dict(get_sovereignty_campaigns_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


