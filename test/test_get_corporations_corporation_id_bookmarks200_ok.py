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

from esi_client.models.get_corporations_corporation_id_bookmarks200_ok import GetCorporationsCorporationIdBookmarks200Ok

class TestGetCorporationsCorporationIdBookmarks200Ok(unittest.TestCase):
    """GetCorporationsCorporationIdBookmarks200Ok unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCorporationsCorporationIdBookmarks200Ok:
        """Test GetCorporationsCorporationIdBookmarks200Ok
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCorporationsCorporationIdBookmarks200Ok`
        """
        model = GetCorporationsCorporationIdBookmarks200Ok()
        if include_optional:
            return GetCorporationsCorporationIdBookmarks200Ok(
                bookmark_id = 56,
                coordinates = esi_client.models.get_corporations_corporation_id_bookmarks_coordinates.get_corporations_corporation_id_bookmarks_coordinates(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                creator_id = 56,
                folder_id = 56,
                item = esi_client.models.get_corporations_corporation_id_bookmarks_item.get_corporations_corporation_id_bookmarks_item(
                    item_id = 56, 
                    type_id = 56, ),
                label = '',
                location_id = 56,
                notes = ''
            )
        else:
            return GetCorporationsCorporationIdBookmarks200Ok(
                bookmark_id = 56,
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                creator_id = 56,
                label = '',
                location_id = 56,
                notes = '',
        )
        """

    def testGetCorporationsCorporationIdBookmarks200Ok(self):
        """Test GetCorporationsCorporationIdBookmarks200Ok"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
