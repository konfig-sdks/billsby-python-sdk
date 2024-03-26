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


class ProductCreatePlanResponseCyclesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            cycleId = schemas.IntSchema
            planId = schemas.IntSchema
        
            @staticmethod
            def pricingModel() -> typing.Type['ProductCreatePlanResponseCyclesItemPricingModel']:
                return ProductCreatePlanResponseCyclesItemPricingModel
            visibility = schemas.StrSchema
            __annotations__ = {
                "cycleId": cycleId,
                "planId": planId,
                "pricingModel": pricingModel,
                "visibility": visibility,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cycleId"]) -> MetaOapg.properties.cycleId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["planId"]) -> MetaOapg.properties.planId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pricingModel"]) -> 'ProductCreatePlanResponseCyclesItemPricingModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibility"]) -> MetaOapg.properties.visibility: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cycleId", "planId", "pricingModel", "visibility", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cycleId"]) -> typing.Union[MetaOapg.properties.cycleId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["planId"]) -> typing.Union[MetaOapg.properties.planId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pricingModel"]) -> typing.Union['ProductCreatePlanResponseCyclesItemPricingModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibility"]) -> typing.Union[MetaOapg.properties.visibility, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cycleId", "planId", "pricingModel", "visibility", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cycleId: typing.Union[MetaOapg.properties.cycleId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        planId: typing.Union[MetaOapg.properties.planId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pricingModel: typing.Union['ProductCreatePlanResponseCyclesItemPricingModel', schemas.Unset] = schemas.unset,
        visibility: typing.Union[MetaOapg.properties.visibility, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProductCreatePlanResponseCyclesItem':
        return super().__new__(
            cls,
            *args,
            cycleId=cycleId,
            planId=planId,
            pricingModel=pricingModel,
            visibility=visibility,
            _configuration=_configuration,
            **kwargs,
        )

from billsby_python_sdk.model.product_create_plan_response_cycles_item_pricing_model import ProductCreatePlanResponseCyclesItemPricingModel
