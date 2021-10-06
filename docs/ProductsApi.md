# swagger_client.ProductsApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_products**](ProductsApi.md#create_products) | **POST** /products | Create product object 🔐
[**list_products**](ProductsApi.md#list_products) | **GET** /products | List products 🔐
[**products_add_attribute_value**](ProductsApi.md#products_add_attribute_value) | **POST** /products/attributes/{id}/values | Add attribute value. 🔐
[**products_add_attributes**](ProductsApi.md#products_add_attributes) | **POST** /products/attributes | Add attributes. 🔐
[**products_add_purchase_price**](ProductsApi.md#products_add_purchase_price) | **POST** /products/{id}/purchase_prices | Add/Update purchase prices for a product. 🔐
[**products_add_subproducts**](ProductsApi.md#products_add_subproducts) | **POST** /products/{id}/subproducts/add | Add subproduct. 🔐
[**products_add_variant**](ProductsApi.md#products_add_variant) | **POST** /products/{id}/variants | Add variant. 🔐
[**products_add_variant_by_product_ref**](ProductsApi.md#products_add_variant_by_product_ref) | **POST** /products/ref/{ref}/variants | Add variant by product ref. 🔐
[**products_del_subproducts**](ProductsApi.md#products_del_subproducts) | **DELETE** /products/{id}/subproducts/remove/{subproduct_id} | Remove subproduct. 🔐
[**products_remove_attribute_value_by_id**](ProductsApi.md#products_remove_attribute_value_by_id) | **DELETE** /products/attributes/values/{id} | Delete attribute value by id. 🔐
[**products_remove_attribute_value_by_ref**](ProductsApi.md#products_remove_attribute_value_by_ref) | **DELETE** /products/attributes/{id}/values/ref/{ref} | Delete attribute value by ref. 🔐
[**products_remove_attributes**](ProductsApi.md#products_remove_attributes) | **DELETE** /products/attributes/{id} | Delete attributes by id. 🔐
[**products_remove_purchase_price**](ProductsApi.md#products_remove_purchase_price) | **DELETE** /products/{id}/purchase_prices/{priceid} | Delete purchase price for a product 🔐
[**products_remove_variant**](ProductsApi.md#products_remove_variant) | **DELETE** /products/variants/{id} | Delete product variants. 🔐
[**products_retrieve_attribute_by_id**](ProductsApi.md#products_retrieve_attribute_by_id) | **GET** /products/attributes/{id} | Get attribute by ID. 🔐
[**products_retrieve_attribute_value_by_id**](ProductsApi.md#products_retrieve_attribute_value_by_id) | **GET** /products/attributes/values/{id} | Get attribute value by id. 🔐
[**products_retrieve_attribute_value_by_ref**](ProductsApi.md#products_retrieve_attribute_value_by_ref) | **GET** /products/attributes/{id}/values/ref/{ref} | Get attribute value by ref. 🔐
[**products_retrieve_attribute_values**](ProductsApi.md#products_retrieve_attribute_values) | **GET** /products/attributes/{id}/values | Get all values for an attribute id. 🔐
[**products_retrieve_attribute_values_by_ref**](ProductsApi.md#products_retrieve_attribute_values_by_ref) | **GET** /products/attributes/ref/{ref}/values | Get all values for an attribute ref. 🔐
[**products_retrieve_attributes**](ProductsApi.md#products_retrieve_attributes) | **GET** /products/attributes | Get attributes. 🔐
[**products_retrieve_attributes_by_ref**](ProductsApi.md#products_retrieve_attributes_by_ref) | **GET** /products/attributes/ref/{ref} | Get attributes by ref. 🔐
[**products_retrieve_attributes_by_ref_ext**](ProductsApi.md#products_retrieve_attributes_by_ref_ext) | **GET** /products/attributes/ref_ext/{ref_ext} | Get attributes by ref_ext. 🔐
[**products_retrieve_by_barcode**](ProductsApi.md#products_retrieve_by_barcode) | **GET** /products/barcode/{barcode} | Get properties of a product object by barcode 🔐
[**products_retrieve_by_ref**](ProductsApi.md#products_retrieve_by_ref) | **GET** /products/ref/{ref} | Get properties of a product object by ref 🔐
[**products_retrieve_by_ref_ext**](ProductsApi.md#products_retrieve_by_ref_ext) | **GET** /products/ref_ext/{ref_ext} | Get properties of a product object by ref_ext 🔐
[**products_retrieve_categories**](ProductsApi.md#products_retrieve_categories) | **GET** /products/{id}/categories | Get categories for a product 🔐
[**products_retrieve_customer_prices_per_customer**](ProductsApi.md#products_retrieve_customer_prices_per_customer) | **GET** /products/{id}/selling_multiprices/per_customer | Get prices per customer for a product 🔐
[**products_retrieve_customer_prices_per_quantity**](ProductsApi.md#products_retrieve_customer_prices_per_quantity) | **GET** /products/{id}/selling_multiprices/per_quantity | Get prices per quantity for a product 🔐
[**products_retrieve_customer_prices_per_segment**](ProductsApi.md#products_retrieve_customer_prices_per_segment) | **GET** /products/{id}/selling_multiprices/per_segment | Get prices per segment for a product 🔐
[**products_retrieve_purchase_prices**](ProductsApi.md#products_retrieve_purchase_prices) | **GET** /products/{id}/purchase_prices | Get purchase prices for a product 🔐
[**products_retrieve_stock**](ProductsApi.md#products_retrieve_stock) | **GET** /products/{id}/stock | Get stock data for the product id given. 🔐
[**products_retrieve_subproducts**](ProductsApi.md#products_retrieve_subproducts) | **GET** /products/{id}/subproducts | Get the list of subproducts of the product. 🔐
[**products_retrieve_supplier_products**](ProductsApi.md#products_retrieve_supplier_products) | **GET** /products/purchase_prices | Get a list of all purchase prices of products 🔐
[**products_retrieve_variants**](ProductsApi.md#products_retrieve_variants) | **GET** /products/{id}/variants | Get product variants. 🔐
[**products_retrieve_variants_by_prod_ref**](ProductsApi.md#products_retrieve_variants_by_prod_ref) | **GET** /products/ref/{ref}/variants | Get product variants by Product ref. 🔐
[**products_update_attribute_value**](ProductsApi.md#products_update_attribute_value) | **PUT** /products/attributes/values/{id} | Update attribute value. 🔐
[**products_update_attributes**](ProductsApi.md#products_update_attributes) | **PUT** /products/attributes/{id} | Update attributes by id. 🔐
[**products_update_variant**](ProductsApi.md#products_update_variant) | **PUT** /products/variants/{id} | Put product variants. 🔐
[**remove_products**](ProductsApi.md#remove_products) | **DELETE** /products/{id} | Delete product 🔐
[**retrieve_products**](ProductsApi.md#retrieve_products) | **GET** /products/{id} | Get properties of a product object by id 🔐
[**update_products**](ProductsApi.md#update_products) | **PUT** /products/{id} | Update product. 🔐

# **create_products**
> int create_products(body=body)

Create product object 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateProductsModel() # CreateProductsModel | request_data  
 (optional)

try:
    # Create product object 🔐
    api_response = api_instance.create_products(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->create_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProductsModel**](CreateProductsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products**
> list[str] list_products(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, mode=mode, category=category, sqlfilters=sqlfilters, ids_only=ids_only, variant_filter=variant_filter, pagination_data=pagination_data)

List products 🔐

Get a list of products

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
mode = 789 # int | Use this param to filter list (0 for all, 1 for only product, 2 for only service) (optional)
category = 789 # int | Use this param to filter list by category (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.tobuy:=:0) and (t.tosell:=:1)\" (optional)
ids_only = true # bool | Return only IDs of product instead of all properties (faster, above all if list is long) (optional)
variant_filter = 789 # int | Use this param to filter list (0 = all, 1=products without variants, 2=parent of variants, 3=variants only) (optional)
pagination_data = true # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0 (optional)

try:
    # List products 🔐
    api_response = api_instance.list_products(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, mode=mode, category=category, sqlfilters=sqlfilters, ids_only=ids_only, variant_filter=variant_filter, pagination_data=pagination_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->list_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **mode** | **int**| Use this param to filter list (0 for all, 1 for only product, 2 for only service) | [optional] 
 **category** | **int**| Use this param to filter list by category | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.tobuy:&#x3D;:0) and (t.tosell:&#x3D;:1)\&quot; | [optional] 
 **ids_only** | **bool**| Return only IDs of product instead of all properties (faster, above all if list is long) | [optional] 
 **variant_filter** | **int**| Use this param to filter list (0 &#x3D; all, 1&#x3D;products without variants, 2&#x3D;parent of variants, 3&#x3D;variants only) | [optional] 
 **pagination_data** | **bool**| If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0 | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_add_attribute_value**
> int products_add_attribute_value(body, id)

Add attribute value. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductsAddAttributeValueModel() # ProductsAddAttributeValueModel | **ref** (required)  
**value** (required)  

id = 789 # int | ID of Attribute

try:
    # Add attribute value. 🔐
    api_response = api_instance.products_add_attribute_value(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_add_attribute_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductsAddAttributeValueModel**](ProductsAddAttributeValueModel.md)| **ref** (required)  
**value** (required)  
 | 
 **id** | **int**| ID of Attribute | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_add_attributes**
> int products_add_attributes(body)

Add attributes. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductsAddAttributesModel() # ProductsAddAttributesModel | **ref** (required)  
**label** (required)  
ref_ext  


try:
    # Add attributes. 🔐
    api_response = api_instance.products_add_attributes(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_add_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductsAddAttributesModel**](ProductsAddAttributesModel.md)| **ref** (required)  
**label** (required)  
ref_ext  
 | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_add_purchase_price**
> int products_add_purchase_price(body, id)

Add/Update purchase prices for a product. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductsAddPurchasePriceModel() # ProductsAddPurchasePriceModel | **qty** (required)  
**buyprice** (required)  
**price_base_type** (required)  
**fourn_id** (required)  
**availability** (required)  
**ref_fourn** (required)  
**tva_tx** (required)  
charges  
remise_percent  
remise  
newnpr  
delivery_time_days  
supplier_reputation  
localtaxes_array  
newdefaultvatcode  
multicurrency_buyprice  
multicurrency_price_base_type  
multicurrency_tx  
multicurrency_code  
desc_fourn  
barcode  
fk_barcode_type  

id = 789 # int | ID of Product

try:
    # Add/Update purchase prices for a product. 🔐
    api_response = api_instance.products_add_purchase_price(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_add_purchase_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductsAddPurchasePriceModel**](ProductsAddPurchasePriceModel.md)| **qty** (required)  
**buyprice** (required)  
**price_base_type** (required)  
**fourn_id** (required)  
**availability** (required)  
**ref_fourn** (required)  
**tva_tx** (required)  
charges  
remise_percent  
remise  
newnpr  
delivery_time_days  
supplier_reputation  
localtaxes_array  
newdefaultvatcode  
multicurrency_buyprice  
multicurrency_price_base_type  
multicurrency_tx  
multicurrency_code  
desc_fourn  
barcode  
fk_barcode_type  
 | 
 **id** | **int**| ID of Product | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_add_subproducts**
> int products_add_subproducts(body, id)

Add subproduct. 🔐

 Link a product/service to a parent product/service

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductsAddSubproductsModel() # ProductsAddSubproductsModel | **subproduct_id** (required)  
**qty** (required)  
incdec  

id = 789 # int | Id of parent product/service

try:
    # Add subproduct. 🔐
    api_response = api_instance.products_add_subproducts(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_add_subproducts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductsAddSubproductsModel**](ProductsAddSubproductsModel.md)| **subproduct_id** (required)  
**qty** (required)  
incdec  
 | 
 **id** | **int**| Id of parent product/service | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_add_variant**
> int products_add_variant(body, id)

Add variant. 🔐

 \"features\" is a list of attributes pairs id_attribute=>id_value. Example: array(id_color=>id_Blue, id_size=>id_small, id_option=>id_val_a, ...)

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductsAddVariantModel() # ProductsAddVariantModel | **weight_impact** (required)  
**price_impact** (required)  
**price_impact_is_percent** (required)  
**features** (required)  
reference  
ref_ext  

id = 789 # int | ID of Product

try:
    # Add variant. 🔐
    api_response = api_instance.products_add_variant(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_add_variant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductsAddVariantModel**](ProductsAddVariantModel.md)| **weight_impact** (required)  
**price_impact** (required)  
**price_impact_is_percent** (required)  
**features** (required)  
reference  
ref_ext  
 | 
 **id** | **int**| ID of Product | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_add_variant_by_product_ref**
> int products_add_variant_by_product_ref(body, ref)

Add variant by product ref. 🔐

 \"features\" is a list of attributes pairs id_attribute=>id_value. Example: array(id_color=>id_Blue, id_size=>id_small, id_option=>id_val_a, ...)

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductsAddVariantByProductRefModel() # ProductsAddVariantByProductRefModel | **weight_impact** (required)  
**price_impact** (required)  
**price_impact_is_percent** (required)  
**features** (required)  

ref = 'ref_example' # str | Ref of Product

try:
    # Add variant by product ref. 🔐
    api_response = api_instance.products_add_variant_by_product_ref(body, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_add_variant_by_product_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductsAddVariantByProductRefModel**](ProductsAddVariantByProductRefModel.md)| **weight_impact** (required)  
**price_impact** (required)  
**price_impact_is_percent** (required)  
**features** (required)  
 | 
 **ref** | **str**| Ref of Product | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_del_subproducts**
> int products_del_subproducts(id, subproduct_id)

Remove subproduct. 🔐

Unlink a product/service from a parent product/service

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of parent product/service
subproduct_id = 789 # int | Id of child product/service

try:
    # Remove subproduct. 🔐
    api_response = api_instance.products_del_subproducts(id, subproduct_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_del_subproducts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of parent product/service | 
 **subproduct_id** | **int**| Id of child product/service | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_remove_attribute_value_by_id**
> int products_remove_attribute_value_by_id(id)

Delete attribute value by id. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of Attribute value

try:
    # Delete attribute value by id. 🔐
    api_response = api_instance.products_remove_attribute_value_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_remove_attribute_value_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute value | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_remove_attribute_value_by_ref**
> int products_remove_attribute_value_by_ref(id, ref)

Delete attribute value by ref. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of Attribute
ref = 'ref_example' # str | Ref of Attribute value

try:
    # Delete attribute value by ref. 🔐
    api_response = api_instance.products_remove_attribute_value_by_ref(id, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_remove_attribute_value_by_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute | 
 **ref** | **str**| Ref of Attribute value | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_remove_attributes**
> int products_remove_attributes(id)

Delete attributes by id. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of Attribute

try:
    # Delete attributes by id. 🔐
    api_response = api_instance.products_remove_attributes(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_remove_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_remove_purchase_price**
> int products_remove_purchase_price(id, priceid)

Delete purchase price for a product 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Product ID
priceid = 789 # int | purchase price ID

try:
    # Delete purchase price for a product 🔐
    api_response = api_instance.products_remove_purchase_price(id, priceid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_remove_purchase_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Product ID | 
 **priceid** | **int**| purchase price ID | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_remove_variant**
> int products_remove_variant(id)

Delete product variants. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of Variant

try:
    # Delete product variants. 🔐
    api_response = api_instance.products_remove_variant(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_remove_variant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Variant | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_attribute_by_id**
> list[str] products_retrieve_attribute_by_id(id)

Get attribute by ID. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of Attribute

try:
    # Get attribute by ID. 🔐
    api_response = api_instance.products_retrieve_attribute_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_attribute_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_attribute_value_by_id**
> list[str] products_retrieve_attribute_value_by_id(id)

Get attribute value by id. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of Attribute value

try:
    # Get attribute value by id. 🔐
    api_response = api_instance.products_retrieve_attribute_value_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_attribute_value_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute value | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_attribute_value_by_ref**
> list[str] products_retrieve_attribute_value_by_ref(id, ref)

Get attribute value by ref. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of Attribute value
ref = 'ref_example' # str | Ref of Attribute value

try:
    # Get attribute value by ref. 🔐
    api_response = api_instance.products_retrieve_attribute_value_by_ref(id, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_attribute_value_by_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute value | 
 **ref** | **str**| Ref of Attribute value | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_attribute_values**
> list[str] products_retrieve_attribute_values(id)

Get all values for an attribute id. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of an Attribute

try:
    # Get all values for an attribute id. 🔐
    api_response = api_instance.products_retrieve_attribute_values(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_attribute_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of an Attribute | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_attribute_values_by_ref**
> list[str] products_retrieve_attribute_values_by_ref(ref)

Get all values for an attribute ref. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
ref = 'ref_example' # str | Ref of an Attribute

try:
    # Get all values for an attribute ref. 🔐
    api_response = api_instance.products_retrieve_attribute_values_by_ref(ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_attribute_values_by_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Ref of an Attribute | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_attributes**
> list[str] products_retrieve_attributes(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters)

Get attributes. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:color)\" (optional)

try:
    # Get attributes. 🔐
    api_response = api_instance.products_retrieve_attributes(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:color)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_attributes_by_ref**
> list[str] products_retrieve_attributes_by_ref(ref)

Get attributes by ref. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
ref = 'ref_example' # str | Reference of Attribute

try:
    # Get attributes by ref. 🔐
    api_response = api_instance.products_retrieve_attributes_by_ref(ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_attributes_by_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Reference of Attribute | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_attributes_by_ref_ext**
> list[str] products_retrieve_attributes_by_ref_ext(ref_ext)

Get attributes by ref_ext. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
ref_ext = 'ref_ext_example' # str | External reference of Attribute

try:
    # Get attributes by ref_ext. 🔐
    api_response = api_instance.products_retrieve_attributes_by_ref_ext(ref_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_attributes_by_ref_ext: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref_ext** | **str**| External reference of Attribute | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_by_barcode**
> str products_retrieve_by_barcode(barcode, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)

Get properties of a product object by barcode 🔐

Return an array with product information.

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
barcode = 'barcode_example' # str | Barcode of element
includestockdata = 789 # int | Load also information about stock (slower) (optional)
includesubproducts = true # bool | Load information about subproducts (optional)
includeparentid = true # bool | Load also ID of parent product (if product is a variant of a parent product) (optional)
includetrans = true # bool | Load also the translations of product label and description (optional)

try:
    # Get properties of a product object by barcode 🔐
    api_response = api_instance.products_retrieve_by_barcode(barcode, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_by_barcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**| Barcode of element | 
 **includestockdata** | **int**| Load also information about stock (slower) | [optional] 
 **includesubproducts** | **bool**| Load information about subproducts | [optional] 
 **includeparentid** | **bool**| Load also ID of parent product (if product is a variant of a parent product) | [optional] 
 **includetrans** | **bool**| Load also the translations of product label and description | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_by_ref**
> str products_retrieve_by_ref(ref, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)

Get properties of a product object by ref 🔐

Return an array with product information.

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
ref = 'ref_example' # str | Ref of element
includestockdata = 789 # int | Load also information about stock (slower) (optional)
includesubproducts = true # bool | Load information about subproducts (optional)
includeparentid = true # bool | Load also ID of parent product (if product is a variant of a parent product) (optional)
includetrans = true # bool | Load also the translations of product label and description (optional)

try:
    # Get properties of a product object by ref 🔐
    api_response = api_instance.products_retrieve_by_ref(ref, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_by_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Ref of element | 
 **includestockdata** | **int**| Load also information about stock (slower) | [optional] 
 **includesubproducts** | **bool**| Load information about subproducts | [optional] 
 **includeparentid** | **bool**| Load also ID of parent product (if product is a variant of a parent product) | [optional] 
 **includetrans** | **bool**| Load also the translations of product label and description | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_by_ref_ext**
> str products_retrieve_by_ref_ext(ref_ext, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)

Get properties of a product object by ref_ext 🔐

Return an array with product information.

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
ref_ext = 'ref_ext_example' # str | Ref_ext of element
includestockdata = 789 # int | Load also information about stock (slower) (optional)
includesubproducts = true # bool | Load information about subproducts (optional)
includeparentid = true # bool | Load also ID of parent product (if product is a variant of a parent product) (optional)
includetrans = true # bool | Load also the translations of product label and description (optional)

try:
    # Get properties of a product object by ref_ext 🔐
    api_response = api_instance.products_retrieve_by_ref_ext(ref_ext, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_by_ref_ext: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref_ext** | **str**| Ref_ext of element | 
 **includestockdata** | **int**| Load also information about stock (slower) | [optional] 
 **includesubproducts** | **bool**| Load information about subproducts | [optional] 
 **includeparentid** | **bool**| Load also ID of parent product (if product is a variant of a parent product) | [optional] 
 **includetrans** | **bool**| Load also the translations of product label and description | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_categories**
> str products_retrieve_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)

Get categories for a product 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of product
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)

try:
    # Get categories for a product 🔐
    api_response = api_instance.products_retrieve_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product | 
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

# **products_retrieve_customer_prices_per_customer**
> str products_retrieve_customer_prices_per_customer(id, thirdparty_id=thirdparty_id)

Get prices per customer for a product 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of product
thirdparty_id = 'thirdparty_id_example' # str | Thirdparty id to filter orders of (example '1') (optional)

try:
    # Get prices per customer for a product 🔐
    api_response = api_instance.products_retrieve_customer_prices_per_customer(id, thirdparty_id=thirdparty_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_customer_prices_per_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product | 
 **thirdparty_id** | **str**| Thirdparty id to filter orders of (example &#x27;1&#x27;) | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_customer_prices_per_quantity**
> str products_retrieve_customer_prices_per_quantity(id)

Get prices per quantity for a product 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of product

try:
    # Get prices per quantity for a product 🔐
    api_response = api_instance.products_retrieve_customer_prices_per_quantity(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_customer_prices_per_quantity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_customer_prices_per_segment**
> str products_retrieve_customer_prices_per_segment(id)

Get prices per segment for a product 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of product

try:
    # Get prices per segment for a product 🔐
    api_response = api_instance.products_retrieve_customer_prices_per_segment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_customer_prices_per_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_purchase_prices**
> str products_retrieve_purchase_prices(id, ref=ref, ref_ext=ref_ext, barcode=barcode)

Get purchase prices for a product 🔐

Return an array with product information. TODO implement getting a product by ref or by $ref_ext

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of product
ref = 'ref_example' # str | Ref of element (optional)
ref_ext = 'ref_ext_example' # str | Ref ext of element (optional)
barcode = 'barcode_example' # str | Barcode of element (optional)

try:
    # Get purchase prices for a product 🔐
    api_response = api_instance.products_retrieve_purchase_prices(id, ref=ref, ref_ext=ref_ext, barcode=barcode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_purchase_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product | 
 **ref** | **str**| Ref of element | [optional] 
 **ref_ext** | **str**| Ref ext of element | [optional] 
 **barcode** | **str**| Barcode of element | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_stock**
> int products_retrieve_stock(id, selected_warehouse_id=selected_warehouse_id)

Get stock data for the product id given. 🔐

Optionaly with $selected_warehouse_id parameter user can get stock of specific warehouse

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of Product
selected_warehouse_id = 789 # int | ID of warehouse (optional)

try:
    # Get stock data for the product id given. 🔐
    api_response = api_instance.products_retrieve_stock(id, selected_warehouse_id=selected_warehouse_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_stock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Product | 
 **selected_warehouse_id** | **int**| ID of warehouse | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_subproducts**
> list[str] products_retrieve_subproducts(id)

Get the list of subproducts of the product. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of parent product/service

try:
    # Get the list of subproducts of the product. 🔐
    api_response = api_instance.products_retrieve_subproducts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_subproducts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of parent product/service | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_supplier_products**
> list[str] products_retrieve_supplier_products(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, mode=mode, category=category, supplier=supplier, sqlfilters=sqlfilters)

Get a list of all purchase prices of products 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
sortfield = 'sortfield_example' # str | Sort field (optional)
sortorder = 'sortorder_example' # str | Sort order (optional)
limit = 789 # int | Limit for list (optional)
page = 789 # int | Page number (optional)
mode = 789 # int | Use this param to filter list (0 for all, 1 for only product, 2 for only service) (optional)
category = 789 # int | Use this param to filter list by category of product (optional)
supplier = 789 # int | Use this param to filter list by supplier (optional)
sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.tobuy:=:0) and (t.tosell:=:1)\" (optional)

try:
    # Get a list of all purchase prices of products 🔐
    api_response = api_instance.products_retrieve_supplier_products(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, mode=mode, category=category, supplier=supplier, sqlfilters=sqlfilters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_supplier_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **mode** | **int**| Use this param to filter list (0 for all, 1 for only product, 2 for only service) | [optional] 
 **category** | **int**| Use this param to filter list by category of product | [optional] 
 **supplier** | **int**| Use this param to filter list by supplier | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.tobuy:&#x3D;:0) and (t.tosell:&#x3D;:1)\&quot; | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_variants**
> list[str] products_retrieve_variants(id, includestock=includestock)

Get product variants. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of Product
includestock = 789 # int | Default value 0. If parameter is set to 1 the response will contain stock data of each variant (optional)

try:
    # Get product variants. 🔐
    api_response = api_instance.products_retrieve_variants(id, includestock=includestock)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_variants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Product | 
 **includestock** | **int**| Default value 0. If parameter is set to 1 the response will contain stock data of each variant | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_variants_by_prod_ref**
> list[str] products_retrieve_variants_by_prod_ref(ref)

Get product variants by Product ref. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
ref = 'ref_example' # str | Ref of Product

try:
    # Get product variants by Product ref. 🔐
    api_response = api_instance.products_retrieve_variants_by_prod_ref(ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_retrieve_variants_by_prod_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Ref of Product | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_update_attribute_value**
> list[str] products_update_attribute_value(body, id)

Update attribute value. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductsUpdateAttributeValueModel() # ProductsUpdateAttributeValueModel | **request_data** (required)  

id = 789 # int | ID of Attribute

try:
    # Update attribute value. 🔐
    api_response = api_instance.products_update_attribute_value(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_update_attribute_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductsUpdateAttributeValueModel**](ProductsUpdateAttributeValueModel.md)| **request_data** (required)  
 | 
 **id** | **int**| ID of Attribute | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_update_attributes**
> list[str] products_update_attributes(id, body=body)

Update attributes by id. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of Attribute
body = swagger_client.ProductsUpdateAttributesModel() # ProductsUpdateAttributesModel | request_data  
 (optional)

try:
    # Update attributes by id. 🔐
    api_response = api_instance.products_update_attributes(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_update_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute | 
 **body** | [**ProductsUpdateAttributesModel**](ProductsUpdateAttributesModel.md)| request_data  
 | [optional] 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_update_variant**
> int products_update_variant(id, body=body)

Put product variants. 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of Variant
body = swagger_client.ProductsUpdateVariantModel() # ProductsUpdateVariantModel | request_data  
 (optional)

try:
    # Put product variants. 🔐
    api_response = api_instance.products_update_variant(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_update_variant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Variant | 
 **body** | [**ProductsUpdateVariantModel**](ProductsUpdateVariantModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_products**
> list[str] remove_products(id)

Delete product 🔐

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Product ID

try:
    # Delete product 🔐
    api_response = api_instance.remove_products(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->remove_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Product ID | 

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_products**
> str retrieve_products(id, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)

Get properties of a product object by id 🔐

Return an array with product information.

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of product
includestockdata = 789 # int | Load also information about stock (slower) (optional)
includesubproducts = true # bool | Load information about subproducts (optional)
includeparentid = true # bool | Load also ID of parent product (if product is a variant of a parent product) (optional)
includetrans = true # bool | Load also the translations of product label and description (optional)

try:
    # Get properties of a product object by id 🔐
    api_response = api_instance.retrieve_products(id, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->retrieve_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product | 
 **includestockdata** | **int**| Load also information about stock (slower) | [optional] 
 **includesubproducts** | **bool**| Load information about subproducts | [optional] 
 **includeparentid** | **bool**| Load also ID of parent product (if product is a variant of a parent product) | [optional] 
 **includetrans** | **bool**| Load also the translations of product label and description | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_products**
> int update_products(id, body=body)

Update product. 🔐

Price will be updated by this API only if option is set on \"One price per product\". See other APIs for other price modes.

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Id of product to update
body = swagger_client.UpdateProductsModel() # UpdateProductsModel | request_data  
 (optional)

try:
    # Update product. 🔐
    api_response = api_instance.update_products(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->update_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of product to update | 
 **body** | [**UpdateProductsModel**](UpdateProductsModel.md)| request_data  
 | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

