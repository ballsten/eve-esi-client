# PostCharactersAffiliation200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alliance_id** | **int** | The character&#39;s alliance ID, if their corporation is in an alliance | [optional] 
**character_id** | **int** | The character&#39;s ID | 
**corporation_id** | **int** | The character&#39;s corporation ID | 
**faction_id** | **int** | The character&#39;s faction ID, if their corporation is in a faction | [optional] 

## Example

```python
from esi_client.models.post_characters_affiliation200_ok import PostCharactersAffiliation200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of PostCharactersAffiliation200Ok from a JSON string
post_characters_affiliation200_ok_instance = PostCharactersAffiliation200Ok.from_json(json)
# print the JSON string representation of the object
print PostCharactersAffiliation200Ok.to_json()

# convert the object into a dict
post_characters_affiliation200_ok_dict = post_characters_affiliation200_ok_instance.to_dict()
# create an instance of PostCharactersAffiliation200Ok from a dict
post_characters_affiliation200_ok_form_dict = post_characters_affiliation200_ok.from_dict(post_characters_affiliation200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


