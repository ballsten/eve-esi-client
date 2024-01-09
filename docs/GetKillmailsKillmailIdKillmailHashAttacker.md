# GetKillmailsKillmailIdKillmailHashAttacker

attacker object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alliance_id** | **int** | alliance_id integer | [optional] 
**character_id** | **int** | character_id integer | [optional] 
**corporation_id** | **int** | corporation_id integer | [optional] 
**damage_done** | **int** | damage_done integer | 
**faction_id** | **int** | faction_id integer | [optional] 
**final_blow** | **bool** | Was the attacker the one to achieve the final blow  | 
**security_status** | **float** | Security status for the attacker  | 
**ship_type_id** | **int** | What ship was the attacker flying  | [optional] 
**weapon_type_id** | **int** | What weapon was used by the attacker for the kill  | [optional] 

## Example

```python
from esi_client.models.get_killmails_killmail_id_killmail_hash_attacker import GetKillmailsKillmailIdKillmailHashAttacker

# TODO update the JSON string below
json = "{}"
# create an instance of GetKillmailsKillmailIdKillmailHashAttacker from a JSON string
get_killmails_killmail_id_killmail_hash_attacker_instance = GetKillmailsKillmailIdKillmailHashAttacker.from_json(json)
# print the JSON string representation of the object
print GetKillmailsKillmailIdKillmailHashAttacker.to_json()

# convert the object into a dict
get_killmails_killmail_id_killmail_hash_attacker_dict = get_killmails_killmail_id_killmail_hash_attacker_instance.to_dict()
# create an instance of GetKillmailsKillmailIdKillmailHashAttacker from a dict
get_killmails_killmail_id_killmail_hash_attacker_form_dict = get_killmails_killmail_id_killmail_hash_attacker.from_dict(get_killmails_killmail_id_killmail_hash_attacker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


