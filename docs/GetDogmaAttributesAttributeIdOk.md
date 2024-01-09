# GetDogmaAttributesAttributeIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **int** | attribute_id integer | 
**default_value** | **float** | default_value number | [optional] 
**description** | **str** | description string | [optional] 
**display_name** | **str** | display_name string | [optional] 
**high_is_good** | **bool** | high_is_good boolean | [optional] 
**icon_id** | **int** | icon_id integer | [optional] 
**name** | **str** | name string | [optional] 
**published** | **bool** | published boolean | [optional] 
**stackable** | **bool** | stackable boolean | [optional] 
**unit_id** | **int** | unit_id integer | [optional] 

## Example

```python
from esi_client.models.get_dogma_attributes_attribute_id_ok import GetDogmaAttributesAttributeIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetDogmaAttributesAttributeIdOk from a JSON string
get_dogma_attributes_attribute_id_ok_instance = GetDogmaAttributesAttributeIdOk.from_json(json)
# print the JSON string representation of the object
print GetDogmaAttributesAttributeIdOk.to_json()

# convert the object into a dict
get_dogma_attributes_attribute_id_ok_dict = get_dogma_attributes_attribute_id_ok_instance.to_dict()
# create an instance of GetDogmaAttributesAttributeIdOk from a dict
get_dogma_attributes_attribute_id_ok_form_dict = get_dogma_attributes_attribute_id_ok.from_dict(get_dogma_attributes_attribute_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


