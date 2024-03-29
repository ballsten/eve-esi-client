# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    The version of the OpenAPI document: 1.19
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from esi_client.api.fittings_api import FittingsApi


class TestFittingsApi(unittest.TestCase):
    """FittingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FittingsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_characters_character_id_fittings_fitting_id(self) -> None:
        """Test case for delete_characters_character_id_fittings_fitting_id

        Delete fitting
        """
        pass

    def test_get_characters_character_id_fittings(self) -> None:
        """Test case for get_characters_character_id_fittings

        Get fittings
        """
        pass

    def test_post_characters_character_id_fittings(self) -> None:
        """Test case for post_characters_character_id_fittings

        Create fitting
        """
        pass


if __name__ == '__main__':
    unittest.main()
