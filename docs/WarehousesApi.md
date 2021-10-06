# swagger_client.WarehousesApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_warehouses**](WarehousesApi.md#create_warehouses) | **POST** /warehouses | Create warehouse object 🔐
[**list_warehouses**](WarehousesApi.md#list_warehouses) | **GET** /warehouses | List warehouses 🔐
[**remove_warehouses**](WarehousesApi.md#remove_warehouses) | **DELETE** /warehouses/{id} | Delete warehouse 🔐
[**retrieve_warehouses**](WarehousesApi.md#retrieve_warehouses) | **GET** /warehouses/{id} | Get properties of a warehouse object 🔐
[**update_warehouses**](WarehousesApi.md#update_warehouses) | **PUT** /warehouses/{id} | Update warehouse 🔐

# **create_warehouses**
> int create_warehouses(body=body)

Create warehouse object 🔐

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
api_instance = swagger_client.WarehousesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateWarehousesModel() # CreateWarehousesModel | request_data  
 (optional)

try:
    # Create warehouse object 🔐
    api_response = api_instance.create_warehouses(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehousesApi->create_warehouses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWarehousesModel**](CreateWarehousesModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_warehouses**
> list[str] list_warehouses(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, category=category, sqlfilters=sqlfilters)

List warehouses 🔐

Get a list of warehouses

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
api_instance = swagger_client.WarehousesApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
category = 789 # int | Use this param to filter list by category (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.label:like:'WH-%') and (t.date_creation:<:'20160101')\" (optional)

try:
    # List warehouses 🔐
    api_response = api_instance.list_warehouses(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, category=category, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehousesApi->list_warehouses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **category** | **int**| Use this param to filter list by category | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.label:like:&#x27;WH-%&#x27;) and (t.date_creation:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_warehouses**
> list[str] remove_warehouses(id)

Delete warehouse 🔐

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
api_instance = swagger_client.WarehousesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Warehouse ID

try:
    # Delete warehouse 🔐
    api_response = api_instance.remove_warehouses(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehousesApi->remove_warehouses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Warehouse ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_warehouses**
> str retrieve_warehouses(id)

Get properties of a warehouse object 🔐

Return an array with warehouse informations

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
api_instance = swagger_client.WarehousesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of warehouse

try:
    # Get properties of a warehouse object 🔐
    api_response = api_instance.retrieve_warehouses(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehousesApi->retrieve_warehouses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of warehouse | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_warehouses**
> int update_warehouses(id, body=body)

Update warehouse 🔐

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
api_instance = swagger_client.WarehousesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of warehouse to update
body = swagger_client.UpdateWarehousesModel() # UpdateWarehousesModel | request_data  
 (optional)

try:
    # Update warehouse 🔐
    api_response = api_instance.update_warehouses(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehousesApi->update_warehouses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of warehouse to update | 
 **body** | [**UpdateWarehousesModel**](UpdateWarehousesModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

