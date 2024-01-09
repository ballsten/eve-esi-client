# GetCorporationsCorporationIdAssets200Ok

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_blueprint_copy** | **bool** | is_blueprint_copy boolean | [optional] 
**is_singleton** | **bool** | is_singleton boolean | 
**item_id** | **int** | item_id integer | 
**location_flag** | **str** | location_flag string | 
**location_id** | **int** | location_id integer | 
**location_type** | **str** | location_type string | 
**quantity** | **int** | quantity integer | 
**type_id** | **int** | type_id integer | 

## Example

```python
from esi_client.models.get_corporations_corporation_id_assets200_ok import GetCorporationsCorporationIdAssets200Ok

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdAssets200Ok from a JSON string
get_corporations_corporation_id_assets200_ok_instance = GetCorporationsCorporationIdAssets200Ok.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdAssets200Ok.to_json()

# convert the object into a dict
get_corporations_corporation_id_assets200_ok_dict = get_corporations_corporation_id_assets200_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdAssets200Ok from a dict
get_corporations_corporation_id_assets200_ok_form_dict = get_corporations_corporation_id_assets200_ok.from_dict(get_corporations_corporation_id_assets200_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


