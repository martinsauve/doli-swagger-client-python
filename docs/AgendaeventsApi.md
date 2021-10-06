# swagger_client.AgendaeventsApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agendaevents**](AgendaeventsApi.md#create_agendaevents) | **POST** /agendaevents | Create Agenda Event object 🔐
[**list_agendaevents**](AgendaeventsApi.md#list_agendaevents) | **GET** /agendaevents | List Agenda Events 🔐
[**remove_agendaevents**](AgendaeventsApi.md#remove_agendaevents) | **DELETE** /agendaevents/{id} | Delete Agenda Event 🔐
[**retrieve_agendaevents**](AgendaeventsApi.md#retrieve_agendaevents) | **GET** /agendaevents/{id} | Get properties of a Agenda Events object 🔐
[**update_agendaevents**](AgendaeventsApi.md#update_agendaevents) | **PUT** /agendaevents/{id} | Update Agenda Event general fields 🔐

# **create_agendaevents**
> int create_agendaevents(body=body)

Create Agenda Event object 🔐

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
api_instance = swagger_client.AgendaeventsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateAgendaeventsModel() # CreateAgendaeventsModel | request_data  
 (optional)

try:
    # Create Agenda Event object 🔐
    api_response = api_instance.create_agendaevents(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgendaeventsApi->create_agendaevents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAgendaeventsModel**](CreateAgendaeventsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agendaevents**
> list[str] list_agendaevents(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, user_ids=user_ids, sqlfilters=sqlfilters)

List Agenda Events 🔐

Get a list of Agenda Events

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
api_instance = swagger_client.AgendaeventsApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
user_ids = 'user_ids_example' # str | User ids filter field (owners of event). Example: '1' or '1,2,3' (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.label:like:'%dol%') and (t.datec:<:'20160101')\" (optional)

try:
    # List Agenda Events 🔐
    api_response = api_instance.list_agendaevents(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, user_ids=user_ids, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgendaeventsApi->list_agendaevents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **user_ids** | **str**| User ids filter field (owners of event). Example: &#x27;1&#x27; or &#x27;1,2,3&#x27; | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.label:like:&#x27;%dol%&#x27;) and (t.datec:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_agendaevents**
> list[str] remove_agendaevents(id)

Delete Agenda Event 🔐

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
api_instance = swagger_client.AgendaeventsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Agenda Event ID

try:
    # Delete Agenda Event 🔐
    api_response = api_instance.remove_agendaevents(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgendaeventsApi->remove_agendaevents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Agenda Event ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_agendaevents**
> str retrieve_agendaevents(id)

Get properties of a Agenda Events object 🔐

Return an array with Agenda Events informations

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
api_instance = swagger_client.AgendaeventsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of Agenda Events

try:
    # Get properties of a Agenda Events object 🔐
    api_response = api_instance.retrieve_agendaevents(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgendaeventsApi->retrieve_agendaevents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Agenda Events | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agendaevents**
> int update_agendaevents(id, body=body)

Update Agenda Event general fields 🔐

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
api_instance = swagger_client.AgendaeventsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of Agenda Event to update
body = swagger_client.UpdateAgendaeventsModel() # UpdateAgendaeventsModel | request_data  
 (optional)

try:
    # Update Agenda Event general fields 🔐
    api_response = api_instance.update_agendaevents(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgendaeventsApi->update_agendaevents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of Agenda Event to update | 
 **body** | [**UpdateAgendaeventsModel**](UpdateAgendaeventsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

