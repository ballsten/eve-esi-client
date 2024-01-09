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

from esi_client.models.get_fw_leaderboards_characters_last_week_last_week import GetFwLeaderboardsCharactersLastWeekLastWeek

class TestGetFwLeaderboardsCharactersLastWeekLastWeek(unittest.TestCase):
    """GetFwLeaderboardsCharactersLastWeekLastWeek unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetFwLeaderboardsCharactersLastWeekLastWeek:
        """Test GetFwLeaderboardsCharactersLastWeekLastWeek
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetFwLeaderboardsCharactersLastWeekLastWeek`
        """
        model = GetFwLeaderboardsCharactersLastWeekLastWeek()
        if include_optional:
            return GetFwLeaderboardsCharactersLastWeekLastWeek(
                amount = 56,
                character_id = 56
            )
        else:
            return GetFwLeaderboardsCharactersLastWeekLastWeek(
        )
        """

    def testGetFwLeaderboardsCharactersLastWeekLastWeek(self):
        """Test GetFwLeaderboardsCharactersLastWeekLastWeek"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
