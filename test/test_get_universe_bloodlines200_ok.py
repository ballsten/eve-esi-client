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

from esi_client.models.get_universe_bloodlines200_ok import GetUniverseBloodlines200Ok

class TestGetUniverseBloodlines200Ok(unittest.TestCase):
    """GetUniverseBloodlines200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUniverseBloodlines200Ok:
        """Test GetUniverseBloodlines200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUniverseBloodlines200Ok`
        """
        model = GetUniverseBloodlines200Ok()
        if include_optional:
            return GetUniverseBloodlines200Ok(
                bloodline_id = 56,
                charisma = 56,
                corporation_id = 56,
                description = '',
                intelligence = 56,
                memory = 56,
                name = '',
                perception = 56,
                race_id = 56,
                ship_type_id = 56,
                willpower = 56
            )
        else:
            return GetUniverseBloodlines200Ok(
                bloodline_id = 56,
                charisma = 56,
                corporation_id = 56,
                description = '',
                intelligence = 56,
                memory = 56,
                name = '',
                perception = 56,
                race_id = 56,
                ship_type_id = 56,
                willpower = 56,
        )
        """

    def testGetUniverseBloodlines200Ok(self):
        """Test GetUniverseBloodlines200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
