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
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetCharactersCharacterIdOk(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    alliance_id: Optional[StrictInt] = Field(default=None, description="The character's alliance ID")
    birthday: datetime = Field(description="Creation date of the character")
    bloodline_id: StrictInt = Field(description="bloodline_id integer")
    corporation_id: StrictInt = Field(description="The character's corporation ID")
    description: Optional[StrictStr] = Field(default=None, description="description string")
    faction_id: Optional[StrictInt] = Field(default=None, description="ID of the faction the character is fighting for, if the character is enlisted in Factional Warfare")
    gender: StrictStr = Field(description="gender string")
    name: StrictStr = Field(description="name string")
    race_id: StrictInt = Field(description="race_id integer")
    security_status: Optional[Union[Annotated[float, Field(le=1E+1, strict=True, ge=-1E+1)], Annotated[int, Field(le=10, strict=True, ge=-10)]]] = Field(default=None, description="security_status number")
    title: Optional[StrictStr] = Field(default=None, description="The individual title of the character")
    __properties: ClassVar[List[str]] = ["alliance_id", "birthday", "bloodline_id", "corporation_id", "description", "faction_id", "gender", "name", "race_id", "security_status", "title"]

    @field_validator('gender')
    def gender_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('female', 'male'):
            raise ValueError("must be one of enum values ('female', 'male')")
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
        """Create an instance of GetCharactersCharacterIdOk from a JSON string"""
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
        """Create an instance of GetCharactersCharacterIdOk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alliance_id": obj.get("alliance_id"),
            "birthday": obj.get("birthday"),
            "bloodline_id": obj.get("bloodline_id"),
            "corporation_id": obj.get("corporation_id"),
            "description": obj.get("description"),
            "faction_id": obj.get("faction_id"),
            "gender": obj.get("gender"),
            "name": obj.get("name"),
            "race_id": obj.get("race_id"),
            "security_status": obj.get("security_status"),
            "title": obj.get("title")
        })
        return _obj

