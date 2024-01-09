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

from esi_client.models.get_fw_leaderboards_last_week_last_week1 import GetFwLeaderboardsLastWeekLastWeek1

class TestGetFwLeaderboardsLastWeekLastWeek1(unittest.TestCase):
    """GetFwLeaderboardsLastWeekLastWeek1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetFwLeaderboardsLastWeekLastWeek1:
        """Test GetFwLeaderboardsLastWeekLastWeek1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetFwLeaderboardsLastWeekLastWeek1`
        """
        model = GetFwLeaderboardsLastWeekLastWeek1()
        if include_optional:
            return GetFwLeaderboardsLastWeekLastWeek1(
                amount = 56,
                faction_id = 56
            )
        else:
            return GetFwLeaderboardsLastWeekLastWeek1(
        )
        """

    def testGetFwLeaderboardsLastWeekLastWeek1(self):
        """Test GetFwLeaderboardsLastWeekLastWeek1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
