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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetUniverseGraphicsGraphicIdOk(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    collision_file: Optional[StrictStr] = Field(default=None, description="collision_file string")
    graphic_file: Optional[StrictStr] = Field(default=None, description="graphic_file string")
    graphic_id: StrictInt = Field(description="graphic_id integer")
    icon_folder: Optional[StrictStr] = Field(default=None, description="icon_folder string")
    sof_dna: Optional[StrictStr] = Field(default=None, description="sof_dna string")
    sof_fation_name: Optional[StrictStr] = Field(default=None, description="sof_fation_name string")
    sof_hull_name: Optional[StrictStr] = Field(default=None, description="sof_hull_name string")
    sof_race_name: Optional[StrictStr] = Field(default=None, description="sof_race_name string")
    __properties: ClassVar[List[str]] = ["collision_file", "graphic_file", "graphic_id", "icon_folder", "sof_dna", "sof_fation_name", "sof_hull_name", "sof_race_name"]

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
        """Create an instance of GetUniverseGraphicsGraphicIdOk from a JSON string"""
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
        """Create an instance of GetUniverseGraphicsGraphicIdOk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "collision_file": obj.get("collision_file"),
            "graphic_file": obj.get("graphic_file"),
            "graphic_id": obj.get("graphic_id"),
            "icon_folder": obj.get("icon_folder"),
            "sof_dna": obj.get("sof_dna"),
            "sof_fation_name": obj.get("sof_fation_name"),
            "sof_hull_name": obj.get("sof_hull_name"),
            "sof_race_name": obj.get("sof_race_name")
        })
        return _obj


