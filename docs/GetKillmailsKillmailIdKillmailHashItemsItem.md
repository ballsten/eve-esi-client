# GetKillmailsKillmailIdKillmailHashItemsItem

item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flag** | **int** | flag integer | 
**item_type_id** | **int** | item_type_id integer | 
**quantity_destroyed** | **int** | quantity_destroyed integer | [optional] 
**quantity_dropped** | **int** | quantity_dropped integer | [optional] 
**singleton** | **int** | singleton integer | 

## Example

```python
from esi_client.models.get_killmails_killmail_id_killmail_hash_items_item import GetKillmailsKillmailIdKillmailHashItemsItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetKillmailsKillmailIdKillmailHashItemsItem from a JSON string
get_killmails_killmail_id_killmail_hash_items_item_instance = GetKillmailsKillmailIdKillmailHashItemsItem.from_json(json)
# print the JSON string representation of the object
print GetKillmailsKillmailIdKillmailHashItemsItem.to_json()

# convert the object into a dict
get_killmails_killmail_id_killmail_hash_items_item_dict = get_killmails_killmail_id_killmail_hash_items_item_instance.to_dict()
# create an instance of GetKillmailsKillmailIdKillmailHashItemsItem from a dict
get_killmails_killmail_id_killmail_hash_items_item_form_dict = get_killmails_killmail_id_killmail_hash_items_item.from_dict(get_killmails_killmail_id_killmail_hash_items_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


