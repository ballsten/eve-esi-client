# esi_client.SovereigntyApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sovereignty_campaigns**](SovereigntyApi.md#get_sovereignty_campaigns) | **GET** /sovereignty/campaigns/ | List sovereignty campaigns
[**get_sovereignty_map**](SovereigntyApi.md#get_sovereignty_map) | **GET** /sovereignty/map/ | List sovereignty of systems
[**get_sovereignty_structures**](SovereigntyApi.md#get_sovereignty_structures) | **GET** /sovereignty/structures/ | List sovereignty structures


# **get_sovereignty_campaigns**
> List[GetSovereigntyCampaigns200Ok] get_sovereignty_campaigns(datasource=datasource, if_none_match=if_none_match)

List sovereignty campaigns

Shows sovereignty data for campaigns.  --- Alternate route: `/dev/sovereignty/campaigns/`  Alternate route: `/legacy/sovereignty/campaigns/`  Alternate route: `/v1/sovereignty/campaigns/`  --- This route is cached for up to 5 seconds

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_sovereignty_campaigns200_ok import GetSovereigntyCampaigns200Ok
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
    api_instance = esi_client.SovereigntyApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # List sovereignty campaigns
        api_response = api_instance.get_sovereignty_campaigns(datasource=datasource, if_none_match=if_none_match)
        print("The response of SovereigntyApi->get_sovereignty_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SovereigntyApi->get_sovereignty_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**List[GetSovereigntyCampaigns200Ok]**](GetSovereigntyCampaigns200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sovereignty campaigns |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sovereignty_map**
> List[GetSovereigntyMap200Ok] get_sovereignty_map(datasource=datasource, if_none_match=if_none_match)

List sovereignty of systems

Shows sovereignty information for solar systems  --- Alternate route: `/dev/sovereignty/map/`  Alternate route: `/legacy/sovereignty/map/`  Alternate route: `/v1/sovereignty/map/`  --- This route is cached for up to 3600 seconds

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_sovereignty_map200_ok import GetSovereigntyMap200Ok
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
    api_instance = esi_client.SovereigntyApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # List sovereignty of systems
        api_response = api_instance.get_sovereignty_map(datasource=datasource, if_none_match=if_none_match)
        print("The response of SovereigntyApi->get_sovereignty_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SovereigntyApi->get_sovereignty_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**List[GetSovereigntyMap200Ok]**](GetSovereigntyMap200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sovereignty information for solar systems in New Eden |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sovereignty_structures**
> List[GetSovereigntyStructures200Ok] get_sovereignty_structures(datasource=datasource, if_none_match=if_none_match)

List sovereignty structures

Shows sovereignty data for structures.  --- Alternate route: `/dev/sovereignty/structures/`  Alternate route: `/legacy/sovereignty/structures/`  Alternate route: `/v1/sovereignty/structures/`  --- This route is cached for up to 120 seconds

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_sovereignty_structures200_ok import GetSovereigntyStructures200Ok
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
    api_instance = esi_client.SovereigntyApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # List sovereignty structures
        api_response = api_instance.get_sovereignty_structures(datasource=datasource, if_none_match=if_none_match)
        print("The response of SovereigntyApi->get_sovereignty_structures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SovereigntyApi->get_sovereignty_structures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**List[GetSovereigntyStructures200Ok]**](GetSovereigntyStructures200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sovereignty structures |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

