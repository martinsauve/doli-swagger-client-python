# swagger_client.SetupApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setup_retrieve_availability**](SetupApi.md#setup_retrieve_availability) | **GET** /setup/dictionary/availability | Get the list of delivery times. 🔐
[**setup_retrieve_check_integrity**](SetupApi.md#setup_retrieve_check_integrity) | **GET** /setup/checkintegrity | Do a test of integrity for files and setup. 🔐
[**setup_retrieve_company**](SetupApi.md#setup_retrieve_company) | **GET** /setup/company | Get properties of company 🔐
[**setup_retrieve_conf**](SetupApi.md#setup_retrieve_conf) | **GET** /setup/conf/{constantname} | Get value of a setup variables 🔐
[**setup_retrieve_country_by_code**](SetupApi.md#setup_retrieve_country_by_code) | **GET** /setup/dictionary/countries/byCode/{code} | Get country by Code. 🔐
[**setup_retrieve_country_by_id**](SetupApi.md#setup_retrieve_country_by_id) | **GET** /setup/dictionary/countries/{id} | Get country by ID. 🔐
[**setup_retrieve_country_by_iso**](SetupApi.md#setup_retrieve_country_by_iso) | **GET** /setup/dictionary/countries/byISO/{iso} | Get country by Iso. 🔐
[**setup_retrieve_list_of_civilities**](SetupApi.md#setup_retrieve_list_of_civilities) | **GET** /setup/dictionary/civilities | Get the list of civilities. 🔐
[**setup_retrieve_list_of_contact_types**](SetupApi.md#setup_retrieve_list_of_contact_types) | **GET** /setup/dictionary/contact_types | Get the list of contacts types. 🔐
[**setup_retrieve_list_of_countries**](SetupApi.md#setup_retrieve_list_of_countries) | **GET** /setup/dictionary/countries | Get the list of countries. 🔐
[**setup_retrieve_list_of_currencies**](SetupApi.md#setup_retrieve_list_of_currencies) | **GET** /setup/dictionary/currencies | Get the list of currencies. 🔐
[**setup_retrieve_list_of_event_types**](SetupApi.md#setup_retrieve_list_of_event_types) | **GET** /setup/dictionary/event_types | Get the list of events types. 🔐
[**setup_retrieve_list_of_expense_reports_types**](SetupApi.md#setup_retrieve_list_of_expense_reports_types) | **GET** /setup/dictionary/expensereport_types | Get the list of Expense Report types. 🔐
[**setup_retrieve_list_of_extrafields**](SetupApi.md#setup_retrieve_list_of_extrafields) | **GET** /setup/extrafields | Get the list of extra fields. 🔐
[**setup_retrieve_list_of_measuring_units**](SetupApi.md#setup_retrieve_list_of_measuring_units) | **GET** /setup/dictionary/units | Get the list of measuring units. 🔐
[**setup_retrieve_list_of_states**](SetupApi.md#setup_retrieve_list_of_states) | **GET** /setup/dictionary/states | Get the list of states/provinces. 🔐
[**setup_retrieve_list_of_towns**](SetupApi.md#setup_retrieve_list_of_towns) | **GET** /setup/dictionary/towns | Get the list of towns. 🔐
[**setup_retrieve_list_ofsocial_networks**](SetupApi.md#setup_retrieve_list_ofsocial_networks) | **GET** /setup/dictionary/socialnetworks | Get the list of social networks. 🔐
[**setup_retrieve_modules**](SetupApi.md#setup_retrieve_modules) | **GET** /setup/modules | Get list of enabled modules 🔐
[**setup_retrieve_ordering_methods**](SetupApi.md#setup_retrieve_ordering_methods) | **GET** /setup/dictionary/ordering_methods | Get the list of ordering methods. 🔐
[**setup_retrieve_ordering_origins**](SetupApi.md#setup_retrieve_ordering_origins) | **GET** /setup/dictionary/ordering_origins | Get the list of ordering origins. 🔐
[**setup_retrieve_payment_terms**](SetupApi.md#setup_retrieve_payment_terms) | **GET** /setup/dictionary/payment_terms | Get the list of payments terms. 🔐
[**setup_retrieve_payment_types**](SetupApi.md#setup_retrieve_payment_types) | **GET** /setup/dictionary/payment_types | Get the list of payments types. 🔐
[**setup_retrieve_shipping_modes**](SetupApi.md#setup_retrieve_shipping_modes) | **GET** /setup/dictionary/shipping_methods | Get the list of shipping methods. 🔐
[**setup_retrieve_state_by_code**](SetupApi.md#setup_retrieve_state_by_code) | **GET** /setup/dictionary/states/byCode/{code} | Get state by Code. 🔐
[**setup_retrieve_state_by_id**](SetupApi.md#setup_retrieve_state_by_id) | **GET** /setup/dictionary/states/{id} | Get state by ID. 🔐
[**setup_retrieve_tickets_categories**](SetupApi.md#setup_retrieve_tickets_categories) | **GET** /setup/dictionary/ticket_categories | Get the list of tickets categories. 🔐
[**setup_retrieve_tickets_severities**](SetupApi.md#setup_retrieve_tickets_severities) | **GET** /setup/dictionary/ticket_severities | Get the list of tickets severity. 🔐
[**setup_retrieve_tickets_types**](SetupApi.md#setup_retrieve_tickets_types) | **GET** /setup/dictionary/ticket_types | Get the list of tickets types. 🔐

# **setup_retrieve_availability**
> list[str] setup_retrieve_availability(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of delivery times. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (optional)
active = 789 # int | Delivery times is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | SQL criteria to filter with. (optional)

try:
    # Get the list of delivery times. 🔐
    api_response = api_instance.setup_retrieve_availability(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_availability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number | [optional] 
 **active** | **int**| Delivery times is active or not | [optional] 
 **sqlfilters** | **str**| SQL criteria to filter with. | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_check_integrity**
> list[str] setup_retrieve_check_integrity(target)

Do a test of integrity for files and setup. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
target = 'target_example' # str | Can be 'local' or 'default' or Url of the signatures file to use for the test. Must be reachable by the tested Dolibarr.

try:
    # Do a test of integrity for files and setup. 🔐
    api_response = api_instance.setup_retrieve_check_integrity(target)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_check_integrity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| Can be &#x27;local&#x27; or &#x27;default&#x27; or Url of the signatures file to use for the test. Must be reachable by the tested Dolibarr. | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_company**
> str setup_retrieve_company()

Get properties of company 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))

try:
    # Get properties of company 🔐
    api_response = api_instance.setup_retrieve_company()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_company: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_conf**
> str setup_retrieve_conf(constantname)

Get value of a setup variables 🔐

Note that conf variables that stores security key or password hashes can't be loaded with API.

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
constantname = 'constantname_example' # str | Name of conf variable to get

try:
    # Get value of a setup variables 🔐
    api_response = api_instance.setup_retrieve_conf(constantname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_conf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **constantname** | **str**| Name of conf variable to get | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_country_by_code**
> list[str] setup_retrieve_country_by_code(code, lang=lang)

Get country by Code. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | Code of country (2 characters)
lang = 'lang_example' # str | Code of the language the name of the country must be translated to (optional)

try:
    # Get country by Code. 🔐
    api_response = api_instance.setup_retrieve_country_by_code(code, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_country_by_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of country (2 characters) | 
 **lang** | **str**| Code of the language the name of the country must be translated to | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_country_by_id**
> list[str] setup_retrieve_country_by_id(id, lang=lang)

Get country by ID. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of country
lang = 'lang_example' # str | Code of the language the name of the country must be translated to (optional)

try:
    # Get country by ID. 🔐
    api_response = api_instance.setup_retrieve_country_by_id(id, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_country_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of country | 
 **lang** | **str**| Code of the language the name of the country must be translated to | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_country_by_iso**
> list[str] setup_retrieve_country_by_iso(iso, lang=lang)

Get country by Iso. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
iso = 'iso_example' # str | ISO of country (3 characters)
lang = 'lang_example' # str | Code of the language the name of the country must be translated to (optional)

try:
    # Get country by Iso. 🔐
    api_response = api_instance.setup_retrieve_country_by_iso(iso, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_country_by_iso: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iso** | **str**| ISO of country (3 characters) | 
 **lang** | **str**| Code of the language the name of the country must be translated to | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_civilities**
> list[str] setup_retrieve_list_of_civilities(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, module=module, active=active, sqlfilters=sqlfilters)

Get the list of civilities. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (starting from zero) (optional)
module = 'module_example' # str | To filter on module events (optional)
active = 789 # int | Civility is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

try:
    # Get the list of civilities. 🔐
    api_response = api_instance.setup_retrieve_list_of_civilities(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, module=module, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_list_of_civilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **module** | **str**| To filter on module events | [optional] 
 **active** | **int**| Civility is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#x27;A%&#x27;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_contact_types**
> list[str] setup_retrieve_list_of_contact_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, type=type, module=module, active=active, sqlfilters=sqlfilters)

Get the list of contacts types. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (starting from zero) (optional)
type = 'type_example' # str | To filter on type of contact (optional)
module = 'module_example' # str | To filter on module contacts (optional)
active = 789 # int | Contact's type is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

try:
    # Get the list of contacts types. 🔐
    api_response = api_instance.setup_retrieve_list_of_contact_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, type=type, module=module, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_list_of_contact_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **type** | **str**| To filter on type of contact | [optional] 
 **module** | **str**| To filter on module contacts | [optional] 
 **active** | **int**| Contact&#x27;s type is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#x27;A%&#x27;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_countries**
> list[str] setup_retrieve_list_of_countries(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, filter=filter, lang=lang, sqlfilters=sqlfilters)

Get the list of countries. 🔐

 The names of the countries will be translated to the given language if the $lang parameter is provided. The value of $lang must be a language code supported by Dolibarr, for example 'en_US' or 'fr_FR'. The returned list is sorted by country ID.

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (starting from zero) (optional)
filter = 'filter_example' # str | To filter the countries by name (optional)
lang = 'lang_example' # str | Code of the language the label of the countries must be translated to (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

try:
    # Get the list of countries. 🔐
    api_response = api_instance.setup_retrieve_list_of_countries(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, filter=filter, lang=lang, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_list_of_countries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **filter** | **str**| To filter the countries by name | [optional] 
 **lang** | **str**| Code of the language the label of the countries must be translated to | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#x27;A%&#x27;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_currencies**
> list[str] setup_retrieve_list_of_currencies(multicurrency=multicurrency, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of currencies. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
multicurrency = 789 # int | Multicurrency rates (0: no multicurrency, 1: last rate, 2: all rates) (optional)
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (starting from zero) (optional)
active = 789 # int | Payment term is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

try:
    # Get the list of currencies. 🔐
    api_response = api_instance.setup_retrieve_list_of_currencies(multicurrency=multicurrency, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_list_of_currencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multicurrency** | **int**| Multicurrency rates (0: no multicurrency, 1: last rate, 2: all rates) | [optional] 
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **active** | **int**| Payment term is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#x27;A%&#x27;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_event_types**
> list[str] setup_retrieve_list_of_event_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, type=type, module=module, active=active, sqlfilters=sqlfilters)

Get the list of events types. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (starting from zero) (optional)
type = 'type_example' # str | To filter on type of event (optional)
module = 'module_example' # str | To filter on module events (optional)
active = 789 # int | Event's type is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

try:
    # Get the list of events types. 🔐
    api_response = api_instance.setup_retrieve_list_of_event_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, type=type, module=module, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_list_of_event_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **type** | **str**| To filter on type of event | [optional] 
 **module** | **str**| To filter on module events | [optional] 
 **active** | **int**| Event&#x27;s type is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#x27;A%&#x27;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_expense_reports_types**
> list[str] setup_retrieve_list_of_expense_reports_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, module=module, active=active, sqlfilters=sqlfilters)

Get the list of Expense Report types. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (starting from zero) (optional)
module = 'module_example' # str | To filter on module (optional)
active = 789 # int | Event's type is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

try:
    # Get the list of Expense Report types. 🔐
    api_response = api_instance.setup_retrieve_list_of_expense_reports_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, module=module, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_list_of_expense_reports_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **module** | **str**| To filter on module | [optional] 
 **active** | **int**| Event&#x27;s type is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#x27;A%&#x27;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_extrafields**
> list[str] setup_retrieve_list_of_extrafields(sortfield=sortfield, sortorder=sortorder, type=type, sqlfilters=sqlfilters)

Get the list of extra fields. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
type = 'type_example' # str | Type of element ('adherent', 'commande', 'thirdparty', 'facture', 'propal', 'product', ...) (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.label:like:'SO-%')\" (optional)

try:
    # Get the list of extra fields. 🔐
    api_response = api_instance.setup_retrieve_list_of_extrafields(sortfield=sortfield, sortorder=sortorder, type=type, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_list_of_extrafields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **type** | **str**| Type of element (&#x27;adherent&#x27;, &#x27;commande&#x27;, &#x27;thirdparty&#x27;, &#x27;facture&#x27;, &#x27;propal&#x27;, &#x27;product&#x27;, ...) | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.label:like:&#x27;SO-%&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_measuring_units**
> list[str] setup_retrieve_list_of_measuring_units(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of measuring units. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (starting from zero) (optional)
active = 789 # int | Measuring unit is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

try:
    # Get the list of measuring units. 🔐
    api_response = api_instance.setup_retrieve_list_of_measuring_units(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_list_of_measuring_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **active** | **int**| Measuring unit is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#x27;A%&#x27;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_states**
> list[str] setup_retrieve_list_of_states(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, filter=filter, sqlfilters=sqlfilters)

Get the list of states/provinces. 🔐

 The names of the states will be translated to the given language if the $lang parameter is provided. The value of $lang must be a language code supported by Dolibarr, for example 'en_US' or 'fr_FR'. The returned list is sorted by state ID.

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (starting from zero) (optional)
filter = 'filter_example' # str | To filter the countries by name (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

try:
    # Get the list of states/provinces. 🔐
    api_response = api_instance.setup_retrieve_list_of_states(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, filter=filter, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_list_of_states: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **filter** | **str**| To filter the countries by name | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#x27;A%&#x27;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_towns**
> list[str] setup_retrieve_list_of_towns(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, zipcode=zipcode, town=town, active=active, sqlfilters=sqlfilters)

Get the list of towns. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (starting from zero) (optional)
zipcode = 'zipcode_example' # str | To filter on zipcode (optional)
town = 'town_example' # str | To filter on city name (optional)
active = 789 # int | Payment term is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

try:
    # Get the list of towns. 🔐
    api_response = api_instance.setup_retrieve_list_of_towns(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, zipcode=zipcode, town=town, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_list_of_towns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **zipcode** | **str**| To filter on zipcode | [optional] 
 **town** | **str**| To filter on city name | [optional] 
 **active** | **int**| Payment term is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#x27;A%&#x27;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_ofsocial_networks**
> list[str] setup_retrieve_list_ofsocial_networks(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of social networks. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (starting from zero) (optional)
active = 789 # int | Social network is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

try:
    # Get the list of social networks. 🔐
    api_response = api_instance.setup_retrieve_list_ofsocial_networks(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_list_ofsocial_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **active** | **int**| Social network is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#x27;A%&#x27;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_modules**
> str setup_retrieve_modules()

Get list of enabled modules 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))

try:
    # Get list of enabled modules 🔐
    api_response = api_instance.setup_retrieve_modules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_modules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_ordering_methods**
> list[str] setup_retrieve_ordering_methods(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of ordering methods. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (optional)
active = 789 # int | Payment type is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | SQL criteria to filter with. Syntax example \"(t.code:=:'OrderByWWW')\" (optional)

try:
    # Get the list of ordering methods. 🔐
    api_response = api_instance.setup_retrieve_ordering_methods(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_ordering_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number | [optional] 
 **active** | **int**| Payment type is active or not | [optional] 
 **sqlfilters** | **str**| SQL criteria to filter with. Syntax example \&quot;(t.code:&#x3D;:&#x27;OrderByWWW&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_ordering_origins**
> list[str] setup_retrieve_ordering_origins(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of ordering origins. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (optional)
active = 789 # int | Payment type is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | SQL criteria to filter with. Syntax example \"(t.code:=:'OrderByWWW')\" (optional)

try:
    # Get the list of ordering origins. 🔐
    api_response = api_instance.setup_retrieve_ordering_origins(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_ordering_origins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number | [optional] 
 **active** | **int**| Payment type is active or not | [optional] 
 **sqlfilters** | **str**| SQL criteria to filter with. Syntax example \&quot;(t.code:&#x3D;:&#x27;OrderByWWW&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_payment_terms**
> list[str] setup_retrieve_payment_terms(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of payments terms. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (optional)
active = 789 # int | Payment term is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | SQL criteria to filter. Syntax example \"(t.code:=:'CHQ')\" (optional)

try:
    # Get the list of payments terms. 🔐
    api_response = api_instance.setup_retrieve_payment_terms(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_payment_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number | [optional] 
 **active** | **int**| Payment term is active or not | [optional] 
 **sqlfilters** | **str**| SQL criteria to filter. Syntax example \&quot;(t.code:&#x3D;:&#x27;CHQ&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_payment_types**
> list[str] setup_retrieve_payment_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of payments types. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (optional)
active = 789 # int | Payment type is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | SQL criteria to filter with. Syntax example \"(t.code:=:'CHQ')\" (optional)

try:
    # Get the list of payments types. 🔐
    api_response = api_instance.setup_retrieve_payment_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_payment_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number | [optional] 
 **active** | **int**| Payment type is active or not | [optional] 
 **sqlfilters** | **str**| SQL criteria to filter with. Syntax example \&quot;(t.code:&#x3D;:&#x27;CHQ&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_shipping_modes**
> list[str] setup_retrieve_shipping_modes(limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of shipping methods. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (optional)
active = 789 # int | Shipping methodsm is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | SQL criteria to filter. Syntax example \"(t.code:=:'CHQ')\" (optional)

try:
    # Get the list of shipping methods. 🔐
    api_response = api_instance.setup_retrieve_shipping_modes(limit=limit, page=page, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_shipping_modes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number | [optional] 
 **active** | **int**| Shipping methodsm is active or not | [optional] 
 **sqlfilters** | **str**| SQL criteria to filter. Syntax example \&quot;(t.code:&#x3D;:&#x27;CHQ&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_state_by_code**
> list[str] setup_retrieve_state_by_code(code)

Get state by Code. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | Code of state

try:
    # Get state by Code. 🔐
    api_response = api_instance.setup_retrieve_state_by_code(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_state_by_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of state | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_state_by_id**
> list[str] setup_retrieve_state_by_id(id)

Get state by ID. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of state

try:
    # Get state by ID. 🔐
    api_response = api_instance.setup_retrieve_state_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_state_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of state | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_tickets_categories**
> list[str] setup_retrieve_tickets_categories(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of tickets categories. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (starting from zero) (optional)
active = 789 # int | Payment term is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

try:
    # Get the list of tickets categories. 🔐
    api_response = api_instance.setup_retrieve_tickets_categories(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_tickets_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **active** | **int**| Payment term is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#x27;A%&#x27;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_tickets_severities**
> list[str] setup_retrieve_tickets_severities(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of tickets severity. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (starting from zero) (optional)
active = 789 # int | Payment term is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

try:
    # Get the list of tickets severity. 🔐
    api_response = api_instance.setup_retrieve_tickets_severities(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_tickets_severities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **active** | **int**| Payment term is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#x27;A%&#x27;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_tickets_types**
> list[str] setup_retrieve_tickets_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of tickets types. 🔐

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
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Number of items per page (optional)
page = 789 # int | Page number (starting from zero) (optional)
active = 789 # int | Payment term is active or not (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

try:
    # Get the list of tickets types. 🔐
    api_response = api_instance.setup_retrieve_tickets_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->setup_retrieve_tickets_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **active** | **int**| Payment term is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#x27;A%&#x27;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

