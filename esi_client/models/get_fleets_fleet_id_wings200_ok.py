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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from esi_client.models.get_fleets_fleet_id_wings_squad import GetFleetsFleetIdWingsSquad
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetFleetsFleetIdWings200Ok(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    id: StrictInt = Field(description="id integer")
    name: StrictStr = Field(description="name string")
    squads: Annotated[List[GetFleetsFleetIdWingsSquad], Field(max_length=25)] = Field(description="squads array")
    __properties: ClassVar[List[str]] = ["id", "name", "squads"]

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
        """Create an instance of GetFleetsFleetIdWings200Ok from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in squads (list)
        _items = []
        if self.squads:
            for _item in self.squads:
                if _item:
                    _items.append(_item.to_dict())
            _dict['squads'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetFleetsFleetIdWings200Ok from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "squads": [GetFleetsFleetIdWingsSquad.from_dict(_item) for _item in obj.get("squads")] if obj.get("squads") is not None else None
        })
        return _obj


