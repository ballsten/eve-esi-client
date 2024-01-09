# esi_client.FactionWarfareApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_characters_character_id_fw_stats**](FactionWarfareApi.md#get_characters_character_id_fw_stats) | **GET** /characters/{character_id}/fw/stats/ | Overview of a character involved in faction warfare
[**get_corporations_corporation_id_fw_stats**](FactionWarfareApi.md#get_corporations_corporation_id_fw_stats) | **GET** /corporations/{corporation_id}/fw/stats/ | Overview of a corporation involved in faction warfare
[**get_fw_leaderboards**](FactionWarfareApi.md#get_fw_leaderboards) | **GET** /fw/leaderboards/ | List of the top factions in faction warfare
[**get_fw_leaderboards_characters**](FactionWarfareApi.md#get_fw_leaderboards_characters) | **GET** /fw/leaderboards/characters/ | List of the top pilots in faction warfare
[**get_fw_leaderboards_corporations**](FactionWarfareApi.md#get_fw_leaderboards_corporations) | **GET** /fw/leaderboards/corporations/ | List of the top corporations in faction warfare
[**get_fw_stats**](FactionWarfareApi.md#get_fw_stats) | **GET** /fw/stats/ | An overview of statistics about factions involved in faction warfare
[**get_fw_systems**](FactionWarfareApi.md#get_fw_systems) | **GET** /fw/systems/ | Ownership of faction warfare systems
[**get_fw_wars**](FactionWarfareApi.md#get_fw_wars) | **GET** /fw/wars/ | Data about which NPC factions are at war


# **get_characters_character_id_fw_stats**
> GetCharactersCharacterIdFwStatsOk get_characters_character_id_fw_stats(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Overview of a character involved in faction warfare

Statistical overview of a character involved in faction warfare  --- Alternate route: `/dev/characters/{character_id}/fw/stats/`  Alternate route: `/legacy/characters/{character_id}/fw/stats/`  Alternate route: `/v1/characters/{character_id}/fw/stats/`  Alternate route: `/v2/characters/{character_id}/fw/stats/`  --- This route expires daily at 11:05

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_fw_stats_ok import GetCharactersCharacterIdFwStatsOk
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
    api_instance = esi_client.FactionWarfareApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Overview of a character involved in faction warfare
        api_response = api_instance.get_characters_character_id_fw_stats(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of FactionWarfareApi->get_characters_character_id_fw_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionWarfareApi->get_characters_character_id_fw_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCharactersCharacterIdFwStatsOk**](GetCharactersCharacterIdFwStatsOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Faction warfare statistics for a given character |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_fw_stats**
> GetCorporationsCorporationIdFwStatsOk get_corporations_corporation_id_fw_stats(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)

Overview of a corporation involved in faction warfare

Statistics about a corporation involved in faction warfare  --- Alternate route: `/dev/corporations/{corporation_id}/fw/stats/`  Alternate route: `/legacy/corporations/{corporation_id}/fw/stats/`  Alternate route: `/v1/corporations/{corporation_id}/fw/stats/`  Alternate route: `/v2/corporations/{corporation_id}/fw/stats/`  --- This route expires daily at 11:05

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_corporations_corporation_id_fw_stats_ok import GetCorporationsCorporationIdFwStatsOk
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
    api_instance = esi_client.FactionWarfareApi(api_client)
    corporation_id = 56 # int | An EVE corporation ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Overview of a corporation involved in faction warfare
        api_response = api_instance.get_corporations_corporation_id_fw_stats(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of FactionWarfareApi->get_corporations_corporation_id_fw_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionWarfareApi->get_corporations_corporation_id_fw_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCorporationsCorporationIdFwStatsOk**](GetCorporationsCorporationIdFwStatsOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Faction warfare statistics for a given corporation |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fw_leaderboards**
> GetFwLeaderboardsOk get_fw_leaderboards(datasource=datasource, if_none_match=if_none_match)

List of the top factions in faction warfare

Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday  --- Alternate route: `/dev/fw/leaderboards/`  Alternate route: `/legacy/fw/leaderboards/`  Alternate route: `/v1/fw/leaderboards/`  Alternate route: `/v2/fw/leaderboards/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_fw_leaderboards_ok import GetFwLeaderboardsOk
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
    api_instance = esi_client.FactionWarfareApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # List of the top factions in faction warfare
        api_response = api_instance.get_fw_leaderboards(datasource=datasource, if_none_match=if_none_match)
        print("The response of FactionWarfareApi->get_fw_leaderboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionWarfareApi->get_fw_leaderboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetFwLeaderboardsOk**](GetFwLeaderboardsOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Corporation leaderboard of kills and victory points within faction warfare |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fw_leaderboards_characters**
> GetFwLeaderboardsCharactersOk get_fw_leaderboards_characters(datasource=datasource, if_none_match=if_none_match)

List of the top pilots in faction warfare

Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday  --- Alternate route: `/dev/fw/leaderboards/characters/`  Alternate route: `/legacy/fw/leaderboards/characters/`  Alternate route: `/v1/fw/leaderboards/characters/`  Alternate route: `/v2/fw/leaderboards/characters/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_fw_leaderboards_characters_ok import GetFwLeaderboardsCharactersOk
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
    api_instance = esi_client.FactionWarfareApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # List of the top pilots in faction warfare
        api_response = api_instance.get_fw_leaderboards_characters(datasource=datasource, if_none_match=if_none_match)
        print("The response of FactionWarfareApi->get_fw_leaderboards_characters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionWarfareApi->get_fw_leaderboards_characters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetFwLeaderboardsCharactersOk**](GetFwLeaderboardsCharactersOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Character leaderboard of kills and victory points within faction warfare |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fw_leaderboards_corporations**
> GetFwLeaderboardsCorporationsOk get_fw_leaderboards_corporations(datasource=datasource, if_none_match=if_none_match)

List of the top corporations in faction warfare

Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday  --- Alternate route: `/dev/fw/leaderboards/corporations/`  Alternate route: `/legacy/fw/leaderboards/corporations/`  Alternate route: `/v1/fw/leaderboards/corporations/`  Alternate route: `/v2/fw/leaderboards/corporations/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_fw_leaderboards_corporations_ok import GetFwLeaderboardsCorporationsOk
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
    api_instance = esi_client.FactionWarfareApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # List of the top corporations in faction warfare
        api_response = api_instance.get_fw_leaderboards_corporations(datasource=datasource, if_none_match=if_none_match)
        print("The response of FactionWarfareApi->get_fw_leaderboards_corporations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionWarfareApi->get_fw_leaderboards_corporations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetFwLeaderboardsCorporationsOk**](GetFwLeaderboardsCorporationsOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Corporation leaderboard of kills and victory points within faction warfare |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fw_stats**
> List[GetFwStats200Ok] get_fw_stats(datasource=datasource, if_none_match=if_none_match)

An overview of statistics about factions involved in faction warfare

Statistical overviews of factions involved in faction warfare  --- Alternate route: `/dev/fw/stats/`  Alternate route: `/legacy/fw/stats/`  Alternate route: `/v1/fw/stats/`  Alternate route: `/v2/fw/stats/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_fw_stats200_ok import GetFwStats200Ok
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
    api_instance = esi_client.FactionWarfareApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # An overview of statistics about factions involved in faction warfare
        api_response = api_instance.get_fw_stats(datasource=datasource, if_none_match=if_none_match)
        print("The response of FactionWarfareApi->get_fw_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionWarfareApi->get_fw_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**List[GetFwStats200Ok]**](GetFwStats200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per faction breakdown of faction warfare statistics |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fw_systems**
> List[GetFwSystems200Ok] get_fw_systems(datasource=datasource, if_none_match=if_none_match)

Ownership of faction warfare systems

An overview of the current ownership of faction warfare solar systems  --- Alternate route: `/dev/fw/systems/`  Alternate route: `/legacy/fw/systems/`  Alternate route: `/v2/fw/systems/`  Alternate route: `/v3/fw/systems/`  --- This route is cached for up to 1800 seconds

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_fw_systems200_ok import GetFwSystems200Ok
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
    api_instance = esi_client.FactionWarfareApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Ownership of faction warfare systems
        api_response = api_instance.get_fw_systems(datasource=datasource, if_none_match=if_none_match)
        print("The response of FactionWarfareApi->get_fw_systems:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionWarfareApi->get_fw_systems: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**List[GetFwSystems200Ok]**](GetFwSystems200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All faction warfare solar systems |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fw_wars**
> List[GetFwWars200Ok] get_fw_wars(datasource=datasource, if_none_match=if_none_match)

Data about which NPC factions are at war

Data about which NPC factions are at war  --- Alternate route: `/dev/fw/wars/`  Alternate route: `/legacy/fw/wars/`  Alternate route: `/v1/fw/wars/`  Alternate route: `/v2/fw/wars/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_fw_wars200_ok import GetFwWars200Ok
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
    api_instance = esi_client.FactionWarfareApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Data about which NPC factions are at war
        api_response = api_instance.get_fw_wars(datasource=datasource, if_none_match=if_none_match)
        print("The response of FactionWarfareApi->get_fw_wars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactionWarfareApi->get_fw_wars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**List[GetFwWars200Ok]**](GetFwWars200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of NPC factions at war |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

