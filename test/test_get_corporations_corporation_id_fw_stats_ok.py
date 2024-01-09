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

from esi_client.models.get_corporations_corporation_id_fw_stats_ok import GetCorporationsCorporationIdFwStatsOk

class TestGetCorporationsCorporationIdFwStatsOk(unittest.TestCase):
    """GetCorporationsCorporationIdFwStatsOk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCorporationsCorporationIdFwStatsOk:
        """Test GetCorporationsCorporationIdFwStatsOk
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCorporationsCorporationIdFwStatsOk`
        """
        model = GetCorporationsCorporationIdFwStatsOk()
        if include_optional:
            return GetCorporationsCorporationIdFwStatsOk(
                enlisted_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                faction_id = 56,
                kills = esi_client.models.get_corporations_corporation_id_fw_stats_kills.get_corporations_corporation_id_fw_stats_kills(
                    last_week = 56, 
                    total = 56, 
                    yesterday = 56, ),
                pilots = 56,
                victory_points = esi_client.models.get_corporations_corporation_id_fw_stats_victory_points.get_corporations_corporation_id_fw_stats_victory_points(
                    last_week = 56, 
                    total = 56, 
                    yesterday = 56, )
            )
        else:
            return GetCorporationsCorporationIdFwStatsOk(
                kills = esi_client.models.get_corporations_corporation_id_fw_stats_kills.get_corporations_corporation_id_fw_stats_kills(
                    last_week = 56, 
                    total = 56, 
                    yesterday = 56, ),
                victory_points = esi_client.models.get_corporations_corporation_id_fw_stats_victory_points.get_corporations_corporation_id_fw_stats_victory_points(
                    last_week = 56, 
                    total = 56, 
                    yesterday = 56, ),
        )
        """

    def testGetCorporationsCorporationIdFwStatsOk(self):
        """Test GetCorporationsCorporationIdFwStatsOk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
