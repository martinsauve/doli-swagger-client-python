# ProductsAddPurchasePriceModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qty** | **float** | Min quantity for which price is valid | 
**buyprice** | **float** | Purchase price for the quantity min | 
**price_base_type** | **str** | HT or TTC | 
**fourn_id** | **int** | Supplier ID | 
**availability** | **int** | Product availability | 
**ref_fourn** | **str** | Supplier ref | 
**tva_tx** | **float** | New VAT Rate (For example 8.5. Should not be a string) | 
**charges** | **str** | costs affering to product | [optional] 
**remise_percent** | **float** | Discount regarding qty (percent) | [optional] 
**remise** | **float** | Discount regarding qty (amount) | [optional] 
**newnpr** | **int** | Set NPR or not | [optional] 
**delivery_time_days** | **int** | Delay in days for delivery (max). May be &#x27;&#x27; if not defined. | [optional] 
**supplier_reputation** | **str** | Reputation with this product to the defined supplier (empty, FAVORITE, DONOTORDER) | [optional] 
**localtaxes_array** | **list[str]** | Array with localtaxes info array(&#x27;0&#x27;&#x3D;&gt;type1,&#x27;1&#x27;&#x3D;&gt;rate1,&#x27;2&#x27;&#x3D;&gt;type2,&#x27;3&#x27;&#x3D;&gt;rate2) (loaded by getLocalTaxesFromRate(vatrate, 0, ...) function). | [optional] 
**newdefaultvatcode** | **str** | Default vat code | [optional] 
**multicurrency_buyprice** | **float** | Purchase price for the quantity min in currency | [optional] 
**multicurrency_price_base_type** | **str** | HT or TTC in currency | [optional] 
**multicurrency_tx** | **float** | Rate currency | [optional] 
**multicurrency_code** | **str** | Currency code | [optional] 
**desc_fourn** | **str** | Custom description for product_fourn_price | [optional] 
**barcode** | **str** | Barcode | [optional] 
**fk_barcode_type** | **int** | Barcode type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

