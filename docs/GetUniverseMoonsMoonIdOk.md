# GetUniverseMoonsMoonIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moon_id** | **int** | moon_id integer | 
**name** | **str** | name string | 
**position** | [**GetUniverseMoonsMoonIdPosition**](GetUniverseMoonsMoonIdPosition.md) |  | 
**system_id** | **int** | The solar system this moon is in | 

## Example

```python
from esi_client.models.get_universe_moons_moon_id_ok import GetUniverseMoonsMoonIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseMoonsMoonIdOk from a JSON string
get_universe_moons_moon_id_ok_instance = GetUniverseMoonsMoonIdOk.from_json(json)
# print the JSON string representation of the object
print GetUniverseMoonsMoonIdOk.to_json()

# convert the object into a dict
get_universe_moons_moon_id_ok_dict = get_universe_moons_moon_id_ok_instance.to_dict()
# create an instance of GetUniverseMoonsMoonIdOk from a dict
get_universe_moons_moon_id_ok_form_dict = get_universe_moons_moon_id_ok.from_dict(get_universe_moons_moon_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


