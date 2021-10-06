# swagger_client.DocumentsApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_documents**](DocumentsApi.md#create_documents) | **POST** /documents/upload | Upload a file. 🔐
[**documents_builddoc**](DocumentsApi.md#documents_builddoc) | **PUT** /documents/builddoc | Build a document. 🔐
[**documents_retrieve_documents_list_by_element**](DocumentsApi.md#documents_retrieve_documents_list_by_element) | **GET** /documents | Return the list of documents of a dedicated element (from its ID or Ref) 🔐
[**list_documents**](DocumentsApi.md#list_documents) | **GET** /documents/download | Download a document. 🔐
[**remove_documents**](DocumentsApi.md#remove_documents) | **DELETE** /documents | Delete a document. 🔐

# **create_documents**
> str create_documents(body)

Upload a file. 🔐

 Test sample for invoice: { \"filename\": \"mynewfile.txt\", \"modulepart\": \"invoice\", \"ref\": \"FA1701-001\", \"subdir\": \"\", \"filecontent\": \"content text\", \"fileencoding\": \"\", \"overwriteifexists\": \"0\" }. Test sample for supplier invoice: { \"filename\": \"mynewfile.txt\", \"modulepart\": \"supplier_invoice\", \"ref\": \"FA1701-001\", \"subdir\": \"\", \"filecontent\": \"content text\", \"fileencoding\": \"\", \"overwriteifexists\": \"0\" }. Test sample for medias file: { \"filename\": \"mynewfile.txt\", \"modulepart\": \"medias\", \"ref\": \"\", \"subdir\": \"image/mywebsite\", \"filecontent\": \"Y29udGVudCB0ZXh0Cg==\", \"fileencoding\": \"base64\", \"overwriteifexists\": \"0\" }.

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateDocumentsModel() # CreateDocumentsModel | **filename** (required)  
**modulepart** (required)  
ref  
subdir  
filecontent  
fileencoding  
overwriteifexists  
createdirifnotexists  


try:
    # Upload a file. 🔐
    api_response = api_instance.create_documents(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->create_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDocumentsModel**](CreateDocumentsModel.md)| **filename** (required)  
**modulepart** (required)  
ref  
subdir  
filecontent  
fileencoding  
overwriteifexists  
createdirifnotexists  
 | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_builddoc**
> list[str] documents_builddoc(body)

Build a document. 🔐

 Test sample 1: { \"modulepart\": \"invoice\", \"original_file\": \"FA1701-001/FA1701-001.pdf\", \"doctemplate\": \"crabe\", \"langcode\": \"fr_FR\" }.

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsBuilddocModel() # DocumentsBuilddocModel | **modulepart** (required)  
original_file  
doctemplate  
langcode  


try:
    # Build a document. 🔐
    api_response = api_instance.documents_builddoc(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_builddoc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsBuilddocModel**](DocumentsBuilddocModel.md)| **modulepart** (required)  
original_file  
doctemplate  
langcode  
 | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_retrieve_documents_list_by_element**
> list[str] documents_retrieve_documents_list_by_element(modulepart, id=id, ref=ref, sortfield=sortfield, sortorder=sortorder)

Return the list of documents of a dedicated element (from its ID or Ref) 🔐

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
modulepart = 'modulepart_example' # str | Name of module or area concerned ('thirdparty', 'member', 'proposal', 'order', 'invoice', 'supplier_invoice', 'shipment', 'project', ...)
id = 789 # int | ID of element (optional)
ref = 'ref_example' # str | Ref of element (optional)
sortfield = 'sortfield_example' # str | Sort criteria ('','fullname','relativename','name','date','size') (optional)
sortorder = 'sortorder_example' # str | Sort order ('asc' or 'desc') (optional)

try:
    # Return the list of documents of a dedicated element (from its ID or Ref) 🔐
    api_response = api_instance.documents_retrieve_documents_list_by_element(modulepart, id=id, ref=ref, sortfield=sortfield, sortorder=sortorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_retrieve_documents_list_by_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modulepart** | **str**| Name of module or area concerned (&#x27;thirdparty&#x27;, &#x27;member&#x27;, &#x27;proposal&#x27;, &#x27;order&#x27;, &#x27;invoice&#x27;, &#x27;supplier_invoice&#x27;, &#x27;shipment&#x27;, &#x27;project&#x27;, ...) | 
 **id** | **int**| ID of element | [optional] 
 **ref** | **str**| Ref of element | [optional] 
 **sortfield** | **str**| Sort criteria (&#x27;&#x27;,&#x27;fullname&#x27;,&#x27;relativename&#x27;,&#x27;name&#x27;,&#x27;date&#x27;,&#x27;size&#x27;) | [optional] 
 **sortorder** | **str**| Sort order (&#x27;asc&#x27; or &#x27;desc&#x27;) | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_documents**
> list[str] list_documents(modulepart, original_file=original_file)

Download a document. 🔐

 Note that, this API is similar to using the wrapper link \"documents.php\" to download a file (used for internal HTML links of documents into application), but with no need to have a session cookie (the token is used instead).

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
modulepart = 'modulepart_example' # str | Name of module or area concerned by file download ('facture', ...)
original_file = 'original_file_example' # str | Relative path with filename, relative to modulepart (for example: IN201701-999/IN201701-999.pdf) (optional)

try:
    # Download a document. 🔐
    api_response = api_instance.list_documents(modulepart, original_file=original_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->list_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modulepart** | **str**| Name of module or area concerned by file download (&#x27;facture&#x27;, ...) | 
 **original_file** | **str**| Relative path with filename, relative to modulepart (for example: IN201701-999/IN201701-999.pdf) | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_documents**
> list[str] remove_documents(modulepart, original_file)

Delete a document. 🔐

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
modulepart = 'modulepart_example' # str | Name of module or area concerned by file download ('product', ...)
original_file = 'original_file_example' # str | Relative path with filename, relative to modulepart (for example: PRODUCT-REF-999/IMAGE-999.jpg)

try:
    # Delete a document. 🔐
    api_response = api_instance.remove_documents(modulepart, original_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->remove_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modulepart** | **str**| Name of module or area concerned by file download (&#x27;product&#x27;, ...) | 
 **original_file** | **str**| Relative path with filename, relative to modulepart (for example: PRODUCT-REF-999/IMAGE-999.jpg) | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

