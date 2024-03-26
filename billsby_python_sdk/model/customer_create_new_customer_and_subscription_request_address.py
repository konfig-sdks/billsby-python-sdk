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


class CustomerCreateNewCustomerAndSubscriptionRequestAddress(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The customer's address
    """


    class MetaOapg:
        
        class properties:
            addressLine1 = schemas.StrSchema
            addressLine2 = schemas.StrSchema
            state = schemas.StrSchema
            city = schemas.StrSchema
            country = schemas.StrSchema
            postCode = schemas.StrSchema
            __annotations__ = {
                "addressLine1": addressLine1,
                "addressLine2": addressLine2,
                "state": state,
                "city": city,
                "country": country,
                "postCode": postCode,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressLine1"]) -> MetaOapg.properties.addressLine1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressLine2"]) -> MetaOapg.properties.addressLine2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postCode"]) -> MetaOapg.properties.postCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["addressLine1", "addressLine2", "state", "city", "country", "postCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressLine1"]) -> typing.Union[MetaOapg.properties.addressLine1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressLine2"]) -> typing.Union[MetaOapg.properties.addressLine2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postCode"]) -> typing.Union[MetaOapg.properties.postCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["addressLine1", "addressLine2", "state", "city", "country", "postCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        addressLine1: typing.Union[MetaOapg.properties.addressLine1, str, schemas.Unset] = schemas.unset,
        addressLine2: typing.Union[MetaOapg.properties.addressLine2, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        postCode: typing.Union[MetaOapg.properties.postCode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomerCreateNewCustomerAndSubscriptionRequestAddress':
        return super().__new__(
            cls,
            *args,
            addressLine1=addressLine1,
            addressLine2=addressLine2,
            state=state,
            city=city,
            country=country,
            postCode=postCode,
            _configuration=_configuration,
            **kwargs,
        )
