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

from esi_client.models.get_characters_character_id_agents_research200_ok import GetCharactersCharacterIdAgentsResearch200Ok

class TestGetCharactersCharacterIdAgentsResearch200Ok(unittest.TestCase):
    """GetCharactersCharacterIdAgentsResearch200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCharactersCharacterIdAgentsResearch200Ok:
        """Test GetCharactersCharacterIdAgentsResearch200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCharactersCharacterIdAgentsResearch200Ok`
        """
        model = GetCharactersCharacterIdAgentsResearch200Ok()
        if include_optional:
            return GetCharactersCharacterIdAgentsResearch200Ok(
                agent_id = 56,
                points_per_day = 1.337,
                remainder_points = 1.337,
                skill_type_id = 56,
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GetCharactersCharacterIdAgentsResearch200Ok(
                agent_id = 56,
                points_per_day = 1.337,
                remainder_points = 1.337,
                skill_type_id = 56,
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testGetCharactersCharacterIdAgentsResearch200Ok(self):
        """Test GetCharactersCharacterIdAgentsResearch200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
