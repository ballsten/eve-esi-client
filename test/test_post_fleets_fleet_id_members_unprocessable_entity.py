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

from esi_client.models.post_fleets_fleet_id_members_unprocessable_entity import PostFleetsFleetIdMembersUnprocessableEntity

class TestPostFleetsFleetIdMembersUnprocessableEntity(unittest.TestCase):
    """PostFleetsFleetIdMembersUnprocessableEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostFleetsFleetIdMembersUnprocessableEntity:
        """Test PostFleetsFleetIdMembersUnprocessableEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostFleetsFleetIdMembersUnprocessableEntity`
        """
        model = PostFleetsFleetIdMembersUnprocessableEntity()
        if include_optional:
            return PostFleetsFleetIdMembersUnprocessableEntity(
                error = ''
            )
        else:
            return PostFleetsFleetIdMembersUnprocessableEntity(
        )
        """

    def testPostFleetsFleetIdMembersUnprocessableEntity(self):
        """Test PostFleetsFleetIdMembersUnprocessableEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
