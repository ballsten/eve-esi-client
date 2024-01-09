# GetUniverseTypesTypeIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **float** | capacity number | [optional] 
**description** | **str** | description string | 
**dogma_attributes** | [**List[GetUniverseTypesTypeIdDogmaAttribute]**](GetUniverseTypesTypeIdDogmaAttribute.md) | dogma_attributes array | [optional] 
**dogma_effects** | [**List[GetUniverseTypesTypeIdDogmaEffect]**](GetUniverseTypesTypeIdDogmaEffect.md) | dogma_effects array | [optional] 
**graphic_id** | **int** | graphic_id integer | [optional] 
**group_id** | **int** | group_id integer | 
**icon_id** | **int** | icon_id integer | [optional] 
**market_group_id** | **int** | This only exists for types that can be put on the market | [optional] 
**mass** | **float** | mass number | [optional] 
**name** | **str** | name string | 
**packaged_volume** | **float** | packaged_volume number | [optional] 
**portion_size** | **int** | portion_size integer | [optional] 
**published** | **bool** | published boolean | 
**radius** | **float** | radius number | [optional] 
**type_id** | **int** | type_id integer | 
**volume** | **float** | volume number | [optional] 

## Example

```python
from esi_client.models.get_universe_types_type_id_ok import GetUniverseTypesTypeIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseTypesTypeIdOk from a JSON string
get_universe_types_type_id_ok_instance = GetUniverseTypesTypeIdOk.from_json(json)
# print the JSON string representation of the object
print GetUniverseTypesTypeIdOk.to_json()

# convert the object into a dict
get_universe_types_type_id_ok_dict = get_universe_types_type_id_ok_instance.to_dict()
# create an instance of GetUniverseTypesTypeIdOk from a dict
get_universe_types_type_id_ok_form_dict = get_universe_types_type_id_ok.from_dict(get_universe_types_type_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


