# swagger_client.LoginApi

All URIs are relative to *//nas.local:8888/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_login**](LoginApi.md#list_login) | **POST** /login | Login 🔓
[**login_login_unsecured**](LoginApi.md#login_login_unsecured) | **GET** /login | Login 🔓

# **list_login**
> list[str] list_login(body)

Login 🔓

Request the API token for a couple username / password. Using method POST is recommanded for security reasons (method GET is often logged by default by web servers with parameters so with login and pass into server log file). Both methods are provided for developer conveniance. Best is to not use at all the login API method and enter directly the \"DOLAPIKEY\" into field at the top right of page. Note: The API token (DOLAPIKEY) can be found/set on the user page.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginApi()
body = swagger_client.ListLoginModel() # ListLoginModel | **login** (required)  
**password** (required)  
entity  
reset  


try:
    # Login 🔓
    api_response = api_instance.list_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->list_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListLoginModel**](ListLoginModel.md)| **login** (required)  
**password** (required)  
entity  
reset  
 | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_login_unsecured**
> list[str] login_login_unsecured(login, password, entity=entity, reset=reset)

Login 🔓

Request the API token for a couple username / password. Using method POST is recommanded for security reasons (method GET is often logged by default by web servers with parameters so with login and pass into server log file). Both methods are provided for developer conveniance. Best is to not use at all the login API method and enter directly the \"DOLAPIKEY\" into field at the top right of page. Note: The API token (DOLAPIKEY) can be found/set on the user page.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginApi()
login = 'login_example' # str | User login
password = 'password_example' # str | User password
entity = 'entity_example' # str | Entity (when multicompany module is used). '' means 1=first company. (optional)
reset = 789 # int | Reset token (0=get current token, 1=ask a new token and canceled old token. This means access using current existing API token of user will fails: new token will be required for new access) (optional)

try:
    # Login 🔓
    api_response = api_instance.login_login_unsecured(login, password, entity=entity, reset=reset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login_login_unsecured: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| User login | 
 **password** | **str**| User password | 
 **entity** | **str**| Entity (when multicompany module is used). &#x27;&#x27; means 1&#x3D;first company. | [optional] 
 **reset** | **int**| Reset token (0&#x3D;get current token, 1&#x3D;ask a new token and canceled old token. This means access using current existing API token of user will fails: new token will be required for new access) | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

