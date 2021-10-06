# swagger_client.SupplierinvoicesApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_supplierinvoices**](SupplierinvoicesApi.md#create_supplierinvoices) | **POST** /supplierinvoices | Create supplier invoice object 🔐
[**list_supplierinvoices**](SupplierinvoicesApi.md#list_supplierinvoices) | **GET** /supplierinvoices | List invoices 🔐
[**remove_supplierinvoices**](SupplierinvoicesApi.md#remove_supplierinvoices) | **DELETE** /supplierinvoices/{id} | Delete supplier invoice 🔐
[**retrieve_supplierinvoices**](SupplierinvoicesApi.md#retrieve_supplierinvoices) | **GET** /supplierinvoices/{id} | Get properties of a supplier invoice object 🔐
[**supplierinvoices_add_payment**](SupplierinvoicesApi.md#supplierinvoices_add_payment) | **POST** /supplierinvoices/{id}/payments | Add payment line to a specific supplier invoice with the remain to pay as amount. 🔐
[**supplierinvoices_create_line**](SupplierinvoicesApi.md#supplierinvoices_create_line) | **POST** /supplierinvoices/{id}/lines | Add a line to given supplier invoice 🔐
[**supplierinvoices_remove_line**](SupplierinvoicesApi.md#supplierinvoices_remove_line) | **DELETE** /supplierinvoices/{id}/lines/{lineid} | Deletes a line of a given supplier invoice 🔐
[**supplierinvoices_retrieve_lines**](SupplierinvoicesApi.md#supplierinvoices_retrieve_lines) | **GET** /supplierinvoices/{id}/lines | Get lines of a supplier invoice 🔐
[**supplierinvoices_retrieve_payments**](SupplierinvoicesApi.md#supplierinvoices_retrieve_payments) | **GET** /supplierinvoices/{id}/payments | Get list of payments of a given supplier invoice 🔐
[**supplierinvoices_update_line**](SupplierinvoicesApi.md#supplierinvoices_update_line) | **PUT** /supplierinvoices/{id}/lines/{lineid} | Update a line to a given supplier invoice 🔐
[**supplierinvoices_validate**](SupplierinvoicesApi.md#supplierinvoices_validate) | **POST** /supplierinvoices/{id}/validate | Validate an invoice 🔐
[**update_supplierinvoices**](SupplierinvoicesApi.md#update_supplierinvoices) | **PUT** /supplierinvoices/{id} | Update supplier invoice 🔐

# **create_supplierinvoices**
> int create_supplierinvoices(body=body)

Create supplier invoice object 🔐

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
api_instance = swagger_client.SupplierinvoicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateSupplierinvoicesModel() # CreateSupplierinvoicesModel | request_data  
 (optional)

try:
    # Create supplier invoice object 🔐
    api_response = api_instance.create_supplierinvoices(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierinvoicesApi->create_supplierinvoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSupplierinvoicesModel**](CreateSupplierinvoicesModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supplierinvoices**
> list[str] list_supplierinvoices(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, status=status, sqlfilters=sqlfilters)

List invoices 🔐

Get a list of supplier invoices

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
api_instance = swagger_client.SupplierinvoicesApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter invoices of (example '1' or '1,2,3') (optional)
status = 'status_example' # str | Filter by invoice status : draft | unpaid | paid | cancelled (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.datec:<:'20160101')\" (optional)

try:
    # List invoices 🔐
    api_response = api_instance.list_supplierinvoices(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, status=status, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierinvoicesApi->list_supplierinvoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Thirdparty ids to filter invoices of (example &#x27;1&#x27; or &#x27;1,2,3&#x27;) | [optional] 
 **status** | **str**| Filter by invoice status : draft | unpaid | paid | cancelled | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#x27;SO-%&#x27;) and (t.datec:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_supplierinvoices**
> list[str] remove_supplierinvoices(id)

Delete supplier invoice 🔐

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
api_instance = swagger_client.SupplierinvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Supplier invoice ID

try:
    # Delete supplier invoice 🔐
    api_response = api_instance.remove_supplierinvoices(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierinvoicesApi->remove_supplierinvoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Supplier invoice ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_supplierinvoices**
> str retrieve_supplierinvoices(id)

Get properties of a supplier invoice object 🔐

Return an array with supplier invoice information

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
api_instance = swagger_client.SupplierinvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of supplier invoice

try:
    # Get properties of a supplier invoice object 🔐
    api_response = api_instance.retrieve_supplierinvoices(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierinvoicesApi->retrieve_supplierinvoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of supplier invoice | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_add_payment**
> int supplierinvoices_add_payment(body, id)

Add payment line to a specific supplier invoice with the remain to pay as amount. 🔐

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
api_instance = swagger_client.SupplierinvoicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.SupplierinvoicesAddPaymentModel() # SupplierinvoicesAddPaymentModel | **datepaye** (required)  
**payment_mode_id** (required)  
**closepaidinvoices** (required)  
**accountid** (required)  
num_payment  
comment  
chqemetteur  
chqbank  

id = 789 # int | Id of invoice

try:
    # Add payment line to a specific supplier invoice with the remain to pay as amount. 🔐
    api_response = api_instance.supplierinvoices_add_payment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierinvoicesApi->supplierinvoices_add_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupplierinvoicesAddPaymentModel**](SupplierinvoicesAddPaymentModel.md)| **datepaye** (required)  
**payment_mode_id** (required)  
**closepaidinvoices** (required)  
**accountid** (required)  
num_payment  
comment  
chqemetteur  
chqbank  
 | 
 **id** | **int**| Id of invoice | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_create_line**
> str supplierinvoices_create_line(id, body=body)

Add a line to given supplier invoice 🔐

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
api_instance = swagger_client.SupplierinvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of supplier invoice to update
body = swagger_client.SupplierinvoicesCreateLineModel() # SupplierinvoicesCreateLineModel | request_data  
 (optional)

try:
    # Add a line to given supplier invoice 🔐
    api_response = api_instance.supplierinvoices_create_line(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierinvoicesApi->supplierinvoices_create_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier invoice to update | 
 **body** | [**SupplierinvoicesCreateLineModel**](SupplierinvoicesCreateLineModel.md)| request_data  
 | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_remove_line**
> list[str] supplierinvoices_remove_line(id, lineid)

Deletes a line of a given supplier invoice 🔐

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
api_instance = swagger_client.SupplierinvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of supplier invoice
lineid = 789 # int | Id of the line to delete

try:
    # Deletes a line of a given supplier invoice 🔐
    api_response = api_instance.supplierinvoices_remove_line(id, lineid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierinvoicesApi->supplierinvoices_remove_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier invoice | 
 **lineid** | **int**| Id of the line to delete | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_retrieve_lines**
> list[str] supplierinvoices_retrieve_lines(id)

Get lines of a supplier invoice 🔐

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
api_instance = swagger_client.SupplierinvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of supplier invoice

try:
    # Get lines of a supplier invoice 🔐
    api_response = api_instance.supplierinvoices_retrieve_lines(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierinvoicesApi->supplierinvoices_retrieve_lines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier invoice | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_retrieve_payments**
> list[str] supplierinvoices_retrieve_payments(id)

Get list of payments of a given supplier invoice 🔐

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
api_instance = swagger_client.SupplierinvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of SupplierInvoice

try:
    # Get list of payments of a given supplier invoice 🔐
    api_response = api_instance.supplierinvoices_retrieve_payments(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierinvoicesApi->supplierinvoices_retrieve_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of SupplierInvoice | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_update_line**
> str supplierinvoices_update_line(id, lineid, body=body)

Update a line to a given supplier invoice 🔐

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
api_instance = swagger_client.SupplierinvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of supplier invoice to update
lineid = 789 # int | Id of line to update
body = swagger_client.SupplierinvoicesUpdateLineModel() # SupplierinvoicesUpdateLineModel | request_data  
 (optional)

try:
    # Update a line to a given supplier invoice 🔐
    api_response = api_instance.supplierinvoices_update_line(id, lineid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierinvoicesApi->supplierinvoices_update_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier invoice to update | 
 **lineid** | **int**| Id of line to update | 
 **body** | [**SupplierinvoicesUpdateLineModel**](SupplierinvoicesUpdateLineModel.md)| request_data  
 | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_validate**
> list[str] supplierinvoices_validate(id, body=body)

Validate an invoice 🔐

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
api_instance = swagger_client.SupplierinvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Invoice ID
body = swagger_client.SupplierinvoicesValidateModel() # SupplierinvoicesValidateModel | idwarehouse  
notrigger  
 (optional)

try:
    # Validate an invoice 🔐
    api_response = api_instance.supplierinvoices_validate(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierinvoicesApi->supplierinvoices_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Invoice ID | 
 **body** | [**SupplierinvoicesValidateModel**](SupplierinvoicesValidateModel.md)| idwarehouse  
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

# **update_supplierinvoices**
> int update_supplierinvoices(id, body=body)

Update supplier invoice 🔐

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
api_instance = swagger_client.SupplierinvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of supplier invoice to update
body = swagger_client.UpdateSupplierinvoicesModel() # UpdateSupplierinvoicesModel | request_data  
 (optional)

try:
    # Update supplier invoice 🔐
    api_response = api_instance.update_supplierinvoices(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierinvoicesApi->update_supplierinvoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier invoice to update | 
 **body** | [**UpdateSupplierinvoicesModel**](UpdateSupplierinvoicesModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

