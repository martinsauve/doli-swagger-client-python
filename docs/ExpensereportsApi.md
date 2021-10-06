# swagger_client.ExpensereportsApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_expensereports**](ExpensereportsApi.md#create_expensereports) | **POST** /expensereports | Create Expense Report object 🔐
[**list_expensereports**](ExpensereportsApi.md#list_expensereports) | **GET** /expensereports | List Expense Reports 🔐
[**remove_expensereports**](ExpensereportsApi.md#remove_expensereports) | **DELETE** /expensereports/{id} | Delete Expense Report 🔐
[**retrieve_expensereports**](ExpensereportsApi.md#retrieve_expensereports) | **GET** /expensereports/{id} | Get properties of a Expense Report object 🔐
[**update_expensereports**](ExpensereportsApi.md#update_expensereports) | **PUT** /expensereports/{id} | Update Expense Report general fields (won&#x27;t touch lines of expensereport) 🔐

# **create_expensereports**
> int create_expensereports(body=body)

Create Expense Report object 🔐

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
api_instance = swagger_client.ExpensereportsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateExpensereportsModel() # CreateExpensereportsModel | request_data  
 (optional)

try:
    # Create Expense Report object 🔐
    api_response = api_instance.create_expensereports(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpensereportsApi->create_expensereports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateExpensereportsModel**](CreateExpensereportsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_expensereports**
> list[str] list_expensereports(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, user_ids=user_ids, sqlfilters=sqlfilters)

List Expense Reports 🔐

Get a list of Expense Reports

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
api_instance = swagger_client.ExpensereportsApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
user_ids = 'user_ids_example' # str | User ids filter field. Example: '1' or '1,2,3' (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)

try:
    # List Expense Reports 🔐
    api_response = api_instance.list_expensereports(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, user_ids=user_ids, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpensereportsApi->list_expensereports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **user_ids** | **str**| User ids filter field. Example: &#x27;1&#x27; or &#x27;1,2,3&#x27; | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#x27;SO-%&#x27;) and (t.date_creation:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_expensereports**
> list[str] remove_expensereports(id)

Delete Expense Report 🔐

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
api_instance = swagger_client.ExpensereportsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Expense Report ID

try:
    # Delete Expense Report 🔐
    api_response = api_instance.remove_expensereports(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpensereportsApi->remove_expensereports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Expense Report ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_expensereports**
> str retrieve_expensereports(id)

Get properties of a Expense Report object 🔐

Return an array with Expense Report informations

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
api_instance = swagger_client.ExpensereportsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of Expense Report

try:
    # Get properties of a Expense Report object 🔐
    api_response = api_instance.retrieve_expensereports(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpensereportsApi->retrieve_expensereports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Expense Report | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_expensereports**
> int update_expensereports(id, body=body)

Update Expense Report general fields (won't touch lines of expensereport) 🔐

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
api_instance = swagger_client.ExpensereportsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of Expense Report to update
body = swagger_client.UpdateExpensereportsModel() # UpdateExpensereportsModel | request_data  
 (optional)

try:
    # Update Expense Report general fields (won't touch lines of expensereport) 🔐
    api_response = api_instance.update_expensereports(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpensereportsApi->update_expensereports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of Expense Report to update | 
 **body** | [**UpdateExpensereportsModel**](UpdateExpensereportsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

