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
from typing import Any, ClassVar, Dict, List, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetCorporationsCorporationIdWalletsDivisionTransactions200Ok(BaseModel):
    """
    wallet transaction
    """ # noqa: E501
    client_id: StrictInt = Field(description="client_id integer")
    var_date: datetime = Field(description="Date and time of transaction", alias="date")
    is_buy: StrictBool = Field(description="is_buy boolean")
    journal_ref_id: StrictInt = Field(description="-1 if there is no corresponding wallet journal entry")
    location_id: StrictInt = Field(description="location_id integer")
    quantity: StrictInt = Field(description="quantity integer")
    transaction_id: StrictInt = Field(description="Unique transaction ID")
    type_id: StrictInt = Field(description="type_id integer")
    unit_price: Union[StrictFloat, StrictInt] = Field(description="Amount paid per unit")
    __properties: ClassVar[List[str]] = ["client_id", "date", "is_buy", "journal_ref_id", "location_id", "quantity", "transaction_id", "type_id", "unit_price"]

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
        """Create an instance of GetCorporationsCorporationIdWalletsDivisionTransactions200Ok from a JSON string"""
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
        """Create an instance of GetCorporationsCorporationIdWalletsDivisionTransactions200Ok from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "client_id": obj.get("client_id"),
            "date": obj.get("date"),
            "is_buy": obj.get("is_buy"),
            "journal_ref_id": obj.get("journal_ref_id"),
            "location_id": obj.get("location_id"),
            "quantity": obj.get("quantity"),
            "transaction_id": obj.get("transaction_id"),
            "type_id": obj.get("type_id"),
            "unit_price": obj.get("unit_price")
        })
        return _obj


