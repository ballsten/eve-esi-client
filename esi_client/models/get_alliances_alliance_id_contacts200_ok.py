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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetAlliancesAllianceIdContacts200Ok(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    contact_id: StrictInt = Field(description="contact_id integer")
    contact_type: StrictStr = Field(description="contact_type string")
    label_ids: Optional[Annotated[List[StrictInt], Field(max_length=63)]] = Field(default=None, description="label_ids array")
    standing: Union[StrictFloat, StrictInt] = Field(description="Standing of the contact")
    __properties: ClassVar[List[str]] = ["contact_id", "contact_type", "label_ids", "standing"]

    @field_validator('contact_type')
    def contact_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('character', 'corporation', 'alliance', 'faction'):
            raise ValueError("must be one of enum values ('character', 'corporation', 'alliance', 'faction')")
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
        """Create an instance of GetAlliancesAllianceIdContacts200Ok from a JSON string"""
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
        """Create an instance of GetAlliancesAllianceIdContacts200Ok from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contact_id": obj.get("contact_id"),
            "contact_type": obj.get("contact_type"),
            "label_ids": obj.get("label_ids"),
            "standing": obj.get("standing")
        })
        return _obj


