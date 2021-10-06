# swagger_client.SupplierordersApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_supplierorders**](SupplierordersApi.md#create_supplierorders) | **POST** /supplierorders | Create supplier order object 🔐
[**list_supplierorders**](SupplierordersApi.md#list_supplierorders) | **GET** /supplierorders | List orders 🔐
[**remove_supplierorders**](SupplierordersApi.md#remove_supplierorders) | **DELETE** /supplierorders/{id} | Delete supplier order 🔐
[**retrieve_supplierorders**](SupplierordersApi.md#retrieve_supplierorders) | **GET** /supplierorders/{id} | Get properties of a supplier order object 🔐
[**supplierorders_validate**](SupplierordersApi.md#supplierorders_validate) | **POST** /supplierorders/{id}/validate | Validate an order 🔐
[**update_supplierorders**](SupplierordersApi.md#update_supplierorders) | **PUT** /supplierorders/{id} | Update supplier order 🔐

# **create_supplierorders**
> int create_supplierorders(body=body)

Create supplier order object 🔐

Example: {\"ref\": \"auto\", \"ref_supplier\": \"1234\", \"socid\": \"1\", \"multicurrency_code\": \"SEK\", \"multicurrency_tx\": 1, \"tva_tx\": 25, \"note\": \"Imported via the REST API\"}

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
api_instance = swagger_client.SupplierordersApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateSupplierordersModel() # CreateSupplierordersModel | request_data  
 (optional)

try:
    # Create supplier order object 🔐
    api_response = api_instance.create_supplierorders(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierordersApi->create_supplierorders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSupplierordersModel**](CreateSupplierordersModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supplierorders**
> list[str] list_supplierorders(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, product_ids=product_ids, status=status, sqlfilters=sqlfilters)

List orders 🔐

Get a list of supplier orders

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
api_instance = swagger_client.SupplierordersApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter orders of (example '1' or '1,2,3') (optional)
product_ids = 'product_ids_example' # str | Product ids to filter orders of (example '1' or '1,2,3') (optional)
status = 'status_example' # str | Filter by order status : draft | validated | approved | running | received_start | received_end | cancelled | refused (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.datec:<:'20160101')\" (optional)

try:
    # List orders 🔐
    api_response = api_instance.list_supplierorders(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, product_ids=product_ids, status=status, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierordersApi->list_supplierorders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Thirdparty ids to filter orders of (example &#x27;1&#x27; or &#x27;1,2,3&#x27;) | [optional] 
 **product_ids** | **str**| Product ids to filter orders of (example &#x27;1&#x27; or &#x27;1,2,3&#x27;) | [optional] 
 **status** | **str**| Filter by order status : draft | validated | approved | running | received_start | received_end | cancelled | refused | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#x27;SO-%&#x27;) and (t.datec:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_supplierorders**
> list[str] remove_supplierorders(id)

Delete supplier order 🔐

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
api_instance = swagger_client.SupplierordersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Supplier order ID

try:
    # Delete supplier order 🔐
    api_response = api_instance.remove_supplierorders(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierordersApi->remove_supplierorders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Supplier order ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_supplierorders**
> str retrieve_supplierorders(id)

Get properties of a supplier order object 🔐

Return an array with supplier order information

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
api_instance = swagger_client.SupplierordersApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of supplier order

try:
    # Get properties of a supplier order object 🔐
    api_response = api_instance.retrieve_supplierorders(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierordersApi->retrieve_supplierorders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of supplier order | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierorders_validate**
> list[str] supplierorders_validate(id, body=body)

Validate an order 🔐

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
api_instance = swagger_client.SupplierordersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Order ID
body = swagger_client.SupplierordersValidateModel() # SupplierordersValidateModel | idwarehouse  
notrigger  
 (optional)

try:
    # Validate an order 🔐
    api_response = api_instance.supplierorders_validate(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierordersApi->supplierorders_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **body** | [**SupplierordersValidateModel**](SupplierordersValidateModel.md)| idwarehouse  
notrigger  
 | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_supplierorders**
> int update_supplierorders(id, body=body)

Update supplier order 🔐

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
api_instance = swagger_client.SupplierordersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of supplier order to update
body = swagger_client.UpdateSupplierordersModel() # UpdateSupplierordersModel | request_data  
 (optional)

try:
    # Update supplier order 🔐
    api_response = api_instance.update_supplierorders(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierordersApi->update_supplierorders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier order to update | 
 **body** | [**UpdateSupplierordersModel**](UpdateSupplierordersModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

