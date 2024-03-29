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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetKillmailsKillmailIdKillmailHashAttacker(BaseModel):
    """
    attacker object
    """ # noqa: E501
    alliance_id: Optional[StrictInt] = Field(default=None, description="alliance_id integer")
    character_id: Optional[StrictInt] = Field(default=None, description="character_id integer")
    corporation_id: Optional[StrictInt] = Field(default=None, description="corporation_id integer")
    damage_done: StrictInt = Field(description="damage_done integer")
    faction_id: Optional[StrictInt] = Field(default=None, description="faction_id integer")
    final_blow: StrictBool = Field(description="Was the attacker the one to achieve the final blow ")
    security_status: Union[StrictFloat, StrictInt] = Field(description="Security status for the attacker ")
    ship_type_id: Optional[StrictInt] = Field(default=None, description="What ship was the attacker flying ")
    weapon_type_id: Optional[StrictInt] = Field(default=None, description="What weapon was used by the attacker for the kill ")
    __properties: ClassVar[List[str]] = ["alliance_id", "character_id", "corporation_id", "damage_done", "faction_id", "final_blow", "security_status", "ship_type_id", "weapon_type_id"]

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
        """Create an instance of GetKillmailsKillmailIdKillmailHashAttacker from a JSON string"""
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
        """Create an instance of GetKillmailsKillmailIdKillmailHashAttacker from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alliance_id": obj.get("alliance_id"),
            "character_id": obj.get("character_id"),
            "corporation_id": obj.get("corporation_id"),
            "damage_done": obj.get("damage_done"),
            "faction_id": obj.get("faction_id"),
            "final_blow": obj.get("final_blow"),
            "security_status": obj.get("security_status"),
            "ship_type_id": obj.get("ship_type_id"),
            "weapon_type_id": obj.get("weapon_type_id")
        })
        return _obj


