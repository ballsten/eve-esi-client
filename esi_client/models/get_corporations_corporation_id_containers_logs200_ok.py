# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    The version of the OpenAPI document: 1.19
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetCorporationsCorporationIdContainersLogs200Ok(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    action: StrictStr = Field(description="action string")
    character_id: StrictInt = Field(description="ID of the character who performed the action.")
    container_id: StrictInt = Field(description="ID of the container")
    container_type_id: StrictInt = Field(description="Type ID of the container")
    location_flag: StrictStr = Field(description="location_flag string")
    location_id: StrictInt = Field(description="location_id integer")
    logged_at: datetime = Field(description="Timestamp when this log was created")
    new_config_bitmask: Optional[StrictInt] = Field(default=None, description="new_config_bitmask integer")
    old_config_bitmask: Optional[StrictInt] = Field(default=None, description="old_config_bitmask integer")
    password_type: Optional[StrictStr] = Field(default=None, description="Type of password set if action is of type SetPassword or EnterPassword")
    quantity: Optional[StrictInt] = Field(default=None, description="Quantity of the item being acted upon")
    type_id: Optional[StrictInt] = Field(default=None, description="Type ID of the item being acted upon")
    __properties: ClassVar[List[str]] = ["action", "character_id", "container_id", "container_type_id", "location_flag", "location_id", "logged_at", "new_config_bitmask", "old_config_bitmask", "password_type", "quantity", "type_id"]

    @field_validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('add', 'assemble', 'configure', 'enter_password', 'lock', 'move', 'repackage', 'set_name', 'set_password', 'unlock'):
            raise ValueError("must be one of enum values ('add', 'assemble', 'configure', 'enter_password', 'lock', 'move', 'repackage', 'set_name', 'set_password', 'unlock')")
        return value

    @field_validator('location_flag')
    def location_flag_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('AssetSafety', 'AutoFit', 'Bonus', 'Booster', 'BoosterBay', 'Capsule', 'Cargo', 'CorpDeliveries', 'CorpSAG1', 'CorpSAG2', 'CorpSAG3', 'CorpSAG4', 'CorpSAG5', 'CorpSAG6', 'CorpSAG7', 'CrateLoot', 'Deliveries', 'DroneBay', 'DustBattle', 'DustDatabank', 'FighterBay', 'FighterTube0', 'FighterTube1', 'FighterTube2', 'FighterTube3', 'FighterTube4', 'FleetHangar', 'FrigateEscapeBay', 'Hangar', 'HangarAll', 'HiSlot0', 'HiSlot1', 'HiSlot2', 'HiSlot3', 'HiSlot4', 'HiSlot5', 'HiSlot6', 'HiSlot7', 'HiddenModifiers', 'Implant', 'Impounded', 'JunkyardReprocessed', 'JunkyardTrashed', 'LoSlot0', 'LoSlot1', 'LoSlot2', 'LoSlot3', 'LoSlot4', 'LoSlot5', 'LoSlot6', 'LoSlot7', 'Locked', 'MedSlot0', 'MedSlot1', 'MedSlot2', 'MedSlot3', 'MedSlot4', 'MedSlot5', 'MedSlot6', 'MedSlot7', 'OfficeFolder', 'Pilot', 'PlanetSurface', 'QuafeBay', 'QuantumCoreRoom', 'Reward', 'RigSlot0', 'RigSlot1', 'RigSlot2', 'RigSlot3', 'RigSlot4', 'RigSlot5', 'RigSlot6', 'RigSlot7', 'SecondaryStorage', 'ServiceSlot0', 'ServiceSlot1', 'ServiceSlot2', 'ServiceSlot3', 'ServiceSlot4', 'ServiceSlot5', 'ServiceSlot6', 'ServiceSlot7', 'ShipHangar', 'ShipOffline', 'Skill', 'SkillInTraining', 'SpecializedAmmoHold', 'SpecializedCommandCenterHold', 'SpecializedFuelBay', 'SpecializedGasHold', 'SpecializedIndustrialShipHold', 'SpecializedLargeShipHold', 'SpecializedMaterialBay', 'SpecializedMediumShipHold', 'SpecializedMineralHold', 'SpecializedOreHold', 'SpecializedPlanetaryCommoditiesHold', 'SpecializedSalvageHold', 'SpecializedShipHold', 'SpecializedSmallShipHold', 'StructureActive', 'StructureFuel', 'StructureInactive', 'StructureOffline', 'SubSystemBay', 'SubSystemSlot0', 'SubSystemSlot1', 'SubSystemSlot2', 'SubSystemSlot3', 'SubSystemSlot4', 'SubSystemSlot5', 'SubSystemSlot6', 'SubSystemSlot7', 'Unlocked', 'Wallet', 'Wardrobe'):
            raise ValueError("must be one of enum values ('AssetSafety', 'AutoFit', 'Bonus', 'Booster', 'BoosterBay', 'Capsule', 'Cargo', 'CorpDeliveries', 'CorpSAG1', 'CorpSAG2', 'CorpSAG3', 'CorpSAG4', 'CorpSAG5', 'CorpSAG6', 'CorpSAG7', 'CrateLoot', 'Deliveries', 'DroneBay', 'DustBattle', 'DustDatabank', 'FighterBay', 'FighterTube0', 'FighterTube1', 'FighterTube2', 'FighterTube3', 'FighterTube4', 'FleetHangar', 'FrigateEscapeBay', 'Hangar', 'HangarAll', 'HiSlot0', 'HiSlot1', 'HiSlot2', 'HiSlot3', 'HiSlot4', 'HiSlot5', 'HiSlot6', 'HiSlot7', 'HiddenModifiers', 'Implant', 'Impounded', 'JunkyardReprocessed', 'JunkyardTrashed', 'LoSlot0', 'LoSlot1', 'LoSlot2', 'LoSlot3', 'LoSlot4', 'LoSlot5', 'LoSlot6', 'LoSlot7', 'Locked', 'MedSlot0', 'MedSlot1', 'MedSlot2', 'MedSlot3', 'MedSlot4', 'MedSlot5', 'MedSlot6', 'MedSlot7', 'OfficeFolder', 'Pilot', 'PlanetSurface', 'QuafeBay', 'QuantumCoreRoom', 'Reward', 'RigSlot0', 'RigSlot1', 'RigSlot2', 'RigSlot3', 'RigSlot4', 'RigSlot5', 'RigSlot6', 'RigSlot7', 'SecondaryStorage', 'ServiceSlot0', 'ServiceSlot1', 'ServiceSlot2', 'ServiceSlot3', 'ServiceSlot4', 'ServiceSlot5', 'ServiceSlot6', 'ServiceSlot7', 'ShipHangar', 'ShipOffline', 'Skill', 'SkillInTraining', 'SpecializedAmmoHold', 'SpecializedCommandCenterHold', 'SpecializedFuelBay', 'SpecializedGasHold', 'SpecializedIndustrialShipHold', 'SpecializedLargeShipHold', 'SpecializedMaterialBay', 'SpecializedMediumShipHold', 'SpecializedMineralHold', 'SpecializedOreHold', 'SpecializedPlanetaryCommoditiesHold', 'SpecializedSalvageHold', 'SpecializedShipHold', 'SpecializedSmallShipHold', 'StructureActive', 'StructureFuel', 'StructureInactive', 'StructureOffline', 'SubSystemBay', 'SubSystemSlot0', 'SubSystemSlot1', 'SubSystemSlot2', 'SubSystemSlot3', 'SubSystemSlot4', 'SubSystemSlot5', 'SubSystemSlot6', 'SubSystemSlot7', 'Unlocked', 'Wallet', 'Wardrobe')")
        return value

    @field_validator('password_type')
    def password_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('config', 'general'):
            raise ValueError("must be one of enum values ('config', 'general')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GetCorporationsCorporationIdContainersLogs200Ok from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetCorporationsCorporationIdContainersLogs200Ok from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "character_id": obj.get("character_id"),
            "container_id": obj.get("container_id"),
            "container_type_id": obj.get("container_type_id"),
            "location_flag": obj.get("location_flag"),
            "location_id": obj.get("location_id"),
            "logged_at": obj.get("logged_at"),
            "new_config_bitmask": obj.get("new_config_bitmask"),
            "old_config_bitmask": obj.get("old_config_bitmask"),
            "password_type": obj.get("password_type"),
            "quantity": obj.get("quantity"),
            "type_id": obj.get("type_id")
        })
        return _obj


