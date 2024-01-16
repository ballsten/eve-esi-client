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

class GetCharactersCharacterIdCalendar200Ok(BaseModel):
    """
    event
    """ # noqa: E501
    event_date: Optional[datetime] = Field(default=None, description="event_date string")
    event_id: Optional[StrictInt] = Field(default=None, description="event_id integer")
    event_response: Optional[StrictStr] = Field(default=None, description="event_response string")
    importance: Optional[StrictInt] = Field(default=None, description="importance integer")
    title: Optional[StrictStr] = Field(default=None, description="title string")
    __properties: ClassVar[List[str]] = ["event_date", "event_id", "event_response", "importance", "title"]

    @field_validator('event_response')
    def event_response_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('declined', 'not_responded', 'accepted', 'tentative'):
            raise ValueError("must be one of enum values ('declined', 'not_responded', 'accepted', 'tentative')")
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
        """Create an instance of GetCharactersCharacterIdCalendar200Ok from a JSON string"""
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
        """Create an instance of GetCharactersCharacterIdCalendar200Ok from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event_date": obj.get("event_date"),
            "event_id": obj.get("event_id"),
            "event_response": obj.get("event_response"),
            "importance": obj.get("importance"),
            "title": obj.get("title")
        })
        return _obj

