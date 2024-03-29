# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    The version of the OpenAPI document: 1.19
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from esi_client.api.planetary_interaction_api import PlanetaryInteractionApi


class TestPlanetaryInteractionApi(unittest.TestCase):
    """PlanetaryInteractionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlanetaryInteractionApi()

    def tearDown(self) -> None:
        pass

    def test_get_characters_character_id_planets(self) -> None:
        """Test case for get_characters_character_id_planets

        Get colonies
        """
        pass

    def test_get_characters_character_id_planets_planet_id(self) -> None:
        """Test case for get_characters_character_id_planets_planet_id

        Get colony layout
        """
        pass

    def test_get_corporations_corporation_id_customs_offices(self) -> None:
        """Test case for get_corporations_corporation_id_customs_offices

        List corporation customs offices
        """
        pass

    def test_get_universe_schematics_schematic_id(self) -> None:
        """Test case for get_universe_schematics_schematic_id

        Get schematic information
        """
        pass


if __name__ == '__main__':
    unittest.main()
