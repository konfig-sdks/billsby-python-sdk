# coding: utf-8

"""
    Billsby API

    Billsby is a feature-rich \"Saas\" recurring payment platform, ranked as the leading subscription billing software by G2.  Billsby is designed to ensure customers can go live quickly, often within 1-2 hours.  To help facilitate this process we have a team of friendly knowledgeable advisors ready to help your business go live.      Billsby specializes in providing great customer service at an affordable price point - our technology is rated No 1 on G2 by our customers.  If you are a developer creating a solution for your customer, Billsby has a friendly well-documented API.  The Billsby team are here to provide support to developers in order to ensure a smooth migration or new system build.   Why not book a call, talk through your Billing requirements and we can let you know how we can help you transform your business..

    The version of the OpenAPI document: 1.3.5
    Generated by: https://konfigthis.com
"""

from billsby_python_sdk.paths.company_domain_allowances_allowance_id.get import GetDetails
from billsby_python_sdk.paths.company_domain_allowances.get import GetList
from billsby_python_sdk.paths.company_domain_subscriptions_subscription_unique_id_allowances.get import GetSpecificSubscriptionAllowances
from billsby_python_sdk.apis.tags.allowance_api_raw import AllowanceApiRaw


class AllowanceApi(
    GetDetails,
    GetList,
    GetSpecificSubscriptionAllowances,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AllowanceApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AllowanceApiRaw(api_client)
