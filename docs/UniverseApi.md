# esi_client.UniverseApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_universe_ancestries**](UniverseApi.md#get_universe_ancestries) | **GET** /universe/ancestries/ | Get ancestries
[**get_universe_asteroid_belts_asteroid_belt_id**](UniverseApi.md#get_universe_asteroid_belts_asteroid_belt_id) | **GET** /universe/asteroid_belts/{asteroid_belt_id}/ | Get asteroid belt information
[**get_universe_bloodlines**](UniverseApi.md#get_universe_bloodlines) | **GET** /universe/bloodlines/ | Get bloodlines
[**get_universe_categories**](UniverseApi.md#get_universe_categories) | **GET** /universe/categories/ | Get item categories
[**get_universe_categories_category_id**](UniverseApi.md#get_universe_categories_category_id) | **GET** /universe/categories/{category_id}/ | Get item category information
[**get_universe_constellations**](UniverseApi.md#get_universe_constellations) | **GET** /universe/constellations/ | Get constellations
[**get_universe_constellations_constellation_id**](UniverseApi.md#get_universe_constellations_constellation_id) | **GET** /universe/constellations/{constellation_id}/ | Get constellation information
[**get_universe_factions**](UniverseApi.md#get_universe_factions) | **GET** /universe/factions/ | Get factions
[**get_universe_graphics**](UniverseApi.md#get_universe_graphics) | **GET** /universe/graphics/ | Get graphics
[**get_universe_graphics_graphic_id**](UniverseApi.md#get_universe_graphics_graphic_id) | **GET** /universe/graphics/{graphic_id}/ | Get graphic information
[**get_universe_groups**](UniverseApi.md#get_universe_groups) | **GET** /universe/groups/ | Get item groups
[**get_universe_groups_group_id**](UniverseApi.md#get_universe_groups_group_id) | **GET** /universe/groups/{group_id}/ | Get item group information
[**get_universe_moons_moon_id**](UniverseApi.md#get_universe_moons_moon_id) | **GET** /universe/moons/{moon_id}/ | Get moon information
[**get_universe_planets_planet_id**](UniverseApi.md#get_universe_planets_planet_id) | **GET** /universe/planets/{planet_id}/ | Get planet information
[**get_universe_races**](UniverseApi.md#get_universe_races) | **GET** /universe/races/ | Get character races
[**get_universe_regions**](UniverseApi.md#get_universe_regions) | **GET** /universe/regions/ | Get regions
[**get_universe_regions_region_id**](UniverseApi.md#get_universe_regions_region_id) | **GET** /universe/regions/{region_id}/ | Get region information
[**get_universe_stargates_stargate_id**](UniverseApi.md#get_universe_stargates_stargate_id) | **GET** /universe/stargates/{stargate_id}/ | Get stargate information
[**get_universe_stars_star_id**](UniverseApi.md#get_universe_stars_star_id) | **GET** /universe/stars/{star_id}/ | Get star information
[**get_universe_stations_station_id**](UniverseApi.md#get_universe_stations_station_id) | **GET** /universe/stations/{station_id}/ | Get station information
[**get_universe_structures**](UniverseApi.md#get_universe_structures) | **GET** /universe/structures/ | List all public structures
[**get_universe_structures_structure_id**](UniverseApi.md#get_universe_structures_structure_id) | **GET** /universe/structures/{structure_id}/ | Get structure information
[**get_universe_system_jumps**](UniverseApi.md#get_universe_system_jumps) | **GET** /universe/system_jumps/ | Get system jumps
[**get_universe_system_kills**](UniverseApi.md#get_universe_system_kills) | **GET** /universe/system_kills/ | Get system kills
[**get_universe_systems**](UniverseApi.md#get_universe_systems) | **GET** /universe/systems/ | Get solar systems
[**get_universe_systems_system_id**](UniverseApi.md#get_universe_systems_system_id) | **GET** /universe/systems/{system_id}/ | Get solar system information
[**get_universe_types**](UniverseApi.md#get_universe_types) | **GET** /universe/types/ | Get types
[**get_universe_types_type_id**](UniverseApi.md#get_universe_types_type_id) | **GET** /universe/types/{type_id}/ | Get type information
[**post_universe_ids**](UniverseApi.md#post_universe_ids) | **POST** /universe/ids/ | Bulk names to IDs
[**post_universe_names**](UniverseApi.md#post_universe_names) | **POST** /universe/names/ | Get names and categories for a set of IDs


# **get_universe_ancestries**
> List[GetUniverseAncestries200Ok] get_universe_ancestries(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get ancestries

Get all character ancestries  --- Alternate route: `/legacy/universe/ancestries/`  Alternate route: `/v1/universe/ancestries/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_ancestries200_ok import GetUniverseAncestries200Ok
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
    api_instance = esi_client.UniverseApi(api_client)
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')

    try:
        # Get ancestries
        api_response = api_instance.get_universe_ancestries(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
        print("The response of UniverseApi->get_universe_ancestries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_ancestries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]

### Return type

[**List[GetUniverseAncestries200Ok]**](GetUniverseAncestries200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of ancestries |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_asteroid_belts_asteroid_belt_id**
> GetUniverseAsteroidBeltsAsteroidBeltIdOk get_universe_asteroid_belts_asteroid_belt_id(asteroid_belt_id, datasource=datasource, if_none_match=if_none_match)

Get asteroid belt information

Get information on an asteroid belt  --- Alternate route: `/legacy/universe/asteroid_belts/{asteroid_belt_id}/`  Alternate route: `/v1/universe/asteroid_belts/{asteroid_belt_id}/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_asteroid_belts_asteroid_belt_id_ok import GetUniverseAsteroidBeltsAsteroidBeltIdOk
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
    api_instance = esi_client.UniverseApi(api_client)
    asteroid_belt_id = 56 # int | asteroid_belt_id integer
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get asteroid belt information
        api_response = api_instance.get_universe_asteroid_belts_asteroid_belt_id(asteroid_belt_id, datasource=datasource, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_asteroid_belts_asteroid_belt_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_asteroid_belts_asteroid_belt_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asteroid_belt_id** | **int**| asteroid_belt_id integer | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetUniverseAsteroidBeltsAsteroidBeltIdOk**](GetUniverseAsteroidBeltsAsteroidBeltIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about an asteroid belt |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | Asteroid belt not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_bloodlines**
> List[GetUniverseBloodlines200Ok] get_universe_bloodlines(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get bloodlines

Get a list of bloodlines  --- Alternate route: `/legacy/universe/bloodlines/`  Alternate route: `/v1/universe/bloodlines/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_bloodlines200_ok import GetUniverseBloodlines200Ok
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
    api_instance = esi_client.UniverseApi(api_client)
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')

    try:
        # Get bloodlines
        api_response = api_instance.get_universe_bloodlines(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
        print("The response of UniverseApi->get_universe_bloodlines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_bloodlines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]

### Return type

[**List[GetUniverseBloodlines200Ok]**](GetUniverseBloodlines200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of bloodlines |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_categories**
> List[int] get_universe_categories(datasource=datasource, if_none_match=if_none_match)

Get item categories

Get a list of item categories  --- Alternate route: `/legacy/universe/categories/`  Alternate route: `/v1/universe/categories/`  --- This route expires daily at 11:05

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
    api_instance = esi_client.UniverseApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get item categories
        api_response = api_instance.get_universe_categories(datasource=datasource, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
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
**200** | A list of item category ids |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_categories_category_id**
> GetUniverseCategoriesCategoryIdOk get_universe_categories_category_id(category_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get item category information

Get information of an item category  --- Alternate route: `/legacy/universe/categories/{category_id}/`  Alternate route: `/v1/universe/categories/{category_id}/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_categories_category_id_ok import GetUniverseCategoriesCategoryIdOk
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
    api_instance = esi_client.UniverseApi(api_client)
    category_id = 56 # int | An Eve item category ID
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')

    try:
        # Get item category information
        api_response = api_instance.get_universe_categories_category_id(category_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
        print("The response of UniverseApi->get_universe_categories_category_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_categories_category_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| An Eve item category ID | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]

### Return type

[**GetUniverseCategoriesCategoryIdOk**](GetUniverseCategoriesCategoryIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about an item category |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | Category not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_constellations**
> List[int] get_universe_constellations(datasource=datasource, if_none_match=if_none_match)

Get constellations

Get a list of constellations  --- Alternate route: `/legacy/universe/constellations/`  Alternate route: `/v1/universe/constellations/`  --- This route expires daily at 11:05

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
    api_instance = esi_client.UniverseApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get constellations
        api_response = api_instance.get_universe_constellations(datasource=datasource, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_constellations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_constellations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
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
**200** | A list of constellation ids |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_constellations_constellation_id**
> GetUniverseConstellationsConstellationIdOk get_universe_constellations_constellation_id(constellation_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get constellation information

Get information on a constellation  --- Alternate route: `/legacy/universe/constellations/{constellation_id}/`  Alternate route: `/v1/universe/constellations/{constellation_id}/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_constellations_constellation_id_ok import GetUniverseConstellationsConstellationIdOk
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
    api_instance = esi_client.UniverseApi(api_client)
    constellation_id = 56 # int | constellation_id integer
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')

    try:
        # Get constellation information
        api_response = api_instance.get_universe_constellations_constellation_id(constellation_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
        print("The response of UniverseApi->get_universe_constellations_constellation_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_constellations_constellation_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **constellation_id** | **int**| constellation_id integer | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]

### Return type

[**GetUniverseConstellationsConstellationIdOk**](GetUniverseConstellationsConstellationIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about a constellation |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | Constellation not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_factions**
> List[GetUniverseFactions200Ok] get_universe_factions(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get factions

Get a list of factions  --- Alternate route: `/dev/universe/factions/`  Alternate route: `/v2/universe/factions/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_factions200_ok import GetUniverseFactions200Ok
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
    api_instance = esi_client.UniverseApi(api_client)
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')

    try:
        # Get factions
        api_response = api_instance.get_universe_factions(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
        print("The response of UniverseApi->get_universe_factions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_factions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]

### Return type

[**List[GetUniverseFactions200Ok]**](GetUniverseFactions200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of factions |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_graphics**
> List[int] get_universe_graphics(datasource=datasource, if_none_match=if_none_match)

Get graphics

Get a list of graphics  --- Alternate route: `/legacy/universe/graphics/`  Alternate route: `/v1/universe/graphics/`  --- This route expires daily at 11:05

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
    api_instance = esi_client.UniverseApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get graphics
        api_response = api_instance.get_universe_graphics(datasource=datasource, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_graphics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_graphics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
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
**200** | A list of graphic ids |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_graphics_graphic_id**
> GetUniverseGraphicsGraphicIdOk get_universe_graphics_graphic_id(graphic_id, datasource=datasource, if_none_match=if_none_match)

Get graphic information

Get information on a graphic  --- Alternate route: `/dev/universe/graphics/{graphic_id}/`  Alternate route: `/legacy/universe/graphics/{graphic_id}/`  Alternate route: `/v1/universe/graphics/{graphic_id}/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_graphics_graphic_id_ok import GetUniverseGraphicsGraphicIdOk
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
    api_instance = esi_client.UniverseApi(api_client)
    graphic_id = 56 # int | graphic_id integer
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get graphic information
        api_response = api_instance.get_universe_graphics_graphic_id(graphic_id, datasource=datasource, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_graphics_graphic_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_graphics_graphic_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graphic_id** | **int**| graphic_id integer | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetUniverseGraphicsGraphicIdOk**](GetUniverseGraphicsGraphicIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about a graphic |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | Graphic not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_groups**
> List[int] get_universe_groups(datasource=datasource, if_none_match=if_none_match, page=page)

Get item groups

Get a list of item groups  --- Alternate route: `/legacy/universe/groups/`  Alternate route: `/v1/universe/groups/`  --- This route expires daily at 11:05

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
    api_instance = esi_client.UniverseApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    page = 1 # int | Which page of results to return (optional) (default to 1)

    try:
        # Get item groups
        api_response = api_instance.get_universe_groups(datasource=datasource, if_none_match=if_none_match, page=page)
        print("The response of UniverseApi->get_universe_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]

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
**200** | A list of item group ids |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * X-Pages - Maximum page number <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_groups_group_id**
> GetUniverseGroupsGroupIdOk get_universe_groups_group_id(group_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get item group information

Get information on an item group  --- Alternate route: `/dev/universe/groups/{group_id}/`  Alternate route: `/legacy/universe/groups/{group_id}/`  Alternate route: `/v1/universe/groups/{group_id}/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_groups_group_id_ok import GetUniverseGroupsGroupIdOk
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
    api_instance = esi_client.UniverseApi(api_client)
    group_id = 56 # int | An Eve item group ID
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')

    try:
        # Get item group information
        api_response = api_instance.get_universe_groups_group_id(group_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
        print("The response of UniverseApi->get_universe_groups_group_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_groups_group_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| An Eve item group ID | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]

### Return type

[**GetUniverseGroupsGroupIdOk**](GetUniverseGroupsGroupIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about an item group |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | Group not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_moons_moon_id**
> GetUniverseMoonsMoonIdOk get_universe_moons_moon_id(moon_id, datasource=datasource, if_none_match=if_none_match)

Get moon information

Get information on a moon  --- Alternate route: `/legacy/universe/moons/{moon_id}/`  Alternate route: `/v1/universe/moons/{moon_id}/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_moons_moon_id_ok import GetUniverseMoonsMoonIdOk
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
    api_instance = esi_client.UniverseApi(api_client)
    moon_id = 56 # int | moon_id integer
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get moon information
        api_response = api_instance.get_universe_moons_moon_id(moon_id, datasource=datasource, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_moons_moon_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_moons_moon_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moon_id** | **int**| moon_id integer | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetUniverseMoonsMoonIdOk**](GetUniverseMoonsMoonIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about a moon |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | Moon not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_planets_planet_id**
> GetUniversePlanetsPlanetIdOk get_universe_planets_planet_id(planet_id, datasource=datasource, if_none_match=if_none_match)

Get planet information

Get information on a planet  --- Alternate route: `/legacy/universe/planets/{planet_id}/`  Alternate route: `/v1/universe/planets/{planet_id}/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_planets_planet_id_ok import GetUniversePlanetsPlanetIdOk
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
    api_instance = esi_client.UniverseApi(api_client)
    planet_id = 56 # int | planet_id integer
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get planet information
        api_response = api_instance.get_universe_planets_planet_id(planet_id, datasource=datasource, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_planets_planet_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_planets_planet_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **planet_id** | **int**| planet_id integer | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetUniversePlanetsPlanetIdOk**](GetUniversePlanetsPlanetIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about a planet |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | Planet not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_races**
> List[GetUniverseRaces200Ok] get_universe_races(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get character races

Get a list of character races  --- Alternate route: `/dev/universe/races/`  Alternate route: `/legacy/universe/races/`  Alternate route: `/v1/universe/races/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_races200_ok import GetUniverseRaces200Ok
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
    api_instance = esi_client.UniverseApi(api_client)
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')

    try:
        # Get character races
        api_response = api_instance.get_universe_races(accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
        print("The response of UniverseApi->get_universe_races:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_races: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]

### Return type

[**List[GetUniverseRaces200Ok]**](GetUniverseRaces200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of character races |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_regions**
> List[int] get_universe_regions(datasource=datasource, if_none_match=if_none_match)

Get regions

Get a list of regions  --- Alternate route: `/legacy/universe/regions/`  Alternate route: `/v1/universe/regions/`  --- This route expires daily at 11:05

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
    api_instance = esi_client.UniverseApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get regions
        api_response = api_instance.get_universe_regions(datasource=datasource, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
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
**200** | A list of region ids |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_regions_region_id**
> GetUniverseRegionsRegionIdOk get_universe_regions_region_id(region_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get region information

Get information on a region  --- Alternate route: `/legacy/universe/regions/{region_id}/`  Alternate route: `/v1/universe/regions/{region_id}/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_regions_region_id_ok import GetUniverseRegionsRegionIdOk
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
    api_instance = esi_client.UniverseApi(api_client)
    region_id = 56 # int | region_id integer
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')

    try:
        # Get region information
        api_response = api_instance.get_universe_regions_region_id(region_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
        print("The response of UniverseApi->get_universe_regions_region_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_regions_region_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **int**| region_id integer | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]

### Return type

[**GetUniverseRegionsRegionIdOk**](GetUniverseRegionsRegionIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about a region |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | Region not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_stargates_stargate_id**
> GetUniverseStargatesStargateIdOk get_universe_stargates_stargate_id(stargate_id, datasource=datasource, if_none_match=if_none_match)

Get stargate information

Get information on a stargate  --- Alternate route: `/legacy/universe/stargates/{stargate_id}/`  Alternate route: `/v1/universe/stargates/{stargate_id}/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_stargates_stargate_id_ok import GetUniverseStargatesStargateIdOk
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
    api_instance = esi_client.UniverseApi(api_client)
    stargate_id = 56 # int | stargate_id integer
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get stargate information
        api_response = api_instance.get_universe_stargates_stargate_id(stargate_id, datasource=datasource, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_stargates_stargate_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_stargates_stargate_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stargate_id** | **int**| stargate_id integer | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetUniverseStargatesStargateIdOk**](GetUniverseStargatesStargateIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about a stargate |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | Stargate not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_stars_star_id**
> GetUniverseStarsStarIdOk get_universe_stars_star_id(star_id, datasource=datasource, if_none_match=if_none_match)

Get star information

Get information on a star  --- Alternate route: `/legacy/universe/stars/{star_id}/`  Alternate route: `/v1/universe/stars/{star_id}/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_stars_star_id_ok import GetUniverseStarsStarIdOk
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
    api_instance = esi_client.UniverseApi(api_client)
    star_id = 56 # int | star_id integer
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get star information
        api_response = api_instance.get_universe_stars_star_id(star_id, datasource=datasource, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_stars_star_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_stars_star_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **star_id** | **int**| star_id integer | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetUniverseStarsStarIdOk**](GetUniverseStarsStarIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about a star |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_stations_station_id**
> GetUniverseStationsStationIdOk get_universe_stations_station_id(station_id, datasource=datasource, if_none_match=if_none_match)

Get station information

Get information on a station  --- Alternate route: `/dev/universe/stations/{station_id}/`  Alternate route: `/v2/universe/stations/{station_id}/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_stations_station_id_ok import GetUniverseStationsStationIdOk
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
    api_instance = esi_client.UniverseApi(api_client)
    station_id = 56 # int | station_id integer
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get station information
        api_response = api_instance.get_universe_stations_station_id(station_id, datasource=datasource, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_stations_station_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_stations_station_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **int**| station_id integer | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetUniverseStationsStationIdOk**](GetUniverseStationsStationIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about a station |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | Station not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_structures**
> List[int] get_universe_structures(datasource=datasource, filter=filter, if_none_match=if_none_match)

List all public structures

List all public structures  --- Alternate route: `/dev/universe/structures/`  Alternate route: `/legacy/universe/structures/`  Alternate route: `/v1/universe/structures/`  --- This route is cached for up to 3600 seconds

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
    api_instance = esi_client.UniverseApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    filter = 'filter_example' # str | Only list public structures that have this service online (optional)
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # List all public structures
        api_response = api_instance.get_universe_structures(datasource=datasource, filter=filter, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_structures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_structures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **filter** | **str**| Only list public structures that have this service online | [optional] 
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
**200** | List of public structure IDs |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_structures_structure_id**
> GetUniverseStructuresStructureIdOk get_universe_structures_structure_id(structure_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get structure information

Returns information on requested structure if you are on the ACL. Otherwise, returns \"Forbidden\" for all inputs.  --- Alternate route: `/v2/universe/structures/{structure_id}/`  --- This route is cached for up to 3600 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_universe_structures_structure_id_ok import GetUniverseStructuresStructureIdOk
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
    api_instance = esi_client.UniverseApi(api_client)
    structure_id = 56 # int | An Eve structure ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get structure information
        api_response = api_instance.get_universe_structures_structure_id(structure_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of UniverseApi->get_universe_structures_structure_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_structures_structure_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **structure_id** | **int**| An Eve structure ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetUniverseStructuresStructureIdOk**](GetUniverseStructuresStructureIdOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data about a structure |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Structure not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_system_jumps**
> List[GetUniverseSystemJumps200Ok] get_universe_system_jumps(datasource=datasource, if_none_match=if_none_match)

Get system jumps

Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed  --- Alternate route: `/legacy/universe/system_jumps/`  Alternate route: `/v1/universe/system_jumps/`  --- This route is cached for up to 3600 seconds

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_system_jumps200_ok import GetUniverseSystemJumps200Ok
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
    api_instance = esi_client.UniverseApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get system jumps
        api_response = api_instance.get_universe_system_jumps(datasource=datasource, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_system_jumps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_system_jumps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**List[GetUniverseSystemJumps200Ok]**](GetUniverseSystemJumps200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of systems and number of jumps |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_system_kills**
> List[GetUniverseSystemKills200Ok] get_universe_system_kills(datasource=datasource, if_none_match=if_none_match)

Get system kills

Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed  --- Alternate route: `/v2/universe/system_kills/`  --- This route is cached for up to 3600 seconds

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_system_kills200_ok import GetUniverseSystemKills200Ok
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
    api_instance = esi_client.UniverseApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get system kills
        api_response = api_instance.get_universe_system_kills(datasource=datasource, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_system_kills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_system_kills: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**List[GetUniverseSystemKills200Ok]**](GetUniverseSystemKills200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of systems and number of ship, pod and NPC kills |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_systems**
> List[int] get_universe_systems(datasource=datasource, if_none_match=if_none_match)

Get solar systems

Get a list of solar systems  --- Alternate route: `/dev/universe/systems/`  Alternate route: `/legacy/universe/systems/`  Alternate route: `/v1/universe/systems/`  --- This route expires daily at 11:05

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
    api_instance = esi_client.UniverseApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

    try:
        # Get solar systems
        api_response = api_instance.get_universe_systems(datasource=datasource, if_none_match=if_none_match)
        print("The response of UniverseApi->get_universe_systems:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_systems: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
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
**200** | A list of solar system ids |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_systems_system_id**
> GetUniverseSystemsSystemIdOk get_universe_systems_system_id(system_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get solar system information

Get information on a solar system.  --- Alternate route: `/dev/universe/systems/{system_id}/`  Alternate route: `/v4/universe/systems/{system_id}/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_systems_system_id_ok import GetUniverseSystemsSystemIdOk
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
    api_instance = esi_client.UniverseApi(api_client)
    system_id = 56 # int | system_id integer
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')

    try:
        # Get solar system information
        api_response = api_instance.get_universe_systems_system_id(system_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
        print("The response of UniverseApi->get_universe_systems_system_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_systems_system_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| system_id integer | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]

### Return type

[**GetUniverseSystemsSystemIdOk**](GetUniverseSystemsSystemIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about a solar system |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | Solar system not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_types**
> List[int] get_universe_types(datasource=datasource, if_none_match=if_none_match, page=page)

Get types

Get a list of type ids  --- Alternate route: `/legacy/universe/types/`  Alternate route: `/v1/universe/types/`  --- This route expires daily at 11:05

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
    api_instance = esi_client.UniverseApi(api_client)
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    page = 1 # int | Which page of results to return (optional) (default to 1)

    try:
        # Get types
        api_response = api_instance.get_universe_types(datasource=datasource, if_none_match=if_none_match, page=page)
        print("The response of UniverseApi->get_universe_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]

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
**200** | A list of type ids |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * X-Pages - Maximum page number <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_types_type_id**
> GetUniverseTypesTypeIdOk get_universe_types_type_id(type_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)

Get type information

Get information on a type  --- Alternate route: `/dev/universe/types/{type_id}/`  Alternate route: `/v3/universe/types/{type_id}/`  --- This route expires daily at 11:05

### Example


```python
import time
import os
import esi_client
from esi_client.models.get_universe_types_type_id_ok import GetUniverseTypesTypeIdOk
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
    api_instance = esi_client.UniverseApi(api_client)
    type_id = 56 # int | An Eve item type ID
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')

    try:
        # Get type information
        api_response = api_instance.get_universe_types_type_id(type_id, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language)
        print("The response of UniverseApi->get_universe_types_type_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->get_universe_types_type_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **int**| An Eve item type ID | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]

### Return type

[**GetUniverseTypesTypeIdOk**](GetUniverseTypesTypeIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about a type |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**404** | Type not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_universe_ids**
> PostUniverseIdsOk post_universe_ids(names, accept_language=accept_language, datasource=datasource, language=language)

Bulk names to IDs

Resolve a set of names to IDs in the following categories: agents, alliances, characters, constellations, corporations factions, inventory_types, regions, stations, and systems. Only exact matches will be returned. All names searched for are cached for 12 hours  --- Alternate route: `/dev/universe/ids/`  Alternate route: `/legacy/universe/ids/`  Alternate route: `/v1/universe/ids/` 

### Example


```python
import time
import os
import esi_client
from esi_client.models.post_universe_ids_ok import PostUniverseIdsOk
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
    api_instance = esi_client.UniverseApi(api_client)
    names = ['names_example'] # List[str] | The names to resolve
    accept_language = 'en' # str | Language to use in the response (optional) (default to 'en')
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to 'en')

    try:
        # Bulk names to IDs
        api_response = api_instance.post_universe_ids(names, accept_language=accept_language, datasource=datasource, language=language)
        print("The response of UniverseApi->post_universe_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->post_universe_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**List[str]**](str.md)| The names to resolve | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to &#39;en&#39;]
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to &#39;en&#39;]

### Return type

[**PostUniverseIdsOk**](PostUniverseIdsOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of id/name associations for a set of names divided by category. Any name passed in that did not have a match will be ommitted |  * Content-Language - The language used in the response <br>  |
**400** | Bad request |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_universe_names**
> List[PostUniverseNames200Ok] post_universe_names(ids, datasource=datasource)

Get names and categories for a set of IDs

Resolve a set of IDs to names and categories. Supported ID's for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types, Factions  --- Alternate route: `/dev/universe/names/`  Alternate route: `/v3/universe/names/` 

### Example


```python
import time
import os
import esi_client
from esi_client.models.post_universe_names200_ok import PostUniverseNames200Ok
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
    api_instance = esi_client.UniverseApi(api_client)
    ids = [56] # List[int] | The ids to resolve
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')

    try:
        # Get names and categories for a set of IDs
        api_response = api_instance.post_universe_names(ids, datasource=datasource)
        print("The response of UniverseApi->post_universe_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniverseApi->post_universe_names: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| The ids to resolve | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]

### Return type

[**List[PostUniverseNames200Ok]**](PostUniverseNames200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of id/name associations for a set of IDs. All IDs must resolve to a name, or nothing will be returned |  -  |
**400** | Bad request |  -  |
**404** | Ensure all IDs are valid before resolving |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

