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
from esi_client.models.get_dogma_dynamic_items_type_id_item_id_dogma_attribute import GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute
from esi_client.models.get_dogma_dynamic_items_type_id_item_id_dogma_effect import GetDogmaDynamicItemsTypeIdItemIdDogmaEffect
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetDogmaDynamicItemsTypeIdItemIdOk(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    created_by: StrictInt = Field(description="The ID of the character who created the item")
    dogma_attributes: Annotated[List[GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute], Field(max_length=1000)] = Field(description="dogma_attributes array")
    dogma_effects: Annotated[List[GetDogmaDynamicItemsTypeIdItemIdDogmaEffect], Field(max_length=1000)] = Field(description="dogma_effects array")
    mutator_type_id: StrictInt = Field(description="The type ID of the mutator used to generate the dynamic item.")
    source_type_id: StrictInt = Field(description="The type ID of the source item the mutator was applied to create the dynamic item.")
    __properties: ClassVar[List[str]] = ["created_by", "dogma_attributes", "dogma_effects", "mutator_type_id", "source_type_id"]

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
        """Create an instance of GetDogmaDynamicItemsTypeIdItemIdOk from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in dogma_attributes (list)
        _items = []
        if self.dogma_attributes:
            for _item in self.dogma_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dogma_attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in dogma_effects (list)
        _items = []
        if self.dogma_effects:
            for _item in self.dogma_effects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dogma_effects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetDogmaDynamicItemsTypeIdItemIdOk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_by": obj.get("created_by"),
            "dogma_attributes": [GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute.from_dict(_item) for _item in obj.get("dogma_attributes")] if obj.get("dogma_attributes") is not None else None,
            "dogma_effects": [GetDogmaDynamicItemsTypeIdItemIdDogmaEffect.from_dict(_item) for _item in obj.get("dogma_effects")] if obj.get("dogma_effects") is not None else None,
            "mutator_type_id": obj.get("mutator_type_id"),
            "source_type_id": obj.get("source_type_id")
        })
        return _obj


