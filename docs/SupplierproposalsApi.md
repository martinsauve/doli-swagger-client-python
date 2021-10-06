# swagger_client.SupplierproposalsApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_supplierproposals**](SupplierproposalsApi.md#list_supplierproposals) | **GET** /supplierproposals | List supplier proposals 🔐
[**retrieve_supplierproposals**](SupplierproposalsApi.md#retrieve_supplierproposals) | **GET** /supplierproposals/{id} | Get properties of a supplier proposal (price request) object 🔐

# **list_supplierproposals**
> list[str] list_supplierproposals(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters)

List supplier proposals 🔐

Get a list of supplier proposals

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
api_instance = swagger_client.SupplierproposalsApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter supplier proposals (example '1' or '1,2,3') (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.datec:<:'20160101')\" (optional)

try:
    # List supplier proposals 🔐
    api_response = api_instance.list_supplierproposals(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierproposalsApi->list_supplierproposals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Thirdparty ids to filter supplier proposals (example &#x27;1&#x27; or &#x27;1,2,3&#x27;) | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#x27;SO-%&#x27;) and (t.datec:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_supplierproposals**
> str retrieve_supplierproposals(id)

Get properties of a supplier proposal (price request) object 🔐

Return an array with supplier proposal informations

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
api_instance = swagger_client.SupplierproposalsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of supplier proposal

try:
    # Get properties of a supplier proposal (price request) object 🔐
    api_response = api_instance.retrieve_supplierproposals(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierproposalsApi->retrieve_supplierproposals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of supplier proposal | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

