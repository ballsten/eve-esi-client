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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetCharactersCharacterIdSearchOk(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    agent: Optional[Annotated[List[StrictInt], Field(max_length=500)]] = Field(default=None, description="agent array")
    alliance: Optional[Annotated[List[StrictInt], Field(max_length=500)]] = Field(default=None, description="alliance array")
    character: Optional[Annotated[List[StrictInt], Field(max_length=500)]] = Field(default=None, description="character array")
    constellation: Optional[Annotated[List[StrictInt], Field(max_length=500)]] = Field(default=None, description="constellation array")
    corporation: Optional[Annotated[List[StrictInt], Field(max_length=500)]] = Field(default=None, description="corporation array")
    faction: Optional[Annotated[List[StrictInt], Field(max_length=500)]] = Field(default=None, description="faction array")
    inventory_type: Optional[Annotated[List[StrictInt], Field(max_length=500)]] = Field(default=None, description="inventory_type array")
    region: Optional[Annotated[List[StrictInt], Field(max_length=500)]] = Field(default=None, description="region array")
    solar_system: Optional[Annotated[List[StrictInt], Field(max_length=500)]] = Field(default=None, description="solar_system array")
    station: Optional[Annotated[List[StrictInt], Field(max_length=500)]] = Field(default=None, description="station array")
    structure: Optional[Annotated[List[StrictInt], Field(max_length=500)]] = Field(default=None, description="structure array")
    __properties: ClassVar[List[str]] = ["agent", "alliance", "character", "constellation", "corporation", "faction", "inventory_type", "region", "solar_system", "station", "structure"]

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
        """Create an instance of GetCharactersCharacterIdSearchOk from a JSON string"""
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
        """Create an instance of GetCharactersCharacterIdSearchOk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agent": obj.get("agent"),
            "alliance": obj.get("alliance"),
            "character": obj.get("character"),
            "constellation": obj.get("constellation"),
            "corporation": obj.get("corporation"),
            "faction": obj.get("faction"),
            "inventory_type": obj.get("inventory_type"),
            "region": obj.get("region"),
            "solar_system": obj.get("solar_system"),
            "station": obj.get("station"),
            "structure": obj.get("structure")
        })
        return _obj

