# esi_client.ContactsApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_characters_character_id_contacts**](ContactsApi.md#delete_characters_character_id_contacts) | **DELETE** /characters/{character_id}/contacts/ | Delete contacts
[**get_alliances_alliance_id_contacts**](ContactsApi.md#get_alliances_alliance_id_contacts) | **GET** /alliances/{alliance_id}/contacts/ | Get alliance contacts
[**get_alliances_alliance_id_contacts_labels**](ContactsApi.md#get_alliances_alliance_id_contacts_labels) | **GET** /alliances/{alliance_id}/contacts/labels/ | Get alliance contact labels
[**get_characters_character_id_contacts**](ContactsApi.md#get_characters_character_id_contacts) | **GET** /characters/{character_id}/contacts/ | Get contacts
[**get_characters_character_id_contacts_labels**](ContactsApi.md#get_characters_character_id_contacts_labels) | **GET** /characters/{character_id}/contacts/labels/ | Get contact labels
[**get_corporations_corporation_id_contacts**](ContactsApi.md#get_corporations_corporation_id_contacts) | **GET** /corporations/{corporation_id}/contacts/ | Get corporation contacts
[**get_corporations_corporation_id_contacts_labels**](ContactsApi.md#get_corporations_corporation_id_contacts_labels) | **GET** /corporations/{corporation_id}/contacts/labels/ | Get corporation contact labels
[**post_characters_character_id_contacts**](ContactsApi.md#post_characters_character_id_contacts) | **POST** /characters/{character_id}/contacts/ | Add contacts
[**put_characters_character_id_contacts**](ContactsApi.md#put_characters_character_id_contacts) | **PUT** /characters/{character_id}/contacts/ | Edit contacts


# **delete_characters_character_id_contacts**
> delete_characters_character_id_contacts(character_id, contact_ids, datasource=datasource, token=token)

Delete contacts

Bulk delete contacts  --- Alternate route: `/dev/characters/{character_id}/contacts/`  Alternate route: `/v2/characters/{character_id}/contacts/` 

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
    api_instance = esi_client.ContactsApi(api_client)
    character_id = 56 # int | An EVE character ID
    contact_ids = [56] # List[int] | A list of contacts to delete
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Delete contacts
        api_instance.delete_characters_character_id_contacts(character_id, contact_ids, datasource=datasource, token=token)
    except Exception as e:
        print("Exception when calling ContactsApi->delete_characters_character_id_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **contact_ids** | [**List[int]**](int.md)| A list of contacts to delete | 
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
**204** | Contacts deleted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alliances_alliance_id_contacts**
> List[GetAlliancesAllianceIdContacts200Ok] get_alliances_alliance_id_contacts(alliance_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get alliance contacts

Return contacts of an alliance  --- Alternate route: `/dev/alliances/{alliance_id}/contacts/`  Alternate route: `/v2/alliances/{alliance_id}/contacts/`  --- This route is cached for up to 300 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_alliances_alliance_id_contacts200_ok import GetAlliancesAllianceIdContacts200Ok
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
    api_instance = esi_client.ContactsApi(api_client)
    alliance_id = 56 # int | An EVE alliance ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    page = 1 # int | Which page of results to return (optional) (default to 1)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get alliance contacts
        api_response = api_instance.get_alliances_alliance_id_contacts(alliance_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
        print("The response of ContactsApi->get_alliances_alliance_id_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_alliances_alliance_id_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alliance_id** | **int**| An EVE alliance ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetAlliancesAllianceIdContacts200Ok]**](GetAlliancesAllianceIdContacts200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of contacts |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * X-Pages - Maximum page number <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alliances_alliance_id_contacts_labels**
> List[GetAlliancesAllianceIdContactsLabels200Ok] get_alliances_alliance_id_contacts_labels(alliance_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get alliance contact labels

Return custom labels for an alliance's contacts  --- Alternate route: `/dev/alliances/{alliance_id}/contacts/labels/`  Alternate route: `/legacy/alliances/{alliance_id}/contacts/labels/`  Alternate route: `/v1/alliances/{alliance_id}/contacts/labels/`  --- This route is cached for up to 300 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_alliances_alliance_id_contacts_labels200_ok import GetAlliancesAllianceIdContactsLabels200Ok
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
    api_instance = esi_client.ContactsApi(api_client)
    alliance_id = 56 # int | An EVE alliance ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get alliance contact labels
        api_response = api_instance.get_alliances_alliance_id_contacts_labels(alliance_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of ContactsApi->get_alliances_alliance_id_contacts_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_alliances_alliance_id_contacts_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alliance_id** | **int**| An EVE alliance ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetAlliancesAllianceIdContactsLabels200Ok]**](GetAlliancesAllianceIdContactsLabels200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of alliance contact labels |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_contacts**
> List[GetCharactersCharacterIdContacts200Ok] get_characters_character_id_contacts(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get contacts

Return contacts of a character  --- Alternate route: `/dev/characters/{character_id}/contacts/`  Alternate route: `/v2/characters/{character_id}/contacts/`  --- This route is cached for up to 300 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_contacts200_ok import GetCharactersCharacterIdContacts200Ok
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
    api_instance = esi_client.ContactsApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    page = 1 # int | Which page of results to return (optional) (default to 1)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get contacts
        api_response = api_instance.get_characters_character_id_contacts(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
        print("The response of ContactsApi->get_characters_character_id_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_characters_character_id_contacts: %s\n" % e)
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

[**List[GetCharactersCharacterIdContacts200Ok]**](GetCharactersCharacterIdContacts200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of contacts |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * X-Pages - Maximum page number <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_contacts_labels**
> List[GetCharactersCharacterIdContactsLabels200Ok] get_characters_character_id_contacts_labels(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get contact labels

Return custom labels for a character's contacts  --- Alternate route: `/dev/characters/{character_id}/contacts/labels/`  Alternate route: `/legacy/characters/{character_id}/contacts/labels/`  Alternate route: `/v1/characters/{character_id}/contacts/labels/`  --- This route is cached for up to 300 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_contacts_labels200_ok import GetCharactersCharacterIdContactsLabels200Ok
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
    api_instance = esi_client.ContactsApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get contact labels
        api_response = api_instance.get_characters_character_id_contacts_labels(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of ContactsApi->get_characters_character_id_contacts_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_characters_character_id_contacts_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCharactersCharacterIdContactsLabels200Ok]**](GetCharactersCharacterIdContactsLabels200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of contact labels |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_contacts**
> List[GetCorporationsCorporationIdContacts200Ok] get_corporations_corporation_id_contacts(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get corporation contacts

Return contacts of a corporation  --- Alternate route: `/dev/corporations/{corporation_id}/contacts/`  Alternate route: `/v2/corporations/{corporation_id}/contacts/`  --- This route is cached for up to 300 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_corporations_corporation_id_contacts200_ok import GetCorporationsCorporationIdContacts200Ok
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
    api_instance = esi_client.ContactsApi(api_client)
    corporation_id = 56 # int | An EVE corporation ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    page = 1 # int | Which page of results to return (optional) (default to 1)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get corporation contacts
        api_response = api_instance.get_corporations_corporation_id_contacts(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
        print("The response of ContactsApi->get_corporations_corporation_id_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_corporations_corporation_id_contacts: %s\n" % e)
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

[**List[GetCorporationsCorporationIdContacts200Ok]**](GetCorporationsCorporationIdContacts200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of contacts |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * X-Pages - Maximum page number <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_contacts_labels**
> List[GetCorporationsCorporationIdContactsLabels200Ok] get_corporations_corporation_id_contacts_labels(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get corporation contact labels

Return custom labels for a corporation's contacts  --- Alternate route: `/dev/corporations/{corporation_id}/contacts/labels/`  Alternate route: `/legacy/corporations/{corporation_id}/contacts/labels/`  Alternate route: `/v1/corporations/{corporation_id}/contacts/labels/`  --- This route is cached for up to 300 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_corporations_corporation_id_contacts_labels200_ok import GetCorporationsCorporationIdContactsLabels200Ok
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
    api_instance = esi_client.ContactsApi(api_client)
    corporation_id = 56 # int | An EVE corporation ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get corporation contact labels
        api_response = api_instance.get_corporations_corporation_id_contacts_labels(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of ContactsApi->get_corporations_corporation_id_contacts_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_corporations_corporation_id_contacts_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCorporationsCorporationIdContactsLabels200Ok]**](GetCorporationsCorporationIdContactsLabels200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of corporation contact labels |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_characters_character_id_contacts**
> List[int] post_characters_character_id_contacts(character_id, standing, contact_ids, datasource=datasource, label_ids=label_ids, token=token, watched=watched)

Add contacts

Bulk add contacts with same settings  --- Alternate route: `/dev/characters/{character_id}/contacts/`  Alternate route: `/v2/characters/{character_id}/contacts/` 

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
    api_instance = esi_client.ContactsApi(api_client)
    character_id = 56 # int | An EVE character ID
    standing = 3.4 # float | Standing for the contact
    contact_ids = [56] # List[int] | A list of contacts
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    label_ids = [56] # List[int] | Add custom labels to the new contact (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)
    watched = False # bool | Whether the contact should be watched, note this is only effective on characters (optional) (default to False)

    try:
        # Add contacts
        api_response = api_instance.post_characters_character_id_contacts(character_id, standing, contact_ids, datasource=datasource, label_ids=label_ids, token=token, watched=watched)
        print("The response of ContactsApi->post_characters_character_id_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->post_characters_character_id_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **standing** | **float**| Standing for the contact | 
 **contact_ids** | [**List[int]**](int.md)| A list of contacts | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **label_ids** | [**List[int]**](int.md)| Add custom labels to the new contact | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 
 **watched** | **bool**| Whether the contact should be watched, note this is only effective on characters | [optional] [default to False]

### Return type

**List[int]**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A list of contact ids that successfully created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |
**520** | Internal error thrown from the EVE server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_characters_character_id_contacts**
> put_characters_character_id_contacts(character_id, standing, contact_ids, datasource=datasource, label_ids=label_ids, token=token, watched=watched)

Edit contacts

Bulk edit contacts with same settings  --- Alternate route: `/dev/characters/{character_id}/contacts/`  Alternate route: `/v2/characters/{character_id}/contacts/` 

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
    api_instance = esi_client.ContactsApi(api_client)
    character_id = 56 # int | An EVE character ID
    standing = 3.4 # float | Standing for the contact
    contact_ids = [56] # List[int] | A list of contacts
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    label_ids = [56] # List[int] | Add custom labels to the contact (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)
    watched = False # bool | Whether the contact should be watched, note this is only effective on characters (optional) (default to False)

    try:
        # Edit contacts
        api_instance.put_characters_character_id_contacts(character_id, standing, contact_ids, datasource=datasource, label_ids=label_ids, token=token, watched=watched)
    except Exception as e:
        print("Exception when calling ContactsApi->put_characters_character_id_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **standing** | **float**| Standing for the contact | 
 **contact_ids** | [**List[int]**](int.md)| A list of contacts | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **label_ids** | [**List[int]**](int.md)| Add custom labels to the contact | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 
 **watched** | **bool**| Whether the contact should be watched, note this is only effective on characters | [optional] [default to False]

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
**204** | Contacts updated |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

