# SupplierinvoicesAddPaymentModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datepaye** | **str** | Payment date | 
**payment_mode_id** | **int** | Payment mode ID (look it up via REST GET to /setup/dictionary/payment_types) | 
**closepaidinvoices** | **str** | Close paid invoices | 
**accountid** | **int** | Bank account ID (look it up via REST GET to /bankaccounts) | 
**num_payment** | **str** | Payment number (optional) | [optional] 
**comment** | **str** | Note (optional) | [optional] 
**chqemetteur** | **str** | Payment issuer (mandatory if payment_mode_id corresponds to &#x27;CHQ&#x27;-payment type) | [optional] 
**chqbank** | **str** | Issuer bank name (optional) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

