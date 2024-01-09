# esi_client.RoutesApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_route_origin_destination**](RoutesApi.md#get_route_origin_destination) | **GET** /route/{origin}/{destination}/ | Get route


# **get_route_origin_destination**
> List[int] get_route_origin_destination(destination, origin, avoid=avoid, connections=connections, datasource=datasource, flag=flag, if_none_match=if_none_match)

Get route

Get the systems between origin and destination  --- Alternate route: `/dev/route/{origin}/{destination}/`  Alternate route: `/legacy/route/{origin}/{destination}/`  Alternate route: `/v1/route/{origin}/{destination}/`  --- This route is cached for up to 86400 seconds

### Example


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


# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.RoutesApi(api_client)
    destination = 56 # int | destination solar system ID
    origin = 56 # int | origin solar system ID
    avoid = [56] # List[int] | avoid solar system ID(s) (optional)
    connections = [esi_client.List[int]()] # List[List[int]] | connected solar system pairs (optional)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    flag = 'shortest' # str | route security preference (optional) (default to 'shortest')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get route
        api_response = api_instance.get_route_origin_destination(destination, origin, avoid=avoid, connections=connections, datasource=datasource, flag=flag, if_none_match=if_none_match)
        print("The response of RoutesApi->get_route_origin_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->get_route_origin_destination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination** | **int**| destination solar system ID | 
 **origin** | **int**| origin solar system ID | 
 **avoid** | [**List[int]**](int.md)| avoid solar system ID(s) | [optional] 
 **connections** | [**List[List[int]]**](List[int].md)| connected solar system pairs | [optional] 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **flag** | **str**| route security preference | [optional] [default to &#39;shortest&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

**List[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Solar systems in route from origin to destination |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | No route found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

