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

from esi_client.models.get_corporations_corporation_id_blueprints200_ok import GetCorporationsCorporationIdBlueprints200Ok

class TestGetCorporationsCorporationIdBlueprints200Ok(unittest.TestCase):
    """GetCorporationsCorporationIdBlueprints200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCorporationsCorporationIdBlueprints200Ok:
        """Test GetCorporationsCorporationIdBlueprints200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCorporationsCorporationIdBlueprints200Ok`
        """
        model = GetCorporationsCorporationIdBlueprints200Ok()
        if include_optional:
            return GetCorporationsCorporationIdBlueprints200Ok(
                item_id = 56,
                location_flag = 'AssetSafety',
                location_id = 56,
                material_efficiency = 0,
                quantity = -2,
                runs = -1,
                time_efficiency = 0,
                type_id = 56
            )
        else:
            return GetCorporationsCorporationIdBlueprints200Ok(
                item_id = 56,
                location_flag = 'AssetSafety',
                location_id = 56,
                material_efficiency = 0,
                quantity = -2,
                runs = -1,
                time_efficiency = 0,
                type_id = 56,
        )
        """

    def testGetCorporationsCorporationIdBlueprints200Ok(self):
        """Test GetCorporationsCorporationIdBlueprints200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
