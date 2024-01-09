# GetCharactersCharacterIdContacts200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **int** | contact_id integer | 
**contact_type** | **str** | contact_type string | 
**is_blocked** | **bool** | Whether this contact is in the blocked list. Note a missing value denotes unknown, not true or false | [optional] 
**is_watched** | **bool** | Whether this contact is being watched | [optional] 
**label_ids** | **List[int]** | label_ids array | [optional] 
**standing** | **float** | Standing of the contact | 

## Example

```python
from esi_client.models.get_characters_character_id_contacts200_ok import GetCharactersCharacterIdContacts200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharactersCharacterIdContacts200Ok from a JSON string
get_characters_character_id_contacts200_ok_instance = GetCharactersCharacterIdContacts200Ok.from_json(json)
# print the JSON string representation of the object
print GetCharactersCharacterIdContacts200Ok.to_json()

# convert the object into a dict
get_characters_character_id_contacts200_ok_dict = get_characters_character_id_contacts200_ok_instance.to_dict()
# create an instance of GetCharactersCharacterIdContacts200Ok from a dict
get_characters_character_id_contacts200_ok_form_dict = get_characters_character_id_contacts200_ok.from_dict(get_characters_character_id_contacts200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


