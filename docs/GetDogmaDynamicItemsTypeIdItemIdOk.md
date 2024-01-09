# GetDogmaDynamicItemsTypeIdItemIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **int** | The ID of the character who created the item | 
**dogma_attributes** | [**List[GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute]**](GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute.md) | dogma_attributes array | 
**dogma_effects** | [**List[GetDogmaDynamicItemsTypeIdItemIdDogmaEffect]**](GetDogmaDynamicItemsTypeIdItemIdDogmaEffect.md) | dogma_effects array | 
**mutator_type_id** | **int** | The type ID of the mutator used to generate the dynamic item. | 
**source_type_id** | **int** | The type ID of the source item the mutator was applied to create the dynamic item. | 

## Example

```python
from esi_client.models.get_dogma_dynamic_items_type_id_item_id_ok import GetDogmaDynamicItemsTypeIdItemIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetDogmaDynamicItemsTypeIdItemIdOk from a JSON string
get_dogma_dynamic_items_type_id_item_id_ok_instance = GetDogmaDynamicItemsTypeIdItemIdOk.from_json(json)
# print the JSON string representation of the object
print GetDogmaDynamicItemsTypeIdItemIdOk.to_json()

# convert the object into a dict
get_dogma_dynamic_items_type_id_item_id_ok_dict = get_dogma_dynamic_items_type_id_item_id_ok_instance.to_dict()
# create an instance of GetDogmaDynamicItemsTypeIdItemIdOk from a dict
get_dogma_dynamic_items_type_id_item_id_ok_form_dict = get_dogma_dynamic_items_type_id_item_id_ok.from_dict(get_dogma_dynamic_items_type_id_item_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


