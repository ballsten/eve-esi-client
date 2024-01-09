# esi_client.FittingsApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_characters_character_id_fittings_fitting_id**](FittingsApi.md#delete_characters_character_id_fittings_fitting_id) | **DELETE** /characters/{character_id}/fittings/{fitting_id}/ | Delete fitting
[**get_characters_character_id_fittings**](FittingsApi.md#get_characters_character_id_fittings) | **GET** /characters/{character_id}/fittings/ | Get fittings
[**post_characters_character_id_fittings**](FittingsApi.md#post_characters_character_id_fittings) | **POST** /characters/{character_id}/fittings/ | Create fitting


# **delete_characters_character_id_fittings_fitting_id**
> delete_characters_character_id_fittings_fitting_id(character_id, fitting_id, datasource=datasource, token=token)

Delete fitting

Delete a fitting from a character  --- Alternate route: `/dev/characters/{character_id}/fittings/{fitting_id}/`  Alternate route: `/legacy/characters/{character_id}/fittings/{fitting_id}/`  Alternate route: `/v1/characters/{character_id}/fittings/{fitting_id}/` 

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
    api_instance = esi_client.FittingsApi(api_client)
    character_id = 56 # int | An EVE character ID
    fitting_id = 56 # int | ID for a fitting of this character
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Delete fitting
        api_instance.delete_characters_character_id_fittings_fitting_id(character_id, fitting_id, datasource=datasource, token=token)
    except Exception as e:
        print("Exception when calling FittingsApi->delete_characters_character_id_fittings_fitting_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **fitting_id** | **int**| ID for a fitting of this character | 
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
**204** | Fitting deleted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_fittings**
> List[GetCharactersCharacterIdFittings200Ok] get_characters_character_id_fittings(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get fittings

Return fittings of a character  --- Alternate route: `/dev/characters/{character_id}/fittings/`  Alternate route: `/v2/characters/{character_id}/fittings/`  --- This route is cached for up to 300 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_fittings200_ok import GetCharactersCharacterIdFittings200Ok
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
    api_instance = esi_client.FittingsApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get fittings
        api_response = api_instance.get_characters_character_id_fittings(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of FittingsApi->get_characters_character_id_fittings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FittingsApi->get_characters_character_id_fittings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCharactersCharacterIdFittings200Ok]**](GetCharactersCharacterIdFittings200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of fittings |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_characters_character_id_fittings**
> PostCharactersCharacterIdFittingsCreated post_characters_character_id_fittings(character_id, fitting, datasource=datasource, token=token)

Create fitting

Save a new fitting for a character  --- Alternate route: `/dev/characters/{character_id}/fittings/`  Alternate route: `/v2/characters/{character_id}/fittings/` 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.post_characters_character_id_fittings_created import PostCharactersCharacterIdFittingsCreated
from esi_client.models.post_characters_character_id_fittings_fitting import PostCharactersCharacterIdFittingsFitting
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
    api_instance = esi_client.FittingsApi(api_client)
    character_id = 56 # int | An EVE character ID
    fitting = esi_client.PostCharactersCharacterIdFittingsFitting() # PostCharactersCharacterIdFittingsFitting | Details about the new fitting
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Create fitting
        api_response = api_instance.post_characters_character_id_fittings(character_id, fitting, datasource=datasource, token=token)
        print("The response of FittingsApi->post_characters_character_id_fittings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FittingsApi->post_characters_character_id_fittings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **fitting** | [**PostCharactersCharacterIdFittingsFitting**](PostCharactersCharacterIdFittingsFitting.md)| Details about the new fitting | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**PostCharactersCharacterIdFittingsCreated**](PostCharactersCharacterIdFittingsCreated.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A list of fittings |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

