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

from esi_client.models.get_fw_stats200_ok import GetFwStats200Ok

class TestGetFwStats200Ok(unittest.TestCase):
    """GetFwStats200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetFwStats200Ok:
        """Test GetFwStats200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetFwStats200Ok`
        """
        model = GetFwStats200Ok()
        if include_optional:
            return GetFwStats200Ok(
                faction_id = 56,
                kills = esi_client.models.get_fw_stats_kills.get_fw_stats_kills(
                    last_week = 56, 
                    total = 56, 
                    yesterday = 56, ),
                pilots = 56,
                systems_controlled = 56,
                victory_points = esi_client.models.get_fw_stats_victory_points.get_fw_stats_victory_points(
                    last_week = 56, 
                    total = 56, 
                    yesterday = 56, )
            )
        else:
            return GetFwStats200Ok(
                faction_id = 56,
                kills = esi_client.models.get_fw_stats_kills.get_fw_stats_kills(
                    last_week = 56, 
                    total = 56, 
                    yesterday = 56, ),
                pilots = 56,
                systems_controlled = 56,
                victory_points = esi_client.models.get_fw_stats_victory_points.get_fw_stats_victory_points(
                    last_week = 56, 
                    total = 56, 
                    yesterday = 56, ),
        )
        """

    def testGetFwStats200Ok(self):
        """Test GetFwStats200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
