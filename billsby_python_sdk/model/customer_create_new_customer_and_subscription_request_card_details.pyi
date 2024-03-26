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


class CustomerCreateNewCustomerAndSubscriptionRequestCardDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The payment card details of the customer
    """


    class MetaOapg:
        
        class properties:
            fullName = schemas.StrSchema
            paymentCardToken = schemas.StrSchema
            expiryMonth = schemas.Int32Schema
            expiryYear = schemas.Int32Schema
            cardType = schemas.StrSchema
            last4Digits = schemas.StrSchema
            __annotations__ = {
                "fullName": fullName,
                "paymentCardToken": paymentCardToken,
                "expiryMonth": expiryMonth,
                "expiryYear": expiryYear,
                "cardType": cardType,
                "last4Digits": last4Digits,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fullName"]) -> MetaOapg.properties.fullName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentCardToken"]) -> MetaOapg.properties.paymentCardToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiryMonth"]) -> MetaOapg.properties.expiryMonth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiryYear"]) -> MetaOapg.properties.expiryYear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardType"]) -> MetaOapg.properties.cardType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last4Digits"]) -> MetaOapg.properties.last4Digits: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["fullName", "paymentCardToken", "expiryMonth", "expiryYear", "cardType", "last4Digits", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fullName"]) -> typing.Union[MetaOapg.properties.fullName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentCardToken"]) -> typing.Union[MetaOapg.properties.paymentCardToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiryMonth"]) -> typing.Union[MetaOapg.properties.expiryMonth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiryYear"]) -> typing.Union[MetaOapg.properties.expiryYear, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardType"]) -> typing.Union[MetaOapg.properties.cardType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last4Digits"]) -> typing.Union[MetaOapg.properties.last4Digits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fullName", "paymentCardToken", "expiryMonth", "expiryYear", "cardType", "last4Digits", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        fullName: typing.Union[MetaOapg.properties.fullName, str, schemas.Unset] = schemas.unset,
        paymentCardToken: typing.Union[MetaOapg.properties.paymentCardToken, str, schemas.Unset] = schemas.unset,
        expiryMonth: typing.Union[MetaOapg.properties.expiryMonth, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        expiryYear: typing.Union[MetaOapg.properties.expiryYear, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cardType: typing.Union[MetaOapg.properties.cardType, str, schemas.Unset] = schemas.unset,
        last4Digits: typing.Union[MetaOapg.properties.last4Digits, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomerCreateNewCustomerAndSubscriptionRequestCardDetails':
        return super().__new__(
            cls,
            *args,
            fullName=fullName,
            paymentCardToken=paymentCardToken,
            expiryMonth=expiryMonth,
            expiryYear=expiryYear,
            cardType=cardType,
            last4Digits=last4Digits,
            _configuration=_configuration,
            **kwargs,
        )
