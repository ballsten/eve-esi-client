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

from esi_client.models.get_corporations_corporation_id_shareholders200_ok import GetCorporationsCorporationIdShareholders200Ok

class TestGetCorporationsCorporationIdShareholders200Ok(unittest.TestCase):
    """GetCorporationsCorporationIdShareholders200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCorporationsCorporationIdShareholders200Ok:
        """Test GetCorporationsCorporationIdShareholders200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCorporationsCorporationIdShareholders200Ok`
        """
        model = GetCorporationsCorporationIdShareholders200Ok()
        if include_optional:
            return GetCorporationsCorporationIdShareholders200Ok(
                share_count = 56,
                shareholder_id = 56,
                shareholder_type = 'character'
            )
        else:
            return GetCorporationsCorporationIdShareholders200Ok(
                share_count = 56,
                shareholder_id = 56,
                shareholder_type = 'character',
        )
        """

    def testGetCorporationsCorporationIdShareholders200Ok(self):
        """Test GetCorporationsCorporationIdShareholders200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
