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

from esi_client.models.get_universe_planets_planet_id_ok import GetUniversePlanetsPlanetIdOk

class TestGetUniversePlanetsPlanetIdOk(unittest.TestCase):
    """GetUniversePlanetsPlanetIdOk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUniversePlanetsPlanetIdOk:
        """Test GetUniversePlanetsPlanetIdOk
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUniversePlanetsPlanetIdOk`
        """
        model = GetUniversePlanetsPlanetIdOk()
        if include_optional:
            return GetUniversePlanetsPlanetIdOk(
                name = '',
                planet_id = 56,
                position = esi_client.models.get_universe_planets_planet_id_position.get_universe_planets_planet_id_position(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
                system_id = 56,
                type_id = 56
            )
        else:
            return GetUniversePlanetsPlanetIdOk(
                name = '',
                planet_id = 56,
                position = esi_client.models.get_universe_planets_planet_id_position.get_universe_planets_planet_id_position(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
                system_id = 56,
                type_id = 56,
        )
        """

    def testGetUniversePlanetsPlanetIdOk(self):
        """Test GetUniversePlanetsPlanetIdOk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
