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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetCharactersCharacterIdIndustryJobs200Ok(BaseModel):
    """
    200 ok object
    """ # noqa: E501
    activity_id: StrictInt = Field(description="Job activity ID")
    blueprint_id: StrictInt = Field(description="blueprint_id integer")
    blueprint_location_id: StrictInt = Field(description="Location ID of the location from which the blueprint was installed. Normally a station ID, but can also be an asset (e.g. container) or corporation facility")
    blueprint_type_id: StrictInt = Field(description="blueprint_type_id integer")
    completed_character_id: Optional[StrictInt] = Field(default=None, description="ID of the character which completed this job")
    completed_date: Optional[datetime] = Field(default=None, description="Date and time when this job was completed")
    cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The sume of job installation fee and industry facility tax")
    duration: StrictInt = Field(description="Job duration in seconds")
    end_date: datetime = Field(description="Date and time when this job finished")
    facility_id: StrictInt = Field(description="ID of the facility where this job is running")
    installer_id: StrictInt = Field(description="ID of the character which installed this job")
    job_id: StrictInt = Field(description="Unique job ID")
    licensed_runs: Optional[StrictInt] = Field(default=None, description="Number of runs blueprint is licensed for")
    output_location_id: StrictInt = Field(description="Location ID of the location to which the output of the job will be delivered. Normally a station ID, but can also be a corporation facility")
    pause_date: Optional[datetime] = Field(default=None, description="Date and time when this job was paused (i.e. time when the facility where this job was installed went offline)")
    probability: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Chance of success for invention")
    product_type_id: Optional[StrictInt] = Field(default=None, description="Type ID of product (manufactured, copied or invented)")
    runs: StrictInt = Field(description="Number of runs for a manufacturing job, or number of copies to make for a blueprint copy")
    start_date: datetime = Field(description="Date and time when this job started")
    station_id: StrictInt = Field(description="ID of the station where industry facility is located")
    status: StrictStr = Field(description="status string")
    successful_runs: Optional[StrictInt] = Field(default=None, description="Number of successful runs for this job. Equal to runs unless this is an invention job")
    __properties: ClassVar[List[str]] = ["activity_id", "blueprint_id", "blueprint_location_id", "blueprint_type_id", "completed_character_id", "completed_date", "cost", "duration", "end_date", "facility_id", "installer_id", "job_id", "licensed_runs", "output_location_id", "pause_date", "probability", "product_type_id", "runs", "start_date", "station_id", "status", "successful_runs"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('active', 'cancelled', 'delivered', 'paused', 'ready', 'reverted'):
            raise ValueError("must be one of enum values ('active', 'cancelled', 'delivered', 'paused', 'ready', 'reverted')")
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
        """Create an instance of GetCharactersCharacterIdIndustryJobs200Ok from a JSON string"""
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
        """Create an instance of GetCharactersCharacterIdIndustryJobs200Ok from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activity_id": obj.get("activity_id"),
            "blueprint_id": obj.get("blueprint_id"),
            "blueprint_location_id": obj.get("blueprint_location_id"),
            "blueprint_type_id": obj.get("blueprint_type_id"),
            "completed_character_id": obj.get("completed_character_id"),
            "completed_date": obj.get("completed_date"),
            "cost": obj.get("cost"),
            "duration": obj.get("duration"),
            "end_date": obj.get("end_date"),
            "facility_id": obj.get("facility_id"),
            "installer_id": obj.get("installer_id"),
            "job_id": obj.get("job_id"),
            "licensed_runs": obj.get("licensed_runs"),
            "output_location_id": obj.get("output_location_id"),
            "pause_date": obj.get("pause_date"),
            "probability": obj.get("probability"),
            "product_type_id": obj.get("product_type_id"),
            "runs": obj.get("runs"),
            "start_date": obj.get("start_date"),
            "station_id": obj.get("station_id"),
            "status": obj.get("status"),
            "successful_runs": obj.get("successful_runs")
        })
        return _obj


