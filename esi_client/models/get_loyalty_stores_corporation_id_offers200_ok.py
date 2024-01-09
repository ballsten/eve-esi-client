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
from esi_client.models.get_loyalty_stores_corporation_id_offers_required_item import GetLoyaltyStoresCorporationIdOffersRequiredItem
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetLoyaltyStoresCorporationIdOffers200Ok(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    ak_cost: Optional[StrictInt] = Field(default=None, description="Analysis kredit cost")
    isk_cost: StrictInt = Field(description="isk_cost integer")
    lp_cost: StrictInt = Field(description="lp_cost integer")
    offer_id: StrictInt = Field(description="offer_id integer")
    quantity: StrictInt = Field(description="quantity integer")
    required_items: Annotated[List[GetLoyaltyStoresCorporationIdOffersRequiredItem], Field(max_length=100)] = Field(description="required_items array")
    type_id: StrictInt = Field(description="type_id integer")
    __properties: ClassVar[List[str]] = ["ak_cost", "isk_cost", "lp_cost", "offer_id", "quantity", "required_items", "type_id"]

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
        """Create an instance of GetLoyaltyStoresCorporationIdOffers200Ok from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in required_items (list)
        _items = []
        if self.required_items:
            for _item in self.required_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['required_items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetLoyaltyStoresCorporationIdOffers200Ok from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ak_cost": obj.get("ak_cost"),
            "isk_cost": obj.get("isk_cost"),
            "lp_cost": obj.get("lp_cost"),
            "offer_id": obj.get("offer_id"),
            "quantity": obj.get("quantity"),
            "required_items": [GetLoyaltyStoresCorporationIdOffersRequiredItem.from_dict(_item) for _item in obj.get("required_items")] if obj.get("required_items") is not None else None,
            "type_id": obj.get("type_id")
        })
        return _obj


