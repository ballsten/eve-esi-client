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

from esi_client.models.get_characters_character_id_clones_ok import GetCharactersCharacterIdClonesOk

class TestGetCharactersCharacterIdClonesOk(unittest.TestCase):
    """GetCharactersCharacterIdClonesOk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCharactersCharacterIdClonesOk:
        """Test GetCharactersCharacterIdClonesOk
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCharactersCharacterIdClonesOk`
        """
        model = GetCharactersCharacterIdClonesOk()
        if include_optional:
            return GetCharactersCharacterIdClonesOk(
                home_location = esi_client.models.get_characters_character_id_clones_home_location.get_characters_character_id_clones_home_location(
                    location_id = 56, 
                    location_type = 'station', ),
                jump_clones = [
                    esi_client.models.get_characters_character_id_clones_jump_clone.get_characters_character_id_clones_jump_clone(
                        implants = [
                            56
                            ], 
                        jump_clone_id = 56, 
                        location_id = 56, 
                        location_type = 'station', 
                        name = '', )
                    ],
                last_clone_jump_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_station_change_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GetCharactersCharacterIdClonesOk(
                jump_clones = [
                    esi_client.models.get_characters_character_id_clones_jump_clone.get_characters_character_id_clones_jump_clone(
                        implants = [
                            56
                            ], 
                        jump_clone_id = 56, 
                        location_id = 56, 
                        location_type = 'station', 
                        name = '', )
                    ],
        )
        """

    def testGetCharactersCharacterIdClonesOk(self):
        """Test GetCharactersCharacterIdClonesOk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
