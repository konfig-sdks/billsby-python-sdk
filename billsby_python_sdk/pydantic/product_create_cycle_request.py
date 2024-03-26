# coding: utf-8

"""
    Billsby API

    Billsby is a feature-rich \"Saas\" recurring payment platform, ranked as the leading subscription billing software by G2.  Billsby is designed to ensure customers can go live quickly, often within 1-2 hours.  To help facilitate this process we have a team of friendly knowledgeable advisors ready to help your business go live.      Billsby specializes in providing great customer service at an affordable price point - our technology is rated No 1 on G2 by our customers.  If you are a developer creating a solution for your customer, Billsby has a friendly well-documented API.  The Billsby team are here to provide support to developers in order to ensure a smooth migration or new system build.   Why not book a call, talk through your Billing requirements and we can let you know how we can help you transform your business..

    The version of the OpenAPI document: 1.3.5
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from billsby_python_sdk.pydantic.product_create_cycle_request_addon_plan_input_models import ProductCreateCycleRequestAddonPlanInputModels
from billsby_python_sdk.pydantic.product_create_cycle_request_allowance_plan_input_model import ProductCreateCycleRequestAllowancePlanInputModel
from billsby_python_sdk.pydantic.product_create_cycle_request_cycles_input_model import ProductCreateCycleRequestCyclesInputModel

class ProductCreateCycleRequest(BaseModel):
    cycles_input_model: ProductCreateCycleRequestCyclesInputModel = Field(alias='cyclesInputModel')

    addon_plan_input_models: ProductCreateCycleRequestAddonPlanInputModels = Field(alias='addonPlanInputModels')

    allowance_plan_input_model: typing.Optional[ProductCreateCycleRequestAllowancePlanInputModel] = Field(None, alias='allowancePlanInputModel')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
