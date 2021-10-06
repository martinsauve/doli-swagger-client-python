# swagger_client.InvoicesApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invoices**](InvoicesApi.md#create_invoices) | **POST** /invoices | Create invoice object 🔐
[**invoices_add_contact**](InvoicesApi.md#invoices_add_contact) | **POST** /invoices/{id}/contacts | Adds a contact to an invoice 🔐
[**invoices_add_payment**](InvoicesApi.md#invoices_add_payment) | **POST** /invoices/{id}/payments | Add payment line to a specific invoice with the remain to pay as amount. 🔐
[**invoices_add_payment_distributed**](InvoicesApi.md#invoices_add_payment_distributed) | **POST** /invoices/paymentsdistributed | Add a payment to pay partially or completely one or several invoices. 🔐
[**invoices_create_contact**](InvoicesApi.md#invoices_create_contact) | **POST** /invoices/{id}/contact/{contactid}/{type} | Add a contact type of given invoice 🔐
[**invoices_create_invoice_from_order**](InvoicesApi.md#invoices_create_invoice_from_order) | **POST** /invoices/createfromorder/{orderid} | Create an invoice using an existing order. 🔐
[**invoices_create_line**](InvoicesApi.md#invoices_create_line) | **POST** /invoices/{id}/lines | Add a line to a given invoice 🔐
[**invoices_mark_as_credit_available**](InvoicesApi.md#invoices_mark_as_credit_available) | **POST** /invoices/{id}/markAsCreditAvailable | Create a discount (credit available) for a credit note or a deposit. 🔐
[**invoices_remove_contact**](InvoicesApi.md#invoices_remove_contact) | **DELETE** /invoices/{id}/contact/{contactid}/{type} | Delete a contact type of given invoice 🔐
[**invoices_remove_line**](InvoicesApi.md#invoices_remove_line) | **DELETE** /invoices/{id}/lines/{lineid} | Deletes a line of a given invoice 🔐
[**invoices_retrieve_by_ref**](InvoicesApi.md#invoices_retrieve_by_ref) | **GET** /invoices/ref/{ref} | Get properties of an invoice object by ref 🔐
[**invoices_retrieve_by_ref_ext**](InvoicesApi.md#invoices_retrieve_by_ref_ext) | **GET** /invoices/ref_ext/{ref_ext} | Get properties of an invoice object by ref_ext 🔐
[**invoices_retrieve_discount**](InvoicesApi.md#invoices_retrieve_discount) | **GET** /invoices/{id}/discount | Get discount from invoice 🔐
[**invoices_retrieve_lines**](InvoicesApi.md#invoices_retrieve_lines) | **GET** /invoices/{id}/lines | Get lines of an invoice 🔐
[**invoices_retrieve_payments**](InvoicesApi.md#invoices_retrieve_payments) | **GET** /invoices/{id}/payments | Get list of payments of a given invoice 🔐
[**invoices_settodraft**](InvoicesApi.md#invoices_settodraft) | **POST** /invoices/{id}/settodraft | Sets an invoice as draft 🔐
[**invoices_settopaid**](InvoicesApi.md#invoices_settopaid) | **POST** /invoices/{id}/settopaid | Sets an invoice as paid 🔐
[**invoices_settounpaid**](InvoicesApi.md#invoices_settounpaid) | **POST** /invoices/{id}/settounpaid | Sets an invoice as unpaid 🔐
[**invoices_update_line**](InvoicesApi.md#invoices_update_line) | **PUT** /invoices/{id}/lines/{lineid} | Update a line to a given invoice 🔐
[**invoices_update_payment**](InvoicesApi.md#invoices_update_payment) | **PUT** /invoices/payments/{id} | Update a payment 🔐
[**invoices_use_credit_note**](InvoicesApi.md#invoices_use_credit_note) | **POST** /invoices/{id}/usecreditnote/{discountid} | Add an available credit note discount to payments of an existing invoice. 🔐
[**invoices_use_discount**](InvoicesApi.md#invoices_use_discount) | **POST** /invoices/{id}/usediscount/{discountid} | Add a discount line into an invoice (as an invoice line) using an existing absolute discount 🔐
[**invoices_validate**](InvoicesApi.md#invoices_validate) | **POST** /invoices/{id}/validate | Validate an invoice 🔐
[**list_invoices**](InvoicesApi.md#list_invoices) | **GET** /invoices | List invoices 🔐
[**remove_invoices**](InvoicesApi.md#remove_invoices) | **DELETE** /invoices/{id} | Delete invoice 🔐
[**retrieve_invoices**](InvoicesApi.md#retrieve_invoices) | **GET** /invoices/{id} | Get properties of a invoice object 🔐
[**update_invoices**](InvoicesApi.md#update_invoices) | **PUT** /invoices/{id} | Update invoice 🔐

# **create_invoices**
> int create_invoices(body=body)

Create invoice object 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateInvoicesModel() # CreateInvoicesModel | request_data  
 (optional)

try:
    # Create invoice object 🔐
    api_response = api_instance.create_invoices(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->create_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateInvoicesModel**](CreateInvoicesModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_add_contact**
> list[str] invoices_add_contact(body, id)

Adds a contact to an invoice 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.InvoicesAddContactModel() # InvoicesAddContactModel | **fk_socpeople** (required)  
**type_contact** (required)  
**source** (required)  
notrigger  

id = 789 # int | Order ID

try:
    # Adds a contact to an invoice 🔐
    api_response = api_instance.invoices_add_contact(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_add_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoicesAddContactModel**](InvoicesAddContactModel.md)| **fk_socpeople** (required)  
**type_contact** (required)  
**source** (required)  
notrigger  
 | 
 **id** | **int**| Order ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_add_payment**
> int invoices_add_payment(body, id)

Add payment line to a specific invoice with the remain to pay as amount. 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.InvoicesAddPaymentModel() # InvoicesAddPaymentModel | **datepaye** (required)  
**paymentid** (required)  
**closepaidinvoices** (required)  
**accountid** (required)  
num_payment  
comment  
chqemetteur  
chqbank  

id = 789 # int | Id of invoice

try:
    # Add payment line to a specific invoice with the remain to pay as amount. 🔐
    api_response = api_instance.invoices_add_payment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_add_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoicesAddPaymentModel**](InvoicesAddPaymentModel.md)| **datepaye** (required)  
**paymentid** (required)  
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

# **invoices_add_payment_distributed**
> int invoices_add_payment_distributed(body)

Add a payment to pay partially or completely one or several invoices. 🔐

Warning: Take care that all invoices are owned by the same customer. Example of value for parameter arrayofamounts: {\"1\": {\"amount\": \"99.99\", \"multicurrency_amount\": \"\"}, \"2\": {\"amount\": \"\", \"multicurrency_amount\": \"10\"}}

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.InvoicesAddPaymentDistributedModel() # InvoicesAddPaymentDistributedModel | **arrayofamounts** (required)  
**datepaye** (required)  
**paymentid** (required)  
**closepaidinvoices** (required)  
**accountid** (required)  
num_payment  
comment  
chqemetteur  
chqbank  
ref_ext  
accepthigherpayment  


try:
    # Add a payment to pay partially or completely one or several invoices. 🔐
    api_response = api_instance.invoices_add_payment_distributed(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_add_payment_distributed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoicesAddPaymentDistributedModel**](InvoicesAddPaymentDistributedModel.md)| **arrayofamounts** (required)  
**datepaye** (required)  
**paymentid** (required)  
**closepaidinvoices** (required)  
**accountid** (required)  
num_payment  
comment  
chqemetteur  
chqbank  
ref_ext  
accepthigherpayment  
 | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_create_contact**
> int invoices_create_contact(id, contactid, type)

Add a contact type of given invoice 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of invoice to update
contactid = 789 # int | Id of contact to add
type = 'type_example' # str | Type of the contact (BILLING, SHIPPING, CUSTOMER)

try:
    # Add a contact type of given invoice 🔐
    api_response = api_instance.invoices_create_contact(id, contactid, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of invoice to update | 
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

# **invoices_create_invoice_from_order**
> int invoices_create_invoice_from_order(orderid)

Create an invoice using an existing order. 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
orderid = 789 # int | Id of the order

try:
    # Create an invoice using an existing order. 🔐
    api_response = api_instance.invoices_create_invoice_from_order(orderid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_create_invoice_from_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderid** | **int**| Id of the order | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_create_line**
> int invoices_create_line(id, body=body)

Add a line to a given invoice 🔐

Exemple of POST query : { \"desc\": \"Desc\", \"subprice\": \"1.00000000\", \"qty\": \"1\", \"tva_tx\": \"20.000\", \"localtax1_tx\": \"0.000\", \"localtax2_tx\": \"0.000\", \"fk_product\": \"1\", \"remise_percent\": \"0\", \"date_start\": \"\", \"date_end\": \"\", \"fk_code_ventilation\": 0, \"info_bits\": \"0\", \"fk_remise_except\": null, \"product_type\": \"1\", \"rang\": \"-1\", \"special_code\": \"0\", \"fk_parent_line\": null, \"fk_fournprice\": null, \"pa_ht\": \"0.00000000\", \"label\": \"\", \"array_options\": [], \"situation_percent\": \"100\", \"fk_prev_id\": null, \"fk_unit\": null }

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of invoice
body = swagger_client.InvoicesCreateLineModel() # InvoicesCreateLineModel | request_data  
 (optional)

try:
    # Add a line to a given invoice 🔐
    api_response = api_instance.invoices_create_line(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_create_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of invoice | 
 **body** | [**InvoicesCreateLineModel**](InvoicesCreateLineModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_mark_as_credit_available**
> list[str] invoices_mark_as_credit_available(id)

Create a discount (credit available) for a credit note or a deposit. 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Invoice ID

try:
    # Create a discount (credit available) for a credit note or a deposit. 🔐
    api_response = api_instance.invoices_mark_as_credit_available(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_mark_as_credit_available: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Invoice ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_remove_contact**
> list[str] invoices_remove_contact(id, contactid, type)

Delete a contact type of given invoice 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of invoice to update
contactid = 789 # int | Row key of the contact in the array contact_ids.
type = 'type_example' # str | Type of the contact (BILLING, SHIPPING, CUSTOMER).

try:
    # Delete a contact type of given invoice 🔐
    api_response = api_instance.invoices_remove_contact(id, contactid, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_remove_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of invoice to update | 
 **contactid** | **int**| Row key of the contact in the array contact_ids. | 
 **type** | **str**| Type of the contact (BILLING, SHIPPING, CUSTOMER). | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_remove_line**
> list[str] invoices_remove_line(id, lineid)

Deletes a line of a given invoice 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of invoice
lineid = 789 # int | Id of the line to delete

try:
    # Deletes a line of a given invoice 🔐
    api_response = api_instance.invoices_remove_line(id, lineid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_remove_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of invoice | 
 **lineid** | **int**| Id of the line to delete | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_retrieve_by_ref**
> str invoices_retrieve_by_ref(ref, contact_list=contact_list)

Get properties of an invoice object by ref 🔐

Return an array with invoice informations

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
ref = 'ref_example' # str | Ref of object
contact_list = 789 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id (optional)

try:
    # Get properties of an invoice object by ref 🔐
    api_response = api_instance.invoices_retrieve_by_ref(ref, contact_list=contact_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_retrieve_by_ref: %s\n" % e)
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

# **invoices_retrieve_by_ref_ext**
> str invoices_retrieve_by_ref_ext(ref_ext, contact_list=contact_list)

Get properties of an invoice object by ref_ext 🔐

Return an array with invoice informations

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
ref_ext = 'ref_ext_example' # str | External reference of object
contact_list = 789 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id (optional)

try:
    # Get properties of an invoice object by ref_ext 🔐
    api_response = api_instance.invoices_retrieve_by_ref_ext(ref_ext, contact_list=contact_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_retrieve_by_ref_ext: %s\n" % e)
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

# **invoices_retrieve_discount**
> str invoices_retrieve_discount(id)

Get discount from invoice 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of invoice

try:
    # Get discount from invoice 🔐
    api_response = api_instance.invoices_retrieve_discount(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_retrieve_discount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of invoice | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_retrieve_lines**
> int invoices_retrieve_lines(id)

Get lines of an invoice 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of invoice

try:
    # Get lines of an invoice 🔐
    api_response = api_instance.invoices_retrieve_lines(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_retrieve_lines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of invoice | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_retrieve_payments**
> list[str] invoices_retrieve_payments(id)

Get list of payments of a given invoice 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of invoice

try:
    # Get list of payments of a given invoice 🔐
    api_response = api_instance.invoices_retrieve_payments(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_retrieve_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of invoice | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_settodraft**
> list[str] invoices_settodraft(id, body=body)

Sets an invoice as draft 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Order ID
body = swagger_client.InvoicesSettodraftModel() # InvoicesSettodraftModel | idwarehouse  
 (optional)

try:
    # Sets an invoice as draft 🔐
    api_response = api_instance.invoices_settodraft(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_settodraft: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **body** | [**InvoicesSettodraftModel**](InvoicesSettodraftModel.md)| idwarehouse  
 | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_settopaid**
> list[str] invoices_settopaid(id, body=body)

Sets an invoice as paid 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Order ID
body = swagger_client.InvoicesSettopaidModel() # InvoicesSettopaidModel | close_code  
close_note  
 (optional)

try:
    # Sets an invoice as paid 🔐
    api_response = api_instance.invoices_settopaid(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_settopaid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **body** | [**InvoicesSettopaidModel**](InvoicesSettopaidModel.md)| close_code  
close_note  
 | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_settounpaid**
> list[str] invoices_settounpaid(id)

Sets an invoice as unpaid 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Order ID

try:
    # Sets an invoice as unpaid 🔐
    api_response = api_instance.invoices_settounpaid(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_settounpaid: %s\n" % e)
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

# **invoices_update_line**
> list[str] invoices_update_line(id, lineid, body=body)

Update a line to a given invoice 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of invoice to update
lineid = 789 # int | Id of line to update
body = swagger_client.InvoicesUpdateLineModel() # InvoicesUpdateLineModel | request_data  
 (optional)

try:
    # Update a line to a given invoice 🔐
    api_response = api_instance.invoices_update_line(id, lineid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_update_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of invoice to update | 
 **lineid** | **int**| Id of line to update | 
 **body** | [**InvoicesUpdateLineModel**](InvoicesUpdateLineModel.md)| request_data  
 | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_update_payment**
> list[str] invoices_update_payment(id, body=body)

Update a payment 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of payment
body = swagger_client.InvoicesUpdatePaymentModel() # InvoicesUpdatePaymentModel | num_payment  
 (optional)

try:
    # Update a payment 🔐
    api_response = api_instance.invoices_update_payment(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_update_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of payment | 
 **body** | [**InvoicesUpdatePaymentModel**](InvoicesUpdatePaymentModel.md)| num_payment  
 | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_use_credit_note**
> int invoices_use_credit_note(id, discountid)

Add an available credit note discount to payments of an existing invoice. 🔐

 Note that this consume the credit note.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of invoice
discountid = 789 # int | Id of a discount coming from a credit note

try:
    # Add an available credit note discount to payments of an existing invoice. 🔐
    api_response = api_instance.invoices_use_credit_note(id, discountid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_use_credit_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of invoice | 
 **discountid** | **int**| Id of a discount coming from a credit note | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_use_discount**
> int invoices_use_discount(id, discountid)

Add a discount line into an invoice (as an invoice line) using an existing absolute discount 🔐

Note that this consume the discount.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of invoice
discountid = 789 # int | Id of discount

try:
    # Add a discount line into an invoice (as an invoice line) using an existing absolute discount 🔐
    api_response = api_instance.invoices_use_discount(id, discountid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_use_discount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of invoice | 
 **discountid** | **int**| Id of discount | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_validate**
> list[str] invoices_validate(id, body=body)

Validate an invoice 🔐

If you get a bad value for param notrigger check that ou provide this in body { \"idwarehouse\": 0, \"notrigger\": 0 }

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Invoice ID
body = swagger_client.InvoicesValidateModel() # InvoicesValidateModel | idwarehouse  
notrigger  
 (optional)

try:
    # Validate an invoice 🔐
    api_response = api_instance.invoices_validate(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Invoice ID | 
 **body** | [**InvoicesValidateModel**](InvoicesValidateModel.md)| idwarehouse  
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

# **list_invoices**
> list[str] list_invoices(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, status=status, sqlfilters=sqlfilters)

List invoices 🔐

Get a list of invoices

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter orders of (example '1' or '1,2,3') (optional)
status = 'status_example' # str | Filter by invoice status : draft | unpaid | paid | cancelled (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)

try:
    # List invoices 🔐
    api_response = api_instance.list_invoices(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, status=status, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->list_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Thirdparty ids to filter orders of (example &#x27;1&#x27; or &#x27;1,2,3&#x27;) | [optional] 
 **status** | **str**| Filter by invoice status : draft | unpaid | paid | cancelled | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#x27;SO-%&#x27;) and (t.date_creation:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_invoices**
> list[str] remove_invoices(id)

Delete invoice 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Invoice ID

try:
    # Delete invoice 🔐
    api_response = api_instance.remove_invoices(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->remove_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Invoice ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_invoices**
> str retrieve_invoices(id, contact_list=contact_list)

Get properties of a invoice object 🔐

Return an array with invoice informations

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of invoice
contact_list = 789 # int | 0:Return array contains all properties, 1:Return array contains just id (optional)

try:
    # Get properties of a invoice object 🔐
    api_response = api_instance.retrieve_invoices(id, contact_list=contact_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->retrieve_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of invoice | 
 **contact_list** | **int**| 0:Return array contains all properties, 1:Return array contains just id | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoices**
> int update_invoices(id, body=body)

Update invoice 🔐

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of invoice to update
body = swagger_client.UpdateInvoicesModel() # UpdateInvoicesModel | request_data  
 (optional)

try:
    # Update invoice 🔐
    api_response = api_instance.update_invoices(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->update_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of invoice to update | 
 **body** | [**UpdateInvoicesModel**](UpdateInvoicesModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

