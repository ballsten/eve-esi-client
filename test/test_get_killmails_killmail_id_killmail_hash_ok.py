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

from esi_client.models.get_killmails_killmail_id_killmail_hash_ok import GetKillmailsKillmailIdKillmailHashOk

class TestGetKillmailsKillmailIdKillmailHashOk(unittest.TestCase):
    """GetKillmailsKillmailIdKillmailHashOk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetKillmailsKillmailIdKillmailHashOk:
        """Test GetKillmailsKillmailIdKillmailHashOk
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetKillmailsKillmailIdKillmailHashOk`
        """
        model = GetKillmailsKillmailIdKillmailHashOk()
        if include_optional:
            return GetKillmailsKillmailIdKillmailHashOk(
                attackers = [
                    esi_client.models.get_killmails_killmail_id_killmail_hash_attacker.get_killmails_killmail_id_killmail_hash_attacker(
                        alliance_id = 56, 
                        character_id = 56, 
                        corporation_id = 56, 
                        damage_done = 56, 
                        faction_id = 56, 
                        final_blow = True, 
                        security_status = 1.337, 
                        ship_type_id = 56, 
                        weapon_type_id = 56, )
                    ],
                killmail_id = 56,
                killmail_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                moon_id = 56,
                solar_system_id = 56,
                victim = esi_client.models.get_killmails_killmail_id_killmail_hash_victim.get_killmails_killmail_id_killmail_hash_victim(
                    alliance_id = 56, 
                    character_id = 56, 
                    corporation_id = 56, 
                    damage_taken = 56, 
                    faction_id = 56, 
                    items = [
                        esi_client.models.get_killmails_killmail_id_killmail_hash_item.get_killmails_killmail_id_killmail_hash_item(
                            flag = 56, 
                            item_type_id = 56, 
                            items = [
                                esi_client.models.get_killmails_killmail_id_killmail_hash_items_item.get_killmails_killmail_id_killmail_hash_items_item(
                                    flag = 56, 
                                    item_type_id = 56, 
                                    quantity_destroyed = 56, 
                                    quantity_dropped = 56, 
                                    singleton = 56, )
                                ], 
                            quantity_destroyed = 56, 
                            quantity_dropped = 56, 
                            singleton = 56, )
                        ], 
                    position = esi_client.models.get_killmails_killmail_id_killmail_hash_position.get_killmails_killmail_id_killmail_hash_position(
                        x = 1.337, 
                        y = 1.337, 
                        z = 1.337, ), 
                    ship_type_id = 56, ),
                war_id = 56
            )
        else:
            return GetKillmailsKillmailIdKillmailHashOk(
                attackers = [
                    esi_client.models.get_killmails_killmail_id_killmail_hash_attacker.get_killmails_killmail_id_killmail_hash_attacker(
                        alliance_id = 56, 
                        character_id = 56, 
                        corporation_id = 56, 
                        damage_done = 56, 
                        faction_id = 56, 
                        final_blow = True, 
                        security_status = 1.337, 
                        ship_type_id = 56, 
                        weapon_type_id = 56, )
                    ],
                killmail_id = 56,
                killmail_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                solar_system_id = 56,
                victim = esi_client.models.get_killmails_killmail_id_killmail_hash_victim.get_killmails_killmail_id_killmail_hash_victim(
                    alliance_id = 56, 
                    character_id = 56, 
                    corporation_id = 56, 
                    damage_taken = 56, 
                    faction_id = 56, 
                    items = [
                        esi_client.models.get_killmails_killmail_id_killmail_hash_item.get_killmails_killmail_id_killmail_hash_item(
                            flag = 56, 
                            item_type_id = 56, 
                            items = [
                                esi_client.models.get_killmails_killmail_id_killmail_hash_items_item.get_killmails_killmail_id_killmail_hash_items_item(
                                    flag = 56, 
                                    item_type_id = 56, 
                                    quantity_destroyed = 56, 
                                    quantity_dropped = 56, 
                                    singleton = 56, )
                                ], 
                            quantity_destroyed = 56, 
                            quantity_dropped = 56, 
                            singleton = 56, )
                        ], 
                    position = esi_client.models.get_killmails_killmail_id_killmail_hash_position.get_killmails_killmail_id_killmail_hash_position(
                        x = 1.337, 
                        y = 1.337, 
                        z = 1.337, ), 
                    ship_type_id = 56, ),
        )
        """

    def testGetKillmailsKillmailIdKillmailHashOk(self):
        """Test GetKillmailsKillmailIdKillmailHashOk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
