# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt


class GeneralAPISettings(BaseModel):
    """
    GeneralAPISettings contains global api settings exposed by it
    """

    default_git_trees_per_page: Optional[StrictInt] = None
    default_max_blob_size: Optional[StrictInt] = None
    default_paging_num: Optional[StrictInt] = None
    max_response_items: Optional[StrictInt] = None
    __properties = [
        "default_git_trees_per_page",
        "default_max_blob_size",
        "default_paging_num",
        "max_response_items",
    ]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GeneralAPISettings:
        """Create an instance of GeneralAPISettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GeneralAPISettings:
        """Create an instance of GeneralAPISettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GeneralAPISettings.parse_obj(obj)

        _obj = GeneralAPISettings.parse_obj(
            {
                "default_git_trees_per_page": obj.get("default_git_trees_per_page"),
                "default_max_blob_size": obj.get("default_max_blob_size"),
                "default_paging_num": obj.get("default_paging_num"),
                "max_response_items": obj.get("max_response_items"),
            }
        )
        return _obj
