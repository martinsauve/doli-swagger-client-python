# ListLoginModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | User login | 
**password** | **str** | User password | 
**entity** | **str** | Entity (when multicompany module is used). &#x27;&#x27; means 1&#x3D;first company. | [optional] 
**reset** | **int** | Reset token (0&#x3D;get current token, 1&#x3D;ask a new token and canceled old token. This means access using current existing API token of user will fails: new token will be required for new access) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

