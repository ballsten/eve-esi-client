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
from esi_client.models.get_characters_character_id_skills_skill import GetCharactersCharacterIdSkillsSkill
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetCharactersCharacterIdSkillsOk(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    skills: Annotated[List[GetCharactersCharacterIdSkillsSkill], Field(max_length=1000)] = Field(description="skills array")
    total_sp: StrictInt = Field(description="total_sp integer")
    unallocated_sp: Optional[StrictInt] = Field(default=None, description="Skill points available to be assigned")
    __properties: ClassVar[List[str]] = ["skills", "total_sp", "unallocated_sp"]

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
        """Create an instance of GetCharactersCharacterIdSkillsOk from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in skills (list)
        _items = []
        if self.skills:
            for _item in self.skills:
                if _item:
                    _items.append(_item.to_dict())
            _dict['skills'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetCharactersCharacterIdSkillsOk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "skills": [GetCharactersCharacterIdSkillsSkill.from_dict(_item) for _item in obj.get("skills")] if obj.get("skills") is not None else None,
            "total_sp": obj.get("total_sp"),
            "unallocated_sp": obj.get("unallocated_sp")
        })
        return _obj


