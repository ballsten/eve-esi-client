# esi_client.InsuranceApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_insurance_prices**](InsuranceApi.md#get_insurance_prices) | **GET** /insurance/prices/ | List insurance levels


# **get_insurance_prices**
> List[GetInsurancePrices200Ok] get_insurance_prices(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

List insurance levels

Return available insurance levels for all ship types  --- Alternate route: `/dev/insurance/prices/`  Alternate route: `/legacy/insurance/prices/`  Alternate route: `/v1/insurance/prices/`  --- This route is cached for up to 3600 seconds

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_insurance_prices200_ok import GetInsurancePrices200Ok
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
    api_instance = esi_client.InsuranceApi(api_client)
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')

    try:
        # List insurance levels
        api_response = api_instance.get_insurance_prices(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
        print("The response of InsuranceApi->get_insurance_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsuranceApi->get_insurance_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]

### Return type

[**List[GetInsurancePrices200Ok]**](GetInsurancePrices200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of insurance levels for all ship types |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

