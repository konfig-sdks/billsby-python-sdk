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

from billsby_python_sdk.pydantic.product_create_cycle_request_addon_plan_input_models_item_addon_price_models_item_unit_tiers import ProductCreateCycleRequestAddonPlanInputModelsItemAddonPriceModelsItemUnitTiers

class ProductCreateCycleRequestAddonPlanInputModelsItemAddonPriceModelsItem(BaseModel):
    # Currency ISO3 Code (for example: USD)
    currency_iso3_code: typing.Optional[str] = Field(None, alias='currencyIso3Code')

    # A number with the update frequency (for example: 5 to renew every five of frequencyType)
    frequency: typing.Optional[int] = Field(None, alias='frequency')

    # Daily = 1, Weekly = 2, Monthly = 3, Yearly = 4
    frequency_type: typing.Optional[int] = Field(None, alias='frequencyType')

    flat_fee_price: typing.Optional[int] = Field(None, alias='flatFeePrice')

    price_per_unit: typing.Optional[int] = Field(None, alias='pricePerUnit')

    unit_tiers: typing.Optional[ProductCreateCycleRequestAddonPlanInputModelsItemAddonPriceModelsItemUnitTiers] = Field(None, alias='unitTiers')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
