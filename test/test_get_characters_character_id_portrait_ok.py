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

from esi_client.models.get_characters_character_id_portrait_ok import GetCharactersCharacterIdPortraitOk

class TestGetCharactersCharacterIdPortraitOk(unittest.TestCase):
    """GetCharactersCharacterIdPortraitOk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCharactersCharacterIdPortraitOk:
        """Test GetCharactersCharacterIdPortraitOk
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCharactersCharacterIdPortraitOk`
        """
        model = GetCharactersCharacterIdPortraitOk()
        if include_optional:
            return GetCharactersCharacterIdPortraitOk(
                px128x128 = '',
                px256x256 = '',
                px512x512 = '',
                px64x64 = ''
            )
        else:
            return GetCharactersCharacterIdPortraitOk(
        )
        """

    def testGetCharactersCharacterIdPortraitOk(self):
        """Test GetCharactersCharacterIdPortraitOk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
