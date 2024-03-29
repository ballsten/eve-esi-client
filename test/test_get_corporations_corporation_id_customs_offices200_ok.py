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

from esi_client.models.get_corporations_corporation_id_customs_offices200_ok import GetCorporationsCorporationIdCustomsOffices200Ok

class TestGetCorporationsCorporationIdCustomsOffices200Ok(unittest.TestCase):
    """GetCorporationsCorporationIdCustomsOffices200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCorporationsCorporationIdCustomsOffices200Ok:
        """Test GetCorporationsCorporationIdCustomsOffices200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCorporationsCorporationIdCustomsOffices200Ok`
        """
        model = GetCorporationsCorporationIdCustomsOffices200Ok()
        if include_optional:
            return GetCorporationsCorporationIdCustomsOffices200Ok(
                alliance_tax_rate = 1.337,
                allow_access_with_standings = True,
                allow_alliance_access = True,
                bad_standing_tax_rate = 1.337,
                corporation_tax_rate = 1.337,
                excellent_standing_tax_rate = 1.337,
                good_standing_tax_rate = 1.337,
                neutral_standing_tax_rate = 1.337,
                office_id = 56,
                reinforce_exit_end = 0,
                reinforce_exit_start = 0,
                standing_level = 'bad',
                system_id = 56,
                terrible_standing_tax_rate = 1.337
            )
        else:
            return GetCorporationsCorporationIdCustomsOffices200Ok(
                allow_access_with_standings = True,
                allow_alliance_access = True,
                office_id = 56,
                reinforce_exit_end = 0,
                reinforce_exit_start = 0,
                system_id = 56,
        )
        """

    def testGetCorporationsCorporationIdCustomsOffices200Ok(self):
        """Test GetCorporationsCorporationIdCustomsOffices200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
