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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetOpportunitiesGroupsGroupIdOk(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    connected_groups: Annotated[List[StrictInt], Field(max_length=50)] = Field(description="The groups that are connected to this group on the opportunities map")
    description: StrictStr = Field(description="description string")
    group_id: StrictInt = Field(description="group_id integer")
    name: StrictStr = Field(description="name string")
    notification: StrictStr = Field(description="notification string")
    required_tasks: Annotated[List[StrictInt], Field(max_length=100)] = Field(description="Tasks need to complete for this group")
    __properties: ClassVar[List[str]] = ["connected_groups", "description", "group_id", "name", "notification", "required_tasks"]

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
        """Create an instance of GetOpportunitiesGroupsGroupIdOk from a JSON string"""
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
        """Create an instance of GetOpportunitiesGroupsGroupIdOk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connected_groups": obj.get("connected_groups"),
            "description": obj.get("description"),
            "group_id": obj.get("group_id"),
            "name": obj.get("name"),
            "notification": obj.get("notification"),
            "required_tasks": obj.get("required_tasks")
        })
        return _obj


