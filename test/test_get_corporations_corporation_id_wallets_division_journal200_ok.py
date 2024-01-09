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

from esi_client.models.get_corporations_corporation_id_wallets_division_journal200_ok import GetCorporationsCorporationIdWalletsDivisionJournal200Ok

class TestGetCorporationsCorporationIdWalletsDivisionJournal200Ok(unittest.TestCase):
    """GetCorporationsCorporationIdWalletsDivisionJournal200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCorporationsCorporationIdWalletsDivisionJournal200Ok:
        """Test GetCorporationsCorporationIdWalletsDivisionJournal200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCorporationsCorporationIdWalletsDivisionJournal200Ok`
        """
        model = GetCorporationsCorporationIdWalletsDivisionJournal200Ok()
        if include_optional:
            return GetCorporationsCorporationIdWalletsDivisionJournal200Ok(
                amount = 1.337,
                balance = 1.337,
                context_id = 56,
                context_id_type = 'structure_id',
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = '',
                first_party_id = 56,
                id = 56,
                reason = '',
                ref_type = 'acceleration_gate_fee',
                second_party_id = 56,
                tax = 1.337,
                tax_receiver_id = 56
            )
        else:
            return GetCorporationsCorporationIdWalletsDivisionJournal200Ok(
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = '',
                id = 56,
                ref_type = 'acceleration_gate_fee',
        )
        """

    def testGetCorporationsCorporationIdWalletsDivisionJournal200Ok(self):
        """Test GetCorporationsCorporationIdWalletsDivisionJournal200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
