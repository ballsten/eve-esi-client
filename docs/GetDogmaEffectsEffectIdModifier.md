# GetDogmaEffectsEffectIdModifier

modifier object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | domain string | [optional] 
**effect_id** | **int** | effect_id integer | [optional] 
**func** | **str** | func string | 
**modified_attribute_id** | **int** | modified_attribute_id integer | [optional] 
**modifying_attribute_id** | **int** | modifying_attribute_id integer | [optional] 
**operator** | **int** | operator integer | [optional] 

## Example

```python
from esi_client.models.get_dogma_effects_effect_id_modifier import GetDogmaEffectsEffectIdModifier

# TODO update the JSON string below
json = "{}"
# create an instance of GetDogmaEffectsEffectIdModifier from a JSON string
get_dogma_effects_effect_id_modifier_instance = GetDogmaEffectsEffectIdModifier.from_json(json)
# print the JSON string representation of the object
print GetDogmaEffectsEffectIdModifier.to_json()

# convert the object into a dict
get_dogma_effects_effect_id_modifier_dict = get_dogma_effects_effect_id_modifier_instance.to_dict()
# create an instance of GetDogmaEffectsEffectIdModifier from a dict
get_dogma_effects_effect_id_modifier_form_dict = get_dogma_effects_effect_id_modifier.from_dict(get_dogma_effects_effect_id_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


