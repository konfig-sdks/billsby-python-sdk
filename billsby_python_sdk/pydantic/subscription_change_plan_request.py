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

from billsby_python_sdk.pydantic.subscription_change_plan_request_add_ons import SubscriptionChangePlanRequestAddOns
from billsby_python_sdk.pydantic.subscription_change_plan_request_allowances import SubscriptionChangePlanRequestAllowances

class SubscriptionChangePlanRequest(BaseModel):
    # The unique identifier of the plan that you want to change the subscription to in the Billsby platform
    plan_id: int = Field(alias='planId')

    # The unique identifier of the cycle that you want to change the subscription to in the Billsby platform
    cycle_id: int = Field(alias='cycleId')

    # The unique identifier of the subscription in the Billsby platform
    customer_unique_id: str = Field(alias='customerUniqueId')

    # Immediate = 1 OnRenewal = 2
    plan_change_type: typing.Optional[int] = Field(None, alias='planChangeType')

    # The number of units required (for cycles with mulitple units allowed)
    units: typing.Optional[int] = Field(None, alias='units')

    add_ons: typing.Optional[SubscriptionChangePlanRequestAddOns] = Field(None, alias='addOns')

    allowances: typing.Optional[SubscriptionChangePlanRequestAllowances] = Field(None, alias='allowances')

    # In case of immediate change, this will apply a refund into the first invoice of the new plan based on the prorated amount of the current plan
    issue_refund: typing.Optional[bool] = Field(None, alias='issueRefund')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
