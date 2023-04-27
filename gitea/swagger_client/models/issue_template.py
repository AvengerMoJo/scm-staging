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


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist
from swagger_client.models.issue_form_field import IssueFormField


class IssueTemplate(BaseModel):
    """
    IssueTemplate represents an issue template for a repository
    """

    about: Optional[StrictStr] = None
    body: Optional[conlist(IssueFormField)] = None
    content: Optional[StrictStr] = None
    file_name: Optional[StrictStr] = None
    labels: Optional[conlist(StrictStr)] = None
    name: Optional[StrictStr] = None
    ref: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    __properties = [
        "about",
        "body",
        "content",
        "file_name",
        "labels",
        "name",
        "ref",
        "title",
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
    def from_json(cls, json_str: str) -> IssueTemplate:
        """Create an instance of IssueTemplate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in body (list)
        _items = []
        if self.body:
            for _item in self.body:
                if _item:
                    _items.append(_item.to_dict())
            _dict["body"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IssueTemplate:
        """Create an instance of IssueTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IssueTemplate.parse_obj(obj)

        _obj = IssueTemplate.parse_obj(
            {
                "about": obj.get("about"),
                "body": [IssueFormField.from_dict(_item) for _item in obj.get("body")]
                if obj.get("body") is not None
                else None,
                "content": obj.get("content"),
                "file_name": obj.get("file_name"),
                "labels": obj.get("labels"),
                "name": obj.get("name"),
                "ref": obj.get("ref"),
                "title": obj.get("title"),
            }
        )
        return _obj
