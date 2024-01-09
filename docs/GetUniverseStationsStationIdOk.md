# GetUniverseStationsStationIdOk

200 ok object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_dockable_ship_volume** | **float** | max_dockable_ship_volume number | 
**name** | **str** | name string | 
**office_rental_cost** | **float** | office_rental_cost number | 
**owner** | **int** | ID of the corporation that controls this station | [optional] 
**position** | [**GetUniverseStationsStationIdPosition**](GetUniverseStationsStationIdPosition.md) |  | 
**race_id** | **int** | race_id integer | [optional] 
**reprocessing_efficiency** | **float** | reprocessing_efficiency number | 
**reprocessing_stations_take** | **float** | reprocessing_stations_take number | 
**services** | **List[str]** | services array | 
**station_id** | **int** | station_id integer | 
**system_id** | **int** | The solar system this station is in | 
**type_id** | **int** | type_id integer | 

## Example

```python
from esi_client.models.get_universe_stations_station_id_ok import GetUniverseStationsStationIdOk

# TODO update the JSON string below
json = "{}"
# create an instance of GetUniverseStationsStationIdOk from a JSON string
get_universe_stations_station_id_ok_instance = GetUniverseStationsStationIdOk.from_json(json)
# print the JSON string representation of the object
print GetUniverseStationsStationIdOk.to_json()

# convert the object into a dict
get_universe_stations_station_id_ok_dict = get_universe_stations_station_id_ok_instance.to_dict()
# create an instance of GetUniverseStationsStationIdOk from a dict
get_universe_stations_station_id_ok_form_dict = get_universe_stations_station_id_ok.from_dict(get_universe_stations_station_id_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


