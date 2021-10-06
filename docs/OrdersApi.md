# swagger_client.OrdersApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_orders**](OrdersApi.md#create_orders) | **POST** /orders | Create a sale order 🔐
[**list_orders**](OrdersApi.md#list_orders) | **GET** /orders | List orders 🔐
[**orders_close**](OrdersApi.md#orders_close) | **POST** /orders/{id}/close | Close an order (Classify it as \&quot;Delivered\&quot;) 🔐
[**orders_create_contact**](OrdersApi.md#orders_create_contact) | **POST** /orders/{id}/contact/{contactid}/{type} | Add a contact type of given order 🔐
[**orders_create_line**](OrdersApi.md#orders_create_line) | **POST** /orders/{id}/lines | Add a line to given order 🔐
[**orders_create_order_from_proposal**](OrdersApi.md#orders_create_order_from_proposal) | **POST** /orders/createfromproposal/{proposalid} | Create an order using an existing proposal. 🔐
[**orders_remove_contact**](OrdersApi.md#orders_remove_contact) | **DELETE** /orders/{id}/contact/{contactid}/{type} | Unlink a contact type of given order 🔐
[**orders_remove_line**](OrdersApi.md#orders_remove_line) | **DELETE** /orders/{id}/lines/{lineid} | Delete a line to given order 🔐
[**orders_reopen**](OrdersApi.md#orders_reopen) | **POST** /orders/{id}/reopen | Tag the order as validated (opened) 🔐
[**orders_retrieve_by_ref**](OrdersApi.md#orders_retrieve_by_ref) | **GET** /orders/ref/{ref} | Get properties of an order object by ref 🔐
[**orders_retrieve_by_ref_ext**](OrdersApi.md#orders_retrieve_by_ref_ext) | **GET** /orders/ref_ext/{ref_ext} | Get properties of an order object by ref_ext 🔐
[**orders_retrieve_contacts**](OrdersApi.md#orders_retrieve_contacts) | **GET** /orders/{id}/contacts | Get contacts of given order 🔐
[**orders_retrieve_lines**](OrdersApi.md#orders_retrieve_lines) | **GET** /orders/{id}/lines | Get lines of an order 🔐
[**orders_setinvoiced**](OrdersApi.md#orders_setinvoiced) | **POST** /orders/{id}/setinvoiced | Classify the order as invoiced. Could be also called setbilled 🔐
[**orders_settodraft**](OrdersApi.md#orders_settodraft) | **POST** /orders/{id}/settodraft | Set an order to draft 🔐
[**orders_update_line**](OrdersApi.md#orders_update_line) | **PUT** /orders/{id}/lines/{lineid} | Update a line to given order 🔐
[**orders_validate**](OrdersApi.md#orders_validate) | **POST** /orders/{id}/validate | Validate an order 🔐
[**remove_orders**](OrdersApi.md#remove_orders) | **DELETE** /orders/{id} | Delete order 🔐
[**retrieve_orders**](OrdersApi.md#retrieve_orders) | **GET** /orders/{id} | Get properties of an order object by id 🔐
[**update_orders**](OrdersApi.md#update_orders) | **PUT** /orders/{id} | Update order general fields (won&#x27;t touch lines of order) 🔐

# **create_orders**
> int create_orders(body=body)

Create a sale order 🔐

Exemple: { \"socid\": 2, \"date\": 1595196000, \"type\": 0, \"lines\": [{ \"fk_product\": 2, \"qty\": 1 }] }

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateOrdersModel() # CreateOrdersModel | request_data  
 (optional)

try:
    # Create a sale order 🔐
    api_response = api_instance.create_orders(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->create_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrdersModel**](CreateOrdersModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> list[str] list_orders(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters)

List orders 🔐

Get a list of orders

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter orders of (example '1' or '1,2,3') (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)

try:
    # List orders 🔐
    api_response = api_instance.list_orders(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->list_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Thirdparty ids to filter orders of (example &#x27;1&#x27; or &#x27;1,2,3&#x27;) | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#x27;SO-%&#x27;) and (t.date_creation:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_close**
> int orders_close(id, body=body)

Close an order (Classify it as \"Delivered\") 🔐

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Order ID
body = swagger_client.OrdersCloseModel() # OrdersCloseModel | notrigger  
 (optional)

try:
    # Close an order (Classify it as \"Delivered\") 🔐
    api_response = api_instance.orders_close(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **body** | [**OrdersCloseModel**](OrdersCloseModel.md)| notrigger  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_create_contact**
> int orders_create_contact(id, contactid, type)

Add a contact type of given order 🔐

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of order to update
contactid = 789 # int | Id of contact to add
type = 'type_example' # str | Type of the contact (BILLING, SHIPPING, CUSTOMER)

try:
    # Add a contact type of given order 🔐
    api_response = api_instance.orders_create_contact(id, contactid, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order to update | 
 **contactid** | **int**| Id of contact to add | 
 **type** | **str**| Type of the contact (BILLING, SHIPPING, CUSTOMER) | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_create_line**
> int orders_create_line(id, body=body)

Add a line to given order 🔐

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of order to update
body = swagger_client.OrdersCreateLineModel() # OrdersCreateLineModel | request_data  
 (optional)

try:
    # Add a line to given order 🔐
    api_response = api_instance.orders_create_line(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_create_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order to update | 
 **body** | [**OrdersCreateLineModel**](OrdersCreateLineModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_create_order_from_proposal**
> int orders_create_order_from_proposal(proposalid)

Create an order using an existing proposal. 🔐

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
proposalid = 789 # int | Id of the proposal

try:
    # Create an order using an existing proposal. 🔐
    api_response = api_instance.orders_create_order_from_proposal(proposalid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_create_order_from_proposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposalid** | **int**| Id of the proposal | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_remove_contact**
> int orders_remove_contact(id, contactid, type)

Unlink a contact type of given order 🔐

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of order to update
contactid = 789 # int | Id of contact
type = 'type_example' # str | Type of the contact (BILLING, SHIPPING, CUSTOMER).

try:
    # Unlink a contact type of given order 🔐
    api_response = api_instance.orders_remove_contact(id, contactid, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_remove_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order to update | 
 **contactid** | **int**| Id of contact | 
 **type** | **str**| Type of the contact (BILLING, SHIPPING, CUSTOMER). | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_remove_line**
> int orders_remove_line(id, lineid)

Delete a line to given order 🔐

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of order to update
lineid = 789 # int | Id of line to delete

try:
    # Delete a line to given order 🔐
    api_response = api_instance.orders_remove_line(id, lineid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_remove_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order to update | 
 **lineid** | **int**| Id of line to delete | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_reopen**
> int orders_reopen(id)

Tag the order as validated (opened) 🔐

Function used when order is reopend after being closed.

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of the order

try:
    # Tag the order as validated (opened) 🔐
    api_response = api_instance.orders_reopen(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_reopen: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the order | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_retrieve_by_ref**
> str orders_retrieve_by_ref(ref, contact_list=contact_list)

Get properties of an order object by ref 🔐

Return an array with order informations

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
ref = 'ref_example' # str | Ref of object
contact_list = 789 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id (optional)

try:
    # Get properties of an order object by ref 🔐
    api_response = api_instance.orders_retrieve_by_ref(ref, contact_list=contact_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_retrieve_by_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Ref of object | 
 **contact_list** | **int**| 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_retrieve_by_ref_ext**
> str orders_retrieve_by_ref_ext(ref_ext, contact_list=contact_list)

Get properties of an order object by ref_ext 🔐

Return an array with order informations

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
ref_ext = 'ref_ext_example' # str | External reference of object
contact_list = 789 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id (optional)

try:
    # Get properties of an order object by ref_ext 🔐
    api_response = api_instance.orders_retrieve_by_ref_ext(ref_ext, contact_list=contact_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_retrieve_by_ref_ext: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref_ext** | **str**| External reference of object | 
 **contact_list** | **int**| 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_retrieve_contacts**
> list[str] orders_retrieve_contacts(id, type=type)

Get contacts of given order 🔐

Return an array with contact informations

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of order
type = 'type_example' # str | Type of the contact (BILLING, SHIPPING, CUSTOMER) (optional)

try:
    # Get contacts of given order 🔐
    api_response = api_instance.orders_retrieve_contacts(id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_retrieve_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of order | 
 **type** | **str**| Type of the contact (BILLING, SHIPPING, CUSTOMER) | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_retrieve_lines**
> int orders_retrieve_lines(id)

Get lines of an order 🔐

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of order

try:
    # Get lines of an order 🔐
    api_response = api_instance.orders_retrieve_lines(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_retrieve_lines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_setinvoiced**
> int orders_setinvoiced(id)

Classify the order as invoiced. Could be also called setbilled 🔐

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of the order

try:
    # Classify the order as invoiced. Could be also called setbilled 🔐
    api_response = api_instance.orders_setinvoiced(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_setinvoiced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the order | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_settodraft**
> list[str] orders_settodraft(id, body=body)

Set an order to draft 🔐

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Order ID
body = swagger_client.OrdersSettodraftModel() # OrdersSettodraftModel | idwarehouse  
 (optional)

try:
    # Set an order to draft 🔐
    api_response = api_instance.orders_settodraft(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_settodraft: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **body** | [**OrdersSettodraftModel**](OrdersSettodraftModel.md)| idwarehouse  
 | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_update_line**
> str orders_update_line(id, lineid, body=body)

Update a line to given order 🔐

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of order to update
lineid = 789 # int | Id of line to update
body = swagger_client.OrdersUpdateLineModel() # OrdersUpdateLineModel | request_data  
 (optional)

try:
    # Update a line to given order 🔐
    api_response = api_instance.orders_update_line(id, lineid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_update_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order to update | 
 **lineid** | **int**| Id of line to update | 
 **body** | [**OrdersUpdateLineModel**](OrdersUpdateLineModel.md)| request_data  
 | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_validate**
> list[str] orders_validate(id, body=body)

Validate an order 🔐

If you get a bad value for param notrigger check, provide this in body { \"idwarehouse\": 0, \"notrigger\": 0 }

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Order ID
body = swagger_client.OrdersValidateModel() # OrdersValidateModel | idwarehouse  
notrigger  
 (optional)

try:
    # Validate an order 🔐
    api_response = api_instance.orders_validate(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **body** | [**OrdersValidateModel**](OrdersValidateModel.md)| idwarehouse  
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

# **remove_orders**
> list[str] remove_orders(id)

Delete order 🔐

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Order ID

try:
    # Delete order 🔐
    api_response = api_instance.remove_orders(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->remove_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_orders**
> str retrieve_orders(id, contact_list=contact_list)

Get properties of an order object by id 🔐

Return an array with order informations

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of order
contact_list = 789 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id (optional)

try:
    # Get properties of an order object by id 🔐
    api_response = api_instance.retrieve_orders(id, contact_list=contact_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->retrieve_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of order | 
 **contact_list** | **int**| 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_orders**
> int update_orders(id, body=body)

Update order general fields (won't touch lines of order) 🔐

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of order to update
body = swagger_client.UpdateOrdersModel() # UpdateOrdersModel | request_data  
 (optional)

try:
    # Update order general fields (won't touch lines of order) 🔐
    api_response = api_instance.update_orders(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->update_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order to update | 
 **body** | [**UpdateOrdersModel**](UpdateOrdersModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

