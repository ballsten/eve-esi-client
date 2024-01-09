# esi_client.KillmailsApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_characters_character_id_killmails_recent**](KillmailsApi.md#get_characters_character_id_killmails_recent) | **GET** /characters/{character_id}/killmails/recent/ | Get a character&#39;s recent kills and losses
[**get_corporations_corporation_id_killmails_recent**](KillmailsApi.md#get_corporations_corporation_id_killmails_recent) | **GET** /corporations/{corporation_id}/killmails/recent/ | Get a corporation&#39;s recent kills and losses
[**get_killmails_killmail_id_killmail_hash**](KillmailsApi.md#get_killmails_killmail_id_killmail_hash) | **GET** /killmails/{killmail_id}/{killmail_hash}/ | Get a single killmail


# **get_characters_character_id_killmails_recent**
> List[GetCharactersCharacterIdKillmailsRecent200Ok] get_characters_character_id_killmails_recent(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get a character's recent kills and losses

Return a list of a character's kills and losses going back 90 days  --- Alternate route: `/dev/characters/{character_id}/killmails/recent/`  Alternate route: `/legacy/characters/{character_id}/killmails/recent/`  Alternate route: `/v1/characters/{character_id}/killmails/recent/`  --- This route is cached for up to 300 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_killmails_recent200_ok import GetCharactersCharacterIdKillmailsRecent200Ok
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
    api_instance = esi_client.KillmailsApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    page = 1 # int | Which page of results to return (optional) (default to 1)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get a character's recent kills and losses
        api_response = api_instance.get_characters_character_id_killmails_recent(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
        print("The response of KillmailsApi->get_characters_character_id_killmails_recent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KillmailsApi->get_characters_character_id_killmails_recent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCharactersCharacterIdKillmailsRecent200Ok]**](GetCharactersCharacterIdKillmailsRecent200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of killmail IDs and hashes |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * X-Pages - Maximum page number <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_killmails_recent**
> List[GetCorporationsCorporationIdKillmailsRecent200Ok] get_corporations_corporation_id_killmails_recent(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get a corporation's recent kills and losses

Get a list of a corporation's kills and losses going back 90 days  --- Alternate route: `/dev/corporations/{corporation_id}/killmails/recent/`  Alternate route: `/legacy/corporations/{corporation_id}/killmails/recent/`  Alternate route: `/v1/corporations/{corporation_id}/killmails/recent/`  --- This route is cached for up to 300 seconds  --- Requires one of the following EVE corporation role(s): Director 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_corporations_corporation_id_killmails_recent200_ok import GetCorporationsCorporationIdKillmailsRecent200Ok
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
    api_instance = esi_client.KillmailsApi(api_client)
    corporation_id = 56 # int | An EVE corporation ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    page = 1 # int | Which page of results to return (optional) (default to 1)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get a corporation's recent kills and losses
        api_response = api_instance.get_corporations_corporation_id_killmails_recent(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
        print("The response of KillmailsApi->get_corporations_corporation_id_killmails_recent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KillmailsApi->get_corporations_corporation_id_killmails_recent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCorporationsCorporationIdKillmailsRecent200Ok]**](GetCorporationsCorporationIdKillmailsRecent200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of killmail IDs and hashes |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * X-Pages - Maximum page number <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_killmails_killmail_id_killmail_hash**
> GetKillmailsKillmailIdKillmailHashOk get_killmails_killmail_id_killmail_hash(killmail_hash, killmail_id, datasource=datasource, if_none_match=if_none_match)

Get a single killmail

Return a single killmail from its ID and hash  --- Alternate route: `/dev/killmails/{killmail_id}/{killmail_hash}/`  Alternate route: `/legacy/killmails/{killmail_id}/{killmail_hash}/`  Alternate route: `/v1/killmails/{killmail_id}/{killmail_hash}/`  --- This route is cached for up to 30758400 seconds

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_killmails_killmail_id_killmail_hash_ok import GetKillmailsKillmailIdKillmailHashOk
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net/latest"
)


# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.KillmailsApi(api_client)
    killmail_hash = 'killmail_hash_example' # str | The killmail hash for verification
    killmail_id = 56 # int | The killmail ID to be queried
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get a single killmail
        api_response = api_instance.get_killmails_killmail_id_killmail_hash(killmail_hash, killmail_id, datasource=datasource, if_none_match=if_none_match)
        print("The response of KillmailsApi->get_killmails_killmail_id_killmail_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KillmailsApi->get_killmails_killmail_id_killmail_hash: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **killmail_hash** | **str**| The killmail hash for verification | 
 **killmail_id** | **int**| The killmail ID to be queried | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetKillmailsKillmailIdKillmailHashOk**](GetKillmailsKillmailIdKillmailHashOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A killmail |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**422** | Invalid killmail_id and/or killmail_hash |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

