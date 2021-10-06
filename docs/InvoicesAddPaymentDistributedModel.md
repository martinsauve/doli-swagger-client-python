# InvoicesAddPaymentDistributedModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrayofamounts** | **list[str]** | Array with id of invoices with amount to pay for each invoice | 
**datepaye** | **str** | Payment date | 
**paymentid** | **int** | Payment mode Id | 
**closepaidinvoices** | **str** | Close paid invoices | 
**accountid** | **int** | Account Id | 
**num_payment** | **str** | Payment number (optional) | [optional] 
**comment** | **str** | Note private (optional) | [optional] 
**chqemetteur** | **str** | Payment issuer (mandatory if paiementcode &#x3D; &#x27;CHQ&#x27;) | [optional] 
**chqbank** | **str** | Issuer bank name (optional) | [optional] 
**ref_ext** | **str** | External reference (optional) | [optional] 
**accepthigherpayment** | **bool** | Accept higher payments that it remains to be paid (optional) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

