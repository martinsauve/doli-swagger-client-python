# swagger_client.ThirdpartiesApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_thirdparties**](ThirdpartiesApi.md#create_thirdparties) | **POST** /thirdparties | Create thirdparty object 🔐
[**list_thirdparties**](ThirdpartiesApi.md#list_thirdparties) | **GET** /thirdparties | List thirdparties 🔐
[**remove_thirdparties**](ThirdpartiesApi.md#remove_thirdparties) | **DELETE** /thirdparties/{id} | Delete thirdparty 🔐
[**retrieve_thirdparties**](ThirdpartiesApi.md#retrieve_thirdparties) | **GET** /thirdparties/{id} | Get properties of a thirdparty object 🔐
[**thirdparties_add_category**](ThirdpartiesApi.md#thirdparties_add_category) | **POST** /thirdparties/{id}/categories/{category_id} | Add a customer category to a thirdparty 🔐
[**thirdparties_add_supplier_category**](ThirdpartiesApi.md#thirdparties_add_supplier_category) | **POST** /thirdparties/{id}/supplier_categories/{category_id} | Add a supplier category to a thirdparty 🔐
[**thirdparties_create_company_bank_account**](ThirdpartiesApi.md#thirdparties_create_company_bank_account) | **POST** /thirdparties/{id}/bankaccounts | Create CompanyBankAccount object for thirdparty 🔐
[**thirdparties_create_societe_account**](ThirdpartiesApi.md#thirdparties_create_societe_account) | **POST** /thirdparties/{id}/gateways | Create and attach a new gateway to an existing thirdparty 🔐
[**thirdparties_generate_bank_account_document**](ThirdpartiesApi.md#thirdparties_generate_bank_account_document) | **GET** /thirdparties/{id}/generateBankAccountDocument/{companybankid}/{model} | Generate a Document from a bank account record (like SEPA mandate) 🔐
[**thirdparties_merge**](ThirdpartiesApi.md#thirdparties_merge) | **PUT** /thirdparties/{id}/merge/{idtodelete} | Merge a thirdparty into another one. 🔐
[**thirdparties_modify_societe_account**](ThirdpartiesApi.md#thirdparties_modify_societe_account) | **PATCH** /thirdparties/{id}/gateways/{site} | Update specified values of a specific gateway attached to a thirdparty 🔐
[**thirdparties_remove_category**](ThirdpartiesApi.md#thirdparties_remove_category) | **DELETE** /thirdparties/{id}/categories/{category_id} | Remove the link between a customer category and the thirdparty 🔐
[**thirdparties_remove_company_bank_account**](ThirdpartiesApi.md#thirdparties_remove_company_bank_account) | **DELETE** /thirdparties/{id}/bankaccounts/{bankaccount_id} | Delete a bank account attached to a thirdparty 🔐
[**thirdparties_remove_societe_account**](ThirdpartiesApi.md#thirdparties_remove_societe_account) | **DELETE** /thirdparties/{id}/gateways/{site} | Delete a specific site gateway attached to a thirdparty (by gateway id) 🔐
[**thirdparties_remove_societe_accounts**](ThirdpartiesApi.md#thirdparties_remove_societe_accounts) | **DELETE** /thirdparties/{id}/gateways | Delete all gateways attached to a thirdparty 🔐
[**thirdparties_remove_supplier_category**](ThirdpartiesApi.md#thirdparties_remove_supplier_category) | **DELETE** /thirdparties/{id}/supplier_categories/{category_id} | Remove the link between a category and the thirdparty 🔐
[**thirdparties_retrieve_by_barcode**](ThirdpartiesApi.md#thirdparties_retrieve_by_barcode) | **GET** /thirdparties/barcode/{barcode} | Get properties of a thirdparty object by barcode. 🔐
[**thirdparties_retrieve_by_email**](ThirdpartiesApi.md#thirdparties_retrieve_by_email) | **GET** /thirdparties/email/{email} | Get properties of a thirdparty object by email. 🔐
[**thirdparties_retrieve_categories**](ThirdpartiesApi.md#thirdparties_retrieve_categories) | **GET** /thirdparties/{id}/categories | Get customer categories for a thirdparty 🔐
[**thirdparties_retrieve_company_bank_account**](ThirdpartiesApi.md#thirdparties_retrieve_company_bank_account) | **GET** /thirdparties/{id}/bankaccounts | Get CompanyBankAccount objects for thirdparty 🔐
[**thirdparties_retrieve_fixed_amount_discounts**](ThirdpartiesApi.md#thirdparties_retrieve_fixed_amount_discounts) | **GET** /thirdparties/{id}/fixedamountdiscounts | Get fixed amount discount of a thirdparty (all sources: deposit, credit note, commercial offers...) 🔐
[**thirdparties_retrieve_invoices_qualified_for_credit_note**](ThirdpartiesApi.md#thirdparties_retrieve_invoices_qualified_for_credit_note) | **GET** /thirdparties/{id}/getinvoicesqualifiedforcreditnote | Return list of invoices qualified to be corrected by a credit note. 🔐
[**thirdparties_retrieve_invoices_qualified_for_replacement**](ThirdpartiesApi.md#thirdparties_retrieve_invoices_qualified_for_replacement) | **GET** /thirdparties/{id}/getinvoicesqualifiedforreplacement | Return list of invoices qualified to be replaced by another invoice. 🔐
[**thirdparties_retrieve_out_standing_invoices**](ThirdpartiesApi.md#thirdparties_retrieve_out_standing_invoices) | **GET** /thirdparties/{id}/outstandinginvoices | Get outstanding invoices of thirdparty 🔐
[**thirdparties_retrieve_out_standing_order**](ThirdpartiesApi.md#thirdparties_retrieve_out_standing_order) | **GET** /thirdparties/{id}/outstandingorders | Get outstanding orders of thirdparty 🔐
[**thirdparties_retrieve_out_standing_proposals**](ThirdpartiesApi.md#thirdparties_retrieve_out_standing_proposals) | **GET** /thirdparties/{id}/outstandingproposals | Get outstanding proposals of thirdparty 🔐
[**thirdparties_retrieve_sales_representatives**](ThirdpartiesApi.md#thirdparties_retrieve_sales_representatives) | **GET** /thirdparties/{id}/representatives | Get representatives of thirdparty 🔐
[**thirdparties_retrieve_societe_accounts**](ThirdpartiesApi.md#thirdparties_retrieve_societe_accounts) | **GET** /thirdparties/{id}/gateways | Get a specific gateway attached to a thirdparty (by specifying the site key) 🔐
[**thirdparties_retrieve_supplier_categories**](ThirdpartiesApi.md#thirdparties_retrieve_supplier_categories) | **GET** /thirdparties/{id}/supplier_categories | Get supplier categories for a thirdparty 🔐
[**thirdparties_set_thirdparty_price_level**](ThirdpartiesApi.md#thirdparties_set_thirdparty_price_level) | **PUT** /thirdparties/{id}/setpricelevel | Set new price level for the given thirdparty 🔐
[**thirdparties_update_company_bank_account**](ThirdpartiesApi.md#thirdparties_update_company_bank_account) | **PUT** /thirdparties/{id}/bankaccounts/{bankaccount_id} | Update CompanyBankAccount object for thirdparty 🔐
[**thirdparties_update_societe_account**](ThirdpartiesApi.md#thirdparties_update_societe_account) | **PUT** /thirdparties/{id}/gateways/{site} | Create and attach a new (or replace an existing) specific site gateway to a thirdparty 🔐
[**update_thirdparties**](ThirdpartiesApi.md#update_thirdparties) | **PUT** /thirdparties/{id} | Update thirdparty 🔐

# **create_thirdparties**
> int create_thirdparties(body=body)

Create thirdparty object 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateThirdpartiesModel() # CreateThirdpartiesModel | request_data  
 (optional)

try:
    # Create thirdparty object 🔐
    api_response = api_instance.create_thirdparties(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->create_thirdparties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateThirdpartiesModel**](CreateThirdpartiesModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_thirdparties**
> list[str] list_thirdparties(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, mode=mode, category=category, sqlfilters=sqlfilters)

List thirdparties 🔐

Get a list of thirdparties

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
mode = 789 # int | Set to 1 to show only customers Set to 2 to show only prospects Set to 3 to show only those are not customer neither prospect Set to 4 to show only suppliers (optional)
category = 789 # int | Use this param to filter list by category (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"((t.nom:like:'TheCompany%') or (t.name_alias:like:'TheCompany%')) and (t.datec:<:'20160101')\" (optional)

try:
    # List thirdparties 🔐
    api_response = api_instance.list_thirdparties(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, mode=mode, category=category, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->list_thirdparties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **mode** | **int**| Set to 1 to show only customers Set to 2 to show only prospects Set to 3 to show only those are not customer neither prospect Set to 4 to show only suppliers | [optional] 
 **category** | **int**| Use this param to filter list by category | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;((t.nom:like:&#x27;TheCompany%&#x27;) or (t.name_alias:like:&#x27;TheCompany%&#x27;)) and (t.datec:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_thirdparties**
> int remove_thirdparties(id)

Delete thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Thirparty ID

try:
    # Delete thirdparty 🔐
    api_response = api_instance.remove_thirdparties(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->remove_thirdparties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Thirparty ID | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_thirdparties**
> str retrieve_thirdparties(id)

Get properties of a thirdparty object 🔐

Return an array with thirdparty informations

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of third party to load

try:
    # Get properties of a thirdparty object 🔐
    api_response = api_instance.retrieve_thirdparties(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->retrieve_thirdparties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of third party to load | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_add_category**
> str thirdparties_add_category(id, category_id)

Add a customer category to a thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of thirdparty
category_id = 789 # int | Id of category

try:
    # Add a customer category to a thirdparty 🔐
    api_response = api_instance.thirdparties_add_category(id, category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_add_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of thirdparty | 
 **category_id** | **int**| Id of category | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_add_supplier_category**
> str thirdparties_add_supplier_category(id, category_id)

Add a supplier category to a thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of thirdparty
category_id = 789 # int | Id of category

try:
    # Add a supplier category to a thirdparty 🔐
    api_response = api_instance.thirdparties_add_supplier_category(id, category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_add_supplier_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of thirdparty | 
 **category_id** | **int**| Id of category | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_create_company_bank_account**
> str thirdparties_create_company_bank_account(id, body=body)

Create CompanyBankAccount object for thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of thirdparty
body = swagger_client.ThirdpartiesCreateCompanyBankAccountModel() # ThirdpartiesCreateCompanyBankAccountModel | request_data  
 (optional)

try:
    # Create CompanyBankAccount object for thirdparty 🔐
    api_response = api_instance.thirdparties_create_company_bank_account(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_create_company_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty | 
 **body** | [**ThirdpartiesCreateCompanyBankAccountModel**](ThirdpartiesCreateCompanyBankAccountModel.md)| request_data  
 | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_create_societe_account**
> str thirdparties_create_societe_account(id, body=body)

Create and attach a new gateway to an existing thirdparty 🔐

Possible fields for request_data (request body) are specified in <code>llx_societe_account</code> table.<br> See <a href=\"https://wiki.dolibarr.org/index.php/Table_llx_societe_account\">Table llx_societe_account</a> wiki page for more information<br><br> <u>Example body payload :</u> <pre>{\"key_account\": \"cus_DAVkLSs1LYyYI\", \"site\": \"stripe\"}</pre>

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of thirdparty
body = swagger_client.ThirdpartiesCreateSocieteAccountModel() # ThirdpartiesCreateSocieteAccountModel | request_data  
 (optional)

try:
    # Create and attach a new gateway to an existing thirdparty 🔐
    api_response = api_instance.thirdparties_create_societe_account(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_create_societe_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty | 
 **body** | [**ThirdpartiesCreateSocieteAccountModel**](ThirdpartiesCreateSocieteAccountModel.md)| request_data  
 | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_generate_bank_account_document**
> str thirdparties_generate_bank_account_document(id, companybankid, model)

Generate a Document from a bank account record (like SEPA mandate) 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Thirdparty id
companybankid = 789 # int | Companybank id
model = 'model_example' # str | Model of document to generate

try:
    # Generate a Document from a bank account record (like SEPA mandate) 🔐
    api_response = api_instance.thirdparties_generate_bank_account_document(id, companybankid, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_generate_bank_account_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Thirdparty id | 
 **companybankid** | **int**| Companybank id | 
 **model** | **str**| Model of document to generate | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_merge**
> int thirdparties_merge(id, idtodelete)

Merge a thirdparty into another one. 🔐

 Merge content (properties, notes) and objects (like invoices, events, orders, proposals, ...) of a thirdparty into a target thirdparty, then delete the merged thirdparty. If a property has a defined value both in thirdparty to delete and thirdparty to keep, the value into the thirdparty to delete will be ignored, the value of target thirdparty will remain, except for notes (content is concatenated).

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of thirdparty to keep (the target thirdparty)
idtodelete = 789 # int | ID of thirdparty to remove (the thirdparty to delete), once data has been merged into the target thirdparty.

try:
    # Merge a thirdparty into another one. 🔐
    api_response = api_instance.thirdparties_merge(id, idtodelete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_merge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty to keep (the target thirdparty) | 
 **idtodelete** | **int**| ID of thirdparty to remove (the thirdparty to delete), once data has been merged into the target thirdparty. | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_modify_societe_account**
> str thirdparties_modify_societe_account(id, site, body=body)

Update specified values of a specific gateway attached to a thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of thirdparty
site = 'site_example' # str | Site key
body = swagger_client.ThirdpartiesModifySocieteAccountModel() # ThirdpartiesModifySocieteAccountModel | request_data  
 (optional)

try:
    # Update specified values of a specific gateway attached to a thirdparty 🔐
    api_response = api_instance.thirdparties_modify_societe_account(id, site, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_modify_societe_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of thirdparty | 
 **site** | **str**| Site key | 
 **body** | [**ThirdpartiesModifySocieteAccountModel**](ThirdpartiesModifySocieteAccountModel.md)| request_data  
 | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_remove_category**
> str thirdparties_remove_category(id, category_id)

Remove the link between a customer category and the thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of thirdparty
category_id = 789 # int | Id of category

try:
    # Remove the link between a customer category and the thirdparty 🔐
    api_response = api_instance.thirdparties_remove_category(id, category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_remove_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of thirdparty | 
 **category_id** | **int**| Id of category | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_remove_company_bank_account**
> int thirdparties_remove_company_bank_account(id, bankaccount_id)

Delete a bank account attached to a thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of thirdparty
bankaccount_id = 789 # int | ID of CompanyBankAccount

try:
    # Delete a bank account attached to a thirdparty 🔐
    api_response = api_instance.thirdparties_remove_company_bank_account(id, bankaccount_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_remove_company_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty | 
 **bankaccount_id** | **int**| ID of CompanyBankAccount | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_remove_societe_account**
> str thirdparties_remove_societe_account(id, site)

Delete a specific site gateway attached to a thirdparty (by gateway id) 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of thirdparty
site = 789 # int | Site key

try:
    # Delete a specific site gateway attached to a thirdparty (by gateway id) 🔐
    api_response = api_instance.thirdparties_remove_societe_account(id, site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_remove_societe_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty | 
 **site** | **int**| Site key | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_remove_societe_accounts**
> str thirdparties_remove_societe_accounts(id)

Delete all gateways attached to a thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of thirdparty

try:
    # Delete all gateways attached to a thirdparty 🔐
    api_response = api_instance.thirdparties_remove_societe_accounts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_remove_societe_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_remove_supplier_category**
> str thirdparties_remove_supplier_category(id, category_id)

Remove the link between a category and the thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of thirdparty
category_id = 789 # int | Id of category

try:
    # Remove the link between a category and the thirdparty 🔐
    api_response = api_instance.thirdparties_remove_supplier_category(id, category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_remove_supplier_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of thirdparty | 
 **category_id** | **int**| Id of category | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_by_barcode**
> str thirdparties_retrieve_by_barcode(barcode)

Get properties of a thirdparty object by barcode. 🔐

 Return an array with thirdparty informations

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
barcode = 'barcode_example' # str | Barcode of third party to load

try:
    # Get properties of a thirdparty object by barcode. 🔐
    api_response = api_instance.thirdparties_retrieve_by_barcode(barcode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_by_barcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**| Barcode of third party to load | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_by_email**
> str thirdparties_retrieve_by_email(email)

Get properties of a thirdparty object by email. 🔐

 Return an array with thirdparty informations

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
email = 'email_example' # str | Email of third party to load

try:
    # Get properties of a thirdparty object by email. 🔐
    api_response = api_instance.thirdparties_retrieve_by_email(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_by_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of third party to load | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_categories**
> str thirdparties_retrieve_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)

Get customer categories for a thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of thirdparty
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)

try:
    # Get customer categories for a thirdparty 🔐
    api_response = api_instance.thirdparties_retrieve_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty | 
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

# **thirdparties_retrieve_company_bank_account**
> list[str] thirdparties_retrieve_company_bank_account(id)

Get CompanyBankAccount objects for thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of thirdparty

try:
    # Get CompanyBankAccount objects for thirdparty 🔐
    api_response = api_instance.thirdparties_retrieve_company_bank_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_company_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_fixed_amount_discounts**
> list[str] thirdparties_retrieve_fixed_amount_discounts(id, filter=filter, sortfield=sortfield, sortorder=sortorder)

Get fixed amount discount of a thirdparty (all sources: deposit, credit note, commercial offers...) 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of the thirdparty
filter = 'filter_example' # str | Filter exceptional discount. \"none\" will return every discount, \"available\" returns unapplied discounts, \"used\" returns applied discounts (optional)
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)

try:
    # Get fixed amount discount of a thirdparty (all sources: deposit, credit note, commercial offers...) 🔐
    api_response = api_instance.thirdparties_retrieve_fixed_amount_discounts(id, filter=filter, sortfield=sortfield, sortorder=sortorder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_fixed_amount_discounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the thirdparty | 
 **filter** | **str**| Filter exceptional discount. \&quot;none\&quot; will return every discount, \&quot;available\&quot; returns unapplied discounts, \&quot;used\&quot; returns applied discounts | [optional] 
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_invoices_qualified_for_credit_note**
> list[str] thirdparties_retrieve_invoices_qualified_for_credit_note(id)

Return list of invoices qualified to be corrected by a credit note. 🔐

Invoices matching the following rules are returned (validated + payment on process) or classified (paid completely or paid partialy) + not already replaced + not already a credit note

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of thirdparty

try:
    # Return list of invoices qualified to be corrected by a credit note. 🔐
    api_response = api_instance.thirdparties_retrieve_invoices_qualified_for_credit_note(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_invoices_qualified_for_credit_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of thirdparty | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_invoices_qualified_for_replacement**
> list[str] thirdparties_retrieve_invoices_qualified_for_replacement(id)

Return list of invoices qualified to be replaced by another invoice. 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of thirdparty

try:
    # Return list of invoices qualified to be replaced by another invoice. 🔐
    api_response = api_instance.thirdparties_retrieve_invoices_qualified_for_replacement(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_invoices_qualified_for_replacement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of thirdparty | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_out_standing_invoices**
> list[str] thirdparties_retrieve_out_standing_invoices(id, mode=mode)

Get outstanding invoices of thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of the thirdparty
mode = 'mode_example' # str | 'customer' or 'supplier' (optional)

try:
    # Get outstanding invoices of thirdparty 🔐
    api_response = api_instance.thirdparties_retrieve_out_standing_invoices(id, mode=mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_out_standing_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the thirdparty | 
 **mode** | **str**| &#x27;customer&#x27; or &#x27;supplier&#x27; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_out_standing_order**
> list[str] thirdparties_retrieve_out_standing_order(id, mode=mode)

Get outstanding orders of thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of the thirdparty
mode = 'mode_example' # str | 'customer' or 'supplier' (optional)

try:
    # Get outstanding orders of thirdparty 🔐
    api_response = api_instance.thirdparties_retrieve_out_standing_order(id, mode=mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_out_standing_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the thirdparty | 
 **mode** | **str**| &#x27;customer&#x27; or &#x27;supplier&#x27; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_out_standing_proposals**
> list[str] thirdparties_retrieve_out_standing_proposals(id, mode=mode)

Get outstanding proposals of thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of the thirdparty
mode = 'mode_example' # str | 'customer' or 'supplier' (optional)

try:
    # Get outstanding proposals of thirdparty 🔐
    api_response = api_instance.thirdparties_retrieve_out_standing_proposals(id, mode=mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_out_standing_proposals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the thirdparty | 
 **mode** | **str**| &#x27;customer&#x27; or &#x27;supplier&#x27; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_sales_representatives**
> list[str] thirdparties_retrieve_sales_representatives(id, mode=mode)

Get representatives of thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of the thirdparty
mode = 'mode_example' # str | 0=Array with properties, 1=Array of id. (optional)

try:
    # Get representatives of thirdparty 🔐
    api_response = api_instance.thirdparties_retrieve_sales_representatives(id, mode=mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_sales_representatives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the thirdparty | 
 **mode** | **str**| 0&#x3D;Array with properties, 1&#x3D;Array of id. | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_societe_accounts**
> str thirdparties_retrieve_societe_accounts(id, site=site)

Get a specific gateway attached to a thirdparty (by specifying the site key) 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of thirdparty
site = 'site_example' # str | Site key (optional)

try:
    # Get a specific gateway attached to a thirdparty (by specifying the site key) 🔐
    api_response = api_instance.thirdparties_retrieve_societe_accounts(id, site=site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_societe_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty | 
 **site** | **str**| Site key | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_supplier_categories**
> str thirdparties_retrieve_supplier_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)

Get supplier categories for a thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of thirdparty
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)

try:
    # Get supplier categories for a thirdparty 🔐
    api_response = api_instance.thirdparties_retrieve_supplier_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_supplier_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty | 
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

# **thirdparties_set_thirdparty_price_level**
> str thirdparties_set_thirdparty_price_level(body, id)

Set new price level for the given thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ThirdpartiesSetThirdpartyPriceLevelModel() # ThirdpartiesSetThirdpartyPriceLevelModel | **priceLevel** (required)  

id = 789 # int | ID of thirdparty

try:
    # Set new price level for the given thirdparty 🔐
    api_response = api_instance.thirdparties_set_thirdparty_price_level(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_set_thirdparty_price_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThirdpartiesSetThirdpartyPriceLevelModel**](ThirdpartiesSetThirdpartyPriceLevelModel.md)| **priceLevel** (required)  
 | 
 **id** | **int**| ID of thirdparty | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_update_company_bank_account**
> str thirdparties_update_company_bank_account(id, bankaccount_id, body=body)

Update CompanyBankAccount object for thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of thirdparty
bankaccount_id = 789 # int | ID of CompanyBankAccount
body = swagger_client.ThirdpartiesUpdateCompanyBankAccountModel() # ThirdpartiesUpdateCompanyBankAccountModel | request_data  
 (optional)

try:
    # Update CompanyBankAccount object for thirdparty 🔐
    api_response = api_instance.thirdparties_update_company_bank_account(id, bankaccount_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_update_company_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty | 
 **bankaccount_id** | **int**| ID of CompanyBankAccount | 
 **body** | [**ThirdpartiesUpdateCompanyBankAccountModel**](ThirdpartiesUpdateCompanyBankAccountModel.md)| request_data  
 | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_update_societe_account**
> str thirdparties_update_societe_account(id, site, body=body)

Create and attach a new (or replace an existing) specific site gateway to a thirdparty 🔐

You <strong>MUST</strong> pass all values to keep (otherwise, they will be deleted) !<br> If you just need to update specific fields prefer <code>PATCH /thirdparties/{id}/gateways/{site}</code> endpoint.<br><br> When a <strong>SocieteAccount</strong> entity does not exist for the <code>id</code> and <code>site</code> supplied, a new one will be created. In that case <code>fk_soc</code> and <code>site</code> members form request body payload will be ignored and <code>id</code> and <code>site</code> query strings parameters will be used instead.

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of thirdparty
site = 'site_example' # str | Site key
body = swagger_client.ThirdpartiesUpdateSocieteAccountModel() # ThirdpartiesUpdateSocieteAccountModel | request_data  
 (optional)

try:
    # Create and attach a new (or replace an existing) specific site gateway to a thirdparty 🔐
    api_response = api_instance.thirdparties_update_societe_account(id, site, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->thirdparties_update_societe_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty | 
 **site** | **str**| Site key | 
 **body** | [**ThirdpartiesUpdateSocieteAccountModel**](ThirdpartiesUpdateSocieteAccountModel.md)| request_data  
 | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_thirdparties**
> str update_thirdparties(id, body=body)

Update thirdparty 🔐

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
api_instance = swagger_client.ThirdpartiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of thirdparty to update
body = swagger_client.UpdateThirdpartiesModel() # UpdateThirdpartiesModel | request_data  
 (optional)

try:
    # Update thirdparty 🔐
    api_response = api_instance.update_thirdparties(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdpartiesApi->update_thirdparties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of thirdparty to update | 
 **body** | [**UpdateThirdpartiesModel**](UpdateThirdpartiesModel.md)| request_data  
 | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

