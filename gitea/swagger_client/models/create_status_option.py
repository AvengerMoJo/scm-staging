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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr


class CreateStatusOption(BaseModel):
    """
    CreateStatusOption holds the information needed to create a new CommitStatus for a Commit
    """

    context: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    state: Optional[StrictStr] = Field(
        None,
        description='CommitStatusState holds the state of a CommitStatus It can be "pending", "success", "error", "failure", and "warning"',
    )
    target_url: Optional[StrictStr] = None
    __properties = ["context", "description", "state", "target_url"]

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
    def from_json(cls, json_str: str) -> CreateStatusOption:
        """Create an instance of CreateStatusOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateStatusOption:
        """Create an instance of CreateStatusOption from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CreateStatusOption.parse_obj(obj)

        _obj = CreateStatusOption.parse_obj(
            {
                "context": obj.get("context"),
                "description": obj.get("description"),
                "state": obj.get("state"),
                "target_url": obj.get("target_url"),
            }
        )
        return _obj
