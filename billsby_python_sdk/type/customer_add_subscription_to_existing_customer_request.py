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

from billsby_python_sdk.type.customer_add_subscription_to_existing_customer_request_add_ons import CustomerAddSubscriptionToExistingCustomerRequestAddOns
from billsby_python_sdk.type.customer_add_subscription_to_existing_customer_request_address import CustomerAddSubscriptionToExistingCustomerRequestAddress
from billsby_python_sdk.type.customer_add_subscription_to_existing_customer_request_coupon_codes import CustomerAddSubscriptionToExistingCustomerRequestCouponCodes
from billsby_python_sdk.type.customer_add_subscription_to_existing_customer_request_custom_field_response import CustomerAddSubscriptionToExistingCustomerRequestCustomFieldResponse

class RequiredCustomerAddSubscriptionToExistingCustomerRequest(TypedDict):
    # The unique identifier of the cycle in the Billsby platform
    cycleId: int

class OptionalCustomerAddSubscriptionToExistingCustomerRequest(TypedDict, total=False):
    # The number of units for unit based plans
    units: int

    address: CustomerAddSubscriptionToExistingCustomerRequestAddress

    # The shipping address of the customer
    shippingAddress: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Any additional email addresses given by the customer
    additionalEmail: str

    # The country associated with the phone number
    phoneNumberDialCountry: str

    # The country dial code for the customer phone number
    phoneNumberDialCode: int

    # The customer's phone number
    phoneNumber: int

    # Gas the customer given marketing consent: true or false
    marketingConsent: bool

    # Tax registration number
    taxRegNumber: str

    ipAddress: str

    customFieldResponse: CustomerAddSubscriptionToExistingCustomerRequestCustomFieldResponse

    addOns: CustomerAddSubscriptionToExistingCustomerRequestAddOns

    # Any allowances to be included with the plan
    allowances: int

    couponCodes: CustomerAddSubscriptionToExistingCustomerRequestCouponCodes

class CustomerAddSubscriptionToExistingCustomerRequest(RequiredCustomerAddSubscriptionToExistingCustomerRequest, OptionalCustomerAddSubscriptionToExistingCustomerRequest):
    pass
