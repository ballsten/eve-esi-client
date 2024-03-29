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

from esi_client.models.get_alliances_alliance_id_contacts200_ok import GetAlliancesAllianceIdContacts200Ok

class TestGetAlliancesAllianceIdContacts200Ok(unittest.TestCase):
    """GetAlliancesAllianceIdContacts200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAlliancesAllianceIdContacts200Ok:
        """Test GetAlliancesAllianceIdContacts200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAlliancesAllianceIdContacts200Ok`
        """
        model = GetAlliancesAllianceIdContacts200Ok()
        if include_optional:
            return GetAlliancesAllianceIdContacts200Ok(
                contact_id = 56,
                contact_type = 'character',
                label_ids = [
                    56
                    ],
                standing = 1.337
            )
        else:
            return GetAlliancesAllianceIdContacts200Ok(
                contact_id = 56,
                contact_type = 'character',
                standing = 1.337,
        )
        """

    def testGetAlliancesAllianceIdContacts200Ok(self):
        """Test GetAlliancesAllianceIdContacts200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
