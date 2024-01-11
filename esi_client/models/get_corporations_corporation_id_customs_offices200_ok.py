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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetCorporationsCorporationIdCustomsOffices200Ok(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    alliance_tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Only present if alliance access is allowed")
    allow_access_with_standings: StrictBool = Field(description="standing_level and any standing related tax rate only present when this is true")
    allow_alliance_access: StrictBool = Field(description="allow_alliance_access boolean")
    bad_standing_tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="bad_standing_tax_rate number")
    corporation_tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="corporation_tax_rate number")
    excellent_standing_tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Tax rate for entities with excellent level of standing, only present if this level is allowed, same for all other standing related tax rates")
    good_standing_tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="good_standing_tax_rate number")
    neutral_standing_tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="neutral_standing_tax_rate number")
    office_id: StrictInt = Field(description="unique ID of this customs office")
    reinforce_exit_end: Annotated[int, Field(le=23, strict=True, ge=0)] = Field(description="reinforce_exit_end integer")
    reinforce_exit_start: Annotated[int, Field(le=23, strict=True, ge=0)] = Field(description="Together with reinforce_exit_end, marks a 2-hour period where this customs office could exit reinforcement mode during the day after initial attack")
    standing_level: Optional[StrictStr] = Field(default=None, description="Access is allowed only for entities with this level of standing or better")
    system_id: StrictInt = Field(description="ID of the solar system this customs office is located in")
    terrible_standing_tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="terrible_standing_tax_rate number")
    __properties: ClassVar[List[str]] = ["alliance_tax_rate", "allow_access_with_standings", "allow_alliance_access", "bad_standing_tax_rate", "corporation_tax_rate", "excellent_standing_tax_rate", "good_standing_tax_rate", "neutral_standing_tax_rate", "office_id", "reinforce_exit_end", "reinforce_exit_start", "standing_level", "system_id", "terrible_standing_tax_rate"]

    @field_validator('standing_level')
    def standing_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('bad', 'excellent', 'good', 'neutral', 'terrible'):
            raise ValueError("must be one of enum values ('bad', 'excellent', 'good', 'neutral', 'terrible')")
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
        """Create an instance of GetCorporationsCorporationIdCustomsOffices200Ok from a JSON string"""
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
        """Create an instance of GetCorporationsCorporationIdCustomsOffices200Ok from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alliance_tax_rate": obj.get("alliance_tax_rate"),
            "allow_access_with_standings": obj.get("allow_access_with_standings"),
            "allow_alliance_access": obj.get("allow_alliance_access"),
            "bad_standing_tax_rate": obj.get("bad_standing_tax_rate"),
            "corporation_tax_rate": obj.get("corporation_tax_rate"),
            "excellent_standing_tax_rate": obj.get("excellent_standing_tax_rate"),
            "good_standing_tax_rate": obj.get("good_standing_tax_rate"),
            "neutral_standing_tax_rate": obj.get("neutral_standing_tax_rate"),
            "office_id": obj.get("office_id"),
            "reinforce_exit_end": obj.get("reinforce_exit_end"),
            "reinforce_exit_start": obj.get("reinforce_exit_start"),
            "standing_level": obj.get("standing_level"),
            "system_id": obj.get("system_id"),
            "terrible_standing_tax_rate": obj.get("terrible_standing_tax_rate")
        })
        return _obj


