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
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetContractsPublicRegionId200Ok(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    buyout: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Buyout price (for Auctions only)")
    collateral: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Collateral price (for Couriers only)")
    contract_id: StrictInt = Field(description="contract_id integer")
    date_expired: datetime = Field(description="Expiration date of the contract")
    date_issued: datetime = Field(description="Сreation date of the contract")
    days_to_complete: Optional[StrictInt] = Field(default=None, description="Number of days to perform the contract")
    end_location_id: Optional[StrictInt] = Field(default=None, description="End location ID (for Couriers contract)")
    for_corporation: Optional[StrictBool] = Field(default=None, description="true if the contract was issued on behalf of the issuer's corporation")
    issuer_corporation_id: StrictInt = Field(description="Character's corporation ID for the issuer")
    issuer_id: StrictInt = Field(description="Character ID for the issuer")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Price of contract (for ItemsExchange and Auctions)")
    reward: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Remuneration for contract (for Couriers only)")
    start_location_id: Optional[StrictInt] = Field(default=None, description="Start location ID (for Couriers contract)")
    title: Optional[StrictStr] = Field(default=None, description="Title of the contract")
    type: StrictStr = Field(description="Type of the contract")
    volume: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Volume of items in the contract")
    __properties: ClassVar[List[str]] = ["buyout", "collateral", "contract_id", "date_expired", "date_issued", "days_to_complete", "end_location_id", "for_corporation", "issuer_corporation_id", "issuer_id", "price", "reward", "start_location_id", "title", "type", "volume"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('unknown', 'item_exchange', 'auction', 'courier', 'loan'):
            raise ValueError("must be one of enum values ('unknown', 'item_exchange', 'auction', 'courier', 'loan')")
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
        """Create an instance of GetContractsPublicRegionId200Ok from a JSON string"""
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
        """Create an instance of GetContractsPublicRegionId200Ok from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "buyout": obj.get("buyout"),
            "collateral": obj.get("collateral"),
            "contract_id": obj.get("contract_id"),
            "date_expired": obj.get("date_expired"),
            "date_issued": obj.get("date_issued"),
            "days_to_complete": obj.get("days_to_complete"),
            "end_location_id": obj.get("end_location_id"),
            "for_corporation": obj.get("for_corporation"),
            "issuer_corporation_id": obj.get("issuer_corporation_id"),
            "issuer_id": obj.get("issuer_id"),
            "price": obj.get("price"),
            "reward": obj.get("reward"),
            "start_location_id": obj.get("start_location_id"),
            "title": obj.get("title"),
            "type": obj.get("type"),
            "volume": obj.get("volume")
        })
        return _obj


