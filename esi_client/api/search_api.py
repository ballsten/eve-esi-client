# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    The version of the OpenAPI document: 1.19
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictBool, StrictStr, field_validator

from typing import List, Optional

from esi_client.models.get_characters_character_id_search_ok import GetCharactersCharacterIdSearchOk

from esi_client.api_client import ApiClient
from esi_client.api_response import ApiResponse
from esi_client.rest import RESTResponseType


class SearchApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_characters_character_id_search(
        self,
        categories: Annotated[List[StrictStr], Field(min_length=1, max_length=11, description="Type of entities to search for")],
        character_id: Annotated[int, Field(strict=True, ge=1, description="An EVE character ID")],
        search: Annotated[str, Field(min_length=3, strict=True, description="The string to search on")],
        accept_language: Annotated[Optional[StrictStr], Field(description="Language to use in the response")] = None,
        datasource: Annotated[Optional[StrictStr], Field(description="The server name you would like data from")] = None,
        if_none_match: Annotated[Optional[StrictStr], Field(description="ETag from a previous request. A 304 will be returned if this matches the current ETag")] = None,
        language: Annotated[Optional[StrictStr], Field(description="Language to use in the response, takes precedence over Accept-Language")] = None,
        strict: Annotated[Optional[StrictBool], Field(description="Whether the search should be a strict match")] = None,
        token: Annotated[Optional[StrictStr], Field(description="Access token to use if unable to set a header")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> GetCharactersCharacterIdSearchOk:
        """Search on a string

        Search for entities that match a given sub-string.  --- Alternate route: `/dev/characters/{character_id}/search/`  Alternate route: `/legacy/characters/{character_id}/search/`  Alternate route: `/v3/characters/{character_id}/search/`  --- This route is cached for up to 3600 seconds

        :param categories: Type of entities to search for (required)
        :type categories: List[str]
        :param character_id: An EVE character ID (required)
        :type character_id: int
        :param search: The string to search on (required)
        :type search: str
        :param accept_language: Language to use in the response
        :type accept_language: str
        :param datasource: The server name you would like data from
        :type datasource: str
        :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :type if_none_match: str
        :param language: Language to use in the response, takes precedence over Accept-Language
        :type language: str
        :param strict: Whether the search should be a strict match
        :type strict: bool
        :param token: Access token to use if unable to set a header
        :type token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_characters_character_id_search_serialize(
            categories=categories,
            character_id=character_id,
            search=search,
            accept_language=accept_language,
            datasource=datasource,
            if_none_match=if_none_match,
            language=language,
            strict=strict,
            token=token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetCharactersCharacterIdSearchOk",
            '304': None,
            '400': "BadRequest",
            '401': "Unauthorized",
            '403': "Forbidden",
            '420': "ErrorLimited",
            '500': "InternalServerError",
            '503': "ServiceUnavailable",
            '504': "GatewayTimeout",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_characters_character_id_search_with_http_info(
        self,
        categories: Annotated[List[StrictStr], Field(min_length=1, max_length=11, description="Type of entities to search for")],
        character_id: Annotated[int, Field(strict=True, ge=1, description="An EVE character ID")],
        search: Annotated[str, Field(min_length=3, strict=True, description="The string to search on")],
        accept_language: Annotated[Optional[StrictStr], Field(description="Language to use in the response")] = None,
        datasource: Annotated[Optional[StrictStr], Field(description="The server name you would like data from")] = None,
        if_none_match: Annotated[Optional[StrictStr], Field(description="ETag from a previous request. A 304 will be returned if this matches the current ETag")] = None,
        language: Annotated[Optional[StrictStr], Field(description="Language to use in the response, takes precedence over Accept-Language")] = None,
        strict: Annotated[Optional[StrictBool], Field(description="Whether the search should be a strict match")] = None,
        token: Annotated[Optional[StrictStr], Field(description="Access token to use if unable to set a header")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[GetCharactersCharacterIdSearchOk]:
        """Search on a string

        Search for entities that match a given sub-string.  --- Alternate route: `/dev/characters/{character_id}/search/`  Alternate route: `/legacy/characters/{character_id}/search/`  Alternate route: `/v3/characters/{character_id}/search/`  --- This route is cached for up to 3600 seconds

        :param categories: Type of entities to search for (required)
        :type categories: List[str]
        :param character_id: An EVE character ID (required)
        :type character_id: int
        :param search: The string to search on (required)
        :type search: str
        :param accept_language: Language to use in the response
        :type accept_language: str
        :param datasource: The server name you would like data from
        :type datasource: str
        :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :type if_none_match: str
        :param language: Language to use in the response, takes precedence over Accept-Language
        :type language: str
        :param strict: Whether the search should be a strict match
        :type strict: bool
        :param token: Access token to use if unable to set a header
        :type token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_characters_character_id_search_serialize(
            categories=categories,
            character_id=character_id,
            search=search,
            accept_language=accept_language,
            datasource=datasource,
            if_none_match=if_none_match,
            language=language,
            strict=strict,
            token=token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetCharactersCharacterIdSearchOk",
            '304': None,
            '400': "BadRequest",
            '401': "Unauthorized",
            '403': "Forbidden",
            '420': "ErrorLimited",
            '500': "InternalServerError",
            '503': "ServiceUnavailable",
            '504': "GatewayTimeout",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_characters_character_id_search_without_preload_content(
        self,
        categories: Annotated[List[StrictStr], Field(min_length=1, max_length=11, description="Type of entities to search for")],
        character_id: Annotated[int, Field(strict=True, ge=1, description="An EVE character ID")],
        search: Annotated[str, Field(min_length=3, strict=True, description="The string to search on")],
        accept_language: Annotated[Optional[StrictStr], Field(description="Language to use in the response")] = None,
        datasource: Annotated[Optional[StrictStr], Field(description="The server name you would like data from")] = None,
        if_none_match: Annotated[Optional[StrictStr], Field(description="ETag from a previous request. A 304 will be returned if this matches the current ETag")] = None,
        language: Annotated[Optional[StrictStr], Field(description="Language to use in the response, takes precedence over Accept-Language")] = None,
        strict: Annotated[Optional[StrictBool], Field(description="Whether the search should be a strict match")] = None,
        token: Annotated[Optional[StrictStr], Field(description="Access token to use if unable to set a header")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Search on a string

        Search for entities that match a given sub-string.  --- Alternate route: `/dev/characters/{character_id}/search/`  Alternate route: `/legacy/characters/{character_id}/search/`  Alternate route: `/v3/characters/{character_id}/search/`  --- This route is cached for up to 3600 seconds

        :param categories: Type of entities to search for (required)
        :type categories: List[str]
        :param character_id: An EVE character ID (required)
        :type character_id: int
        :param search: The string to search on (required)
        :type search: str
        :param accept_language: Language to use in the response
        :type accept_language: str
        :param datasource: The server name you would like data from
        :type datasource: str
        :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :type if_none_match: str
        :param language: Language to use in the response, takes precedence over Accept-Language
        :type language: str
        :param strict: Whether the search should be a strict match
        :type strict: bool
        :param token: Access token to use if unable to set a header
        :type token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_characters_character_id_search_serialize(
            categories=categories,
            character_id=character_id,
            search=search,
            accept_language=accept_language,
            datasource=datasource,
            if_none_match=if_none_match,
            language=language,
            strict=strict,
            token=token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetCharactersCharacterIdSearchOk",
            '304': None,
            '400': "BadRequest",
            '401': "Unauthorized",
            '403': "Forbidden",
            '420': "ErrorLimited",
            '500': "InternalServerError",
            '503': "ServiceUnavailable",
            '504': "GatewayTimeout",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_characters_character_id_search_serialize(
        self,
        categories,
        character_id,
        search,
        accept_language,
        datasource,
        if_none_match,
        language,
        strict,
        token,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            'categories': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if character_id is not None:
            _path_params['character_id'] = character_id
        # process the query parameters
        if categories is not None:
            
            _query_params.append(('categories', categories))
            
        if datasource is not None:
            
            _query_params.append(('datasource', datasource))
            
        if language is not None:
            
            _query_params.append(('language', language))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        if strict is not None:
            
            _query_params.append(('strict', strict))
            
        if token is not None:
            
            _query_params.append(('token', token))
            
        # process the header parameters
        if accept_language is not None:
            _header_params['Accept-Language'] = accept_language
        if if_none_match is not None:
            _header_params['If-None-Match'] = if_none_match
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'evesso'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/characters/{character_id}/search/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

