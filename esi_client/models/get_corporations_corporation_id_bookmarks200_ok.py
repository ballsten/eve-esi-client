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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from esi_client.models.get_corporations_corporation_id_bookmarks_coordinates import GetCorporationsCorporationIdBookmarksCoordinates
from esi_client.models.get_corporations_corporation_id_bookmarks_item import GetCorporationsCorporationIdBookmarksItem
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetCorporationsCorporationIdBookmarks200Ok(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    bookmark_id: StrictInt = Field(description="bookmark_id integer")
    coordinates: Optional[GetCorporationsCorporationIdBookmarksCoordinates] = None
    created: datetime = Field(description="created string")
    creator_id: StrictInt = Field(description="creator_id integer")
    folder_id: Optional[StrictInt] = Field(default=None, description="folder_id integer")
    item: Optional[GetCorporationsCorporationIdBookmarksItem] = None
    label: StrictStr = Field(description="label string")
    location_id: StrictInt = Field(description="location_id integer")
    notes: StrictStr = Field(description="notes string")
    __properties: ClassVar[List[str]] = ["bookmark_id", "coordinates", "created", "creator_id", "folder_id", "item", "label", "location_id", "notes"]

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
        """Create an instance of GetCorporationsCorporationIdBookmarks200Ok from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of coordinates
        if self.coordinates:
            _dict['coordinates'] = self.coordinates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetCorporationsCorporationIdBookmarks200Ok from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bookmark_id": obj.get("bookmark_id"),
            "coordinates": GetCorporationsCorporationIdBookmarksCoordinates.from_dict(obj.get("coordinates")) if obj.get("coordinates") is not None else None,
            "created": obj.get("created"),
            "creator_id": obj.get("creator_id"),
            "folder_id": obj.get("folder_id"),
            "item": GetCorporationsCorporationIdBookmarksItem.from_dict(obj.get("item")) if obj.get("item") is not None else None,
            "label": obj.get("label"),
            "location_id": obj.get("location_id"),
            "notes": obj.get("notes")
        })
        return _obj


