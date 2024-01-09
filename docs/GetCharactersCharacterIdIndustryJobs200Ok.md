# GetCharactersCharacterIdIndustryJobs200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **int** | Job activity ID | 
**blueprint_id** | **int** | blueprint_id integer | 
**blueprint_location_id** | **int** | Location ID of the location from which the blueprint was installed. Normally a station ID, but can also be an asset (e.g. container) or corporation facility | 
**blueprint_type_id** | **int** | blueprint_type_id integer | 
**completed_character_id** | **int** | ID of the character which completed this job | [optional] 
**completed_date** | **datetime** | Date and time when this job was completed | [optional] 
**cost** | **float** | The sume of job installation fee and industry facility tax | [optional] 
**duration** | **int** | Job duration in seconds | 
**end_date** | **datetime** | Date and time when this job finished | 
**facility_id** | **int** | ID of the facility where this job is running | 
**installer_id** | **int** | ID of the character which installed this job | 
**job_id** | **int** | Unique job ID | 
**licensed_runs** | **int** | Number of runs blueprint is licensed for | [optional] 
**output_location_id** | **int** | Location ID of the location to which the output of the job will be delivered. Normally a station ID, but can also be a corporation facility | 
**pause_date** | **datetime** | Date and time when this job was paused (i.e. time when the facility where this job was installed went offline) | [optional] 
**probability** | **float** | Chance of success for invention | [optional] 
**product_type_id** | **int** | Type ID of product (manufactured, copied or invented) | [optional] 
**runs** | **int** | Number of runs for a manufacturing job, or number of copies to make for a blueprint copy | 
**start_date** | **datetime** | Date and time when this job started | 
**station_id** | **int** | ID of the station where industry facility is located | 
**status** | **str** | status string | 
**successful_runs** | **int** | Number of successful runs for this job. Equal to runs unless this is an invention job | [optional] 

## Example

```python
from esi_client.models.get_characters_character_id_industry_jobs200_ok import GetCharactersCharacterIdIndustryJobs200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdIndustryJobs200Ok from a JSON string
get_characters_character_id_industry_jobs200_ok_instance = GetCharactersCharacterIdIndustryJobs200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdIndustryJobs200Ok.to_json()

# convert the object into a dict
get_characters_character_id_industry_jobs200_ok_dict = get_characters_character_id_industry_jobs200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdIndustryJobs200Ok from a dict
get_characters_character_id_industry_jobs200_ok_form_dict = get_characters_character_id_industry_jobs200_ok.from_dict(get_characters_character_id_industry_jobs200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


