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

class GetCorporationsCorporationIdStarbases200Ok(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    moon_id: Optional[StrictInt] = Field(default=None, description="The moon this starbase (POS) is anchored on, unanchored POSes do not have this information")
    onlined_since: Optional[datetime] = Field(default=None, description="When the POS onlined, for starbases (POSes) in online state")
    reinforced_until: Optional[datetime] = Field(default=None, description="When the POS will be out of reinforcement, for starbases (POSes) in reinforced state")
    starbase_id: StrictInt = Field(description="Unique ID for this starbase (POS)")
    state: Optional[StrictStr] = Field(default=None, description="state string")
    system_id: StrictInt = Field(description="The solar system this starbase (POS) is in, unanchored POSes have this information")
    type_id: StrictInt = Field(description="Starbase (POS) type")
    unanchor_at: Optional[datetime] = Field(default=None, description="When the POS started unanchoring, for starbases (POSes) in unanchoring state")
    __properties: ClassVar[List[str]] = ["moon_id", "onlined_since", "reinforced_until", "starbase_id", "state", "system_id", "type_id", "unanchor_at"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('offline', 'online', 'onlining', 'reinforced', 'unanchoring'):
            raise ValueError("must be one of enum values ('offline', 'online', 'onlining', 'reinforced', 'unanchoring')")
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
        """Create an instance of GetCorporationsCorporationIdStarbases200Ok from a JSON string"""
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
        """Create an instance of GetCorporationsCorporationIdStarbases200Ok from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "moon_id": obj.get("moon_id"),
            "onlined_since": obj.get("onlined_since"),
            "reinforced_until": obj.get("reinforced_until"),
            "starbase_id": obj.get("starbase_id"),
            "state": obj.get("state"),
            "system_id": obj.get("system_id"),
            "type_id": obj.get("type_id"),
            "unanchor_at": obj.get("unanchor_at")
        })
        return _obj

