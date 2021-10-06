# swagger_client.TicketsApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tickets**](TicketsApi.md#create_tickets) | **POST** /tickets | Create ticket object 🔐
[**list_tickets**](TicketsApi.md#list_tickets) | **GET** /tickets | List tickets 🔐
[**remove_tickets**](TicketsApi.md#remove_tickets) | **DELETE** /tickets/{id} | Delete ticket 🔐
[**retrieve_tickets**](TicketsApi.md#retrieve_tickets) | **GET** /tickets/{id} | Get properties of a Ticket object. 🔐
[**tickets_create_new_message**](TicketsApi.md#tickets_create_new_message) | **POST** /tickets/newmessage | Create ticket object 🔐
[**tickets_retrieve_by_ref**](TicketsApi.md#tickets_retrieve_by_ref) | **GET** /tickets/ref/{ref} | Get properties of a Ticket object from ref 🔐
[**tickets_retrieve_by_track_id**](TicketsApi.md#tickets_retrieve_by_track_id) | **GET** /tickets/track_id/{track_id} | Get properties of a Ticket object from track id 🔐
[**update_tickets**](TicketsApi.md#update_tickets) | **PUT** /tickets/{id} | Update ticket 🔐

# **create_tickets**
> int create_tickets(body=body)

Create ticket object 🔐

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
api_instance = swagger_client.TicketsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateTicketsModel() # CreateTicketsModel | request_data  
 (optional)

try:
    # Create ticket object 🔐
    api_response = api_instance.create_tickets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->create_tickets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTicketsModel**](CreateTicketsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tickets**
> list[str] list_tickets(socid=socid, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters)

List tickets 🔐

Get a list of tickets

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
api_instance = swagger_client.TicketsApi(swagger_client.ApiClient(configuration))
socid = 789 # int | Filter list with thirdparty ID (optional)
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101') and (t.fk_statut:=:1)\" (optional)

try:
    # List tickets 🔐
    api_response = api_instance.list_tickets(socid=socid, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->list_tickets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **socid** | **int**| Filter list with thirdparty ID | [optional] 
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#x27;SO-%&#x27;) and (t.date_creation:&lt;:&#x27;20160101&#x27;) and (t.fk_statut:&#x3D;:1)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tickets**
> list[str] remove_tickets(id)

Delete ticket 🔐

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
api_instance = swagger_client.TicketsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Ticket ID

try:
    # Delete ticket 🔐
    api_response = api_instance.remove_tickets(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->remove_tickets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Ticket ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_tickets**
> str retrieve_tickets(id)

Get properties of a Ticket object. 🔐

 Return an array with ticket informations

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
api_instance = swagger_client.TicketsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of ticket

try:
    # Get properties of a Ticket object. 🔐
    api_response = api_instance.retrieve_tickets(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->retrieve_tickets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of ticket | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tickets_create_new_message**
> int tickets_create_new_message(body=body)

Create ticket object 🔐

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
api_instance = swagger_client.TicketsApi(swagger_client.ApiClient(configuration))
body = swagger_client.TicketsCreateNewMessageModel() # TicketsCreateNewMessageModel | request_data  
 (optional)

try:
    # Create ticket object 🔐
    api_response = api_instance.tickets_create_new_message(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->tickets_create_new_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TicketsCreateNewMessageModel**](TicketsCreateNewMessageModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tickets_retrieve_by_ref**
> str tickets_retrieve_by_ref(ref)

Get properties of a Ticket object from ref 🔐

Return an array with ticket informations

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
api_instance = swagger_client.TicketsApi(swagger_client.ApiClient(configuration))
ref = 'ref_example' # str | Reference for ticket

try:
    # Get properties of a Ticket object from ref 🔐
    api_response = api_instance.tickets_retrieve_by_ref(ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->tickets_retrieve_by_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Reference for ticket | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tickets_retrieve_by_track_id**
> str tickets_retrieve_by_track_id(track_id)

Get properties of a Ticket object from track id 🔐

Return an array with ticket informations

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
api_instance = swagger_client.TicketsApi(swagger_client.ApiClient(configuration))
track_id = 'track_id_example' # str | Tracking ID of ticket

try:
    # Get properties of a Ticket object from track id 🔐
    api_response = api_instance.tickets_retrieve_by_track_id(track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->tickets_retrieve_by_track_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **track_id** | **str**| Tracking ID of ticket | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tickets**
> int update_tickets(id, body=body)

Update ticket 🔐

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
api_instance = swagger_client.TicketsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of ticket to update
body = swagger_client.UpdateTicketsModel() # UpdateTicketsModel | request_data  
 (optional)

try:
    # Update ticket 🔐
    api_response = api_instance.update_tickets(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->update_tickets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of ticket to update | 
 **body** | [**UpdateTicketsModel**](UpdateTicketsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

