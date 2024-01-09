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

from esi_client.models.get_dogma_effects_effect_id_ok import GetDogmaEffectsEffectIdOk

class TestGetDogmaEffectsEffectIdOk(unittest.TestCase):
    """GetDogmaEffectsEffectIdOk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDogmaEffectsEffectIdOk:
        """Test GetDogmaEffectsEffectIdOk
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDogmaEffectsEffectIdOk`
        """
        model = GetDogmaEffectsEffectIdOk()
        if include_optional:
            return GetDogmaEffectsEffectIdOk(
                description = '',
                disallow_auto_repeat = True,
                discharge_attribute_id = 56,
                display_name = '',
                duration_attribute_id = 56,
                effect_category = 56,
                effect_id = 56,
                electronic_chance = True,
                falloff_attribute_id = 56,
                icon_id = 56,
                is_assistance = True,
                is_offensive = True,
                is_warp_safe = True,
                modifiers = [
                    esi_client.models.get_dogma_effects_effect_id_modifier.get_dogma_effects_effect_id_modifier(
                        domain = '', 
                        effect_id = 56, 
                        func = '', 
                        modified_attribute_id = 56, 
                        modifying_attribute_id = 56, 
                        operator = 56, )
                    ],
                name = '',
                post_expression = 56,
                pre_expression = 56,
                published = True,
                range_attribute_id = 56,
                range_chance = True,
                tracking_speed_attribute_id = 56
            )
        else:
            return GetDogmaEffectsEffectIdOk(
                effect_id = 56,
        )
        """

    def testGetDogmaEffectsEffectIdOk(self):
        """Test GetDogmaEffectsEffectIdOk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
