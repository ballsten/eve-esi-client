# GetUniverseAncestries200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bloodline_id** | **int** | The bloodline associated with this ancestry | 
**description** | **str** | description string | 
**icon_id** | **int** | icon_id integer | [optional] 
**id** | **int** | id integer | 
**name** | **str** | name string | 
**short_description** | **str** | short_description string | [optional] 

## Example

```python
from esi_client.models.get_universe_ancestries200_ok import GetUniverseAncestries200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseAncestries200Ok from a JSON string
get_universe_ancestries200_ok_instance = GetUniverseAncestries200Ok.from_json(json)
# print the JSON string representation of the object
print GetUniverseAncestries200Ok.to_json()

# convert the object into a dict
get_universe_ancestries200_ok_dict = get_universe_ancestries200_ok_instance.to_dict()
# create an instance of GetUniverseAncestries200Ok from a dict
get_universe_ancestries200_ok_form_dict = get_universe_ancestries200_ok.from_dict(get_universe_ancestries200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


