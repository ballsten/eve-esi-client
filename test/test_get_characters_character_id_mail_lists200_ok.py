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

from esi_client.models.get_characters_character_id_mail_lists200_ok import GetCharactersCharacterIdMailLists200Ok

class TestGetCharactersCharacterIdMailLists200Ok(unittest.TestCase):
    """GetCharactersCharacterIdMailLists200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCharactersCharacterIdMailLists200Ok:
        """Test GetCharactersCharacterIdMailLists200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCharactersCharacterIdMailLists200Ok`
        """
        model = GetCharactersCharacterIdMailLists200Ok()
        if include_optional:
            return GetCharactersCharacterIdMailLists200Ok(
                mailing_list_id = 56,
                name = ''
            )
        else:
            return GetCharactersCharacterIdMailLists200Ok(
                mailing_list_id = 56,
                name = '',
        )
        """

    def testGetCharactersCharacterIdMailLists200Ok(self):
        """Test GetCharactersCharacterIdMailLists200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
