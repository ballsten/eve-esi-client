# esi_client.CharacterApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_characters_character_id**](CharacterApi.md#get_characters_character_id) | **GET** /characters/{character_id}/ | Get character&#39;s public information
[**get_characters_character_id_agents_research**](CharacterApi.md#get_characters_character_id_agents_research) | **GET** /characters/{character_id}/agents_research/ | Get agents research
[**get_characters_character_id_blueprints**](CharacterApi.md#get_characters_character_id_blueprints) | **GET** /characters/{character_id}/blueprints/ | Get blueprints
[**get_characters_character_id_corporationhistory**](CharacterApi.md#get_characters_character_id_corporationhistory) | **GET** /characters/{character_id}/corporationhistory/ | Get corporation history
[**get_characters_character_id_fatigue**](CharacterApi.md#get_characters_character_id_fatigue) | **GET** /characters/{character_id}/fatigue/ | Get jump fatigue
[**get_characters_character_id_medals**](CharacterApi.md#get_characters_character_id_medals) | **GET** /characters/{character_id}/medals/ | Get medals
[**get_characters_character_id_notifications**](CharacterApi.md#get_characters_character_id_notifications) | **GET** /characters/{character_id}/notifications/ | Get character notifications
[**get_characters_character_id_notifications_contacts**](CharacterApi.md#get_characters_character_id_notifications_contacts) | **GET** /characters/{character_id}/notifications/contacts/ | Get new contact notifications
[**get_characters_character_id_portrait**](CharacterApi.md#get_characters_character_id_portrait) | **GET** /characters/{character_id}/portrait/ | Get character portraits
[**get_characters_character_id_roles**](CharacterApi.md#get_characters_character_id_roles) | **GET** /characters/{character_id}/roles/ | Get character corporation roles
[**get_characters_character_id_standings**](CharacterApi.md#get_characters_character_id_standings) | **GET** /characters/{character_id}/standings/ | Get standings
[**get_characters_character_id_titles**](CharacterApi.md#get_characters_character_id_titles) | **GET** /characters/{character_id}/titles/ | Get character corporation titles
[**post_characters_affiliation**](CharacterApi.md#post_characters_affiliation) | **POST** /characters/affiliation/ | Character affiliation
[**post_characters_character_id_cspa**](CharacterApi.md#post_characters_character_id_cspa) | **POST** /characters/{character_id}/cspa/ | Calculate a CSPA charge cost


# **get_characters_character_id**
> GetCharactersCharacterIdOk get_characters_character_id(character_id, datasource=datasource, if_none_match=if_none_match)

Get character's public information

Public information about a character  --- Alternate route: `/dev/characters/{character_id}/`  Alternate route: `/legacy/characters/{character_id}/`  Alternate route: `/v5/characters/{character_id}/`  --- This route is cached for up to 604800 seconds

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_ok import GetCharactersCharacterIdOk
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
    api_instance = esi_client.CharacterApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get character's public information
        api_response = api_instance.get_characters_character_id(character_id, datasource=datasource, if_none_match=if_none_match)
        print("The response of CharacterApi->get_characters_character_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetCharactersCharacterIdOk**](GetCharactersCharacterIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public data for the given character |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | Character not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_agents_research**
> List[GetCharactersCharacterIdAgentsResearch200Ok] get_characters_character_id_agents_research(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get agents research

Return a list of agents research information for a character. The formula for finding the current research points with an agent is: currentPoints = remainderPoints + pointsPerDay * days(currentTime - researchStartDate)  --- Alternate route: `/dev/characters/{character_id}/agents_research/`  Alternate route: `/v2/characters/{character_id}/agents_research/`  --- This route is cached for up to 3600 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_agents_research200_ok import GetCharactersCharacterIdAgentsResearch200Ok
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
    api_instance = esi_client.CharacterApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get agents research
        api_response = api_instance.get_characters_character_id_agents_research(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of CharacterApi->get_characters_character_id_agents_research:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_agents_research: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCharactersCharacterIdAgentsResearch200Ok]**](GetCharactersCharacterIdAgentsResearch200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of agents research information |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_blueprints**
> List[GetCharactersCharacterIdBlueprints200Ok] get_characters_character_id_blueprints(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get blueprints

Return a list of blueprints the character owns  --- Alternate route: `/dev/characters/{character_id}/blueprints/`  Alternate route: `/v3/characters/{character_id}/blueprints/`  --- This route is cached for up to 3600 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_blueprints200_ok import GetCharactersCharacterIdBlueprints200Ok
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
    api_instance = esi_client.CharacterApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    page = 1 # int | Which page of results to return (optional) (default to 1)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get blueprints
        api_response = api_instance.get_characters_character_id_blueprints(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
        print("The response of CharacterApi->get_characters_character_id_blueprints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_blueprints: %s\n" % e)
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

[**List[GetCharactersCharacterIdBlueprints200Ok]**](GetCharactersCharacterIdBlueprints200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of blueprints |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * X-Pages - Maximum page number <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_corporationhistory**
> List[GetCharactersCharacterIdCorporationhistory200Ok] get_characters_character_id_corporationhistory(character_id, datasource=datasource, if_none_match=if_none_match)

Get corporation history

Get a list of all the corporations a character has been a member of  --- Alternate route: `/dev/characters/{character_id}/corporationhistory/`  Alternate route: `/v2/characters/{character_id}/corporationhistory/`  --- This route is cached for up to 86400 seconds

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_corporationhistory200_ok import GetCharactersCharacterIdCorporationhistory200Ok
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
    api_instance = esi_client.CharacterApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get corporation history
        api_response = api_instance.get_characters_character_id_corporationhistory(character_id, datasource=datasource, if_none_match=if_none_match)
        print("The response of CharacterApi->get_characters_character_id_corporationhistory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_corporationhistory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**List[GetCharactersCharacterIdCorporationhistory200Ok]**](GetCharactersCharacterIdCorporationhistory200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Corporation history for the given character |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_fatigue**
> GetCharactersCharacterIdFatigueOk get_characters_character_id_fatigue(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get jump fatigue

Return a character's jump activation and fatigue information  --- Alternate route: `/dev/characters/{character_id}/fatigue/`  Alternate route: `/v2/characters/{character_id}/fatigue/`  --- This route is cached for up to 300 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_fatigue_ok import GetCharactersCharacterIdFatigueOk
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
    api_instance = esi_client.CharacterApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get jump fatigue
        api_response = api_instance.get_characters_character_id_fatigue(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of CharacterApi->get_characters_character_id_fatigue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_fatigue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCharactersCharacterIdFatigueOk**](GetCharactersCharacterIdFatigueOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Jump activation and fatigue information |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_medals**
> List[GetCharactersCharacterIdMedals200Ok] get_characters_character_id_medals(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get medals

Return a list of medals the character has  --- Alternate route: `/dev/characters/{character_id}/medals/`  Alternate route: `/v2/characters/{character_id}/medals/`  --- This route is cached for up to 3600 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_medals200_ok import GetCharactersCharacterIdMedals200Ok
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
    api_instance = esi_client.CharacterApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get medals
        api_response = api_instance.get_characters_character_id_medals(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of CharacterApi->get_characters_character_id_medals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_medals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCharactersCharacterIdMedals200Ok]**](GetCharactersCharacterIdMedals200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of medals |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_notifications**
> List[GetCharactersCharacterIdNotifications200Ok] get_characters_character_id_notifications(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get character notifications

Return character notifications  --- Alternate route: `/dev/characters/{character_id}/notifications/`  Alternate route: `/v5/characters/{character_id}/notifications/`  Alternate route: `/v6/characters/{character_id}/notifications/`  --- This route is cached for up to 600 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_notifications200_ok import GetCharactersCharacterIdNotifications200Ok
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
    api_instance = esi_client.CharacterApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get character notifications
        api_response = api_instance.get_characters_character_id_notifications(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of CharacterApi->get_characters_character_id_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCharactersCharacterIdNotifications200Ok]**](GetCharactersCharacterIdNotifications200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns your recent notifications |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_notifications_contacts**
> List[GetCharactersCharacterIdNotificationsContacts200Ok] get_characters_character_id_notifications_contacts(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get new contact notifications

Return notifications about having been added to someone's contact list  --- Alternate route: `/dev/characters/{character_id}/notifications/contacts/`  Alternate route: `/v2/characters/{character_id}/notifications/contacts/`  --- This route is cached for up to 600 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_notifications_contacts200_ok import GetCharactersCharacterIdNotificationsContacts200Ok
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
    api_instance = esi_client.CharacterApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get new contact notifications
        api_response = api_instance.get_characters_character_id_notifications_contacts(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of CharacterApi->get_characters_character_id_notifications_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_notifications_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCharactersCharacterIdNotificationsContacts200Ok]**](GetCharactersCharacterIdNotificationsContacts200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of contact notifications |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_portrait**
> GetCharactersCharacterIdPortraitOk get_characters_character_id_portrait(character_id, datasource=datasource, if_none_match=if_none_match)

Get character portraits

Get portrait urls for a character  --- Alternate route: `/dev/characters/{character_id}/portrait/`  Alternate route: `/v2/characters/{character_id}/portrait/`  Alternate route: `/v3/characters/{character_id}/portrait/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_portrait_ok import GetCharactersCharacterIdPortraitOk
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
    api_instance = esi_client.CharacterApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get character portraits
        api_response = api_instance.get_characters_character_id_portrait(character_id, datasource=datasource, if_none_match=if_none_match)
        print("The response of CharacterApi->get_characters_character_id_portrait:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_portrait: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetCharactersCharacterIdPortraitOk**](GetCharactersCharacterIdPortraitOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public data for the given character |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | No image server for this datasource |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_roles**
> GetCharactersCharacterIdRolesOk get_characters_character_id_roles(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get character corporation roles

Returns a character's corporation roles  --- Alternate route: `/dev/characters/{character_id}/roles/`  Alternate route: `/v3/characters/{character_id}/roles/`  --- This route is cached for up to 3600 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_roles_ok import GetCharactersCharacterIdRolesOk
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
    api_instance = esi_client.CharacterApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get character corporation roles
        api_response = api_instance.get_characters_character_id_roles(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of CharacterApi->get_characters_character_id_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCharactersCharacterIdRolesOk**](GetCharactersCharacterIdRolesOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The character&#39;s roles in thier corporation |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_standings**
> List[GetCharactersCharacterIdStandings200Ok] get_characters_character_id_standings(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get standings

Return character standings from agents, NPC corporations, and factions  --- Alternate route: `/dev/characters/{character_id}/standings/`  Alternate route: `/v2/characters/{character_id}/standings/`  --- This route is cached for up to 3600 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_standings200_ok import GetCharactersCharacterIdStandings200Ok
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
    api_instance = esi_client.CharacterApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get standings
        api_response = api_instance.get_characters_character_id_standings(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of CharacterApi->get_characters_character_id_standings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_standings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCharactersCharacterIdStandings200Ok]**](GetCharactersCharacterIdStandings200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of standings |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_titles**
> List[GetCharactersCharacterIdTitles200Ok] get_characters_character_id_titles(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get character corporation titles

Returns a character's titles  --- Alternate route: `/dev/characters/{character_id}/titles/`  Alternate route: `/v2/characters/{character_id}/titles/`  --- This route is cached for up to 3600 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_titles200_ok import GetCharactersCharacterIdTitles200Ok
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
    api_instance = esi_client.CharacterApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get character corporation titles
        api_response = api_instance.get_characters_character_id_titles(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of CharacterApi->get_characters_character_id_titles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_titles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCharactersCharacterIdTitles200Ok]**](GetCharactersCharacterIdTitles200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of titles |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_characters_affiliation**
> List[PostCharactersAffiliation200Ok] post_characters_affiliation(characters, datasource=datasource)

Character affiliation

Bulk lookup of character IDs to corporation, alliance and faction  --- Alternate route: `/dev/characters/affiliation/`  Alternate route: `/v2/characters/affiliation/`  --- This route is cached for up to 3600 seconds

### Example


```python
import time
import os
import esi_client
from esi_client.models.post_characters_affiliation200_ok import PostCharactersAffiliation200Ok
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
    api_instance = esi_client.CharacterApi(api_client)
    characters = [56] # List[int] | The character IDs to fetch affiliations for. All characters must exist, or none will be returned
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')

    try:
        # Character affiliation
        api_response = api_instance.post_characters_affiliation(characters, datasource=datasource)
        print("The response of CharacterApi->post_characters_affiliation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->post_characters_affiliation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **characters** | [**List[int]**](int.md)| The character IDs to fetch affiliations for. All characters must exist, or none will be returned | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]

### Return type

[**List[PostCharactersAffiliation200Ok]**](PostCharactersAffiliation200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Character corporation, alliance and faction IDs |  -  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_characters_character_id_cspa**
> float post_characters_character_id_cspa(character_id, characters, datasource=datasource, token=token)

Calculate a CSPA charge cost

Takes a source character ID in the url and a set of target character ID's in the body, returns a CSPA charge cost  --- Alternate route: `/dev/characters/{character_id}/cspa/`  Alternate route: `/v5/characters/{character_id}/cspa/` 

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
    api_instance = esi_client.CharacterApi(api_client)
    character_id = 56 # int | An EVE character ID
    characters = [56] # List[int] | The target characters to calculate the charge for
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Calculate a CSPA charge cost
        api_response = api_instance.post_characters_character_id_cspa(character_id, characters, datasource=datasource, token=token)
        print("The response of CharacterApi->post_characters_character_id_cspa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->post_characters_character_id_cspa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **characters** | [**List[int]**](int.md)| The target characters to calculate the charge for | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

**float**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Aggregate cost of sending a mail from the source character to the target characters, in ISK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

