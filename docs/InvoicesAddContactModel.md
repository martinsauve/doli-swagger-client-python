# InvoicesAddContactModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_socpeople** | **int** | Id of thirdparty contact (if source &#x3D; &#x27;external&#x27;) or id of user (if souce &#x3D; &#x27;internal&#x27;) to link | 
**type_contact** | **str** | Type of contact (code). Must a code found into table llx_c_type_contact. For example: BILLING | 
**source** | **str** | external&#x3D;Contact extern (llx_socpeople), internal&#x3D;Contact intern (llx_user) | 
**notrigger** | **int** | Disable all triggers | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

