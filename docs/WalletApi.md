# esi_client.WalletApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_characters_character_id_wallet**](WalletApi.md#get_characters_character_id_wallet) | **GET** /characters/{character_id}/wallet/ | Get a character&#39;s wallet balance
[**get_characters_character_id_wallet_journal**](WalletApi.md#get_characters_character_id_wallet_journal) | **GET** /characters/{character_id}/wallet/journal/ | Get character wallet journal
[**get_characters_character_id_wallet_transactions**](WalletApi.md#get_characters_character_id_wallet_transactions) | **GET** /characters/{character_id}/wallet/transactions/ | Get wallet transactions
[**get_corporations_corporation_id_wallets**](WalletApi.md#get_corporations_corporation_id_wallets) | **GET** /corporations/{corporation_id}/wallets/ | Returns a corporation&#39;s wallet balance
[**get_corporations_corporation_id_wallets_division_journal**](WalletApi.md#get_corporations_corporation_id_wallets_division_journal) | **GET** /corporations/{corporation_id}/wallets/{division}/journal/ | Get corporation wallet journal
[**get_corporations_corporation_id_wallets_division_transactions**](WalletApi.md#get_corporations_corporation_id_wallets_division_transactions) | **GET** /corporations/{corporation_id}/wallets/{division}/transactions/ | Get corporation wallet transactions


# **get_characters_character_id_wallet**
> float get_characters_character_id_wallet(character_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get a character's wallet balance

Returns a character's wallet balance  --- Alternate route: `/legacy/characters/{character_id}/wallet/`  Alternate route: `/v1/characters/{character_id}/wallet/`  --- This route is cached for up to 120 seconds  --- [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/characters/{character_id}/wallet/)

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
    api_instance = esi_client.WalletApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get a character's wallet balance
        api_response = api_instance.get_characters_character_id_wallet(character_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of WalletApi->get_characters_character_id_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_characters_character_id_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

**float**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Wallet balance |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_wallet_journal**
> List[GetCharactersCharacterIdWalletJournal200Ok] get_characters_character_id_wallet_journal(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get character wallet journal

Retrieve the given character's wallet journal going 30 days back  --- Alternate route: `/dev/characters/{character_id}/wallet/journal/`  Alternate route: `/v6/characters/{character_id}/wallet/journal/`  --- This route is cached for up to 3600 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_wallet_journal200_ok import GetCharactersCharacterIdWalletJournal200Ok
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
    api_instance = esi_client.WalletApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    page = 1 # int | Which page of results to return (optional) (default to 1)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get character wallet journal
        api_response = api_instance.get_characters_character_id_wallet_journal(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
        print("The response of WalletApi->get_characters_character_id_wallet_journal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_characters_character_id_wallet_journal: %s\n" % e)
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

[**List[GetCharactersCharacterIdWalletJournal200Ok]**](GetCharactersCharacterIdWalletJournal200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Journal entries |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * X-Pages - Maximum page number <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_wallet_transactions**
> List[GetCharactersCharacterIdWalletTransactions200Ok] get_characters_character_id_wallet_transactions(character_id, datasource=datasource, from_id=from_id, if_none_match=if_none_match, token=token)

Get wallet transactions

Get wallet transactions of a character  --- Alternate route: `/dev/characters/{character_id}/wallet/transactions/`  Alternate route: `/legacy/characters/{character_id}/wallet/transactions/`  Alternate route: `/v1/characters/{character_id}/wallet/transactions/`  --- This route is cached for up to 3600 seconds

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_characters_character_id_wallet_transactions200_ok import GetCharactersCharacterIdWalletTransactions200Ok
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
    api_instance = esi_client.WalletApi(api_client)
    character_id = 56 # int | An EVE character ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    from_id = 56 # int | Only show transactions happened before the one referenced by this id (optional)
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get wallet transactions
        api_response = api_instance.get_characters_character_id_wallet_transactions(character_id, datasource=datasource, from_id=from_id, if_none_match=if_none_match, token=token)
        print("The response of WalletApi->get_characters_character_id_wallet_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_characters_character_id_wallet_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **from_id** | **int**| Only show transactions happened before the one referenced by this id | [optional] 
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCharactersCharacterIdWalletTransactions200Ok]**](GetCharactersCharacterIdWalletTransactions200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Wallet transactions |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_wallets**
> List[GetCorporationsCorporationIdWallets200Ok] get_corporations_corporation_id_wallets(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)

Returns a corporation's wallet balance

Get a corporation's wallets  --- Alternate route: `/dev/corporations/{corporation_id}/wallets/`  Alternate route: `/legacy/corporations/{corporation_id}/wallets/`  Alternate route: `/v1/corporations/{corporation_id}/wallets/`  --- This route is cached for up to 300 seconds  --- Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_corporations_corporation_id_wallets200_ok import GetCorporationsCorporationIdWallets200Ok
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
    api_instance = esi_client.WalletApi(api_client)
    corporation_id = 56 # int | An EVE corporation ID
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Returns a corporation's wallet balance
        api_response = api_instance.get_corporations_corporation_id_wallets(corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)
        print("The response of WalletApi->get_corporations_corporation_id_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_corporations_corporation_id_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCorporationsCorporationIdWallets200Ok]**](GetCorporationsCorporationIdWallets200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of corporation wallets |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_wallets_division_journal**
> List[GetCorporationsCorporationIdWalletsDivisionJournal200Ok] get_corporations_corporation_id_wallets_division_journal(corporation_id, division, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get corporation wallet journal

Retrieve the given corporation's wallet journal for the given division going 30 days back  --- Alternate route: `/dev/corporations/{corporation_id}/wallets/{division}/journal/`  Alternate route: `/v4/corporations/{corporation_id}/wallets/{division}/journal/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_corporations_corporation_id_wallets_division_journal200_ok import GetCorporationsCorporationIdWalletsDivisionJournal200Ok
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
    api_instance = esi_client.WalletApi(api_client)
    corporation_id = 56 # int | An EVE corporation ID
    division = 56 # int | Wallet key of the division to fetch journals from
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    page = 1 # int | Which page of results to return (optional) (default to 1)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get corporation wallet journal
        api_response = api_instance.get_corporations_corporation_id_wallets_division_journal(corporation_id, division, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
        print("The response of WalletApi->get_corporations_corporation_id_wallets_division_journal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_corporations_corporation_id_wallets_division_journal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **division** | **int**| Wallet key of the division to fetch journals from | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCorporationsCorporationIdWalletsDivisionJournal200Ok]**](GetCorporationsCorporationIdWalletsDivisionJournal200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Journal entries |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * X-Pages - Maximum page number <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_wallets_division_transactions**
> List[GetCorporationsCorporationIdWalletsDivisionTransactions200Ok] get_corporations_corporation_id_wallets_division_transactions(corporation_id, division, datasource=datasource, from_id=from_id, if_none_match=if_none_match, token=token)

Get corporation wallet transactions

Get wallet transactions of a corporation  --- Alternate route: `/dev/corporations/{corporation_id}/wallets/{division}/transactions/`  Alternate route: `/legacy/corporations/{corporation_id}/wallets/{division}/transactions/`  Alternate route: `/v1/corporations/{corporation_id}/wallets/{division}/transactions/`  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant 

### Example

* OAuth Authentication (evesso):

```python
import time
import os
import esi_client
from esi_client.models.get_corporations_corporation_id_wallets_division_transactions200_ok import GetCorporationsCorporationIdWalletsDivisionTransactions200Ok
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
    api_instance = esi_client.WalletApi(api_client)
    corporation_id = 56 # int | An EVE corporation ID
    division = 56 # int | Wallet key of the division to fetch journals from
    datasource = 'tranquility' # str | The server name you would like data from (optional) (default to 'tranquility')
    from_id = 56 # int | Only show journal entries happened before the transaction referenced by this id (optional)
    if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
    token = 'token_example' # str | Access token to use if unable to set a header (optional)

    try:
        # Get corporation wallet transactions
        api_response = api_instance.get_corporations_corporation_id_wallets_division_transactions(corporation_id, division, datasource=datasource, from_id=from_id, if_none_match=if_none_match, token=token)
        print("The response of WalletApi->get_corporations_corporation_id_wallets_division_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_corporations_corporation_id_wallets_division_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **division** | **int**| Wallet key of the division to fetch journals from | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **from_id** | **int**| Only show journal entries happened before the transaction referenced by this id | [optional] 
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

[**List[GetCorporationsCorporationIdWalletsDivisionTransactions200Ok]**](GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Wallet transactions |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

