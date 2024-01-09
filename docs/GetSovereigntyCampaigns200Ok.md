# GetSovereigntyCampaigns200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attackers_score** | **float** | Score for all attacking parties, only present in Defense Events.  | [optional] 
**campaign_id** | **int** | Unique ID for this campaign. | 
**constellation_id** | **int** | The constellation in which the campaign will take place.  | 
**defender_id** | **int** | Defending alliance, only present in Defense Events  | [optional] 
**defender_score** | **float** | Score for the defending alliance, only present in Defense Events.  | [optional] 
**event_type** | **str** | Type of event this campaign is for. tcu_defense, ihub_defense and station_defense are referred to as \&quot;Defense Events\&quot;, station_freeport as \&quot;Freeport Events\&quot;.  | 
**participants** | [**List[GetSovereigntyCampaignsParticipant]**](GetSovereigntyCampaignsParticipant.md) | Alliance participating and their respective scores, only present in Freeport Events.  | [optional] 
**solar_system_id** | **int** | The solar system the structure is located in.  | 
**start_time** | **datetime** | Time the event is scheduled to start.  | 
**structure_id** | **int** | The structure item ID that is related to this campaign.  | 

## Example

```python
from esi_client.models.get_sovereignty_campaigns200_ok import GetSovereigntyCampaigns200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetSovereigntyCampaigns200Ok from a JSON string
get_sovereignty_campaigns200_ok_instance = GetSovereigntyCampaigns200Ok.from_json(json)
# print the JSON string representation of the object
print GetSovereigntyCampaigns200Ok.to_json()

# convert the object into a dict
get_sovereignty_campaigns200_ok_dict = get_sovereignty_campaigns200_ok_instance.to_dict()
# create an instance of GetSovereigntyCampaigns200Ok from a dict
get_sovereignty_campaigns200_ok_form_dict = get_sovereignty_campaigns200_ok.from_dict(get_sovereignty_campaigns200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


