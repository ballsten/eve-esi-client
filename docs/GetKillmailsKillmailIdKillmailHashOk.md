# GetKillmailsKillmailIdKillmailHashOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attackers** | [**List[GetKillmailsKillmailIdKillmailHashAttacker]**](GetKillmailsKillmailIdKillmailHashAttacker.md) | attackers array | 
**killmail_id** | **int** | ID of the killmail | 
**killmail_time** | **datetime** | Time that the victim was killed and the killmail generated  | 
**moon_id** | **int** | Moon if the kill took place at one | [optional] 
**solar_system_id** | **int** | Solar system that the kill took place in  | 
**victim** | [**GetKillmailsKillmailIdKillmailHashVictim**](GetKillmailsKillmailIdKillmailHashVictim.md) |  | 
**war_id** | **int** | War if the killmail is generated in relation to an official war  | [optional] 

## Example

```python
from esi_client.models.get_killmails_killmail_id_killmail_hash_ok import GetKillmailsKillmailIdKillmailHashOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetKillmailsKillmailIdKillmailHashOk from a JSON string
get_killmails_killmail_id_killmail_hash_ok_instance = GetKillmailsKillmailIdKillmailHashOk.from_json(json)
# print the JSON string representation of the object
print GetKillmailsKillmailIdKillmailHashOk.to_json()

# convert the object into a dict
get_killmails_killmail_id_killmail_hash_ok_dict = get_killmails_killmail_id_killmail_hash_ok_instance.to_dict()
# create an instance of GetKillmailsKillmailIdKillmailHashOk from a dict
get_killmails_killmail_id_killmail_hash_ok_form_dict = get_killmails_killmail_id_killmail_hash_ok.from_dict(get_killmails_killmail_id_killmail_hash_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


