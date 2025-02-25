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


class SubscriptionListSubscriptionsResponseResultsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            subscriptionId = schemas.IntSchema
            subscriptionUniqueID = schemas.StrSchema
            customerId = schemas.IntSchema
            customerUniqueId = schemas.StrSchema
            customerEmail = schemas.StrSchema
            customerFullname = schemas.StrSchema
            planId = schemas.StrSchema
            planName = schemas.StrSchema
            productId = schemas.StrSchema
            productName = schemas.StrSchema
            createdOn = schemas.StrSchema
            status = schemas.StrSchema
            isInFreeTrial = schemas.BoolSchema
            __annotations__ = {
                "subscriptionId": subscriptionId,
                "subscriptionUniqueID": subscriptionUniqueID,
                "customerId": customerId,
                "customerUniqueId": customerUniqueId,
                "customerEmail": customerEmail,
                "customerFullname": customerFullname,
                "planId": planId,
                "planName": planName,
                "productId": productId,
                "productName": productName,
                "createdOn": createdOn,
                "status": status,
                "isInFreeTrial": isInFreeTrial,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriptionId"]) -> MetaOapg.properties.subscriptionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriptionUniqueID"]) -> MetaOapg.properties.subscriptionUniqueID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerUniqueId"]) -> MetaOapg.properties.customerUniqueId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerEmail"]) -> MetaOapg.properties.customerEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerFullname"]) -> MetaOapg.properties.customerFullname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["planId"]) -> MetaOapg.properties.planId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["planName"]) -> MetaOapg.properties.planName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productId"]) -> MetaOapg.properties.productId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productName"]) -> MetaOapg.properties.productName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdOn"]) -> MetaOapg.properties.createdOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isInFreeTrial"]) -> MetaOapg.properties.isInFreeTrial: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["subscriptionId", "subscriptionUniqueID", "customerId", "customerUniqueId", "customerEmail", "customerFullname", "planId", "planName", "productId", "productName", "createdOn", "status", "isInFreeTrial", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriptionId"]) -> typing.Union[MetaOapg.properties.subscriptionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriptionUniqueID"]) -> typing.Union[MetaOapg.properties.subscriptionUniqueID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerId"]) -> typing.Union[MetaOapg.properties.customerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerUniqueId"]) -> typing.Union[MetaOapg.properties.customerUniqueId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerEmail"]) -> typing.Union[MetaOapg.properties.customerEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerFullname"]) -> typing.Union[MetaOapg.properties.customerFullname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["planId"]) -> typing.Union[MetaOapg.properties.planId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["planName"]) -> typing.Union[MetaOapg.properties.planName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productId"]) -> typing.Union[MetaOapg.properties.productId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productName"]) -> typing.Union[MetaOapg.properties.productName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdOn"]) -> typing.Union[MetaOapg.properties.createdOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isInFreeTrial"]) -> typing.Union[MetaOapg.properties.isInFreeTrial, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["subscriptionId", "subscriptionUniqueID", "customerId", "customerUniqueId", "customerEmail", "customerFullname", "planId", "planName", "productId", "productName", "createdOn", "status", "isInFreeTrial", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        subscriptionId: typing.Union[MetaOapg.properties.subscriptionId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        subscriptionUniqueID: typing.Union[MetaOapg.properties.subscriptionUniqueID, str, schemas.Unset] = schemas.unset,
        customerId: typing.Union[MetaOapg.properties.customerId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        customerUniqueId: typing.Union[MetaOapg.properties.customerUniqueId, str, schemas.Unset] = schemas.unset,
        customerEmail: typing.Union[MetaOapg.properties.customerEmail, str, schemas.Unset] = schemas.unset,
        customerFullname: typing.Union[MetaOapg.properties.customerFullname, str, schemas.Unset] = schemas.unset,
        planId: typing.Union[MetaOapg.properties.planId, str, schemas.Unset] = schemas.unset,
        planName: typing.Union[MetaOapg.properties.planName, str, schemas.Unset] = schemas.unset,
        productId: typing.Union[MetaOapg.properties.productId, str, schemas.Unset] = schemas.unset,
        productName: typing.Union[MetaOapg.properties.productName, str, schemas.Unset] = schemas.unset,
        createdOn: typing.Union[MetaOapg.properties.createdOn, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        isInFreeTrial: typing.Union[MetaOapg.properties.isInFreeTrial, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SubscriptionListSubscriptionsResponseResultsItem':
        return super().__new__(
            cls,
            *args,
            subscriptionId=subscriptionId,
            subscriptionUniqueID=subscriptionUniqueID,
            customerId=customerId,
            customerUniqueId=customerUniqueId,
            customerEmail=customerEmail,
            customerFullname=customerFullname,
            planId=planId,
            planName=planName,
            productId=productId,
            productName=productName,
            createdOn=createdOn,
            status=status,
            isInFreeTrial=isInFreeTrial,
            _configuration=_configuration,
            **kwargs,
        )
