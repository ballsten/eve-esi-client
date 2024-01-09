# GetKillmailsKillmailIdKillmailHashVictim

victim object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alliance_id** | **int** | alliance_id integer | [optional] 
**character_id** | **int** | character_id integer | [optional] 
**corporation_id** | **int** | corporation_id integer | [optional] 
**damage_taken** | **int** | How much total damage was taken by the victim  | 
**faction_id** | **int** | faction_id integer | [optional] 
**items** | [**List[GetKillmailsKillmailIdKillmailHashItem]**](GetKillmailsKillmailIdKillmailHashItem.md) | items array | [optional] 
**position** | [**GetKillmailsKillmailIdKillmailHashPosition**](GetKillmailsKillmailIdKillmailHashPosition.md) |  | [optional] 
**ship_type_id** | **int** | The ship that the victim was piloting and was destroyed  | 

## Example

```python
from esi_client.models.get_killmails_killmail_id_killmail_hash_victim import GetKillmailsKillmailIdKillmailHashVictim

# TODO update the JSON string below
json = "{}"
# create an instance of GetKillmailsKillmailIdKillmailHashVictim from a JSON string
get_killmails_killmail_id_killmail_hash_victim_instance = GetKillmailsKillmailIdKillmailHashVictim.from_json(json)
# print the JSON string representation of the object
print GetKillmailsKillmailIdKillmailHashVictim.to_json()

# convert the object into a dict
get_killmails_killmail_id_killmail_hash_victim_dict = get_killmails_killmail_id_killmail_hash_victim_instance.to_dict()
# create an instance of GetKillmailsKillmailIdKillmailHashVictim from a dict
get_killmails_killmail_id_killmail_hash_victim_form_dict = get_killmails_killmail_id_killmail_hash_victim.from_dict(get_killmails_killmail_id_killmail_hash_victim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


