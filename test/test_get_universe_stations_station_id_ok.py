# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    The version of the OpenAPI document: 1.19
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from esi_client.models.get_universe_stations_station_id_ok import GetUniverseStationsStationIdOk

class TestGetUniverseStationsStationIdOk(unittest.TestCase):
    """GetUniverseStationsStationIdOk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUniverseStationsStationIdOk:
        """Test GetUniverseStationsStationIdOk
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUniverseStationsStationIdOk`
        """
        model = GetUniverseStationsStationIdOk()
        if include_optional:
            return GetUniverseStationsStationIdOk(
                max_dockable_ship_volume = 1.337,
                name = '',
                office_rental_cost = 1.337,
                owner = 56,
                position = esi_client.models.get_universe_stations_station_id_position.get_universe_stations_station_id_position(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
                race_id = 56,
                reprocessing_efficiency = 1.337,
                reprocessing_stations_take = 1.337,
                services = [
                    'bounty-missions'
                    ],
                station_id = 56,
                system_id = 56,
                type_id = 56
            )
        else:
            return GetUniverseStationsStationIdOk(
                max_dockable_ship_volume = 1.337,
                name = '',
                office_rental_cost = 1.337,
                position = esi_client.models.get_universe_stations_station_id_position.get_universe_stations_station_id_position(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
                reprocessing_efficiency = 1.337,
                reprocessing_stations_take = 1.337,
                services = [
                    'bounty-missions'
                    ],
                station_id = 56,
                system_id = 56,
                type_id = 56,
        )
        """

    def testGetUniverseStationsStationIdOk(self):
        """Test GetUniverseStationsStationIdOk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
