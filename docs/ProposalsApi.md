# swagger_client.ProposalsApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_proposals**](ProposalsApi.md#create_proposals) | **POST** /proposals | Create commercial proposal object 🔐
[**list_proposals**](ProposalsApi.md#list_proposals) | **GET** /proposals | List commercial proposals 🔐
[**proposals_close**](ProposalsApi.md#proposals_close) | **POST** /proposals/{id}/close | Close (Accept or refuse) a quote / commercial proposal 🔐
[**proposals_create_contact**](ProposalsApi.md#proposals_create_contact) | **POST** /proposals/{id}/contact/{contactid}/{type} | Add a contact type of given commercial proposal 🔐
[**proposals_create_line**](ProposalsApi.md#proposals_create_line) | **POST** /proposals/{id}/lines | Add a line to given commercial proposal 🔐
[**proposals_remove_contact**](ProposalsApi.md#proposals_remove_contact) | **DELETE** /proposals/{id}/contact/{contactid}/{type} | Delete a contact type of given commercial proposal 🔐
[**proposals_remove_line**](ProposalsApi.md#proposals_remove_line) | **DELETE** /proposals/{id}/lines/{lineid} | Delete a line of given commercial proposal 🔐
[**proposals_retrieve_by_ref**](ProposalsApi.md#proposals_retrieve_by_ref) | **GET** /proposals/ref/{ref} | Get properties of an proposal object by ref 🔐
[**proposals_retrieve_by_ref_ext**](ProposalsApi.md#proposals_retrieve_by_ref_ext) | **GET** /proposals/ref_ext/{ref_ext} | Get properties of an proposal object by ref_ext 🔐
[**proposals_retrieve_lines**](ProposalsApi.md#proposals_retrieve_lines) | **GET** /proposals/{id}/lines | Get lines of a commercial proposal 🔐
[**proposals_setinvoiced**](ProposalsApi.md#proposals_setinvoiced) | **POST** /proposals/{id}/setinvoiced | Set a commercial proposal billed. Could be also called setbilled 🔐
[**proposals_settodraft**](ProposalsApi.md#proposals_settodraft) | **POST** /proposals/{id}/settodraft | Set a proposal to draft 🔐
[**proposals_update_line**](ProposalsApi.md#proposals_update_line) | **PUT** /proposals/{id}/lines/{lineid} | Update a line of given commercial proposal 🔐
[**proposals_validate**](ProposalsApi.md#proposals_validate) | **POST** /proposals/{id}/validate | Validate a commercial proposal 🔐
[**remove_proposals**](ProposalsApi.md#remove_proposals) | **DELETE** /proposals/{id} | Delete commercial proposal 🔐
[**retrieve_proposals**](ProposalsApi.md#retrieve_proposals) | **GET** /proposals/{id} | Get properties of a commercial proposal object 🔐
[**update_proposals**](ProposalsApi.md#update_proposals) | **PUT** /proposals/{id} | Update commercial proposal general fields (won&#x27;t touch lines of commercial proposal) 🔐

# **create_proposals**
> int create_proposals(body=body)

Create commercial proposal object 🔐

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateProposalsModel() # CreateProposalsModel | request_data  
 (optional)

try:
    # Create commercial proposal object 🔐
    api_response = api_instance.create_proposals(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->create_proposals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProposalsModel**](CreateProposalsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_proposals**
> list[str] list_proposals(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters)

List commercial proposals 🔐

Get a list of commercial proposals

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter commercial proposals (example '1' or '1,2,3') (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.datec:<:'20160101')\" (optional)

try:
    # List commercial proposals 🔐
    api_response = api_instance.list_proposals(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->list_proposals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Thirdparty ids to filter commercial proposals (example &#x27;1&#x27; or &#x27;1,2,3&#x27;) | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#x27;SO-%&#x27;) and (t.datec:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proposals_close**
> list[str] proposals_close(body, id)

Close (Accept or refuse) a quote / commercial proposal 🔐

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProposalsCloseModel() # ProposalsCloseModel | **status** (required)  
note_private  
notrigger  

id = 789 # int | Commercial proposal ID

try:
    # Close (Accept or refuse) a quote / commercial proposal 🔐
    api_response = api_instance.proposals_close(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->proposals_close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProposalsCloseModel**](ProposalsCloseModel.md)| **status** (required)  
note_private  
notrigger  
 | 
 **id** | **int**| Commercial proposal ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proposals_create_contact**
> int proposals_create_contact(id, contactid, type)

Add a contact type of given commercial proposal 🔐

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of commercial proposal to update
contactid = 789 # int | Id of contact to add
type = 'type_example' # str | Type of the contact (BILLING, SHIPPING, CUSTOMER)

try:
    # Add a contact type of given commercial proposal 🔐
    api_response = api_instance.proposals_create_contact(id, contactid, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->proposals_create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal to update | 
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

# **proposals_create_line**
> int proposals_create_line(id, body=body)

Add a line to given commercial proposal 🔐

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of commercial proposal to update
body = swagger_client.ProposalsCreateLineModel() # ProposalsCreateLineModel | request_data  
 (optional)

try:
    # Add a line to given commercial proposal 🔐
    api_response = api_instance.proposals_create_line(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->proposals_create_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal to update | 
 **body** | [**ProposalsCreateLineModel**](ProposalsCreateLineModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proposals_remove_contact**
> int proposals_remove_contact(id, contactid, type)

Delete a contact type of given commercial proposal 🔐

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of commercial proposal to update
contactid = 789 # int | Row key of the contact in the array contact_ids.
type = 'type_example' # str | Type of the contact (BILLING, SHIPPING, CUSTOMER).

try:
    # Delete a contact type of given commercial proposal 🔐
    api_response = api_instance.proposals_remove_contact(id, contactid, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->proposals_remove_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal to update | 
 **contactid** | **int**| Row key of the contact in the array contact_ids. | 
 **type** | **str**| Type of the contact (BILLING, SHIPPING, CUSTOMER). | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proposals_remove_line**
> int proposals_remove_line(id, lineid)

Delete a line of given commercial proposal 🔐

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of commercial proposal to update
lineid = 789 # int | Id of line to delete

try:
    # Delete a line of given commercial proposal 🔐
    api_response = api_instance.proposals_remove_line(id, lineid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->proposals_remove_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal to update | 
 **lineid** | **int**| Id of line to delete | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proposals_retrieve_by_ref**
> str proposals_retrieve_by_ref(ref, contact_list=contact_list)

Get properties of an proposal object by ref 🔐

Return an array with proposal informations

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
ref = 'ref_example' # str | Ref of object
contact_list = 789 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id (optional)

try:
    # Get properties of an proposal object by ref 🔐
    api_response = api_instance.proposals_retrieve_by_ref(ref, contact_list=contact_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->proposals_retrieve_by_ref: %s\n" % e)
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

# **proposals_retrieve_by_ref_ext**
> str proposals_retrieve_by_ref_ext(ref_ext, contact_list=contact_list)

Get properties of an proposal object by ref_ext 🔐

Return an array with proposal informations

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
ref_ext = 'ref_ext_example' # str | External reference of object
contact_list = 789 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id (optional)

try:
    # Get properties of an proposal object by ref_ext 🔐
    api_response = api_instance.proposals_retrieve_by_ref_ext(ref_ext, contact_list=contact_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->proposals_retrieve_by_ref_ext: %s\n" % e)
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

# **proposals_retrieve_lines**
> int proposals_retrieve_lines(id)

Get lines of a commercial proposal 🔐

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of commercial proposal

try:
    # Get lines of a commercial proposal 🔐
    api_response = api_instance.proposals_retrieve_lines(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->proposals_retrieve_lines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proposals_setinvoiced**
> list[str] proposals_setinvoiced(id)

Set a commercial proposal billed. Could be also called setbilled 🔐

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Commercial proposal ID

try:
    # Set a commercial proposal billed. Could be also called setbilled 🔐
    api_response = api_instance.proposals_setinvoiced(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->proposals_setinvoiced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Commercial proposal ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proposals_settodraft**
> list[str] proposals_settodraft(id)

Set a proposal to draft 🔐

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Order ID

try:
    # Set a proposal to draft 🔐
    api_response = api_instance.proposals_settodraft(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->proposals_settodraft: %s\n" % e)
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

# **proposals_update_line**
> str proposals_update_line(id, lineid, body=body)

Update a line of given commercial proposal 🔐

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of commercial proposal to update
lineid = 789 # int | Id of line to update
body = swagger_client.ProposalsUpdateLineModel() # ProposalsUpdateLineModel | request_data  
 (optional)

try:
    # Update a line of given commercial proposal 🔐
    api_response = api_instance.proposals_update_line(id, lineid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->proposals_update_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal to update | 
 **lineid** | **int**| Id of line to update | 
 **body** | [**ProposalsUpdateLineModel**](ProposalsUpdateLineModel.md)| request_data  
 | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proposals_validate**
> list[str] proposals_validate(id, body=body)

Validate a commercial proposal 🔐

If you get a bad value for param notrigger check that ou provide this in body { \"notrigger\": 0 }

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Commercial proposal ID
body = swagger_client.ProposalsValidateModel() # ProposalsValidateModel | notrigger  
 (optional)

try:
    # Validate a commercial proposal 🔐
    api_response = api_instance.proposals_validate(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->proposals_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Commercial proposal ID | 
 **body** | [**ProposalsValidateModel**](ProposalsValidateModel.md)| notrigger  
 | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_proposals**
> list[str] remove_proposals(id)

Delete commercial proposal 🔐

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Commercial proposal ID

try:
    # Delete commercial proposal 🔐
    api_response = api_instance.remove_proposals(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->remove_proposals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Commercial proposal ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_proposals**
> str retrieve_proposals(id, contact_list=contact_list)

Get properties of a commercial proposal object 🔐

Return an array with commercial proposal informations

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of commercial proposal
contact_list = 789 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id (optional)

try:
    # Get properties of a commercial proposal object 🔐
    api_response = api_instance.retrieve_proposals(id, contact_list=contact_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->retrieve_proposals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of commercial proposal | 
 **contact_list** | **int**| 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_proposals**
> int update_proposals(id, body=body)

Update commercial proposal general fields (won't touch lines of commercial proposal) 🔐

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
api_instance = swagger_client.ProposalsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of commercial proposal to update
body = swagger_client.UpdateProposalsModel() # UpdateProposalsModel | request_data  
 (optional)

try:
    # Update commercial proposal general fields (won't touch lines of commercial proposal) 🔐
    api_response = api_instance.update_proposals(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProposalsApi->update_proposals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal to update | 
 **body** | [**UpdateProposalsModel**](UpdateProposalsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

