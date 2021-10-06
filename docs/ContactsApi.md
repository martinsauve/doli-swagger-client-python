# swagger_client.ContactsApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contacts_add_category**](ContactsApi.md#contacts_add_category) | **POST** /contacts/{id}/categories/{category_id} | Add a category to a contact 🔐
[**contacts_create_user**](ContactsApi.md#contacts_create_user) | **POST** /contacts/{id}/createUser | Create an user account object from contact (external user) 🔐
[**contacts_remove_category**](ContactsApi.md#contacts_remove_category) | **DELETE** /contacts/{id}/categories/{category_id} | Remove the link between a category and a contact 🔐
[**contacts_retrieve_by_email**](ContactsApi.md#contacts_retrieve_by_email) | **GET** /contacts/email/{email} | Get properties of a contact object by Email 🔐
[**contacts_retrieve_categories**](ContactsApi.md#contacts_retrieve_categories) | **GET** /contacts/{id}/categories | Get categories for a contact 🔐
[**create_contacts**](ContactsApi.md#create_contacts) | **POST** /contacts | Create contact object 🔐
[**list_contacts**](ContactsApi.md#list_contacts) | **GET** /contacts | List contacts 🔐
[**remove_contacts**](ContactsApi.md#remove_contacts) | **DELETE** /contacts/{id} | Delete contact 🔐
[**retrieve_contacts**](ContactsApi.md#retrieve_contacts) | **GET** /contacts/{id} | Get properties of a contact object 🔐
[**update_contacts**](ContactsApi.md#update_contacts) | **PUT** /contacts/{id} | Update contact 🔐

# **contacts_add_category**
> str contacts_add_category(id, category_id)

Add a category to a contact 🔐

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
api_instance = swagger_client.ContactsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of contact
category_id = 789 # int | Id of category

try:
    # Add a category to a contact 🔐
    api_response = api_instance.contacts_add_category(id, category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_add_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of contact | 
 **category_id** | **int**| Id of category | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_create_user**
> int contacts_create_user(id, body=body)

Create an user account object from contact (external user) 🔐

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
api_instance = swagger_client.ContactsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of contact
body = swagger_client.ContactsCreateUserModel() # ContactsCreateUserModel | request_data  
 (optional)

try:
    # Create an user account object from contact (external user) 🔐
    api_response = api_instance.contacts_create_user(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of contact | 
 **body** | [**ContactsCreateUserModel**](ContactsCreateUserModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_remove_category**
> str contacts_remove_category(id, category_id)

Remove the link between a category and a contact 🔐

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
api_instance = swagger_client.ContactsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of contact
category_id = 789 # int | Id of category

try:
    # Remove the link between a category and a contact 🔐
    api_response = api_instance.contacts_remove_category(id, category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_remove_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of contact | 
 **category_id** | **int**| Id of category | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_retrieve_by_email**
> str contacts_retrieve_by_email(email, includecount=includecount, includeroles=includeroles)

Get properties of a contact object by Email 🔐

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
api_instance = swagger_client.ContactsApi(swagger_client.ApiClient(configuration))
email = 'email_example' # str | Email of contact
includecount = 789 # int | Count and return also number of elements the contact is used as a link for (optional)
includeroles = 789 # int | Includes roles of the contact (optional)

try:
    # Get properties of a contact object by Email 🔐
    api_response = api_instance.contacts_retrieve_by_email(email, includecount=includecount, includeroles=includeroles)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_retrieve_by_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of contact | 
 **includecount** | **int**| Count and return also number of elements the contact is used as a link for | [optional] 
 **includeroles** | **int**| Includes roles of the contact | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_retrieve_categories**
> str contacts_retrieve_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)

Get categories for a contact 🔐

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
api_instance = swagger_client.ContactsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of contact
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)

try:
    # Get categories for a contact 🔐
    api_response = api_instance.contacts_retrieve_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_retrieve_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of contact | 
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contacts**
> int create_contacts(body=body)

Create contact object 🔐

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
api_instance = swagger_client.ContactsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateContactsModel() # CreateContactsModel | request_data  
 (optional)

try:
    # Create contact object 🔐
    api_response = api_instance.create_contacts(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->create_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateContactsModel**](CreateContactsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contacts**
> list[str] list_contacts(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, category=category, sqlfilters=sqlfilters, includecount=includecount, includeroles=includeroles)

List contacts 🔐

Get a list of contacts

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
api_instance = swagger_client.ContactsApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter contacts of (example '1' or '1,2,3') (optional)
category = 789 # int | Use this param to filter list by category (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)
includecount = 789 # int | Count and return also number of elements the contact is used as a link for (optional)
includeroles = 789 # int | Includes roles of the contact (optional)

try:
    # List contacts 🔐
    api_response = api_instance.list_contacts(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, category=category, sqlfilters=sqlfilters, includecount=includecount, includeroles=includeroles)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->list_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Thirdparty ids to filter contacts of (example &#x27;1&#x27; or &#x27;1,2,3&#x27;) | [optional] 
 **category** | **int**| Use this param to filter list by category | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#x27;SO-%&#x27;) and (t.date_creation:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 
 **includecount** | **int**| Count and return also number of elements the contact is used as a link for | [optional] 
 **includeroles** | **int**| Includes roles of the contact | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_contacts**
> int remove_contacts(id)

Delete contact 🔐

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
api_instance = swagger_client.ContactsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Contact ID

try:
    # Delete contact 🔐
    api_response = api_instance.remove_contacts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->remove_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Contact ID | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_contacts**
> str retrieve_contacts(id, includecount=includecount, includeroles=includeroles)

Get properties of a contact object 🔐

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
api_instance = swagger_client.ContactsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of contact
includecount = 789 # int | Count and return also number of elements the contact is used as a link for (optional)
includeroles = 789 # int | Includes roles of the contact (optional)

try:
    # Get properties of a contact object 🔐
    api_response = api_instance.retrieve_contacts(id, includecount=includecount, includeroles=includeroles)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->retrieve_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of contact | 
 **includecount** | **int**| Count and return also number of elements the contact is used as a link for | [optional] 
 **includeroles** | **int**| Includes roles of the contact | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contacts**
> int update_contacts(id, body=body)

Update contact 🔐

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
api_instance = swagger_client.ContactsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of contact to update
body = swagger_client.UpdateContactsModel() # UpdateContactsModel | request_data  
 (optional)

try:
    # Update contact 🔐
    api_response = api_instance.update_contacts(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->update_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of contact to update | 
 **body** | [**UpdateContactsModel**](UpdateContactsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

