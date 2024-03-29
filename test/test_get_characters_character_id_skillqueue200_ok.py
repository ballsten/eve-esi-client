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

from esi_client.models.get_characters_character_id_skillqueue200_ok import GetCharactersCharacterIdSkillqueue200Ok

class TestGetCharactersCharacterIdSkillqueue200Ok(unittest.TestCase):
    """GetCharactersCharacterIdSkillqueue200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCharactersCharacterIdSkillqueue200Ok:
        """Test GetCharactersCharacterIdSkillqueue200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCharactersCharacterIdSkillqueue200Ok`
        """
        model = GetCharactersCharacterIdSkillqueue200Ok()
        if include_optional:
            return GetCharactersCharacterIdSkillqueue200Ok(
                finish_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                finished_level = 0,
                level_end_sp = 56,
                level_start_sp = 56,
                queue_position = 56,
                skill_id = 56,
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                training_start_sp = 56
            )
        else:
            return GetCharactersCharacterIdSkillqueue200Ok(
                finished_level = 0,
                queue_position = 56,
                skill_id = 56,
        )
        """

    def testGetCharactersCharacterIdSkillqueue200Ok(self):
        """Test GetCharactersCharacterIdSkillqueue200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
