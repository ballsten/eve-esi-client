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

from esi_client.models.get_characters_character_id_fatigue_ok import GetCharactersCharacterIdFatigueOk

class TestGetCharactersCharacterIdFatigueOk(unittest.TestCase):
    """GetCharactersCharacterIdFatigueOk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCharactersCharacterIdFatigueOk:
        """Test GetCharactersCharacterIdFatigueOk
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCharactersCharacterIdFatigueOk`
        """
        model = GetCharactersCharacterIdFatigueOk()
        if include_optional:
            return GetCharactersCharacterIdFatigueOk(
                jump_fatigue_expire_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_jump_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GetCharactersCharacterIdFatigueOk(
        )
        """

    def testGetCharactersCharacterIdFatigueOk(self):
        """Test GetCharactersCharacterIdFatigueOk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
