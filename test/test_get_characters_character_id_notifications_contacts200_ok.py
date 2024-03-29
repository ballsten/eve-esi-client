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

from esi_client.models.get_characters_character_id_notifications_contacts200_ok import GetCharactersCharacterIdNotificationsContacts200Ok

class TestGetCharactersCharacterIdNotificationsContacts200Ok(unittest.TestCase):
    """GetCharactersCharacterIdNotificationsContacts200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCharactersCharacterIdNotificationsContacts200Ok:
        """Test GetCharactersCharacterIdNotificationsContacts200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCharactersCharacterIdNotificationsContacts200Ok`
        """
        model = GetCharactersCharacterIdNotificationsContacts200Ok()
        if include_optional:
            return GetCharactersCharacterIdNotificationsContacts200Ok(
                message = '',
                notification_id = 56,
                send_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sender_character_id = 56,
                standing_level = 1.337
            )
        else:
            return GetCharactersCharacterIdNotificationsContacts200Ok(
                message = '',
                notification_id = 56,
                send_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sender_character_id = 56,
                standing_level = 1.337,
        )
        """

    def testGetCharactersCharacterIdNotificationsContacts200Ok(self):
        """Test GetCharactersCharacterIdNotificationsContacts200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
