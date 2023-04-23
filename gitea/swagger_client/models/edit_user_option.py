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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EditUserOption(BaseModel):
    """
    EditUserOption edit user options
    """

    active: Optional[StrictBool] = None
    admin: Optional[StrictBool] = None
    allow_create_organization: Optional[StrictBool] = None
    allow_git_hook: Optional[StrictBool] = None
    allow_import_local: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    login_name: StrictStr = ...
    max_repo_creation: Optional[StrictInt] = None
    must_change_password: Optional[StrictBool] = None
    password: Optional[StrictStr] = None
    prohibit_login: Optional[StrictBool] = None
    restricted: Optional[StrictBool] = None
    source_id: StrictInt = ...
    visibility: Optional[StrictStr] = None
    website: Optional[StrictStr] = None
    __properties = [
        "active",
        "admin",
        "allow_create_organization",
        "allow_git_hook",
        "allow_import_local",
        "description",
        "email",
        "full_name",
        "location",
        "login_name",
        "max_repo_creation",
        "must_change_password",
        "password",
        "prohibit_login",
        "restricted",
        "source_id",
        "visibility",
        "website",
    ]

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
    def from_json(cls, json_str: str) -> EditUserOption:
        """Create an instance of EditUserOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EditUserOption:
        """Create an instance of EditUserOption from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EditUserOption.parse_obj(obj)

        _obj = EditUserOption.parse_obj(
            {
                "active": obj.get("active"),
                "admin": obj.get("admin"),
                "allow_create_organization": obj.get("allow_create_organization"),
                "allow_git_hook": obj.get("allow_git_hook"),
                "allow_import_local": obj.get("allow_import_local"),
                "description": obj.get("description"),
                "email": obj.get("email"),
                "full_name": obj.get("full_name"),
                "location": obj.get("location"),
                "login_name": obj.get("login_name"),
                "max_repo_creation": obj.get("max_repo_creation"),
                "must_change_password": obj.get("must_change_password"),
                "password": obj.get("password"),
                "prohibit_login": obj.get("prohibit_login"),
                "restricted": obj.get("restricted"),
                "source_id": obj.get("source_id"),
                "visibility": obj.get("visibility"),
                "website": obj.get("website"),
            }
        )
        return _obj
