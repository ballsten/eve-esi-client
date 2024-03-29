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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from esi_client.models.get_characters_character_id_mail_recipient import GetCharactersCharacterIdMailRecipient
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetCharactersCharacterIdMail200Ok(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    var_from: Optional[StrictInt] = Field(default=None, description="From whom the mail was sent", alias="from")
    is_read: Optional[StrictBool] = Field(default=None, description="is_read boolean")
    labels: Optional[Annotated[List[StrictInt], Field(max_length=25)]] = Field(default=None, description="labels array")
    mail_id: Optional[StrictInt] = Field(default=None, description="mail_id integer")
    recipients: Optional[Annotated[List[GetCharactersCharacterIdMailRecipient], Field(min_length=0, max_length=52)]] = Field(default=None, description="Recipients of the mail")
    subject: Optional[StrictStr] = Field(default=None, description="Mail subject")
    timestamp: Optional[datetime] = Field(default=None, description="When the mail was sent")
    __properties: ClassVar[List[str]] = ["from", "is_read", "labels", "mail_id", "recipients", "subject", "timestamp"]

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
        """Create an instance of GetCharactersCharacterIdMail200Ok from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in recipients (list)
        _items = []
        if self.recipients:
            for _item in self.recipients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recipients'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetCharactersCharacterIdMail200Ok from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "from": obj.get("from"),
            "is_read": obj.get("is_read"),
            "labels": obj.get("labels"),
            "mail_id": obj.get("mail_id"),
            "recipients": [GetCharactersCharacterIdMailRecipient.from_dict(_item) for _item in obj.get("recipients")] if obj.get("recipients") is not None else None,
            "subject": obj.get("subject"),
            "timestamp": obj.get("timestamp")
        })
        return _obj


