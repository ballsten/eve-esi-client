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

from esi_client.models.get_universe_constellations_constellation_id_position import GetUniverseConstellationsConstellationIdPosition

class TestGetUniverseConstellationsConstellationIdPosition(unittest.TestCase):
    """GetUniverseConstellationsConstellationIdPosition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUniverseConstellationsConstellationIdPosition:
        """Test GetUniverseConstellationsConstellationIdPosition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUniverseConstellationsConstellationIdPosition`
        """
        model = GetUniverseConstellationsConstellationIdPosition()
        if include_optional:
            return GetUniverseConstellationsConstellationIdPosition(
                x = 1.337,
                y = 1.337,
                z = 1.337
            )
        else:
            return GetUniverseConstellationsConstellationIdPosition(
                x = 1.337,
                y = 1.337,
                z = 1.337,
        )
        """

    def testGetUniverseConstellationsConstellationIdPosition(self):
        """Test GetUniverseConstellationsConstellationIdPosition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
