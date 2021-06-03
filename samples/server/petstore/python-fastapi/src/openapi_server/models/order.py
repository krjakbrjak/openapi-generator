# coding: utf-8

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class Order(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Order - a model defined in OpenAPI

        id: The id of this Order [Optional].
        pet_id: The pet_id of this Order [Optional].
        quantity: The quantity of this Order [Optional].
        ship_date: The ship_date of this Order [Optional].
        status: The status of this Order [Optional].
        complete: The complete of this Order [Optional].
    """

    id: Optional[int] = None
    pet_id: Optional[int] = None
    quantity: Optional[int] = None
    ship_date: Optional[datetime] = None
    status: Optional[str] = None
    complete: Optional[bool] = None
