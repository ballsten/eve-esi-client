# GetCorporationsCorporationIdStarbasesStarbaseIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_alliance_members** | **bool** | allow_alliance_members boolean | 
**allow_corporation_members** | **bool** | allow_corporation_members boolean | 
**anchor** | **str** | Who can anchor starbase (POS) and its structures | 
**attack_if_at_war** | **bool** | attack_if_at_war boolean | 
**attack_if_other_security_status_dropping** | **bool** | attack_if_other_security_status_dropping boolean | 
**attack_security_status_threshold** | **float** | Starbase (POS) will attack if target&#39;s security standing is lower than this value | [optional] 
**attack_standing_threshold** | **float** | Starbase (POS) will attack if target&#39;s standing is lower than this value | [optional] 
**fuel_bay_take** | **str** | Who can take fuel blocks out of the starbase (POS)&#39;s fuel bay | 
**fuel_bay_view** | **str** | Who can view the starbase (POS)&#39;s fule bay. Characters either need to have required role or belong to the starbase (POS) owner&#39;s corporation or alliance, as described by the enum, all other access settings follows the same scheme | 
**fuels** | [**List[GetCorporationsCorporationIdStarbasesStarbaseIdFuel]**](GetCorporationsCorporationIdStarbasesStarbaseIdFuel.md) | Fuel blocks and other things that will be consumed when operating a starbase (POS) | [optional] 
**offline** | **str** | Who can offline starbase (POS) and its structures | 
**online** | **str** | Who can online starbase (POS) and its structures | 
**unanchor** | **str** | Who can unanchor starbase (POS) and its structures | 
**use_alliance_standings** | **bool** | True if the starbase (POS) is using alliance standings, otherwise using corporation&#39;s | 

## Example

```python
from esi_client.models.get_corporations_corporation_id_starbases_starbase_id_ok import GetCorporationsCorporationIdStarbasesStarbaseIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetCorporationsCorporationIdStarbasesStarbaseIdOk from a JSON string
get_corporations_corporation_id_starbases_starbase_id_ok_instance = GetCorporationsCorporationIdStarbasesStarbaseIdOk.from_json(json)
# print the JSON string representation of the object
print GetCorporationsCorporationIdStarbasesStarbaseIdOk.to_json()

# convert the object into a dict
get_corporations_corporation_id_starbases_starbase_id_ok_dict = get_corporations_corporation_id_starbases_starbase_id_ok_instance.to_dict()
# create an instance of GetCorporationsCorporationIdStarbasesStarbaseIdOk from a dict
get_corporations_corporation_id_starbases_starbase_id_ok_form_dict = get_corporations_corporation_id_starbases_starbase_id_ok.from_dict(get_corporations_corporation_id_starbases_starbase_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


