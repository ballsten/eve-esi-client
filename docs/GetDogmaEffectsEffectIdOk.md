# GetDogmaEffectsEffectIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description string | [optional] 
**disallow_auto_repeat** | **bool** | disallow_auto_repeat boolean | [optional] 
**discharge_attribute_id** | **int** | discharge_attribute_id integer | [optional] 
**display_name** | **str** | display_name string | [optional] 
**duration_attribute_id** | **int** | duration_attribute_id integer | [optional] 
**effect_category** | **int** | effect_category integer | [optional] 
**effect_id** | **int** | effect_id integer | 
**electronic_chance** | **bool** | electronic_chance boolean | [optional] 
**falloff_attribute_id** | **int** | falloff_attribute_id integer | [optional] 
**icon_id** | **int** | icon_id integer | [optional] 
**is_assistance** | **bool** | is_assistance boolean | [optional] 
**is_offensive** | **bool** | is_offensive boolean | [optional] 
**is_warp_safe** | **bool** | is_warp_safe boolean | [optional] 
**modifiers** | [**List[GetDogmaEffectsEffectIdModifier]**](GetDogmaEffectsEffectIdModifier.md) | modifiers array | [optional] 
**name** | **str** | name string | [optional] 
**post_expression** | **int** | post_expression integer | [optional] 
**pre_expression** | **int** | pre_expression integer | [optional] 
**published** | **bool** | published boolean | [optional] 
**range_attribute_id** | **int** | range_attribute_id integer | [optional] 
**range_chance** | **bool** | range_chance boolean | [optional] 
**tracking_speed_attribute_id** | **int** | tracking_speed_attribute_id integer | [optional] 

## Example

```python
from esi_client.models.get_dogma_effects_effect_id_ok import GetDogmaEffectsEffectIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetDogmaEffectsEffectIdOk from a JSON string
get_dogma_effects_effect_id_ok_instance = GetDogmaEffectsEffectIdOk.from_json(json)
# print the JSON string representation of the object
print GetDogmaEffectsEffectIdOk.to_json()

# convert the object into a dict
get_dogma_effects_effect_id_ok_dict = get_dogma_effects_effect_id_ok_instance.to_dict()
# create an instance of GetDogmaEffectsEffectIdOk from a dict
get_dogma_effects_effect_id_ok_form_dict = get_dogma_effects_effect_id_ok.from_dict(get_dogma_effects_effect_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


