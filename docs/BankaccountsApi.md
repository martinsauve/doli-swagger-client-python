# swagger_client.BankaccountsApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bankaccounts_add_line**](BankaccountsApi.md#bankaccounts_add_line) | **POST** /bankaccounts/{id}/lines | Add a line to an account 🔐
[**bankaccounts_add_link**](BankaccountsApi.md#bankaccounts_add_link) | **POST** /bankaccounts/{id}/lines/{line_id}/links | Add a link to an account line 🔐
[**bankaccounts_retrieve_lines**](BankaccountsApi.md#bankaccounts_retrieve_lines) | **GET** /bankaccounts/{id}/lines | Get the list of lines of the account. 🔐
[**bankaccounts_transfer**](BankaccountsApi.md#bankaccounts_transfer) | **POST** /bankaccounts/transfer | Create an internal wire transfer between two bank accounts 🔐
[**create_bankaccounts**](BankaccountsApi.md#create_bankaccounts) | **POST** /bankaccounts | Create account object 🔐
[**list_bankaccounts**](BankaccountsApi.md#list_bankaccounts) | **GET** /bankaccounts | Get the list of accounts. 🔐
[**remove_bankaccounts**](BankaccountsApi.md#remove_bankaccounts) | **DELETE** /bankaccounts/{id} | Delete account 🔐
[**retrieve_bankaccounts**](BankaccountsApi.md#retrieve_bankaccounts) | **GET** /bankaccounts/{id} | Get account by ID. 🔐
[**update_bankaccounts**](BankaccountsApi.md#update_bankaccounts) | **PUT** /bankaccounts/{id} | Update account 🔐

# **bankaccounts_add_line**
> int bankaccounts_add_line(body, id)

Add a line to an account 🔐

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.BankaccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BankaccountsAddLineModel() # BankaccountsAddLineModel | **date** (required)  
**type** (required)  
**label** (required)  
**amount** (required)  
category  
cheque_number  
cheque_writer  
cheque_bank  
accountancycode  
datev  
num_releve  

id = 789 # int | ID of account

try:
    # Add a line to an account 🔐
    api_response = api_instance.bankaccounts_add_line(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankaccountsApi->bankaccounts_add_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BankaccountsAddLineModel**](BankaccountsAddLineModel.md)| **date** (required)  
**type** (required)  
**label** (required)  
**amount** (required)  
category  
cheque_number  
cheque_writer  
cheque_bank  
accountancycode  
datev  
num_releve  
 | 
 **id** | **int**| ID of account | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bankaccounts_add_link**
> int bankaccounts_add_link(body, id, line_id)

Add a link to an account line 🔐

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.BankaccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BankaccountsAddLinkModel() # BankaccountsAddLinkModel | **url_id** (required)  
**url** (required)  
**label** (required)  
**type** (required)  

id = 789 # int | ID of account
line_id = 789 # int | ID of account line

try:
    # Add a link to an account line 🔐
    api_response = api_instance.bankaccounts_add_link(body, id, line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankaccountsApi->bankaccounts_add_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BankaccountsAddLinkModel**](BankaccountsAddLinkModel.md)| **url_id** (required)  
**url** (required)  
**label** (required)  
**type** (required)  
 | 
 **id** | **int**| ID of account | 
 **line_id** | **int**| ID of account line | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bankaccounts_retrieve_lines**
> list[str] bankaccounts_retrieve_lines(id, sqlfilters=sqlfilters)

Get the list of lines of the account. 🔐

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.BankaccountsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of account
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.import_key:<:'20160101')\" (optional)

try:
    # Get the list of lines of the account. 🔐
    api_response = api_instance.bankaccounts_retrieve_lines(id, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankaccountsApi->bankaccounts_retrieve_lines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of account | 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#x27;SO-%&#x27;) and (t.import_key:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bankaccounts_transfer**
> list[str] bankaccounts_transfer(body)

Create an internal wire transfer between two bank accounts 🔐

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.BankaccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BankaccountsTransferModel() # BankaccountsTransferModel | bankaccount_from_id  
bankaccount_to_id  
date  
description  
amount  
amount_to  


try:
    # Create an internal wire transfer between two bank accounts 🔐
    api_response = api_instance.bankaccounts_transfer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankaccountsApi->bankaccounts_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BankaccountsTransferModel**](BankaccountsTransferModel.md)| bankaccount_from_id  
bankaccount_to_id  
date  
description  
amount  
amount_to  
 | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bankaccounts**
> int create_bankaccounts(body=body)

Create account object 🔐

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.BankaccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateBankaccountsModel() # CreateBankaccountsModel | request_data  
 (optional)

try:
    # Create account object 🔐
    api_response = api_instance.create_bankaccounts(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankaccountsApi->create_bankaccounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBankaccountsModel**](CreateBankaccountsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bankaccounts**
> list[str] list_bankaccounts(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, category=category, sqlfilters=sqlfilters)

Get the list of accounts. 🔐

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.BankaccountsApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
category = 789 # int | Use this param to filter list by category (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.import_key:<:'20160101')\" (optional)

try:
    # Get the list of accounts. 🔐
    api_response = api_instance.list_bankaccounts(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, category=category, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankaccountsApi->list_bankaccounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **category** | **int**| Use this param to filter list by category | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#x27;SO-%&#x27;) and (t.import_key:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_bankaccounts**
> list[str] remove_bankaccounts(id)

Delete account 🔐

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.BankaccountsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of account

try:
    # Delete account 🔐
    api_response = api_instance.remove_bankaccounts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankaccountsApi->remove_bankaccounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of account | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_bankaccounts**
> list[str] retrieve_bankaccounts(id)

Get account by ID. 🔐

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.BankaccountsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of account

try:
    # Get account by ID. 🔐
    api_response = api_instance.retrieve_bankaccounts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankaccountsApi->retrieve_bankaccounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of account | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bankaccounts**
> int update_bankaccounts(id, body=body)

Update account 🔐

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.BankaccountsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of account
body = swagger_client.UpdateBankaccountsModel() # UpdateBankaccountsModel | request_data  
 (optional)

try:
    # Update account 🔐
    api_response = api_instance.update_bankaccounts(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankaccountsApi->update_bankaccounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of account | 
 **body** | [**UpdateBankaccountsModel**](UpdateBankaccountsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

