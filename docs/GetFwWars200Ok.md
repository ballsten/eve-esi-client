# GetFwWars200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**against_id** | **int** | The faction ID of the enemy faction. | 
**faction_id** | **int** | faction_id integer | 

## Example

```python
from esi_client.models.get_fw_wars200_ok import GetFwWars200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetFwWars200Ok from a JSON string
get_fw_wars200_ok_instance = GetFwWars200Ok.from_json(json)
# print the JSON string representation of the object
print GetFwWars200Ok.to_json()

# convert the object into a dict
get_fw_wars200_ok_dict = get_fw_wars200_ok_instance.to_dict()
# create an instance of GetFwWars200Ok from a dict
get_fw_wars200_ok_form_dict = get_fw_wars200_ok.from_dict(get_fw_wars200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


