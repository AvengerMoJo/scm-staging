# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr


class Cron(BaseModel):
    """
    Cron represents a Cron task
    """

    exec_times: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    next: Optional[datetime] = None
    prev: Optional[datetime] = None
    schedule: Optional[StrictStr] = None
    __properties = ["exec_times", "name", "next", "prev", "schedule"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Cron:
        """Create an instance of Cron from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Cron:
        """Create an instance of Cron from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Cron.parse_obj(obj)

        _obj = Cron.parse_obj(
            {
                "exec_times": obj.get("exec_times"),
                "name": obj.get("name"),
                "next": obj.get("next"),
                "prev": obj.get("prev"),
                "schedule": obj.get("schedule"),
            }
        )
        return _obj
