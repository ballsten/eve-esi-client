# GetKillmailsKillmailIdKillmailHashItem

item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flag** | **int** | Flag for the location of the item  | 
**item_type_id** | **int** | item_type_id integer | 
**items** | [**List[GetKillmailsKillmailIdKillmailHashItemsItem]**](GetKillmailsKillmailIdKillmailHashItemsItem.md) | items array | [optional] 
**quantity_destroyed** | **int** | How many of the item were destroyed if any  | [optional] 
**quantity_dropped** | **int** | How many of the item were dropped if any  | [optional] 
**singleton** | **int** | singleton integer | 

## Example

```python
from esi_client.models.get_killmails_killmail_id_killmail_hash_item import GetKillmailsKillmailIdKillmailHashItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetKillmailsKillmailIdKillmailHashItem from a JSON string
get_killmails_killmail_id_killmail_hash_item_instance = GetKillmailsKillmailIdKillmailHashItem.from_json(json)
# print the JSON string representation of the object
print GetKillmailsKillmailIdKillmailHashItem.to_json()

# convert the object into a dict
get_killmails_killmail_id_killmail_hash_item_dict = get_killmails_killmail_id_killmail_hash_item_instance.to_dict()
# create an instance of GetKillmailsKillmailIdKillmailHashItem from a dict
get_killmails_killmail_id_killmail_hash_item_form_dict = get_killmails_killmail_id_killmail_hash_item.from_dict(get_killmails_killmail_id_killmail_hash_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


