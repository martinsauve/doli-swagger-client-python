# CreateStockmovementsModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** | Id product id | 
**warehouse_id** | **int** | Id warehouse | 
**qty** | **float** | Qty to add (Use negative value for a stock decrease) | 
**lot** | **str** | Lot | [optional] 
**movementcode** | **str** | Movement code | [optional] 
**movementlabel** | **str** | Movement label | [optional] 
**price** | **str** | To update AWP (Average Weighted Price) when you make a stock increase (qty must be higher then 0). | [optional] 
**dlc** | **date** | Eat-by date. | [optional] 
**dluo** | **date** | Sell-by date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

