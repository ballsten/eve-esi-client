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
from pydantic import BaseModel, StrictInt
from pydantic import Field
from typing_extensions import Annotated
from esi_client.models.get_killmails_killmail_id_killmail_hash_attacker import GetKillmailsKillmailIdKillmailHashAttacker
from esi_client.models.get_killmails_killmail_id_killmail_hash_victim import GetKillmailsKillmailIdKillmailHashVictim
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetKillmailsKillmailIdKillmailHashOk(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    attackers: Annotated[List[GetKillmailsKillmailIdKillmailHashAttacker], Field(max_length=10000)] = Field(description="attackers array")
    killmail_id: StrictInt = Field(description="ID of the killmail")
    killmail_time: datetime = Field(description="Time that the victim was killed and the killmail generated ")
    moon_id: Optional[StrictInt] = Field(default=None, description="Moon if the kill took place at one")
    solar_system_id: StrictInt = Field(description="Solar system that the kill took place in ")
    victim: GetKillmailsKillmailIdKillmailHashVictim
    war_id: Optional[StrictInt] = Field(default=None, description="War if the killmail is generated in relation to an official war ")
    __properties: ClassVar[List[str]] = ["attackers", "killmail_id", "killmail_time", "moon_id", "solar_system_id", "victim", "war_id"]

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
        """Create an instance of GetKillmailsKillmailIdKillmailHashOk from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attackers (list)
        _items = []
        if self.attackers:
            for _item in self.attackers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attackers'] = _items
        # override the default output from pydantic by calling `to_dict()` of victim
        if self.victim:
            _dict['victim'] = self.victim.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetKillmailsKillmailIdKillmailHashOk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attackers": [GetKillmailsKillmailIdKillmailHashAttacker.from_dict(_item) for _item in obj.get("attackers")] if obj.get("attackers") is not None else None,
            "killmail_id": obj.get("killmail_id"),
            "killmail_time": obj.get("killmail_time"),
            "moon_id": obj.get("moon_id"),
            "solar_system_id": obj.get("solar_system_id"),
            "victim": GetKillmailsKillmailIdKillmailHashVictim.from_dict(obj.get("victim")) if obj.get("victim") is not None else None,
            "war_id": obj.get("war_id")
        })
        return _obj

