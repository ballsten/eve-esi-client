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

from esi_client.models.get_fw_leaderboards_corporations_victory_points import GetFwLeaderboardsCorporationsVictoryPoints

class TestGetFwLeaderboardsCorporationsVictoryPoints(unittest.TestCase):
    """GetFwLeaderboardsCorporationsVictoryPoints unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetFwLeaderboardsCorporationsVictoryPoints:
        """Test GetFwLeaderboardsCorporationsVictoryPoints
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetFwLeaderboardsCorporationsVictoryPoints`
        """
        model = GetFwLeaderboardsCorporationsVictoryPoints()
        if include_optional:
            return GetFwLeaderboardsCorporationsVictoryPoints(
                active_total = [
                    esi_client.models.get_fw_leaderboards_corporations_active_total_active_total_1.get_fw_leaderboards_corporations_active_total_active_total_1(
                        amount = 56, 
                        corporation_id = 56, )
                    ],
                last_week = [
                    esi_client.models.get_fw_leaderboards_corporations_last_week_last_week_1.get_fw_leaderboards_corporations_last_week_last_week_1(
                        amount = 56, 
                        corporation_id = 56, )
                    ],
                yesterday = [
                    esi_client.models.get_fw_leaderboards_corporations_yesterday_yesterday_1.get_fw_leaderboards_corporations_yesterday_yesterday_1(
                        amount = 56, 
                        corporation_id = 56, )
                    ]
            )
        else:
            return GetFwLeaderboardsCorporationsVictoryPoints(
                active_total = [
                    esi_client.models.get_fw_leaderboards_corporations_active_total_active_total_1.get_fw_leaderboards_corporations_active_total_active_total_1(
                        amount = 56, 
                        corporation_id = 56, )
                    ],
                last_week = [
                    esi_client.models.get_fw_leaderboards_corporations_last_week_last_week_1.get_fw_leaderboards_corporations_last_week_last_week_1(
                        amount = 56, 
                        corporation_id = 56, )
                    ],
                yesterday = [
                    esi_client.models.get_fw_leaderboards_corporations_yesterday_yesterday_1.get_fw_leaderboards_corporations_yesterday_yesterday_1(
                        amount = 56, 
                        corporation_id = 56, )
                    ],
        )
        """

    def testGetFwLeaderboardsCorporationsVictoryPoints(self):
        """Test GetFwLeaderboardsCorporationsVictoryPoints"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
