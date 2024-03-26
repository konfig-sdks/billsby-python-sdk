# coding: utf-8

"""
    Billsby API

    Billsby is a feature-rich \"Saas\" recurring payment platform, ranked as the leading subscription billing software by G2.  Billsby is designed to ensure customers can go live quickly, often within 1-2 hours.  To help facilitate this process we have a team of friendly knowledgeable advisors ready to help your business go live.      Billsby specializes in providing great customer service at an affordable price point - our technology is rated No 1 on G2 by our customers.  If you are a developer creating a solution for your customer, Billsby has a friendly well-documented API.  The Billsby team are here to provide support to developers in order to ensure a smooth migration or new system build.   Why not book a call, talk through your Billing requirements and we can let you know how we can help you transform your business..

    The version of the OpenAPI document: 1.3.5
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from billsby_python_sdk import schemas  # noqa: F401


class SubscriptionChangePlanRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "customerUniqueId",
            "cycleId",
            "planId",
        }
        
        class properties:
            planId = schemas.Int32Schema
            cycleId = schemas.Int32Schema
            customerUniqueId = schemas.StrSchema
            planChangeType = schemas.Int32Schema
            units = schemas.Int32Schema
        
            @staticmethod
            def addOns() -> typing.Type['SubscriptionChangePlanRequestAddOns']:
                return SubscriptionChangePlanRequestAddOns
        
            @staticmethod
            def allowances() -> typing.Type['SubscriptionChangePlanRequestAllowances']:
                return SubscriptionChangePlanRequestAllowances
            issueRefund = schemas.BoolSchema
            __annotations__ = {
                "planId": planId,
                "cycleId": cycleId,
                "customerUniqueId": customerUniqueId,
                "planChangeType": planChangeType,
                "units": units,
                "addOns": addOns,
                "allowances": allowances,
                "issueRefund": issueRefund,
            }
    
    customerUniqueId: MetaOapg.properties.customerUniqueId
    cycleId: MetaOapg.properties.cycleId
    planId: MetaOapg.properties.planId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["planId"]) -> MetaOapg.properties.planId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cycleId"]) -> MetaOapg.properties.cycleId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerUniqueId"]) -> MetaOapg.properties.customerUniqueId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["planChangeType"]) -> MetaOapg.properties.planChangeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["units"]) -> MetaOapg.properties.units: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addOns"]) -> 'SubscriptionChangePlanRequestAddOns': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowances"]) -> 'SubscriptionChangePlanRequestAllowances': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issueRefund"]) -> MetaOapg.properties.issueRefund: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["planId", "cycleId", "customerUniqueId", "planChangeType", "units", "addOns", "allowances", "issueRefund", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["planId"]) -> MetaOapg.properties.planId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cycleId"]) -> MetaOapg.properties.cycleId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerUniqueId"]) -> MetaOapg.properties.customerUniqueId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["planChangeType"]) -> typing.Union[MetaOapg.properties.planChangeType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["units"]) -> typing.Union[MetaOapg.properties.units, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addOns"]) -> typing.Union['SubscriptionChangePlanRequestAddOns', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowances"]) -> typing.Union['SubscriptionChangePlanRequestAllowances', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issueRefund"]) -> typing.Union[MetaOapg.properties.issueRefund, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["planId", "cycleId", "customerUniqueId", "planChangeType", "units", "addOns", "allowances", "issueRefund", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        customerUniqueId: typing.Union[MetaOapg.properties.customerUniqueId, str, ],
        cycleId: typing.Union[MetaOapg.properties.cycleId, decimal.Decimal, int, ],
        planId: typing.Union[MetaOapg.properties.planId, decimal.Decimal, int, ],
        planChangeType: typing.Union[MetaOapg.properties.planChangeType, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        units: typing.Union[MetaOapg.properties.units, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        addOns: typing.Union['SubscriptionChangePlanRequestAddOns', schemas.Unset] = schemas.unset,
        allowances: typing.Union['SubscriptionChangePlanRequestAllowances', schemas.Unset] = schemas.unset,
        issueRefund: typing.Union[MetaOapg.properties.issueRefund, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SubscriptionChangePlanRequest':
        return super().__new__(
            cls,
            *args,
            customerUniqueId=customerUniqueId,
            cycleId=cycleId,
            planId=planId,
            planChangeType=planChangeType,
            units=units,
            addOns=addOns,
            allowances=allowances,
            issueRefund=issueRefund,
            _configuration=_configuration,
            **kwargs,
        )

from billsby_python_sdk.model.subscription_change_plan_request_add_ons import SubscriptionChangePlanRequestAddOns
from billsby_python_sdk.model.subscription_change_plan_request_allowances import SubscriptionChangePlanRequestAllowances
