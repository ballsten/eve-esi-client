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
from pydantic import BaseModel, StrictBool, StrictInt
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetContractsPublicItemsContractId200Ok(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    is_blueprint_copy: Optional[StrictBool] = Field(default=None, description="is_blueprint_copy boolean")
    is_included: StrictBool = Field(description="true if the contract issuer has submitted this item with the contract, false if the isser is asking for this item in the contract")
    item_id: Optional[StrictInt] = Field(default=None, description="Unique ID for the item being sold. Not present if item is being requested by contract rather than sold with contract")
    material_efficiency: Optional[Annotated[int, Field(le=25, strict=True, ge=0)]] = Field(default=None, description="Material Efficiency Level of the blueprint")
    quantity: StrictInt = Field(description="Number of items in the stack")
    record_id: StrictInt = Field(description="Unique ID for the item, used by the contract system")
    runs: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, description="Number of runs remaining if the blueprint is a copy, -1 if it is an original")
    time_efficiency: Optional[Annotated[int, Field(le=20, strict=True, ge=0)]] = Field(default=None, description="Time Efficiency Level of the blueprint")
    type_id: StrictInt = Field(description="Type ID for item")
    __properties: ClassVar[List[str]] = ["is_blueprint_copy", "is_included", "item_id", "material_efficiency", "quantity", "record_id", "runs", "time_efficiency", "type_id"]

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
        """Create an instance of GetContractsPublicItemsContractId200Ok from a JSON string"""
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
        """Create an instance of GetContractsPublicItemsContractId200Ok from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "is_blueprint_copy": obj.get("is_blueprint_copy"),
            "is_included": obj.get("is_included"),
            "item_id": obj.get("item_id"),
            "material_efficiency": obj.get("material_efficiency"),
            "quantity": obj.get("quantity"),
            "record_id": obj.get("record_id"),
            "runs": obj.get("runs"),
            "time_efficiency": obj.get("time_efficiency"),
            "type_id": obj.get("type_id")
        })
        return _obj


