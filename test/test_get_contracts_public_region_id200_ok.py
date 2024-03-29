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

from esi_client.models.get_contracts_public_region_id200_ok import GetContractsPublicRegionId200Ok

class TestGetContractsPublicRegionId200Ok(unittest.TestCase):
    """GetContractsPublicRegionId200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetContractsPublicRegionId200Ok:
        """Test GetContractsPublicRegionId200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetContractsPublicRegionId200Ok`
        """
        model = GetContractsPublicRegionId200Ok()
        if include_optional:
            return GetContractsPublicRegionId200Ok(
                buyout = 1.337,
                collateral = 1.337,
                contract_id = 56,
                date_expired = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                date_issued = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                days_to_complete = 56,
                end_location_id = 56,
                for_corporation = True,
                issuer_corporation_id = 56,
                issuer_id = 56,
                price = 1.337,
                reward = 1.337,
                start_location_id = 56,
                title = '',
                type = 'unknown',
                volume = 1.337
            )
        else:
            return GetContractsPublicRegionId200Ok(
                contract_id = 56,
                date_expired = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                date_issued = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                issuer_corporation_id = 56,
                issuer_id = 56,
                type = 'unknown',
        )
        """

    def testGetContractsPublicRegionId200Ok(self):
        """Test GetContractsPublicRegionId200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
