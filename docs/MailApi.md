# esi_client.MailApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_characters_character_id_mail_labels_label_id**](MailApi.md#delete_characters_character_id_mail_labels_label_id) | **DELETE** /characters/{character_id}/mail/labels/{label_id}/ | Delete a mail label
[**delete_characters_character_id_mail_mail_id**](MailApi.md#delete_characters_character_id_mail_mail_id) | **DELETE** /characters/{character_id}/mail/{mail_id}/ | Delete a mail
[**get_characters_character_id_mail**](MailApi.md#get_characters_character_id_mail) | **GET** /characters/{character_id}/mail/ | Return mail headers
[**get_characters_character_id_mail_labels**](MailApi.md#get_characters_character_id_mail_labels) | **GET** /characters/{character_id}/mail/labels/ | Get mail labels and unread counts
[**get_characters_character_id_mail_lists**](MailApi.md#get_characters_character_id_mail_lists) | **GET** /characters/{character_id}/mail/lists/ | Return mailing list subscriptions
[**get_characters_character_id_mail_mail_id**](MailApi.md#get_characters_character_id_mail_mail_id) | **GET** /characters/{character_id}/mail/{mail_id}/ | Return a mail
[**post_characters_character_id_mail**](MailApi.md#post_characters_character_id_mail) | **POST** /characters/{character_id}/mail/ | Send a new mail
[**post_characters_character_id_mail_labels**](MailApi.md#post_characters_character_id_mail_labels) | **POST** /characters/{character_id}/mail/labels/ | Create a mail label
[**put_characters_character_id_mail_mail_id**](MailApi.md#put_characters_character_id_mail_mail_id) | **PUT** /characters/{character_id}/mail/{mail_id}/ | Update metadata about a mail


# **delete_characters_character_id_mail_labels_label_id**
> delete_characters_character_id_mail_labels_label_id(character_id, label_id, datasource=datasource, token=token)

Delete a mail label

Delete a mail label  --- Alternate route: `/dev/characters/{character_id}/mail/labels/{label_id}/`  Alternate route: `/legacy/characters/{character_id}/mail/labels/{label_id}/`  Alternate route: `/v1/characters/{character_id}/mail/labels/{label_id}/` 

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
    api_instance = esi_client.MailApi(api_client)
    character_id = 56 # int | An EVE character ID
    label_id = 56 # int | An EVE label id
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Delete a mail label
        api_instance.delete_characters_character_id_mail_labels_label_id(character_id, label_id, datasource=datasource, token=token)
    except Exception as e:
        print("Exception when calling MailApi->delete_characters_character_id_mail_labels_label_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **label_id** | **int**| An EVE label id | 
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
**204** | Label deleted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**422** | Default labels cannot be deleted |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_characters_character_id_mail_mail_id**
> delete_characters_character_id_mail_mail_id(character_id, mail_id, datasource=datasource, token=token)

Delete a mail

Delete a mail  --- Alternate route: `/dev/characters/{character_id}/mail/{mail_id}/`  Alternate route: `/legacy/characters/{character_id}/mail/{mail_id}/`  Alternate route: `/v1/characters/{character_id}/mail/{mail_id}/` 

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
    api_instance = esi_client.MailApi(api_client)
    character_id = 56 # int | An EVE character ID
    mail_id = 56 # int | An EVE mail ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Delete a mail
        api_instance.delete_characters_character_id_mail_mail_id(character_id, mail_id, datasource=datasource, token=token)
    except Exception as e:
        print("Exception when calling MailApi->delete_characters_character_id_mail_mail_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **mail_id** | **int**| An EVE mail ID | 
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
**204** | Mail deleted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_mail**
> List[GetCharactersCharacterIdMail200Ok] get_characters_character_id_mail(character_id, datasource=datasource, if_none_match=if_none_match, labels=labels, last_mail_id=last_mail_id, token=token)

Return mail headers

Return the 50 most recent mail headers belonging to the character that match the query criteria. Queries can be filtered by label, and last_mail_id can be used to paginate backwards  --- Alternate route: `/dev/characters/{character_id}/mail/`  Alternate route: `/legacy/characters/{character_id}/mail/`  Alternate route: `/v1/characters/{character_id}/mail/`  --- This route is cached for up to 30 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_mail200_ok import GetCharactersCharacterIdMail200Ok
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
    api_instance = esi_client.MailApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    labels = [56] # List[int] | Fetch only mails that match one or more of the given labels (optional)
    last_mail_id = 56 # int | List only mail with an ID lower than the given ID, if present (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Return mail headers
        api_response = api_instance.get_characters_character_id_mail(character_id, datasource=datasource, if_none_match=if_none_match, labels=labels, last_mail_id=last_mail_id, token=token)
        print("The response of MailApi->get_characters_character_id_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->get_characters_character_id_mail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **labels** | [**List[int]**](int.md)| Fetch only mails that match one or more of the given labels | [optional] 
 **last_mail_id** | **int**| List only mail with an ID lower than the given ID, if present | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCharactersCharacterIdMail200Ok]**](GetCharactersCharacterIdMail200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested mail |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_mail_labels**
> GetCharactersCharacterIdMailLabelsOk get_characters_character_id_mail_labels(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get mail labels and unread counts

Return a list of the users mail labels, unread counts for each label and a total unread count.  --- Alternate route: `/dev/characters/{character_id}/mail/labels/`  Alternate route: `/v3/characters/{character_id}/mail/labels/`  --- This route is cached for up to 30 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_mail_labels_ok import GetCharactersCharacterIdMailLabelsOk
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
    api_instance = esi_client.MailApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get mail labels and unread counts
        api_response = api_instance.get_characters_character_id_mail_labels(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of MailApi->get_characters_character_id_mail_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->get_characters_character_id_mail_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCharactersCharacterIdMailLabelsOk**](GetCharactersCharacterIdMailLabelsOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of mail labels and unread counts |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_mail_lists**
> List[GetCharactersCharacterIdMailLists200Ok] get_characters_character_id_mail_lists(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Return mailing list subscriptions

Return all mailing lists that the character is subscribed to  --- Alternate route: `/dev/characters/{character_id}/mail/lists/`  Alternate route: `/legacy/characters/{character_id}/mail/lists/`  Alternate route: `/v1/characters/{character_id}/mail/lists/`  --- This route is cached for up to 120 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_mail_lists200_ok import GetCharactersCharacterIdMailLists200Ok
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
    api_instance = esi_client.MailApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Return mailing list subscriptions
        api_response = api_instance.get_characters_character_id_mail_lists(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of MailApi->get_characters_character_id_mail_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->get_characters_character_id_mail_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCharactersCharacterIdMailLists200Ok]**](GetCharactersCharacterIdMailLists200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mailing lists |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_mail_mail_id**
> GetCharactersCharacterIdMailMailIdOk get_characters_character_id_mail_mail_id(character_id, mail_id, datasource=datasource, if_none_match=if_none_match, token=token)

Return a mail

Return the contents of an EVE mail  --- Alternate route: `/dev/characters/{character_id}/mail/{mail_id}/`  Alternate route: `/legacy/characters/{character_id}/mail/{mail_id}/`  Alternate route: `/v1/characters/{character_id}/mail/{mail_id}/`  --- This route is cached for up to 30 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_mail_mail_id_ok import GetCharactersCharacterIdMailMailIdOk
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
    api_instance = esi_client.MailApi(api_client)
    character_id = 56 # int | An EVE character ID
    mail_id = 56 # int | An EVE mail ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Return a mail
        api_response = api_instance.get_characters_character_id_mail_mail_id(character_id, mail_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of MailApi->get_characters_character_id_mail_mail_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->get_characters_character_id_mail_mail_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **mail_id** | **int**| An EVE mail ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCharactersCharacterIdMailMailIdOk**](GetCharactersCharacterIdMailMailIdOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contents of a mail |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Mail not found |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_characters_character_id_mail**
> int post_characters_character_id_mail(character_id, mail, datasource=datasource, token=token)

Send a new mail

Create and send a new mail  --- Alternate route: `/dev/characters/{character_id}/mail/`  Alternate route: `/legacy/characters/{character_id}/mail/`  Alternate route: `/v1/characters/{character_id}/mail/` 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.post_characters_character_id_mail_mail import PostCharactersCharacterIdMailMail
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
    api_instance = esi_client.MailApi(api_client)
    character_id = 56 # int | An EVE character ID
    mail = esi_client.PostCharactersCharacterIdMailMail() # PostCharactersCharacterIdMailMail | The mail to send
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Send a new mail
        api_response = api_instance.post_characters_character_id_mail(character_id, mail, datasource=datasource, token=token)
        print("The response of MailApi->post_characters_character_id_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->post_characters_character_id_mail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **mail** | [**PostCharactersCharacterIdMailMail**](PostCharactersCharacterIdMailMail.md)| The mail to send | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

**int**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Mail created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |
**520** | Internal error thrown from the EVE server. Most of the time this means you have hit an EVE server rate limit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_characters_character_id_mail_labels**
> int post_characters_character_id_mail_labels(character_id, label, datasource=datasource, token=token)

Create a mail label

Create a mail label  --- Alternate route: `/dev/characters/{character_id}/mail/labels/`  Alternate route: `/legacy/characters/{character_id}/mail/labels/`  Alternate route: `/v2/characters/{character_id}/mail/labels/` 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.post_characters_character_id_mail_labels_label import PostCharactersCharacterIdMailLabelsLabel
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
    api_instance = esi_client.MailApi(api_client)
    character_id = 56 # int | An EVE character ID
    label = esi_client.PostCharactersCharacterIdMailLabelsLabel() # PostCharactersCharacterIdMailLabelsLabel | Label to create
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Create a mail label
        api_response = api_instance.post_characters_character_id_mail_labels(character_id, label, datasource=datasource, token=token)
        print("The response of MailApi->post_characters_character_id_mail_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->post_characters_character_id_mail_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **label** | [**PostCharactersCharacterIdMailLabelsLabel**](PostCharactersCharacterIdMailLabelsLabel.md)| Label to create | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

**int**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Label created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_characters_character_id_mail_mail_id**
> put_characters_character_id_mail_mail_id(character_id, mail_id, contents, datasource=datasource, token=token)

Update metadata about a mail

Update metadata about a mail  --- Alternate route: `/dev/characters/{character_id}/mail/{mail_id}/`  Alternate route: `/legacy/characters/{character_id}/mail/{mail_id}/`  Alternate route: `/v1/characters/{character_id}/mail/{mail_id}/` 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.put_characters_character_id_mail_mail_id_contents import PutCharactersCharacterIdMailMailIdContents
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
    api_instance = esi_client.MailApi(api_client)
    character_id = 56 # int | An EVE character ID
    mail_id = 56 # int | An EVE mail ID
    contents = esi_client.PutCharactersCharacterIdMailMailIdContents() # PutCharactersCharacterIdMailMailIdContents | Data used to update the mail
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Update metadata about a mail
        api_instance.put_characters_character_id_mail_mail_id(character_id, mail_id, contents, datasource=datasource, token=token)
    except Exception as e:
        print("Exception when calling MailApi->put_characters_character_id_mail_mail_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **mail_id** | **int**| An EVE mail ID | 
 **contents** | [**PutCharactersCharacterIdMailMailIdContents**](PutCharactersCharacterIdMailMailIdContents.md)| Data used to update the mail | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

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
**204** | Mail updated |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

