# esi_client.SearchApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_characters_character_id_search**](SearchApi.md#get_characters_character_id_search) | **GET** /characters/{character_id}/search/ | Search on a string


# **get_characters_character_id_search**
> GetCharactersCharacterIdSearchOk get_characters_character_id_search(categories, character_id, search, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language, strict=strict, token=token)

Search on a string

Search for entities that match a given sub-string.  --- Alternate route: `/dev/characters/{character_id}/search/`  Alternate route: `/legacy/characters/{character_id}/search/`  Alternate route: `/v3/characters/{character_id}/search/`  --- This route is cached for up to 3600 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_search_ok import GetCharactersCharacterIdSearchOk
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
    api_instance = esi_client.SearchApi(api_client)
    categories = ['categories_example'] # List[str] | Type of entities to search for
    character_id = 56 # int | An EVE character ID
    search = 'search_example' # str | The string to search on
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')
    strict = False # bool | Whether the search should be a strict match (optional) (default to False)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Search on a string
        api_response = api_instance.get_characters_character_id_search(categories, character_id, search, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language, strict=strict, token=token)
        print("The response of SearchApi->get_characters_character_id_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_characters_character_id_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categories** | [**List[str]**](str.md)| Type of entities to search for | 
 **character_id** | **int**| An EVE character ID | 
 **search** | **str**| The string to search on | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]
 **strict** | **bool**| Whether the search should be a strict match | [optional] [default to False]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCharactersCharacterIdSearchOk**](GetCharactersCharacterIdSearchOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of search results |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

