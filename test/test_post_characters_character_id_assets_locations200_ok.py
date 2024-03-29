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

from esi_client.models.post_characters_character_id_assets_locations200_ok import PostCharactersCharacterIdAssetsLocations200Ok

class TestPostCharactersCharacterIdAssetsLocations200Ok(unittest.TestCase):
    """PostCharactersCharacterIdAssetsLocations200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostCharactersCharacterIdAssetsLocations200Ok:
        """Test PostCharactersCharacterIdAssetsLocations200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostCharactersCharacterIdAssetsLocations200Ok`
        """
        model = PostCharactersCharacterIdAssetsLocations200Ok()
        if include_optional:
            return PostCharactersCharacterIdAssetsLocations200Ok(
                item_id = 56,
                position = esi_client.models.post_characters_character_id_assets_locations_position.post_characters_character_id_assets_locations_position(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, )
            )
        else:
            return PostCharactersCharacterIdAssetsLocations200Ok(
                item_id = 56,
                position = esi_client.models.post_characters_character_id_assets_locations_position.post_characters_character_id_assets_locations_position(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
        )
        """

    def testPostCharactersCharacterIdAssetsLocations200Ok(self):
        """Test PostCharactersCharacterIdAssetsLocations200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
