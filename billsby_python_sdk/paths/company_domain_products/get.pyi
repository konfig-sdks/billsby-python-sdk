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

from billsby_python_sdk.model.product_list_products_response import ProductListProductsResponse as ProductListProductsResponseSchema

from billsby_python_sdk.type.product_list_products_response import ProductListProductsResponse

from ...api_client import Dictionary
from billsby_python_sdk.pydantic.product_list_products_response import ProductListProductsResponse as ProductListProductsResponsePydantic

# Query params
PageSchema = schemas.Int32Schema
PageSizeSchema = schemas.Int32Schema
SearchSchema = schemas.StrSchema
VisibilityTypeSchema = schemas.Int32Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'pageSize': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'search': typing.Union[SearchSchema, str, ],
        'visibilityType': typing.Union[VisibilityTypeSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    required=True,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="pageSize",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    required=True,
    explode=True,
)
request_query_search = api_client.QueryParameter(
    name="search",
    style=api_client.ParameterStyle.FORM,
    schema=SearchSchema,
    explode=True,
)
request_query_visibility_type = api_client.QueryParameter(
    name="visibilityType",
    style=api_client.ParameterStyle.FORM,
    schema=VisibilityTypeSchema,
    explode=True,
)
# Path params
CompanyDomainSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'companyDomain': typing.Union[CompanyDomainSchema, str, ],
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
SchemaFor200ResponseBodyApplicationJson = ProductListProductsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ProductListProductsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ProductListProductsResponse


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

    def _list_products_mapped_args(
        self,
        company_domain: str,
        page: int,
        page_size: int,
        search: typing.Optional[str] = None,
        visibility_type: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if page is not None:
            _query_params["page"] = page
        if page_size is not None:
            _query_params["pageSize"] = page_size
        if search is not None:
            _query_params["search"] = search
        if visibility_type is not None:
            _query_params["visibilityType"] = visibility_type
        if company_domain is not None:
            _path_params["companyDomain"] = company_domain
        args.query = _query_params
        args.path = _path_params
        return args

    async def _alist_products_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List products
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_domain,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_page,
            request_query_page_size,
            request_query_search,
            request_query_visibility_type,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{companyDomain}/products',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _list_products_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List products
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_domain,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_page,
            request_query_page_size,
            request_query_search,
            request_query_visibility_type,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{companyDomain}/products',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class ListProductsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_products(
        self,
        company_domain: str,
        page: int,
        page_size: int,
        search: typing.Optional[str] = None,
        visibility_type: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_products_mapped_args(
            company_domain=company_domain,
            page=page,
            page_size=page_size,
            search=search,
            visibility_type=visibility_type,
        )
        return await self._alist_products_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def list_products(
        self,
        company_domain: str,
        page: int,
        page_size: int,
        search: typing.Optional[str] = None,
        visibility_type: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_products_mapped_args(
            company_domain=company_domain,
            page=page,
            page_size=page_size,
            search=search,
            visibility_type=visibility_type,
        )
        return self._list_products_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class ListProducts(BaseApi):

    async def alist_products(
        self,
        company_domain: str,
        page: int,
        page_size: int,
        search: typing.Optional[str] = None,
        visibility_type: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> ProductListProductsResponsePydantic:
        raw_response = await self.raw.alist_products(
            company_domain=company_domain,
            page=page,
            page_size=page_size,
            search=search,
            visibility_type=visibility_type,
            **kwargs,
        )
        if validate:
            return ProductListProductsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ProductListProductsResponsePydantic, raw_response.body)
    
    
    def list_products(
        self,
        company_domain: str,
        page: int,
        page_size: int,
        search: typing.Optional[str] = None,
        visibility_type: typing.Optional[int] = None,
        validate: bool = False,
    ) -> ProductListProductsResponsePydantic:
        raw_response = self.raw.list_products(
            company_domain=company_domain,
            page=page,
            page_size=page_size,
            search=search,
            visibility_type=visibility_type,
        )
        if validate:
            return ProductListProductsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ProductListProductsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        company_domain: str,
        page: int,
        page_size: int,
        search: typing.Optional[str] = None,
        visibility_type: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_products_mapped_args(
            company_domain=company_domain,
            page=page,
            page_size=page_size,
            search=search,
            visibility_type=visibility_type,
        )
        return await self._alist_products_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        company_domain: str,
        page: int,
        page_size: int,
        search: typing.Optional[str] = None,
        visibility_type: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_products_mapped_args(
            company_domain=company_domain,
            page=page,
            page_size=page_size,
            search=search,
            visibility_type=visibility_type,
        )
        return self._list_products_oapg(
            query_params=args.query,
            path_params=args.path,
        )

