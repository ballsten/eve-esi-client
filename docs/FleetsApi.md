# esi_client.FleetsApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_fleets_fleet_id_members_member_id**](FleetsApi.md#delete_fleets_fleet_id_members_member_id) | **DELETE** /fleets/{fleet_id}/members/{member_id}/ | Kick fleet member
[**delete_fleets_fleet_id_squads_squad_id**](FleetsApi.md#delete_fleets_fleet_id_squads_squad_id) | **DELETE** /fleets/{fleet_id}/squads/{squad_id}/ | Delete fleet squad
[**delete_fleets_fleet_id_wings_wing_id**](FleetsApi.md#delete_fleets_fleet_id_wings_wing_id) | **DELETE** /fleets/{fleet_id}/wings/{wing_id}/ | Delete fleet wing
[**get_characters_character_id_fleet**](FleetsApi.md#get_characters_character_id_fleet) | **GET** /characters/{character_id}/fleet/ | Get character fleet info
[**get_fleets_fleet_id**](FleetsApi.md#get_fleets_fleet_id) | **GET** /fleets/{fleet_id}/ | Get fleet information
[**get_fleets_fleet_id_members**](FleetsApi.md#get_fleets_fleet_id_members) | **GET** /fleets/{fleet_id}/members/ | Get fleet members
[**get_fleets_fleet_id_wings**](FleetsApi.md#get_fleets_fleet_id_wings) | **GET** /fleets/{fleet_id}/wings/ | Get fleet wings
[**post_fleets_fleet_id_members**](FleetsApi.md#post_fleets_fleet_id_members) | **POST** /fleets/{fleet_id}/members/ | Create fleet invitation
[**post_fleets_fleet_id_wings**](FleetsApi.md#post_fleets_fleet_id_wings) | **POST** /fleets/{fleet_id}/wings/ | Create fleet wing
[**post_fleets_fleet_id_wings_wing_id_squads**](FleetsApi.md#post_fleets_fleet_id_wings_wing_id_squads) | **POST** /fleets/{fleet_id}/wings/{wing_id}/squads/ | Create fleet squad
[**put_fleets_fleet_id**](FleetsApi.md#put_fleets_fleet_id) | **PUT** /fleets/{fleet_id}/ | Update fleet
[**put_fleets_fleet_id_members_member_id**](FleetsApi.md#put_fleets_fleet_id_members_member_id) | **PUT** /fleets/{fleet_id}/members/{member_id}/ | Move fleet member
[**put_fleets_fleet_id_squads_squad_id**](FleetsApi.md#put_fleets_fleet_id_squads_squad_id) | **PUT** /fleets/{fleet_id}/squads/{squad_id}/ | Rename fleet squad
[**put_fleets_fleet_id_wings_wing_id**](FleetsApi.md#put_fleets_fleet_id_wings_wing_id) | **PUT** /fleets/{fleet_id}/wings/{wing_id}/ | Rename fleet wing


# **delete_fleets_fleet_id_members_member_id**
> delete_fleets_fleet_id_members_member_id(fleet_id, member_id, datasource=datasource, token=token)

Kick fleet member

Kick a fleet member  --- Alternate route: `/dev/fleets/{fleet_id}/members/{member_id}/`  Alternate route: `/legacy/fleets/{fleet_id}/members/{member_id}/`  Alternate route: `/v1/fleets/{fleet_id}/members/{member_id}/` 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.FleetsApi(api_client)
    fleet_id = 56 # int | ID for a fleet
    member_id = 56 # int | The character ID of a member in this fleet
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Kick fleet member
        api_instance.delete_fleets_fleet_id_members_member_id(fleet_id, member_id, datasource=datasource, token=token)
    except Exception as e:
        print("Exception when calling FleetsApi->delete_fleets_fleet_id_members_member_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**| ID for a fleet | 
 **member_id** | **int**| The character ID of a member in this fleet | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

void (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Fleet member kicked |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The fleet does not exist or you don&#39;t have access to it |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fleets_fleet_id_squads_squad_id**
> delete_fleets_fleet_id_squads_squad_id(fleet_id, squad_id, datasource=datasource, token=token)

Delete fleet squad

Delete a fleet squad, only empty squads can be deleted  --- Alternate route: `/dev/fleets/{fleet_id}/squads/{squad_id}/`  Alternate route: `/legacy/fleets/{fleet_id}/squads/{squad_id}/`  Alternate route: `/v1/fleets/{fleet_id}/squads/{squad_id}/` 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.FleetsApi(api_client)
    fleet_id = 56 # int | ID for a fleet
    squad_id = 56 # int | The squad to delete
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Delete fleet squad
        api_instance.delete_fleets_fleet_id_squads_squad_id(fleet_id, squad_id, datasource=datasource, token=token)
    except Exception as e:
        print("Exception when calling FleetsApi->delete_fleets_fleet_id_squads_squad_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**| ID for a fleet | 
 **squad_id** | **int**| The squad to delete | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

void (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Squad deleted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The fleet does not exist or you don&#39;t have access to it |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fleets_fleet_id_wings_wing_id**
> delete_fleets_fleet_id_wings_wing_id(fleet_id, wing_id, datasource=datasource, token=token)

Delete fleet wing

Delete a fleet wing, only empty wings can be deleted. The wing may contain squads, but the squads must be empty  --- Alternate route: `/dev/fleets/{fleet_id}/wings/{wing_id}/`  Alternate route: `/legacy/fleets/{fleet_id}/wings/{wing_id}/`  Alternate route: `/v1/fleets/{fleet_id}/wings/{wing_id}/` 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.FleetsApi(api_client)
    fleet_id = 56 # int | ID for a fleet
    wing_id = 56 # int | The wing to delete
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Delete fleet wing
        api_instance.delete_fleets_fleet_id_wings_wing_id(fleet_id, wing_id, datasource=datasource, token=token)
    except Exception as e:
        print("Exception when calling FleetsApi->delete_fleets_fleet_id_wings_wing_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**| ID for a fleet | 
 **wing_id** | **int**| The wing to delete | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

void (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Wing deleted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The fleet does not exist or you don&#39;t have access to it |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_fleet**
> GetCharactersCharacterIdFleetOk get_characters_character_id_fleet(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get character fleet info

Return the fleet ID the character is in, if any.  --- Alternate route: `/legacy/characters/{character_id}/fleet/`  Alternate route: `/v1/characters/{character_id}/fleet/`  --- This route is cached for up to 60 seconds  --- Warning: This route has an upgrade available  --- [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/characters/{character_id}/fleet/)

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_fleet_ok import GetCharactersCharacterIdFleetOk
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.FleetsApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get character fleet info
        api_response = api_instance.get_characters_character_id_fleet(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of FleetsApi->get_characters_character_id_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->get_characters_character_id_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCharactersCharacterIdFleetOk**](GetCharactersCharacterIdFleetOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the character&#39;s fleet |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The character is not in a fleet |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleets_fleet_id**
> GetFleetsFleetIdOk get_fleets_fleet_id(fleet_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get fleet information

Return details about a fleet  --- Alternate route: `/dev/fleets/{fleet_id}/`  Alternate route: `/legacy/fleets/{fleet_id}/`  Alternate route: `/v1/fleets/{fleet_id}/`  --- This route is cached for up to 5 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_fleets_fleet_id_ok import GetFleetsFleetIdOk
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.FleetsApi(api_client)
    fleet_id = 56 # int | ID for a fleet
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get fleet information
        api_response = api_instance.get_fleets_fleet_id(fleet_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of FleetsApi->get_fleets_fleet_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->get_fleets_fleet_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**| ID for a fleet | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetFleetsFleetIdOk**](GetFleetsFleetIdOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about a fleet |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The fleet does not exist or you don&#39;t have access to it |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleets_fleet_id_members**
> List[GetFleetsFleetIdMembers200Ok] get_fleets_fleet_id_members(fleet_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language, token=token)

Get fleet members

Return information about fleet members  --- Alternate route: `/dev/fleets/{fleet_id}/members/`  Alternate route: `/legacy/fleets/{fleet_id}/members/`  Alternate route: `/v1/fleets/{fleet_id}/members/`  --- This route is cached for up to 5 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_fleets_fleet_id_members200_ok import GetFleetsFleetIdMembers200Ok
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.FleetsApi(api_client)
    fleet_id = 56 # int | ID for a fleet
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get fleet members
        api_response = api_instance.get_fleets_fleet_id_members(fleet_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language, token=token)
        print("The response of FleetsApi->get_fleets_fleet_id_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->get_fleets_fleet_id_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**| ID for a fleet | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetFleetsFleetIdMembers200Ok]**](GetFleetsFleetIdMembers200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of fleet members |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The fleet does not exist or you don&#39;t have access to it |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleets_fleet_id_wings**
> List[GetFleetsFleetIdWings200Ok] get_fleets_fleet_id_wings(fleet_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language, token=token)

Get fleet wings

Return information about wings in a fleet  --- Alternate route: `/dev/fleets/{fleet_id}/wings/`  Alternate route: `/legacy/fleets/{fleet_id}/wings/`  Alternate route: `/v1/fleets/{fleet_id}/wings/`  --- This route is cached for up to 5 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_fleets_fleet_id_wings200_ok import GetFleetsFleetIdWings200Ok
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.FleetsApi(api_client)
    fleet_id = 56 # int | ID for a fleet
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get fleet wings
        api_response = api_instance.get_fleets_fleet_id_wings(fleet_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language, token=token)
        print("The response of FleetsApi->get_fleets_fleet_id_wings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->get_fleets_fleet_id_wings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**| ID for a fleet | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetFleetsFleetIdWings200Ok]**](GetFleetsFleetIdWings200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of fleet wings |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The fleet does not exist or you don&#39;t have access to it |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_fleets_fleet_id_members**
> post_fleets_fleet_id_members(fleet_id, invitation, datasource=datasource, token=token)

Create fleet invitation

Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI  --- Alternate route: `/dev/fleets/{fleet_id}/members/`  Alternate route: `/legacy/fleets/{fleet_id}/members/`  Alternate route: `/v1/fleets/{fleet_id}/members/` 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.post_fleets_fleet_id_members_invitation import PostFleetsFleetIdMembersInvitation
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.FleetsApi(api_client)
    fleet_id = 56 # int | ID for a fleet
    invitation = esi_client.PostFleetsFleetIdMembersInvitation() # PostFleetsFleetIdMembersInvitation | Details of the invitation
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Create fleet invitation
        api_instance.post_fleets_fleet_id_members(fleet_id, invitation, datasource=datasource, token=token)
    except Exception as e:
        print("Exception when calling FleetsApi->post_fleets_fleet_id_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**| ID for a fleet | 
 **invitation** | [**PostFleetsFleetIdMembersInvitation**](PostFleetsFleetIdMembersInvitation.md)| Details of the invitation | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

void (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Fleet invitation sent |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The fleet does not exist or you don&#39;t have access to it |  -  |
**420** | Error limited |  -  |
**422** | Errors in invitation |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_fleets_fleet_id_wings**
> PostFleetsFleetIdWingsCreated post_fleets_fleet_id_wings(fleet_id, datasource=datasource, token=token)

Create fleet wing

Create a new wing in a fleet  --- Alternate route: `/dev/fleets/{fleet_id}/wings/`  Alternate route: `/legacy/fleets/{fleet_id}/wings/`  Alternate route: `/v1/fleets/{fleet_id}/wings/` 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.post_fleets_fleet_id_wings_created import PostFleetsFleetIdWingsCreated
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.FleetsApi(api_client)
    fleet_id = 56 # int | ID for a fleet
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Create fleet wing
        api_response = api_instance.post_fleets_fleet_id_wings(fleet_id, datasource=datasource, token=token)
        print("The response of FleetsApi->post_fleets_fleet_id_wings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->post_fleets_fleet_id_wings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**| ID for a fleet | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**PostFleetsFleetIdWingsCreated**](PostFleetsFleetIdWingsCreated.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Wing created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The fleet does not exist or you don&#39;t have access to it |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_fleets_fleet_id_wings_wing_id_squads**
> PostFleetsFleetIdWingsWingIdSquadsCreated post_fleets_fleet_id_wings_wing_id_squads(fleet_id, wing_id, datasource=datasource, token=token)

Create fleet squad

Create a new squad in a fleet  --- Alternate route: `/dev/fleets/{fleet_id}/wings/{wing_id}/squads/`  Alternate route: `/legacy/fleets/{fleet_id}/wings/{wing_id}/squads/`  Alternate route: `/v1/fleets/{fleet_id}/wings/{wing_id}/squads/` 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.post_fleets_fleet_id_wings_wing_id_squads_created import PostFleetsFleetIdWingsWingIdSquadsCreated
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.FleetsApi(api_client)
    fleet_id = 56 # int | ID for a fleet
    wing_id = 56 # int | The wing_id to create squad in
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Create fleet squad
        api_response = api_instance.post_fleets_fleet_id_wings_wing_id_squads(fleet_id, wing_id, datasource=datasource, token=token)
        print("The response of FleetsApi->post_fleets_fleet_id_wings_wing_id_squads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->post_fleets_fleet_id_wings_wing_id_squads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**| ID for a fleet | 
 **wing_id** | **int**| The wing_id to create squad in | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**PostFleetsFleetIdWingsWingIdSquadsCreated**](PostFleetsFleetIdWingsWingIdSquadsCreated.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Squad created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The fleet does not exist or you don&#39;t have access to it |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_fleets_fleet_id**
> put_fleets_fleet_id(fleet_id, new_settings, datasource=datasource, token=token)

Update fleet

Update settings about a fleet  --- Alternate route: `/dev/fleets/{fleet_id}/`  Alternate route: `/legacy/fleets/{fleet_id}/`  Alternate route: `/v1/fleets/{fleet_id}/` 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.put_fleets_fleet_id_new_settings import PutFleetsFleetIdNewSettings
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.FleetsApi(api_client)
    fleet_id = 56 # int | ID for a fleet
    new_settings = esi_client.PutFleetsFleetIdNewSettings() # PutFleetsFleetIdNewSettings | What to update for this fleet
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Update fleet
        api_instance.put_fleets_fleet_id(fleet_id, new_settings, datasource=datasource, token=token)
    except Exception as e:
        print("Exception when calling FleetsApi->put_fleets_fleet_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**| ID for a fleet | 
 **new_settings** | [**PutFleetsFleetIdNewSettings**](PutFleetsFleetIdNewSettings.md)| What to update for this fleet | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

void (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Fleet updated |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The fleet does not exist or you don&#39;t have access to it |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_fleets_fleet_id_members_member_id**
> put_fleets_fleet_id_members_member_id(fleet_id, member_id, movement, datasource=datasource, token=token)

Move fleet member

Move a fleet member around  --- Alternate route: `/dev/fleets/{fleet_id}/members/{member_id}/`  Alternate route: `/legacy/fleets/{fleet_id}/members/{member_id}/`  Alternate route: `/v1/fleets/{fleet_id}/members/{member_id}/` 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.put_fleets_fleet_id_members_member_id_movement import PutFleetsFleetIdMembersMemberIdMovement
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.FleetsApi(api_client)
    fleet_id = 56 # int | ID for a fleet
    member_id = 56 # int | The character ID of a member in this fleet
    movement = esi_client.PutFleetsFleetIdMembersMemberIdMovement() # PutFleetsFleetIdMembersMemberIdMovement | Details of the invitation
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Move fleet member
        api_instance.put_fleets_fleet_id_members_member_id(fleet_id, member_id, movement, datasource=datasource, token=token)
    except Exception as e:
        print("Exception when calling FleetsApi->put_fleets_fleet_id_members_member_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**| ID for a fleet | 
 **member_id** | **int**| The character ID of a member in this fleet | 
 **movement** | [**PutFleetsFleetIdMembersMemberIdMovement**](PutFleetsFleetIdMembersMemberIdMovement.md)| Details of the invitation | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

void (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Fleet invitation sent |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The fleet does not exist or you don&#39;t have access to it |  -  |
**420** | Error limited |  -  |
**422** | Errors in invitation |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_fleets_fleet_id_squads_squad_id**
> put_fleets_fleet_id_squads_squad_id(fleet_id, squad_id, naming, datasource=datasource, token=token)

Rename fleet squad

Rename a fleet squad  --- Alternate route: `/dev/fleets/{fleet_id}/squads/{squad_id}/`  Alternate route: `/legacy/fleets/{fleet_id}/squads/{squad_id}/`  Alternate route: `/v1/fleets/{fleet_id}/squads/{squad_id}/` 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.put_fleets_fleet_id_squads_squad_id_naming import PutFleetsFleetIdSquadsSquadIdNaming
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.FleetsApi(api_client)
    fleet_id = 56 # int | ID for a fleet
    squad_id = 56 # int | The squad to rename
    naming = esi_client.PutFleetsFleetIdSquadsSquadIdNaming() # PutFleetsFleetIdSquadsSquadIdNaming | New name of the squad
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Rename fleet squad
        api_instance.put_fleets_fleet_id_squads_squad_id(fleet_id, squad_id, naming, datasource=datasource, token=token)
    except Exception as e:
        print("Exception when calling FleetsApi->put_fleets_fleet_id_squads_squad_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**| ID for a fleet | 
 **squad_id** | **int**| The squad to rename | 
 **naming** | [**PutFleetsFleetIdSquadsSquadIdNaming**](PutFleetsFleetIdSquadsSquadIdNaming.md)| New name of the squad | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

void (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Squad renamed |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The fleet does not exist or you don&#39;t have access to it |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_fleets_fleet_id_wings_wing_id**
> put_fleets_fleet_id_wings_wing_id(fleet_id, wing_id, naming, datasource=datasource, token=token)

Rename fleet wing

Rename a fleet wing  --- Alternate route: `/dev/fleets/{fleet_id}/wings/{wing_id}/`  Alternate route: `/legacy/fleets/{fleet_id}/wings/{wing_id}/`  Alternate route: `/v1/fleets/{fleet_id}/wings/{wing_id}/` 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.put_fleets_fleet_id_wings_wing_id_naming import PutFleetsFleetIdWingsWingIdNaming
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.FleetsApi(api_client)
    fleet_id = 56 # int | ID for a fleet
    wing_id = 56 # int | The wing to rename
    naming = esi_client.PutFleetsFleetIdWingsWingIdNaming() # PutFleetsFleetIdWingsWingIdNaming | New name of the wing
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Rename fleet wing
        api_instance.put_fleets_fleet_id_wings_wing_id(fleet_id, wing_id, naming, datasource=datasource, token=token)
    except Exception as e:
        print("Exception when calling FleetsApi->put_fleets_fleet_id_wings_wing_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**| ID for a fleet | 
 **wing_id** | **int**| The wing to rename | 
 **naming** | [**PutFleetsFleetIdWingsWingIdNaming**](PutFleetsFleetIdWingsWingIdNaming.md)| New name of the wing | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

void (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Wing renamed |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | The fleet does not exist or you don&#39;t have access to it |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

