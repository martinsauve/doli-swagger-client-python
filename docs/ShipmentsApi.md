# swagger_client.ShipmentsApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shipments**](ShipmentsApi.md#create_shipments) | **POST** /shipments | Create shipment object 🔐
[**list_shipments**](ShipmentsApi.md#list_shipments) | **GET** /shipments | List shipments 🔐
[**remove_shipments**](ShipmentsApi.md#remove_shipments) | **DELETE** /shipments/{id} | Delete shipment 🔐
[**retrieve_shipments**](ShipmentsApi.md#retrieve_shipments) | **GET** /shipments/{id} | Get properties of a shipment object 🔐
[**shipments_remove_line**](ShipmentsApi.md#shipments_remove_line) | **DELETE** /shipments/{id}/lines/{lineid} | Delete a line to given shipment 🔐
[**shipments_validate**](ShipmentsApi.md#shipments_validate) | **POST** /shipments/{id}/validate | Validate a shipment 🔐
[**update_shipments**](ShipmentsApi.md#update_shipments) | **PUT** /shipments/{id} | Update shipment general fields (won&#x27;t touch lines of shipment) 🔐

# **create_shipments**
> int create_shipments(body=body)

Create shipment object 🔐

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
api_instance = swagger_client.ShipmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateShipmentsModel() # CreateShipmentsModel | request_data  
 (optional)

try:
    # Create shipment object 🔐
    api_response = api_instance.create_shipments(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->create_shipments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateShipmentsModel**](CreateShipmentsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shipments**
> list[str] list_shipments(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters)

List shipments 🔐

Get a list of shipments

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
api_instance = swagger_client.ShipmentsApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter shipments of (example '1' or '1,2,3') (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)

try:
    # List shipments 🔐
    api_response = api_instance.list_shipments(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->list_shipments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Thirdparty ids to filter shipments of (example &#x27;1&#x27; or &#x27;1,2,3&#x27;) | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#x27;SO-%&#x27;) and (t.date_creation:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shipments**
> list[str] remove_shipments(id)

Delete shipment 🔐

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
api_instance = swagger_client.ShipmentsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Shipment ID

try:
    # Delete shipment 🔐
    api_response = api_instance.remove_shipments(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->remove_shipments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Shipment ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_shipments**
> str retrieve_shipments(id)

Get properties of a shipment object 🔐

Return an array with shipment informations

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
api_instance = swagger_client.ShipmentsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of shipment

try:
    # Get properties of a shipment object 🔐
    api_response = api_instance.retrieve_shipments(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->retrieve_shipments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of shipment | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipments_remove_line**
> int shipments_remove_line(id, lineid)

Delete a line to given shipment 🔐

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
api_instance = swagger_client.ShipmentsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of shipment to update
lineid = 789 # int | Id of line to delete

try:
    # Delete a line to given shipment 🔐
    api_response = api_instance.shipments_remove_line(id, lineid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->shipments_remove_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of shipment to update | 
 **lineid** | **int**| Id of line to delete | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipments_validate**
> list[str] shipments_validate(id, body=body)

Validate a shipment 🔐

This may record stock movements if module stock is enabled and option to decrease stock on shipment is on.

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
api_instance = swagger_client.ShipmentsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Shipment ID
body = swagger_client.ShipmentsValidateModel() # ShipmentsValidateModel | notrigger  
 (optional)

try:
    # Validate a shipment 🔐
    api_response = api_instance.shipments_validate(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->shipments_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Shipment ID | 
 **body** | [**ShipmentsValidateModel**](ShipmentsValidateModel.md)| notrigger  
 | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipments**
> int update_shipments(id, body=body)

Update shipment general fields (won't touch lines of shipment) 🔐

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
api_instance = swagger_client.ShipmentsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of shipment to update
body = swagger_client.UpdateShipmentsModel() # UpdateShipmentsModel | request_data  
 (optional)

try:
    # Update shipment general fields (won't touch lines of shipment) 🔐
    api_response = api_instance.update_shipments(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->update_shipments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of shipment to update | 
 **body** | [**UpdateShipmentsModel**](UpdateShipmentsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

