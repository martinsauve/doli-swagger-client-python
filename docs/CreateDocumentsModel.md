# CreateDocumentsModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | Name of file to create (&#x27;FA1705-0123.txt&#x27;) | 
**modulepart** | **str** | Name of module or area concerned by file upload (&#x27;facture&#x27;, &#x27;project&#x27;, &#x27;project_task&#x27;, ...) | 
**ref** | **str** | Reference of object (This will define subdir automatically and store submited file into it) | [optional] 
**subdir** | **str** | Subdirectory (Only if ref not provided) | [optional] 
**filecontent** | **str** | File content (string with file content. An empty file will be created if this parameter is not provided) | [optional] 
**fileencoding** | **str** | File encoding (&#x27;&#x27;&#x3D;no encoding, &#x27;base64&#x27;&#x3D;Base 64) | [optional] 
**overwriteifexists** | **int** | Overwrite file if exists (1 by default) | [optional] 
**createdirifnotexists** | **int** | Create subdirectories if the doesn&#x27;t exists (1 by default) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

