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

from esi_client.models.get_characters_character_id_contracts_contract_id_bids200_ok import GetCharactersCharacterIdContractsContractIdBids200Ok

class TestGetCharactersCharacterIdContractsContractIdBids200Ok(unittest.TestCase):
    """GetCharactersCharacterIdContractsContractIdBids200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCharactersCharacterIdContractsContractIdBids200Ok:
        """Test GetCharactersCharacterIdContractsContractIdBids200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCharactersCharacterIdContractsContractIdBids200Ok`
        """
        model = GetCharactersCharacterIdContractsContractIdBids200Ok()
        if include_optional:
            return GetCharactersCharacterIdContractsContractIdBids200Ok(
                amount = 1.337,
                bid_id = 56,
                bidder_id = 56,
                date_bid = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GetCharactersCharacterIdContractsContractIdBids200Ok(
                amount = 1.337,
                bid_id = 56,
                bidder_id = 56,
                date_bid = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testGetCharactersCharacterIdContractsContractIdBids200Ok(self):
        """Test GetCharactersCharacterIdContractsContractIdBids200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
