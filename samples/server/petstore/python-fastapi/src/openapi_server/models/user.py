# coding: utf-8

from datetime import date, datetime

from typing import Dict, List, Optional

from pydantic import BaseModel, EmailStr, validator


class User(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    User - a model defined in OpenAPI

        id: The id of this User [Optional].
        username: The username of this User [Optional].
        first_name: The first_name of this User [Optional].
        last_name: The last_name of this User [Optional].
        email: The email of this User [Optional].
        password: The password of this User [Optional].
        phone: The phone of this User [Optional].
        user_status: The user_status of this User [Optional].
    """

    id: Optional[int] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    user_status: Optional[int] = None
