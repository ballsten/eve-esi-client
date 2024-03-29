# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    The version of the OpenAPI document: 1.19
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from esi_client.api.loyalty_api import LoyaltyApi


class TestLoyaltyApi(unittest.TestCase):
    """LoyaltyApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LoyaltyApi()

    def tearDown(self) -> None:
        pass

    def test_get_characters_character_id_loyalty_points(self) -> None:
        """Test case for get_characters_character_id_loyalty_points

        Get loyalty points
        """
        pass

    def test_get_loyalty_stores_corporation_id_offers(self) -> None:
        """Test case for get_loyalty_stores_corporation_id_offers

        List loyalty store offers
        """
        pass


if __name__ == '__main__':
    unittest.main()
