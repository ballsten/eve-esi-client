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
from pydantic import BaseModel, StrictInt
from pydantic import Field
from typing_extensions import Annotated
from esi_client.models.post_characters_character_id_fittings_item import PostCharactersCharacterIdFittingsItem
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PostCharactersCharacterIdFittingsFitting(BaseModel):
    """
    fitting object
    """ # noqa: E501
    description: Annotated[str, Field(min_length=0, strict=True, max_length=500)] = Field(description="description string")
    items: Annotated[List[PostCharactersCharacterIdFittingsItem], Field(min_length=1, max_length=512)] = Field(description="items array")
    name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="name string")
    ship_type_id: StrictInt = Field(description="ship_type_id integer")
    __properties: ClassVar[List[str]] = ["description", "items", "name", "ship_type_id"]

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
        """Create an instance of PostCharactersCharacterIdFittingsFitting from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PostCharactersCharacterIdFittingsFitting from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "items": [PostCharactersCharacterIdFittingsItem.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "name": obj.get("name"),
            "ship_type_id": obj.get("ship_type_id")
        })
        return _obj


