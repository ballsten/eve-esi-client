# GetUniverseStarsStarIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** | Age of star in years | 
**luminosity** | **float** | luminosity number | 
**name** | **str** | name string | 
**radius** | **int** | radius integer | 
**solar_system_id** | **int** | solar_system_id integer | 
**spectral_class** | **str** | spectral_class string | 
**temperature** | **int** | temperature integer | 
**type_id** | **int** | type_id integer | 

## Example

```python
from esi_client.models.get_universe_stars_star_id_ok import GetUniverseStarsStarIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseStarsStarIdOk from a JSON string
get_universe_stars_star_id_ok_instance = GetUniverseStarsStarIdOk.from_json(json)
# print the JSON string representation of the object
print GetUniverseStarsStarIdOk.to_json()

# convert the object into a dict
get_universe_stars_star_id_ok_dict = get_universe_stars_star_id_ok_instance.to_dict()
# create an instance of GetUniverseStarsStarIdOk from a dict
get_universe_stars_star_id_ok_form_dict = get_universe_stars_star_id_ok.from_dict(get_universe_stars_star_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


