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


class ProductCreateCycleRequestCyclesInputModelItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "visibility",
            "price",
            "frequencyType",
            "billingDateType",
            "frequency",
        }
        
        class properties:
            frequency = schemas.Int32Schema
            frequencyType = schemas.Int32Schema
            price = schemas.Int32Schema
            billingDateType = schemas.Int32Schema
            visibility = schemas.Int32Schema
            freeTrial = schemas.Int32Schema
            freeTrialFrequencyType = schemas.Int32Schema
            contractTerm = schemas.Int32Schema
            contractTermFrequencyType = schemas.Int32Schema
            setupFeePrice = schemas.Int32Schema
            freeQuantity = schemas.Int32Schema
            fixedBillingDateDay = schemas.Int32Schema
            fixedBillingDateMonth = schemas.Int32Schema
            proRateOption = schemas.Int32Schema
        
            @staticmethod
            def tiers() -> typing.Type['ProductCreateCycleRequestCyclesInputModelItemTiers']:
                return ProductCreateCycleRequestCyclesInputModelItemTiers
            __annotations__ = {
                "frequency": frequency,
                "frequencyType": frequencyType,
                "price": price,
                "billingDateType": billingDateType,
                "visibility": visibility,
                "freeTrial": freeTrial,
                "freeTrialFrequencyType": freeTrialFrequencyType,
                "contractTerm": contractTerm,
                "contractTermFrequencyType": contractTermFrequencyType,
                "setupFeePrice": setupFeePrice,
                "freeQuantity": freeQuantity,
                "fixedBillingDateDay": fixedBillingDateDay,
                "fixedBillingDateMonth": fixedBillingDateMonth,
                "proRateOption": proRateOption,
                "tiers": tiers,
            }
    
    visibility: MetaOapg.properties.visibility
    price: MetaOapg.properties.price
    frequencyType: MetaOapg.properties.frequencyType
    billingDateType: MetaOapg.properties.billingDateType
    frequency: MetaOapg.properties.frequency
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequency"]) -> MetaOapg.properties.frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequencyType"]) -> MetaOapg.properties.frequencyType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingDateType"]) -> MetaOapg.properties.billingDateType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibility"]) -> MetaOapg.properties.visibility: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["freeTrial"]) -> MetaOapg.properties.freeTrial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["freeTrialFrequencyType"]) -> MetaOapg.properties.freeTrialFrequencyType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractTerm"]) -> MetaOapg.properties.contractTerm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractTermFrequencyType"]) -> MetaOapg.properties.contractTermFrequencyType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["setupFeePrice"]) -> MetaOapg.properties.setupFeePrice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["freeQuantity"]) -> MetaOapg.properties.freeQuantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fixedBillingDateDay"]) -> MetaOapg.properties.fixedBillingDateDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fixedBillingDateMonth"]) -> MetaOapg.properties.fixedBillingDateMonth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["proRateOption"]) -> MetaOapg.properties.proRateOption: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tiers"]) -> 'ProductCreateCycleRequestCyclesInputModelItemTiers': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["frequency", "frequencyType", "price", "billingDateType", "visibility", "freeTrial", "freeTrialFrequencyType", "contractTerm", "contractTermFrequencyType", "setupFeePrice", "freeQuantity", "fixedBillingDateDay", "fixedBillingDateMonth", "proRateOption", "tiers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequency"]) -> MetaOapg.properties.frequency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequencyType"]) -> MetaOapg.properties.frequencyType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingDateType"]) -> MetaOapg.properties.billingDateType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibility"]) -> MetaOapg.properties.visibility: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["freeTrial"]) -> typing.Union[MetaOapg.properties.freeTrial, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["freeTrialFrequencyType"]) -> typing.Union[MetaOapg.properties.freeTrialFrequencyType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractTerm"]) -> typing.Union[MetaOapg.properties.contractTerm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractTermFrequencyType"]) -> typing.Union[MetaOapg.properties.contractTermFrequencyType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["setupFeePrice"]) -> typing.Union[MetaOapg.properties.setupFeePrice, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["freeQuantity"]) -> typing.Union[MetaOapg.properties.freeQuantity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fixedBillingDateDay"]) -> typing.Union[MetaOapg.properties.fixedBillingDateDay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fixedBillingDateMonth"]) -> typing.Union[MetaOapg.properties.fixedBillingDateMonth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["proRateOption"]) -> typing.Union[MetaOapg.properties.proRateOption, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tiers"]) -> typing.Union['ProductCreateCycleRequestCyclesInputModelItemTiers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["frequency", "frequencyType", "price", "billingDateType", "visibility", "freeTrial", "freeTrialFrequencyType", "contractTerm", "contractTermFrequencyType", "setupFeePrice", "freeQuantity", "fixedBillingDateDay", "fixedBillingDateMonth", "proRateOption", "tiers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        visibility: typing.Union[MetaOapg.properties.visibility, decimal.Decimal, int, ],
        price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, ],
        frequencyType: typing.Union[MetaOapg.properties.frequencyType, decimal.Decimal, int, ],
        billingDateType: typing.Union[MetaOapg.properties.billingDateType, decimal.Decimal, int, ],
        frequency: typing.Union[MetaOapg.properties.frequency, decimal.Decimal, int, ],
        freeTrial: typing.Union[MetaOapg.properties.freeTrial, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        freeTrialFrequencyType: typing.Union[MetaOapg.properties.freeTrialFrequencyType, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        contractTerm: typing.Union[MetaOapg.properties.contractTerm, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        contractTermFrequencyType: typing.Union[MetaOapg.properties.contractTermFrequencyType, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        setupFeePrice: typing.Union[MetaOapg.properties.setupFeePrice, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        freeQuantity: typing.Union[MetaOapg.properties.freeQuantity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        fixedBillingDateDay: typing.Union[MetaOapg.properties.fixedBillingDateDay, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        fixedBillingDateMonth: typing.Union[MetaOapg.properties.fixedBillingDateMonth, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        proRateOption: typing.Union[MetaOapg.properties.proRateOption, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tiers: typing.Union['ProductCreateCycleRequestCyclesInputModelItemTiers', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProductCreateCycleRequestCyclesInputModelItem':
        return super().__new__(
            cls,
            *args,
            visibility=visibility,
            price=price,
            frequencyType=frequencyType,
            billingDateType=billingDateType,
            frequency=frequency,
            freeTrial=freeTrial,
            freeTrialFrequencyType=freeTrialFrequencyType,
            contractTerm=contractTerm,
            contractTermFrequencyType=contractTermFrequencyType,
            setupFeePrice=setupFeePrice,
            freeQuantity=freeQuantity,
            fixedBillingDateDay=fixedBillingDateDay,
            fixedBillingDateMonth=fixedBillingDateMonth,
            proRateOption=proRateOption,
            tiers=tiers,
            _configuration=_configuration,
            **kwargs,
        )

from billsby_python_sdk.model.product_create_cycle_request_cycles_input_model_item_tiers import ProductCreateCycleRequestCyclesInputModelItemTiers
