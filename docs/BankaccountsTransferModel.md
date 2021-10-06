# BankaccountsTransferModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bankaccount_from_id** | **int** | BankAccount ID to use as the source of the internal wire transfer | 
**bankaccount_to_id** | **int** | BankAccount ID to use as the destination of the internal wire transfer | 
**_date** | **str** | Date of the internal wire transfer (UNIX timestamp) | 
**description** | **str** | Description of the internal wire transfer | 
**amount** | **float** | Amount to transfer from the source to the destination BankAccount | 
**amount_to** | **float** | Amount to transfer to the destination BankAccount (only when accounts does not share the same currency) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

