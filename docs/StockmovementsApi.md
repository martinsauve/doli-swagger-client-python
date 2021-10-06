# swagger_client.StockmovementsApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stockmovements**](StockmovementsApi.md#create_stockmovements) | **POST** /stockmovements | Create stock movement object. 🔐
[**list_stockmovements**](StockmovementsApi.md#list_stockmovements) | **GET** /stockmovements | Get a list of stock movement 🔐

# **create_stockmovements**
> int create_stockmovements(body)

Create stock movement object. 🔐

You can use the following message to test this RES API: { \"product_id\": 1, \"warehouse_id\": 1, \"qty\": 1, \"lot\": \"\", \"movementcode\": \"INV123\", \"movementlabel\": \"Inventory 123\", \"price\": 0 } $price Can be set to update AWP (Average Weighted Price) when you make a stock increase $dlc Eat-by date. Will be used if lot does not exists yet and will be created. $dluo Sell-by date. Will be used if lot does not exists yet and will be created.

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
api_instance = swagger_client.StockmovementsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateStockmovementsModel() # CreateStockmovementsModel | **product_id** (required)  
**warehouse_id** (required)  
**qty** (required)  
lot  
movementcode  
movementlabel  
price  
dlc  
dluo  


try:
    # Create stock movement object. 🔐
    api_response = api_instance.create_stockmovements(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockmovementsApi->create_stockmovements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateStockmovementsModel**](CreateStockmovementsModel.md)| **product_id** (required)  
**warehouse_id** (required)  
**qty** (required)  
lot  
movementcode  
movementlabel  
price  
dlc  
dluo  
 | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stockmovements**
> list[str] list_stockmovements(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters)

Get a list of stock movement 🔐

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
api_instance = swagger_client.StockmovementsApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.product_id:=:1) and (t.date_creation:<:'20160101')\" (optional)

try:
    # Get a list of stock movement 🔐
    api_response = api_instance.list_stockmovements(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockmovementsApi->list_stockmovements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.product_id:&#x3D;:1) and (t.date_creation:&lt;:&#x27;20160101&#x27;)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

