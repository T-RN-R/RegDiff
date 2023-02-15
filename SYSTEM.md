
d16a1cca-3eee-41d9-9952-5f04f75b40a7 1c103928-9a3d-4d59-bde1-9a01e428d506 Diff
==============================================================================

Table of contents
=================

* [Core](#core)
	* [SYSTEM](#system)
		* [Added](#added)
			* [WMI AutoLoggers](#wmi-autologgers)
				* [SpoolerLogger](#spoolerlogger)
			* [Services](#services)
				* [CldFlt](#cldflt)
				* [EventLog](#eventlog)
				* [McpManagementService](#mcpmanagementservice)
				* [PrintWorkflowUserSvc](#printworkflowusersvc)
				* [stisvc](#stisvc)

# Core

## SYSTEM

### Added

#### WMI AutoLoggers

##### SpoolerLogger

|EnableFlags|EnableLevel|Enabled|guid|
| :---: | :---: | :---: | :---: |
|0x00|0x05|0x01|{ba4936a1-31db-4edc-89ce-9190e3c0653b}|
  
<br></br>  
<br></br>
#### Services

##### CldFlt



###### Service Parameters
  
USMsgTimeoutMillis : `0x3e8`  
<br></br>
##### EventLog
  
Application : `{'Universal Print': {'EventMessageFile': '%SystemRoot%\\System32\\McpManagementService.dll', 'TypesSupported': 7}}`
##### McpManagementService
  
DependOnService : `RpcSs`  
Description : `@%SystemRoot%\system32\McpManagementService.dll,-101`  
DisplayName : `@%SystemRoot%\system32\McpManagementService.dll,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 01 00 00 00 14 00 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k McpManagementServiceGroup`  
ObjectName : `LocalSystem`  
RequiredPrivileges : `['SeTcbPrivilege', 'SeChangeNotifyPrivilege', 'SeImpersonatePrivilege', 'SeCreateGlobalPrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`


###### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\McpManagementService.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>
##### PrintWorkflowUserSvc



###### Service Triggers

|ID|Action|Data0|DataType0|GUID|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`75 10 bc a3 3d 0a 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|
  
<br></br>
##### stisvc



###### Service Triggers

|ID|Action|Data0|DataType0|GUID|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|||`c61fdd6b-0f81-d011-bec7-08002be2092f`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>  
<br></br>