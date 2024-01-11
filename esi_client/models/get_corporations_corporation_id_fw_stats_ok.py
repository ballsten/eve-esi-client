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
from esi_client.models.get_corporations_corporation_id_fw_stats_kills import GetCorporationsCorporationIdFwStatsKills
from esi_client.models.get_corporations_corporation_id_fw_stats_victory_points import GetCorporationsCorporationIdFwStatsVictoryPoints
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetCorporationsCorporationIdFwStatsOk(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    enlisted_on: Optional[datetime] = Field(default=None, description="The enlistment date of the given corporation into faction warfare. Will not be included if corporation is not enlisted in faction warfare")
    faction_id: Optional[StrictInt] = Field(default=None, description="The faction the given corporation is enlisted to fight for. Will not be included if corporation is not enlisted in faction warfare")
    kills: GetCorporationsCorporationIdFwStatsKills
    pilots: Optional[StrictInt] = Field(default=None, description="How many pilots the enlisted corporation has. Will not be included if corporation is not enlisted in faction warfare")
    victory_points: GetCorporationsCorporationIdFwStatsVictoryPoints
    __properties: ClassVar[List[str]] = ["enlisted_on", "faction_id", "kills", "pilots", "victory_points"]

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
        """Create an instance of GetCorporationsCorporationIdFwStatsOk from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of kills
        if self.kills:
            _dict['kills'] = self.kills.to_dict()
        # override the default output from pydantic by calling `to_dict()` of victory_points
        if self.victory_points:
            _dict['victory_points'] = self.victory_points.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetCorporationsCorporationIdFwStatsOk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enlisted_on": obj.get("enlisted_on"),
            "faction_id": obj.get("faction_id"),
            "kills": GetCorporationsCorporationIdFwStatsKills.from_dict(obj.get("kills")) if obj.get("kills") is not None else None,
            "pilots": obj.get("pilots"),
            "victory_points": GetCorporationsCorporationIdFwStatsVictoryPoints.from_dict(obj.get("victory_points")) if obj.get("victory_points") is not None else None
        })
        return _obj


