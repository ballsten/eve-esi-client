# PostUniverseIdsInventoryType

inventory_type object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id integer | [optional] 
**name** | **str** | name string | [optional] 

## Example

```python
from esi_client.models.post_universe_ids_inventory_type import PostUniverseIdsInventoryType

# TODO update the JSON string below
json = "{}"
# create an instance of PostUniverseIdsInventoryType from a JSON string
post_universe_ids_inventory_type_instance = PostUniverseIdsInventoryType.from_json(json)
# print the JSON string representation of the object
print PostUniverseIdsInventoryType.to_json()

# convert the object into a dict
post_universe_ids_inventory_type_dict = post_universe_ids_inventory_type_instance.to_dict()
# create an instance of PostUniverseIdsInventoryType from a dict
post_universe_ids_inventory_type_form_dict = post_universe_ids_inventory_type.from_dict(post_universe_ids_inventory_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


