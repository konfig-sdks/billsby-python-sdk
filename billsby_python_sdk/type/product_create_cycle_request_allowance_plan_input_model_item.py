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

from billsby_python_sdk.type.product_create_cycle_request_allowance_plan_input_model_item_allowance_price_models import ProductCreateCycleRequestAllowancePlanInputModelItemAllowancePriceModels

class RequiredProductCreateCycleRequestAllowancePlanInputModelItem(TypedDict):
    # Allowance ID to be attached to the cycle
    allowanceId: int

class OptionalProductCreateCycleRequestAllowancePlanInputModelItem(TypedDict, total=False):
    # Set mandatory
    isForced: bool

    allowancePriceModels: ProductCreateCycleRequestAllowancePlanInputModelItemAllowancePriceModels

class ProductCreateCycleRequestAllowancePlanInputModelItem(RequiredProductCreateCycleRequestAllowancePlanInputModelItem, OptionalProductCreateCycleRequestAllowancePlanInputModelItem):
    pass
