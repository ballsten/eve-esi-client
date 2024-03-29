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
from esi_client.models.get_universe_stations_station_id_position import GetUniverseStationsStationIdPosition
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetUniverseStationsStationIdOk(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    max_dockable_ship_volume: Union[StrictFloat, StrictInt] = Field(description="max_dockable_ship_volume number")
    name: StrictStr = Field(description="name string")
    office_rental_cost: Union[StrictFloat, StrictInt] = Field(description="office_rental_cost number")
    owner: Optional[StrictInt] = Field(default=None, description="ID of the corporation that controls this station")
    position: GetUniverseStationsStationIdPosition
    race_id: Optional[StrictInt] = Field(default=None, description="race_id integer")
    reprocessing_efficiency: Union[StrictFloat, StrictInt] = Field(description="reprocessing_efficiency number")
    reprocessing_stations_take: Union[StrictFloat, StrictInt] = Field(description="reprocessing_stations_take number")
    services: Annotated[List[StrictStr], Field(max_length=30)] = Field(description="services array")
    station_id: StrictInt = Field(description="station_id integer")
    system_id: StrictInt = Field(description="The solar system this station is in")
    type_id: StrictInt = Field(description="type_id integer")
    __properties: ClassVar[List[str]] = ["max_dockable_ship_volume", "name", "office_rental_cost", "owner", "position", "race_id", "reprocessing_efficiency", "reprocessing_stations_take", "services", "station_id", "system_id", "type_id"]

    @field_validator('services')
    def services_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in ('bounty-missions', 'assasination-missions', 'courier-missions', 'interbus', 'reprocessing-plant', 'refinery', 'market', 'black-market', 'stock-exchange', 'cloning', 'surgery', 'dna-therapy', 'repair-facilities', 'factory', 'labratory', 'gambling', 'fitting', 'paintshop', 'news', 'storage', 'insurance', 'docking', 'office-rental', 'jump-clone-facility', 'loyalty-point-store', 'navy-offices', 'security-offices'):
                raise ValueError("each list item must be one of ('bounty-missions', 'assasination-missions', 'courier-missions', 'interbus', 'reprocessing-plant', 'refinery', 'market', 'black-market', 'stock-exchange', 'cloning', 'surgery', 'dna-therapy', 'repair-facilities', 'factory', 'labratory', 'gambling', 'fitting', 'paintshop', 'news', 'storage', 'insurance', 'docking', 'office-rental', 'jump-clone-facility', 'loyalty-point-store', 'navy-offices', 'security-offices')")
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
        """Create an instance of GetUniverseStationsStationIdOk from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of position
        if self.position:
            _dict['position'] = self.position.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetUniverseStationsStationIdOk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "max_dockable_ship_volume": obj.get("max_dockable_ship_volume"),
            "name": obj.get("name"),
            "office_rental_cost": obj.get("office_rental_cost"),
            "owner": obj.get("owner"),
            "position": GetUniverseStationsStationIdPosition.from_dict(obj.get("position")) if obj.get("position") is not None else None,
            "race_id": obj.get("race_id"),
            "reprocessing_efficiency": obj.get("reprocessing_efficiency"),
            "reprocessing_stations_take": obj.get("reprocessing_stations_take"),
            "services": obj.get("services"),
            "station_id": obj.get("station_id"),
            "system_id": obj.get("system_id"),
            "type_id": obj.get("type_id")
        })
        return _obj


