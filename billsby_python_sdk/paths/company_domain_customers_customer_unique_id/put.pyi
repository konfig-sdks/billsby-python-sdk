# coding: utf-8

"""
    Billsby API

    Billsby is a feature-rich \"Saas\" recurring payment platform, ranked as the leading subscription billing software by G2.  Billsby is designed to ensure customers can go live quickly, often within 1-2 hours.  To help facilitate this process we have a team of friendly knowledgeable advisors ready to help your business go live.      Billsby specializes in providing great customer service at an affordable price point - our technology is rated No 1 on G2 by our customers.  If you are a developer creating a solution for your customer, Billsby has a friendly well-documented API.  The Billsby team are here to provide support to developers in order to ensure a smooth migration or new system build.   Why not book a call, talk through your Billing requirements and we can let you know how we can help you transform your business..

    The version of the OpenAPI document: 1.3.5
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from billsby_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from billsby_python_sdk.api_response import AsyncGeneratorResponse
from billsby_python_sdk import api_client, exceptions
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

from billsby_python_sdk.model.customer_update_details_request_billing_address import CustomerUpdateDetailsRequestBillingAddress as CustomerUpdateDetailsRequestBillingAddressSchema
from billsby_python_sdk.model.customer_update_details_response import CustomerUpdateDetailsResponse as CustomerUpdateDetailsResponseSchema
from billsby_python_sdk.model.customer_update_details_request import CustomerUpdateDetailsRequest as CustomerUpdateDetailsRequestSchema

from billsby_python_sdk.type.customer_update_details_request_billing_address import CustomerUpdateDetailsRequestBillingAddress
from billsby_python_sdk.type.customer_update_details_response import CustomerUpdateDetailsResponse
from billsby_python_sdk.type.customer_update_details_request import CustomerUpdateDetailsRequest

from ...api_client import Dictionary
from billsby_python_sdk.pydantic.customer_update_details_response import CustomerUpdateDetailsResponse as CustomerUpdateDetailsResponsePydantic
from billsby_python_sdk.pydantic.customer_update_details_request_billing_address import CustomerUpdateDetailsRequestBillingAddress as CustomerUpdateDetailsRequestBillingAddressPydantic
from billsby_python_sdk.pydantic.customer_update_details_request import CustomerUpdateDetailsRequest as CustomerUpdateDetailsRequestPydantic

# Path params
CompanyDomainSchema = schemas.StrSchema
CustomerUniqueIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'companyDomain': typing.Union[CompanyDomainSchema, str, ],
        'customerUniqueId': typing.Union[CustomerUniqueIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_company_domain = api_client.PathParameter(
    name="companyDomain",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CompanyDomainSchema,
    required=True,
)
request_path_customer_unique_id = api_client.PathParameter(
    name="customerUniqueId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CustomerUniqueIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = CustomerUpdateDetailsRequestSchema


request_body_customer_update_details_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = CustomerUpdateDetailsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CustomerUpdateDetailsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CustomerUpdateDetailsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_details_mapped_args(
        self,
        first_name: str,
        last_name: str,
        email: str,
        billing_address: CustomerUpdateDetailsRequestBillingAddress,
        company_domain: str,
        customer_unique_id: str,
        phone_number_dial_country: typing.Optional[str] = None,
        phone_number_dial_code: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if first_name is not None:
            _body["firstName"] = first_name
        if last_name is not None:
            _body["lastName"] = last_name
        if phone_number_dial_country is not None:
            _body["phoneNumberDialCountry"] = phone_number_dial_country
        if phone_number_dial_code is not None:
            _body["phoneNumberDialCode"] = phone_number_dial_code
        if email is not None:
            _body["email"] = email
        if phone_number is not None:
            _body["phoneNumber"] = phone_number
        if billing_address is not None:
            _body["billingAddress"] = billing_address
        args.body = _body
        if company_domain is not None:
            _path_params["companyDomain"] = company_domain
        if customer_unique_id is not None:
            _path_params["customerUniqueId"] = customer_unique_id
        args.path = _path_params
        return args

    async def _aupdate_details_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update customer
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_domain,
            request_path_customer_unique_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{companyDomain}/customers/{customerUniqueId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_customer_update_details_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _update_details_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update customer
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_domain,
            request_path_customer_unique_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{companyDomain}/customers/{customerUniqueId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_customer_update_details_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UpdateDetailsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_details(
        self,
        first_name: str,
        last_name: str,
        email: str,
        billing_address: CustomerUpdateDetailsRequestBillingAddress,
        company_domain: str,
        customer_unique_id: str,
        phone_number_dial_country: typing.Optional[str] = None,
        phone_number_dial_code: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_details_mapped_args(
            first_name=first_name,
            last_name=last_name,
            email=email,
            billing_address=billing_address,
            company_domain=company_domain,
            customer_unique_id=customer_unique_id,
            phone_number_dial_country=phone_number_dial_country,
            phone_number_dial_code=phone_number_dial_code,
            phone_number=phone_number,
        )
        return await self._aupdate_details_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_details(
        self,
        first_name: str,
        last_name: str,
        email: str,
        billing_address: CustomerUpdateDetailsRequestBillingAddress,
        company_domain: str,
        customer_unique_id: str,
        phone_number_dial_country: typing.Optional[str] = None,
        phone_number_dial_code: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_details_mapped_args(
            first_name=first_name,
            last_name=last_name,
            email=email,
            billing_address=billing_address,
            company_domain=company_domain,
            customer_unique_id=customer_unique_id,
            phone_number_dial_country=phone_number_dial_country,
            phone_number_dial_code=phone_number_dial_code,
            phone_number=phone_number,
        )
        return self._update_details_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateDetails(BaseApi):

    async def aupdate_details(
        self,
        first_name: str,
        last_name: str,
        email: str,
        billing_address: CustomerUpdateDetailsRequestBillingAddress,
        company_domain: str,
        customer_unique_id: str,
        phone_number_dial_country: typing.Optional[str] = None,
        phone_number_dial_code: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CustomerUpdateDetailsResponsePydantic:
        raw_response = await self.raw.aupdate_details(
            first_name=first_name,
            last_name=last_name,
            email=email,
            billing_address=billing_address,
            company_domain=company_domain,
            customer_unique_id=customer_unique_id,
            phone_number_dial_country=phone_number_dial_country,
            phone_number_dial_code=phone_number_dial_code,
            phone_number=phone_number,
            **kwargs,
        )
        if validate:
            return CustomerUpdateDetailsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CustomerUpdateDetailsResponsePydantic, raw_response.body)
    
    
    def update_details(
        self,
        first_name: str,
        last_name: str,
        email: str,
        billing_address: CustomerUpdateDetailsRequestBillingAddress,
        company_domain: str,
        customer_unique_id: str,
        phone_number_dial_country: typing.Optional[str] = None,
        phone_number_dial_code: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CustomerUpdateDetailsResponsePydantic:
        raw_response = self.raw.update_details(
            first_name=first_name,
            last_name=last_name,
            email=email,
            billing_address=billing_address,
            company_domain=company_domain,
            customer_unique_id=customer_unique_id,
            phone_number_dial_country=phone_number_dial_country,
            phone_number_dial_code=phone_number_dial_code,
            phone_number=phone_number,
        )
        if validate:
            return CustomerUpdateDetailsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CustomerUpdateDetailsResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        first_name: str,
        last_name: str,
        email: str,
        billing_address: CustomerUpdateDetailsRequestBillingAddress,
        company_domain: str,
        customer_unique_id: str,
        phone_number_dial_country: typing.Optional[str] = None,
        phone_number_dial_code: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_details_mapped_args(
            first_name=first_name,
            last_name=last_name,
            email=email,
            billing_address=billing_address,
            company_domain=company_domain,
            customer_unique_id=customer_unique_id,
            phone_number_dial_country=phone_number_dial_country,
            phone_number_dial_code=phone_number_dial_code,
            phone_number=phone_number,
        )
        return await self._aupdate_details_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        first_name: str,
        last_name: str,
        email: str,
        billing_address: CustomerUpdateDetailsRequestBillingAddress,
        company_domain: str,
        customer_unique_id: str,
        phone_number_dial_country: typing.Optional[str] = None,
        phone_number_dial_code: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_details_mapped_args(
            first_name=first_name,
            last_name=last_name,
            email=email,
            billing_address=billing_address,
            company_domain=company_domain,
            customer_unique_id=customer_unique_id,
            phone_number_dial_country=phone_number_dial_country,
            phone_number_dial_code=phone_number_dial_code,
            phone_number=phone_number,
        )
        return self._update_details_oapg(
            body=args.body,
            path_params=args.path,
        )

