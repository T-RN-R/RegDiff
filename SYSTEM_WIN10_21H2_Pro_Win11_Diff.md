
Win10 (21H2 19044.1706)
=======================

Table of contents
=================

* [](#)
	* [SYSTEM](#system)
		* [WMI AutoLoggers](#wmi-autologgers)
			* [BioEnrollment](#bioenrollment)
			* [EventLog-Application](#eventlog-application)
			* [EventLog-System](#eventlog-system)
			* [FaceCredProv](#facecredprov)
			* [FaceTel](#facetel)
			* [NetCore](#netcore)
			* [NtfsLog](#ntfslog)
			* [ReFSLog](#refslog)
			* [SetupPlatformTel](#setupplatformtel)
			* [SpoolerLogger](#spoolerlogger)
			* [WiFiSession](#wifisession)
		* [<span style="text-align: center; font-size:2em;">Services </span>](#span-styletext-align-center-font-size2emservices-span)
			* [<span style="text-align: center; font-size:2em;">ACPI Service </span>](#span-styletext-align-center-font-size2emacpi-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Appinfo Service </span>](#span-styletext-align-center-font-size2emappinfo-service-span)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">AppleSSD Service </span>](#span-styletext-align-center-font-size2emapplessd-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">BFE Service </span>](#span-styletext-align-center-font-size2embfe-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">cbdhsvc Service </span>](#span-styletext-align-center-font-size2emcbdhsvc-service-span)
			* [<span style="text-align: center; font-size:2em;">CldFlt Service </span>](#span-styletext-align-center-font-size2emcldflt-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">dcsvc Service </span>](#span-styletext-align-center-font-size2emdcsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">DeviceInstall Service </span>](#span-styletext-align-center-font-size2emdeviceinstall-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">disk Service </span>](#span-styletext-align-center-font-size2emdisk-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Dnscache Service </span>](#span-styletext-align-center-font-size2emdnscache-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">EapHost Service </span>](#span-styletext-align-center-font-size2emeaphost-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">ebdrv0 Service </span>](#span-styletext-align-center-font-size2emebdrv0-service-span)
			* [<span style="text-align: center; font-size:2em;">EhStorClass Service </span>](#span-styletext-align-center-font-size2emehstorclass-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">EventLog Service </span>](#span-styletext-align-center-font-size2emeventlog-service-span)
			* [<span style="text-align: center; font-size:2em;">ExecutionContext Service </span>](#span-styletext-align-center-font-size2emexecutioncontext-service-span)
			* [<span style="text-align: center; font-size:2em;">FrameServerMonitor Service </span>](#span-styletext-align-center-font-size2emframeservermonitor-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">fvevol Service </span>](#span-styletext-align-center-font-size2emfvevol-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">hidspi Service </span>](#span-styletext-align-center-font-size2emhidspi-service-span)
			* [<span style="text-align: center; font-size:2em;">HidSpiCx Service </span>](#span-styletext-align-center-font-size2emhidspicx-service-span)
			* [<span style="text-align: center; font-size:2em;">Hsp Service </span>](#span-styletext-align-center-font-size2emhsp-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">hvservice Service </span>](#span-styletext-align-center-font-size2emhvservice-service-span)
			* [<span style="text-align: center; font-size:2em;">IntelPMT Service </span>](#span-styletext-align-center-font-size2emintelpmt-service-span)
			* [<span style="text-align: center; font-size:2em;">iorate Service </span>](#span-styletext-align-center-font-size2emiorate-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">lfsvc Service </span>](#span-styletext-align-center-font-size2emlfsvc-service-span)
			* [<span style="text-align: center; font-size:2em;">McpManagementService Service </span>](#span-styletext-align-center-font-size2emmcpmanagementservice-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">mpi3drvi Service </span>](#span-styletext-align-center-font-size2emmpi3drvi-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">NDIS Service </span>](#span-styletext-align-center-font-size2emndis-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">NDKPerf Service </span>](#span-styletext-align-center-font-size2emndkperf-service-span)
			* [<span style="text-align: center; font-size:2em;">NPSMSvc Service </span>](#span-styletext-align-center-font-size2emnpsmsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">nvmedisk Service </span>](#span-styletext-align-center-font-size2emnvmedisk-service-span)
			* [<span style="text-align: center; font-size:2em;">P9NP Service </span>](#span-styletext-align-center-font-size2emp9np-service-span)
			* [<span style="text-align: center; font-size:2em;">P9Rdr Service </span>](#span-styletext-align-center-font-size2emp9rdr-service-span)
			* [<span style="text-align: center; font-size:2em;">P9RdrService Service </span>](#span-styletext-align-center-font-size2emp9rdrservice-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">partmgr Service </span>](#span-styletext-align-center-font-size2empartmgr-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">PcaSvc Service </span>](#span-styletext-align-center-font-size2empcasvc-service-span)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">pci Service </span>](#span-styletext-align-center-font-size2empci-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">PenService Service </span>](#span-styletext-align-center-font-size2empenservice-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">PerfDisk Service </span>](#span-styletext-align-center-font-size2emperfdisk-service-span)
			* [<span style="text-align: center; font-size:2em;">PerfNet Service </span>](#span-styletext-align-center-font-size2emperfnet-service-span)
			* [<span style="text-align: center; font-size:2em;">PerfOS Service </span>](#span-styletext-align-center-font-size2emperfos-service-span)
			* [<span style="text-align: center; font-size:2em;">PerfProc Service </span>](#span-styletext-align-center-font-size2emperfproc-service-span)
			* [<span style="text-align: center; font-size:2em;">PrintWorkflowUserSvc Service </span>](#span-styletext-align-center-font-size2emprintworkflowusersvc-service-span)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">PRM Service </span>](#span-styletext-align-center-font-size2emprm-service-span)
			* [<span style="text-align: center; font-size:2em;">RasMan Service </span>](#span-styletext-align-center-font-size2emrasman-service-span)
			* [<span style="text-align: center; font-size:2em;">rdyboost Service </span>](#span-styletext-align-center-font-size2emrdyboost-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">RemoteAccess Service </span>](#span-styletext-align-center-font-size2emremoteaccess-service-span)
			* [<span style="text-align: center; font-size:2em;">RetailDemo Service </span>](#span-styletext-align-center-font-size2emretaildemo-service-span)
			* [<span style="text-align: center; font-size:2em;">SecurityHealthService Service </span>](#span-styletext-align-center-font-size2emsecurityhealthservice-service-span)
			* [<span style="text-align: center; font-size:2em;">SensorService Service </span>](#span-styletext-align-center-font-size2emsensorservice-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">SNMPTrap Service </span>](#span-styletext-align-center-font-size2emsnmptrap-service-span)
			* [<span style="text-align: center; font-size:2em;">StiSvc Service </span>](#span-styletext-align-center-font-size2emstisvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">stornvme Service </span>](#span-styletext-align-center-font-size2emstornvme-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">TapiSrv Service </span>](#span-styletext-align-center-font-size2emtapisrv-service-span)
			* [<span style="text-align: center; font-size:2em;">TermService Service </span>](#span-styletext-align-center-font-size2emtermservice-service-span)
			* [<span style="text-align: center; font-size:2em;">TPM Service </span>](#span-styletext-align-center-font-size2emtpm-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">tzautoupdate Service </span>](#span-styletext-align-center-font-size2emtzautoupdate-service-span)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">UGatherer Service </span>](#span-styletext-align-center-font-size2emugatherer-service-span)
			* [<span style="text-align: center; font-size:2em;">UGTHRSVC Service </span>](#span-styletext-align-center-font-size2emugthrsvc-service-span)
			* [<span style="text-align: center; font-size:2em;">Usb4DeviceRouter Service </span>](#span-styletext-align-center-font-size2emusb4devicerouter-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Usb4HostRouter Service </span>](#span-styletext-align-center-font-size2emusb4hostrouter-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">usbhub Service </span>](#span-styletext-align-center-font-size2emusbhub-service-span)
			* [<span style="text-align: center; font-size:2em;">volmgr Service </span>](#span-styletext-align-center-font-size2emvolmgr-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">volsnap Service </span>](#span-styletext-align-center-font-size2emvolsnap-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">volume Service </span>](#span-styletext-align-center-font-size2emvolume-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WifiCx Service </span>](#span-styletext-align-center-font-size2emwificx-service-span)
			* [<span style="text-align: center; font-size:2em;">XblGameSave Service </span>](#span-styletext-align-center-font-size2emxblgamesave-service-span)
				* [Service Parameters](#service-parameters)
		* [WMI AutoLoggers](#wmi-autologgers)
			* [DataMarket](#datamarket)
			* [EventLog-Application](#eventlog-application)
			* [EventLog-System](#eventlog-system)
			* [LwtNetLog](#lwtnetlog)
			* [NtfsLog](#ntfslog)
			* [SQMLogger](#sqmlogger)
			* [WiFiSession](#wifisession)
			* [WinPhoneCritical](#winphonecritical)
		* [<span style="text-align: center; font-size:2em;">Services </span>](#span-styletext-align-center-font-size2emservices-span)
			* [<span style="text-align: center; font-size:2em;">BluetoothUserService Service </span>](#span-styletext-align-center-font-size2embluetoothuserservice-service-span)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">BthEnum Service </span>](#span-styletext-align-center-font-size2embthenum-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">BthLEEnum Service </span>](#span-styletext-align-center-font-size2embthleenum-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">BTHPORT Service </span>](#span-styletext-align-center-font-size2embthport-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">dmwappushservice Service </span>](#span-styletext-align-center-font-size2emdmwappushservice-service-span)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">Eaphost Service </span>](#span-styletext-align-center-font-size2emeaphost-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">EventLog Service </span>](#span-styletext-align-center-font-size2emeventlog-service-span)
			* [<span style="text-align: center; font-size:2em;">FrameServer Service </span>](#span-styletext-align-center-font-size2emframeserver-service-span)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">HomeGroupListener Service </span>](#span-styletext-align-center-font-size2emhomegrouplistener-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">HomeGroupProvider Service </span>](#span-styletext-align-center-font-size2emhomegroupprovider-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">hvservice Service </span>](#span-styletext-align-center-font-size2emhvservice-service-span)
			* [<span style="text-align: center; font-size:2em;">Lsa Service </span>](#span-styletext-align-center-font-size2emlsa-service-span)
			* [<span style="text-align: center; font-size:2em;">LSI_SSS Service </span>](#span-styletext-align-center-font-size2emlsi_sss-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">megasas Service </span>](#span-styletext-align-center-font-size2emmegasas-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">mshidkmdf Service </span>](#span-styletext-align-center-font-size2emmshidkmdf-service-span)
			* [<span style="text-align: center; font-size:2em;">MSSCNTRS Service </span>](#span-styletext-align-center-font-size2emmsscntrs-service-span)
			* [<span style="text-align: center; font-size:2em;">NlaSvc Service </span>](#span-styletext-align-center-font-size2emnlasvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">RFCOMM Service </span>](#span-styletext-align-center-font-size2emrfcomm-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">SensorService Service </span>](#span-styletext-align-center-font-size2emsensorservice-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">SharedAccess Service </span>](#span-styletext-align-center-font-size2emsharedaccess-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">SNMPTRAP Service </span>](#span-styletext-align-center-font-size2emsnmptrap-service-span)
			* [<span style="text-align: center; font-size:2em;">stisvc Service </span>](#span-styletext-align-center-font-size2emstisvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Synth3dVsc Service </span>](#span-styletext-align-center-font-size2emsynth3dvsc-service-span)
			* [<span style="text-align: center; font-size:2em;">TapiSrv Service </span>](#span-styletext-align-center-font-size2emtapisrv-service-span)
			* [<span style="text-align: center; font-size:2em;">Telemetry Service </span>](#span-styletext-align-center-font-size2emtelemetry-service-span)
			* [<span style="text-align: center; font-size:2em;">wcnfs Service </span>](#span-styletext-align-center-font-size2emwcnfs-service-span)
				* [Service Parameters](#service-parameters)

# 

## SYSTEM
  
<br></br><br></br>Added
### WMI AutoLoggers
  

---
<br></br>
#### BioEnrollment
  
Start : `0x00`
|Enabled|guid|
| :---: | :---: |
|None|Start|
|0x00|{4b8b1947-ae4d-54e2-826a-1aee78ef05b2}|
|0x00|{a55d5a23-1a5b-580a-2be5-d7188f43fae1}|
  

---
<br></br>
#### EventLog-Application

|EnableLevel|EnableProperty|Enabled|LoggerName|MatchAllKeyword|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{04d66358-c4a1-419b-8023-23b73902de2c}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{15f4cd44-ca53-5422-db17-4e76821b5a69}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x2000000000000000|{6e0df32c-7f11-54f7-e8ee-5ad4032727ce}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{7628e972-6d6f-4974-b58f-6428622ec09a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x2000000000000000|{7d44233d-3055-4b9c-ba64-0d47ca40a232}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{9068a924-f97e-5506-c3a3-5c020c00e8e0}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{a70ff94f-570b-4979-ba5c-e59c9feab61b}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{ad8aa069-a01b-40a0-ba40-948d1d8dedc5}|
  

---
<br></br>
#### EventLog-System

|EnableLevel|EnableProperty|Enabled|LoggerName|MatchAllKeyword|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{0075e1ab-e1d1-5d1f-35f5-da36fb4f41b1}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{17d2a329-4539-5f4d-3435-f510634ce3b9}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{5bcf2a5c-2e90-5a03-aa4e-2e459bae21b4}|
|0x00|0x01|0x01|EventLog-System|0x00|0x2000000000000000|{6600e712-c3b6-44a2-8a48-935c511f28c8}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{7f54ca8a-6c72-5cbc-b96f-d0ef905b8bce}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{87a623f0-8db5-5c11-7c80-a2ebbcbe5189}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{93db76c2-63ab-5de1-88b3-c068686675b8}|
|0x00|0x01|0x01|EventLog-System|0x00|0x2000000000000000|{9799276c-fb04-47e8-845e-36946045c218}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{a2d34bf1-70ab-5b21-c819-5a0dd42748fd}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{b931ed29-66f4-576e-0579-0b8818a5dc6b}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{bcf0c6a7-6130-5208-f27d-fa77a91f12df}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{d07e8c3f-78fb-4c22-b77c-2203d00bfdf3}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{f6cf91be-e7d7-57d6-2a3d-278ca406d190}|
  

---
<br></br>
#### FaceCredProv
  
Start : `0x00`
|Enabled|guid|
| :---: | :---: |
|None|Start|
|0x00|{1D480C11-3870-4B19-9144-47A53CD973BD}|
  

---
<br></br>
#### FaceTel
  
Start : `0x00`
|Enabled|guid|
| :---: | :---: |
|None|Start|
|0x00|{22eb0808-0b6c-5cd4-5511-6a77e6e73a93}|
  

---
<br></br>
#### NetCore

|@|EnableLevel|Enabled|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: | :---: |
|triage_routepolicymanagement_tracelogging|0x05|0x01|0x00|{923C0FFD-7933-4B52-8A49-121ABF2DC357}|
  

---
<br></br>
#### NtfsLog

|EnableFlags|EnableLevel|Enabled|_Description|guid|
| :---: | :---: | :---: | :---: | :---: |
|0x0f|0x05|0x01|TmLog Trace Provider|{aa381297-bccb-4569-8e39-bbbb3b400893}|
  

---
<br></br>
#### ReFSLog
  
ClockType : `0x02`  
GUID : `{81a69395-9f48-48f2-b88c-2401db1e3a91}`  
Start : `0x01`
|EnableFlags|EnableLevel|Enabled|_Description|guid|
| :---: | :---: | :---: | :---: | :---: |
|None|None|None|None|ClockType|
|None|None|None|None|GUID|
|None|None|None|None|Start|
|0x07|0x03|0x01|ReFS WPP Trace|{740f3c34-57df-4bad-8eea-72ac69ad5df5}|
  

---
<br></br>
#### SetupPlatformTel

|EnableLevel|Enabled|guid|
| :---: | :---: | :---: |
|0xff|0x01|{D2F37B94-92A5-44E2-AFC9-2F4489D39268}|
  

---
<br></br>
#### SpoolerLogger

|EnableFlags|EnableLevel|Enabled|guid|
| :---: | :---: | :---: | :---: |
|0x00|0x05|0x01|{ba4936a1-31db-4edc-89ce-9190e3c0653b}|
  

---
<br></br>
#### WiFiSession

|EnableLevel|Enabled|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: |
|0x05|0x01|0x00|{745976be-5e09-5c76-eabd-76c93c9212d2}|
|0x05|0x01|0x00|{ae164ede-2246-5b24-c145-29c484f7362a}|
|0x05|0x01|0x00|{EA893635-5AB7-562B-75A2-A22107D8058F}|
  

---
<br></br>  
<br></br>
### <span style="text-align: center; font-size:2em;">Services </span>
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ACPI Service </span>



##### Service Parameters
  
PnpAsyncNewDevices : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Appinfo Service </span>



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`0f738e20-73c0-4ca8-aa6a-8dfef545fea8`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AppleSSD Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\AppleSSD.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`SCSI Miniport`|`0x01`|`@AppleSSD.inf,%DevDesc1%;Apple Solid State Drive Device`|`AppleSSD.inf`|



##### Service Parameters
  
BusType : `0x01`  
Device : `{'MaxTranLenInPages': 64}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BFE Service </span>



##### Service Parameters
  
Policy  
Persistent  
ProviderContext
|GUID|Data|
| :---: | :---: |
|{30433c31-b05f-421f-8fde-018ea4c68af4}|`01 10 08 00 cc cc cc cc 10 01 00 00 00 00 00 00 00 00 02 00 01 00 00 00 f0 00 00 00 04 00 02 00 00 00 00 00 00 00 00 00 f0 00 00 00 01 10 08 00 cc cc cc cc e0 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 31 3c 43 30 5f b0 1f 42 8f de 01 8e a4 c6 8a f4 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 00 00 00 00 00 00 00 00 08 00 00 00 08 00 00 00 10 00 02 00 00 00 00 00 05 00 00 00 00 00 00 80 07 00 00 00 00 00 00 00 07 00 00 00 4d 00 50 00 53 00 53 00 56 00 43 00 00 00 00 00 15 00 00 00 00 00 00 00 15 00 00 00 53 00 74 00 6f 00 72 00 65 00 73 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 20 00 6f 00 72 00 69 00 67 00 69 00 6e 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 26 00 00 00 14 00 02 00 26 00 00 00 51 00 75 00 61 00 72 00 61 00 6e 00 74 00 69 00 6e 00 65 00 20 00 44 00 65 00 66 00 61 00 75 00 6c 00 74 00 00 00 00 00 00 00 00 00`|
|{93132c36-6e06-4e6f-a10b-218787cd49cf}|`01 10 08 00 cc cc cc cc 10 01 00 00 00 00 00 00 00 00 02 00 01 00 00 00 f0 00 00 00 04 00 02 00 00 00 00 00 00 00 00 00 f0 00 00 00 01 10 08 00 cc cc cc cc e0 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 36 2c 13 93 06 6e 6f 4e a1 0b 21 87 87 cd 49 cf 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 00 00 00 00 00 00 00 00 08 00 00 00 08 00 00 00 10 00 02 00 00 00 00 00 06 00 00 00 00 00 00 80 07 00 00 00 00 00 00 00 07 00 00 00 4d 00 50 00 53 00 53 00 56 00 43 00 00 00 00 00 15 00 00 00 00 00 00 00 15 00 00 00 53 00 74 00 6f 00 72 00 65 00 73 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 20 00 6f 00 72 00 69 00 67 00 69 00 6e 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 22 00 00 00 14 00 02 00 22 00 00 00 42 00 6f 00 6f 00 74 00 74 00 69 00 6d 00 65 00 20 00 44 00 65 00 66 00 61 00 75 00 6c 00 74 00 00 00 00 00 00 00 00 00 00 00 00 00`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">cbdhsvc Service </span>

|DelayedAutoStart|
| :---: |
|`0x01`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CldFlt Service </span>



##### Service Parameters
  
USMsgTimeoutMillis : `0x3e8`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">dcsvc Service </span>

|DelayedAutoStart|DependOnService|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`0x01`|`rpcss`|`@%systemroot%\system32\dcsvc.dll,-101`|`@%systemroot%\system32\dcsvc,-100`|`SERVICE_ERROR_NORMAL`|`80 51 01 00 00 00 00 00 00 00 00 00 04 00 00 00 14 00 00 00 01 00 00 00 10 27 00 00 01 00 00 00 10 27 00 00 01 00 00 00 10 27 00 00 00 00 00 00 00 00 00 00`|`%systemroot%\system32\svchost.exe -k netsvcs -p`|`LocalSystem`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|



##### Service Parameters
  
IdleTimeout(sec) : `0x78`  
ServiceDll : `%SystemRoot%\system32\dcsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`59beb977-d037-48f4-af74-ca075493a523`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`0a0db614-e9fb-48cf-9143-7ae718ff2c83`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DeviceInstall Service </span>



##### Service Parameters
  
DeviceInstallMode : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">disk Service </span>



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Dnscache Service </span>



##### Service Parameters
  
DohWellKnownServers : `{'1.0.0.1': {'Template': 'https://cloudflare-dns.com/dns-query'}, '1.1.1.1': {'Template': 'https://cloudflare-dns.com/dns-query'}, '149.112.112.112': {'Template': 'https://dns.quad9.net/dns-query'}, '2001:4860:4860::8844': {'Template': 'https://dns.google/dns-query'}, '2001:4860:4860::8888': {'Template': 'https://dns.google/dns-query'}, '2606:4700:4700::1001': {'Template': 'https://cloudflare-dns.com/dns-query'}, '2606:4700:4700::1111': {'Template': 'https://cloudflare-dns.com/dns-query'}, '2620:fe::fe': {'Template': 'https://dns.quad9.net/dns-query'}, '2620:fe::fe:9': {'Template': 'https://dns.quad9.net/dns-query'}, '8.8.4.4': {'Template': 'https://dns.google/dns-query'}, '8.8.8.8': {'Template': 'https://dns.google/dns-query'}, '9.9.9.9': {'Template': 'https://dns.quad9.net/dns-query'}}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">EapHost Service </span>

|DependOnService|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`RPCSSKeyIso`|`@%systemroot%\system32\eapsvc.dll,-2`|`@%systemroot%\system32\eapsvc.dll,-1`|`SERVICE_ERROR_NORMAL`|`80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 c0 d4 01 00 00 00 00 00 00 00 00 00`|`%SystemRoot%\System32\svchost.exe -k netsvcs -p`|`localSystem`|`['SeTcbPrivilege', 'SeDebugPrivilege', 'SeImpersonatePrivilege']`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_SHARE_PROCESS`|
  
Methods : `{'311': {'Name': 'Microsoft', '18': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '21': {'PeerConfigUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\TtlsAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\TtlsCfg.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 389863599, 'LANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}, 'WLANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}, '23': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1002', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '254': {'14122': {'1': {'PeerDllPath': '%SystemRoot%\\System32\\WcnEapPeerProxy.dll', 'PeerFriendlyName': 'Windows Connect Now EAP Peer', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 8683520}}}, '50': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1003', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '55': {'PeerConfigUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerDllPath': '%SystemRoot%\\System32\\EapTeapAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\EapTeapAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'Properties': 1065154751, 'LANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}, 'WLANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="utf-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><TrustedRootCAHash></TrustedRootCAHash></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection> </CertificateStore> </CredentialsSource><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="utf-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><TrustedRootCAHash></TrustedRootCAHash></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}}}`


##### Service Parameters
  
PeerInstalled : `0x01`  
ServiceDll : `%SystemRoot%\System32\eapsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
EapProvPlugin : `{'(Default)': '%SystemRoot%\\System32\\eapprovp.dll', 'DllEntryPoint': 'EapProvPlugGetInfo'}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ebdrv0 Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\evbd0a.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`System Bus Extender`|`0x03`|`@netevbd0a.inf,%vbd_srv_desc%;QLogic Legacy Ethernet Adapter VBD`|`netevbd0a.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">EhStorClass Service </span>



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">EventLog Service </span>

|Application|System|
| :---: | :---: |
|`{'Microsoft-Windows-PDH': {'ProviderGuid': '{04d66358-c4a1-419b-8023-23b73902de2c}', 'EventMessageFile': '%SystemRoot%\\system32\\pdh.dll'}, 'Universal Print': {'EventMessageFile': '%SystemRoot%\\System32\\McpManagementService.dll', 'TypesSupported': 7}}`|`{'AppleSSD': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'ebdrv0': {'eventmessagefile': '%SystemRoot%\\System32\\drivers\\evbd0a.sys;%SystemRoot%\\System32\\iologmsg.dll', 'typessupported': 7}, 'EventLog': {'EventMessageFile': '%SystemRoot%\\System32\\netevent.dll', 'TypesSupported': 7}, 'hvservice': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'Microsoft-Windows-Iphlpsvc-Trace': {'ProviderGuid': '{6600e712-c3b6-44a2-8a48-935c511f28c8}', 'EventMessageFile': '%windir%\\system32\\iphlpsvc.dll'}, 'Microsoft-Windows-Network-ExecutionContext': {'ProviderGuid': '{0075e1ab-e1d1-5d1f-35f5-da36fb4f41b1}', 'EventMessageFile': '%SystemRoot%\\system32\\drivers\\ExecutionContext.sys'}, 'Microsoft-Windows-USB-USB4DeviceRouter-EventLogs': {'ProviderGuid': '{d07e8c3f-78fb-4c22-b77c-2203d00bfdf3}', 'EventMessageFile': '%SystemRoot%\\System32\\DriverStore\\FileRepository\\usb4devicerouter.inf_amd64_3bffb5f5105936e5\\Usb4DeviceRouter.sys'}, 'mpi3drvi': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'nvmedisk': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll;%SystemRoot%\\System32\\drivers\\nvmedisk.sys', 'TypesSupported': 7}}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ExecutionContext Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\System32\Drivers\ExecutionContext.sys,-101`|`SERVICE_ERROR_NORMAL`|`System`|`System32\Drivers\ExecutionContext.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">FrameServerMonitor Service </span>

|DependOnService|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`rpcss`|`@%systemroot%\system32\FrameServerMonitor.dll,-101`|`@%systemroot%\system32\FrameServerMonitor.dll,-100`|`SERVICE_ERROR_NORMAL`|`80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 20 bf 02 00`|`%SystemRoot%\System32\svchost.exe -k CameraMonitor`|`LocalSystem`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\FrameServerMonitor.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`BE0D95BA-21A5-4A5F-A1F0-9ADA84AC1144`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 26 1d 90 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 21 bc a3 2e 0f 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`773732e5-76f9-5b4f-9b55-b94699c46e44`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`d752e524-2365-f747-a647-d3465bf1f5ca`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 b8 bc a3 3d 01 c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">fvevol Service </span>



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">hidspi Service </span>

|DependOnService|
| :---: |
|`HidSpiCx`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HidSpiCx Service </span>

|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: |
|`HidSpi KMDF Class Extension`|`SERVICE_ERROR_NORMAL`|`system32\drivers\HidSpiCx.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Hsp Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\Hsp.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@hsp.inf,%Hsp.SVCDESC%;Microsoft Pluton Service`|`hsp.inf`|



##### Service Parameters
  
Wdf : `{'KmdfLibraryVersion': '1.15'}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">hvservice Service </span>

|Owners|
| :---: |
|`hvservice.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">IntelPMT Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\IntelPMT.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`Core Security Extensions`|`0x02`|`@intelpmt.inf,%IntelPMT.SVCDESC%;Intel(R) Platform Monitoring Technology Service`|`intelpmt.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iorate Service </span>



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">lfsvc Service </span>

|Settings|
| :---: |
|`{'LocationWebServiceProxy': {'USE_CLIENT_PROXY_INFERENCE_ONLY': 0}}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">McpManagementService Service </span>

|DependOnService|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`RpcSs`|`@%SystemRoot%\system32\McpManagementService.dll,-101`|`@%SystemRoot%\system32\McpManagementService.dll,-100`|`SERVICE_ERROR_NORMAL`|`80 51 01 00 00 00 00 00 00 00 00 00 01 00 00 00 14 00 00 00 00 00 00 00 00 00 00 00`|`%SystemRoot%\system32\svchost.exe -k McpManagementServiceGroup`|`LocalSystem`|`['SeTcbPrivilege', 'SeChangeNotifyPrivilege', 'SeImpersonatePrivilege', 'SeCreateGlobalPrivilege']`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\McpManagementService.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mpi3drvi Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\mpi3drvi.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`SCSI Miniport`|`0x10`|`mpi3drvi.inf`|



##### Service Parameters
  
BusType : `0x08`  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NDIS Service </span>



##### Service Parameters
  
Reserved : `{'ExecutionContextProfiles': {'Balanced': {'DpcWatchdogTimerThreshold': 80, 'Flags': 0, 'MaxPacketsReceiveAtDispatch': 64, 'MaxPacketsReceiveAtPassive': 64, 'MaxPacketsReceiveCompleteAtDispatch': 64, 'MaxPacketsReceiveCompleteAtPassive': 64, 'MaxPacketsSendAtDispatch': 64, 'MaxPacketsSendAtPassive': 64, 'MaxPacketsSendCompleteAtDispatch': 64, 'MaxPacketsSendCompleteAtPassive': 64, 'MaxTimeAtDispatch': 0, 'WorkerThreadPriority': 10}}}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NDKPerf Service </span>

|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: |
|`NDKPerf Driver`|`SERVICE_ERROR_NORMAL`|`system32\drivers\NDKPerf.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NPSMSvc Service </span>

|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\npsm.dll,-101`|`@%SystemRoot%\system32\npsm.dll,-100`|`SERVICE_ERROR_NORMAL`|`80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 b8 0b 00 00 01 00 00 00 b8 0b 00 00 00 00 00 00 00 00 00 00`|`%SystemRoot%\system32\svchost.exe -k LocalService -p`|`NT AUTHORITY\LocalService`|`['SeImpersonatePrivilege']`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`96`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\npsm.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x100
    SID: S-1-0-11
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">nvmedisk Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\nvmedisk.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`@nvmedisk.inf,%nvmedisk.SvcDesc%;Microsoft NVMe disk driver`|`nvmedisk.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">P9NP Service </span>

|Description|DisplayName|NetworkProvider|
| :---: | :---: | :---: |
|`@%systemroot%\system32\p9np.dll,-101`|`@%systemroot%\system32\p9np.dll,-100`|`{'DeviceName': '\\Device\\P9Rdr', 'DisplayName': '@%systemroot%\\system32\\p9np.dll,-100', 'Name': 'Plan 9 Network Provider', 'ProviderPath': '%SystemRoot%\\System32\\p9np.dll', 'TriggerStartCompleteNotification': b'u\x10\xbc\xa3T\x1e\xc6A', 'TriggerStartNotification': b'u\x08\xbc\xa3T\x1e\xc6A', 'TriggerStartPrefix': b'w\x00s\x00l\x00.\x00l\x00o\x00c\x00a\x00l\x00h\x00o\x00s\x00t\x00\x00\x00w\x00s\x00l\x00$\x00\x00\x00\x00\x00'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">P9Rdr Service </span>

|DependOnService|Description|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`RDBSS`|`@%SystemRoot%\System32\drivers\p9rdr.sys,-101`|`@%SystemRoot%\System32\drivers\p9rdr.sys,-100`|`SERVICE_ERROR_NORMAL`|`System32\drivers\p9rdr.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">P9RdrService Service </span>

|DependOnService|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|ServiceSidType|Start|Type|UserServiceFlags|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`P9RdrRPCSS`|`@%systemroot%\system32\p9rdrservice.dll,-101`|`@%systemroot%\system32\p9rdrservice.dll,-102`|`SERVICE_ERROR_NORMAL`|`80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 b8 0b 00 00 01 00 00 00 b8 0b 00 00 00 00 00 00 00 00 00 00`|`%systemroot%\system32\svchost.exe -k P9RdrService -p`|`LocalSystem`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`96`|`0x03`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\p9rdrservice.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 54 1e c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">partmgr Service </span>



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PcaSvc Service </span>



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 d0 be a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 18 bc a3 2e 07 c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 2e 03 96 15`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">pci Service </span>



##### Service Parameters
  
PnpAsyncNewDevices : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PenService Service </span>

|Description|DisplayName|ErrorControl|FailureActions|ImagePath|Start|Type|UserServiceFlags|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\PenService.dll,-101`|`@%SystemRoot%\system32\PenService.dll,-100`|`SERVICE_ERROR_NORMAL`|`80 51 01 00 00 00 00 00 00 00 00 00 02 00 00 00 14 00 00 00 01 00 00 00 10 27 00 00 00 00 00 00 00 00 00 00`|`%SystemRoot%\system32\svchost.exe -k PenService`|`SERVICE_DEMAND_START`|`96`|`0x02`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\PenService.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|Data1|Data2|Data3|DataType0|DataType1|DataType2|DataType3|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`b2551e4d-6ff1-cf11-88cb-001111000030`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|`HID_DEVICE_UP:000D_U:0001`|`HID_DEVICE_UP:000D_U:0002`|`HID_DEVICE_UP:000D_U:0003`|`HID_DEVICE_UP:000D_U:000F`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PerfDisk Service </span>

|Performance|
| :---: |
|`{'Collect Supports Metadata': 1}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PerfNet Service </span>

|Performance|
| :---: |
|`{'Collect Supports Metadata': 1}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PerfOS Service </span>

|Performance|
| :---: |
|`{'Collect Supports Metadata': 1}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PerfProc Service </span>

|Performance|
| :---: |
|`{'Collect Supports Metadata': 1}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PrintWorkflowUserSvc Service </span>



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 3d 0a 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PRM Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\DriverStore\FileRepository\prm.inf_amd64_7fc9bb8ba2b73803\PRM.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`@prm.inf,%PRM.SvcDesc%;Microsoft PRM Driver`|`prm.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RasMan Service </span>

|PPP|
| :---: |
|`{'EAP': {'13': {'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '25': {'LANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">25</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>25</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV1"><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><FastReconnect>true</FastReconnect><InnerEapOptional>false</InnerEapOptional><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap><EnableQuarantineChecks>false</EnableQuarantineChecks><RequireCryptoBinding>false</RequireCryptoBinding><PeapExtensions><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</AcceptServerName><IdentityPrivacy xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2"><EnableIdentityPrivacy>true</EnableIdentityPrivacy><AnonymousUserName>anonymous</AnonymousUserName></IdentityPrivacy></PeapExtensions></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">25</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>25</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV1"><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><FastReconnect>true</FastReconnect><InnerEapOptional>false</InnerEapOptional><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap><EnableQuarantineChecks>false</EnableQuarantineChecks><RequireCryptoBinding>false</RequireCryptoBinding><PeapExtensions><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</AcceptServerName><IdentityPrivacy xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2"><EnableIdentityPrivacy>true</EnableIdentityPrivacy><AnonymousUserName>anonymous</AnonymousUserName></IdentityPrivacy></PeapExtensions></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}}}}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">rdyboost Service </span>



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RemoteAccess Service </span>

|Performance|
| :---: |
|`{'Object List': '7584 7620'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RetailDemo Service </span>

|StateFlags|
| :---: |
|`0x01`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SecurityHealthService Service </span>
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf00ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SensorService Service </span>



##### Service Parameters
  
Sensors : `{'{934F17E7-42EF-470B-BE7C-1AD0983C9E6C}': {'RequiredHingeJointsCount': 1, 'RequiredPanelGroupsCount': 2, 'SensorType': '{0D49D945-FA83-4630-A22C-01387F906DE6}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}, '{AEDD7472-297F-4285-B2FB-9422731BCDA6}': {'RequiredHingeJointsCount': 2, 'RequiredPanelGroupsCount': 3, 'SensorType': '{0D49D945-FA83-4630-A22C-01387F906DE6}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}}`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`D09BDEB5-6171-4A34-BFE2-06FA82652568:8489BE1C-80A4-48BC-901A-AA91BD827A7C`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`DB2CE634-191D-42AF-A28C-16BE97924CA7`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|6|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`97BE9507-17DA-4999-87D7-66C0B2D83CC7`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|7|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`6328DCC4-1658-4133-8062-A9943DAC2093`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SNMPTrap Service </span>

|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@firewallapi.dll,-50324`|`@firewallapi.dll,-50323`|`SERVICE_ERROR_NORMAL`|`ff ff ff ff 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 60 ea 00 00 00 00 00 00 00 00 00 00`|`%SystemRoot%\System32\snmptrap.exe`|`NT AUTHORITY\LocalService`|`['SeChangeNotifyPrivilege']`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">StiSvc Service </span>

|DependOnService|Description|DisplayName|ErrorControl|ImagePath|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`RpcSs`|`@%SystemRoot%\system32\wiaservc.dll,-10`|`@%SystemRoot%\system32\wiaservc.dll,-9`|`SERVICE_ERROR_NORMAL`|`%SystemRoot%\system32\svchost.exe -k imgsvc`|`NT Authority\LocalService`|`['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege']`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wiaservc.dll`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x100
    SID: S-1-0-11
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`c61fdd6b-0f81-d011-bec7-08002be2092f`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">stornvme Service </span>



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TapiSrv Service </span>

|Performance|
| :---: |
|`{'Object List': '1150'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TermService Service </span>

|Performance|
| :---: |
|`{'Collect Supports Metadata': 1}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TPM Service </span>



##### Service Parameters
  
KsrGuid : `{F141DC89-3D00-450A-B2D2-AD995267F8FC}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">tzautoupdate Service </span>

|StateFlags|
| :---: |
|`0x01`|



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 58 bc a3 3e 06 83 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 30 bc a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|6|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 d0 be a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UGatherer Service </span>

|Performance|
| :---: |
|`{'Object List': '7654'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UGTHRSVC Service </span>

|Performance|
| :---: |
|`{'Object List': '7760'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Usb4DeviceRouter Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\DriverStore\FileRepository\usb4devicerouter.inf_amd64_3bffb5f5105936e5\Usb4DeviceRouter.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x15`|`@Usb4DeviceRouter.inf,%Usb4DeviceRouter.SVCDESC%;USB4 Device Router Service`|`Usb4DeviceRouter.inf`|



##### Service Parameters
  
ForceLogsInMiniDump : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Usb4HostRouter Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\DriverStore\FileRepository\usb4hostrouter.inf_amd64_dd61aa4ab70fa4fb\Usb4HostRouter.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@Usb4HostRouter.inf,%Usb4HostRouter.SVCDESC%;USB4 Host Router Service`|`Usb4HostRouter.inf`|



##### Service Parameters
  
DmaRemappingCompatible : `0x01`  
ForceLogsInMiniDump : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">usbhub Service </span>

|Performance|
| :---: |
|`{'Object List': '9956'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">volmgr Service </span>



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">volsnap Service </span>



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">volume Service </span>



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WifiCx Service </span>

|DependOnService|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`NetAdapterCx`|`Wifi Network Adapter Class Extension`|`SERVICE_ERROR_NORMAL`|`system32\drivers\WifiCx.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">XblGameSave Service </span>



##### Service Parameters
  
FeatureLevel : `0x01`  
<br></br>  

---
<br></br>  
<br></br>  
<br></br><br></br>Deleted
### WMI AutoLoggers
  

---
<br></br>
#### DataMarket
  
BufferSize : `0x50`  
ClockType : `0x01`  
FileMax : `0x04`  
FileName : `%SystemRoot%\System32\LogFiles\WMI\DataMarket.etl`  
Guid : `{4D89A833-DFB3-4774-94ED-7BFA5864A83F}`  
LogFileMode : `0x80000002`  
MaxFileSize : `0x0c`  
MaximumBuffers : `0x10`  
MinimumBuffers : `0x02`  
Start : `0x00`
|EnableLevel|Enabled|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: |
|None|None|None|BufferSize|
|None|None|None|ClockType|
|None|None|None|FileMax|
|None|None|None|FileName|
|None|None|None|Guid|
|None|None|None|LogFileMode|
|None|None|None|MaxFileSize|
|None|None|None|MaximumBuffers|
|None|None|None|MinimumBuffers|
|None|None|None|Start|
|0x04|0x00|0xff00000000000000|{B1D067C7-2F8C-436E-9E82-C5C2C22229D5}|
  

---
<br></br>
#### EventLog-Application

|EnableLevel|EnableProperty|Enabled|LoggerName|MatchAllKeyword|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{28e25b07-c47f-473d-8b24-2e171cca808a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{579402a2-883c-45d8-b70a-9bc856407751}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{83d6e83b-900b-48a3-9835-57656b6f6474}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{973143dd-f3c7-4ef5-b156-544ac38c39b6}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{9f973c1d-d056-4e38-84a5-7be81cdd6ab6}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{af0a5a6d-e009-46d4-8867-42f2240f8a72}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{f43c3c35-22e2-53eb-f169-07594054779e}|
  

---
<br></br>
#### EventLog-System

|EnableLevel|EnableProperty|Enabled|LoggerName|MatchAllKeyword|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{2bef5442-d402-5a72-58e1-cb7e491bf179}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{3903d5b9-988d-4c31-9ccd-4022f96703f0}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{928f7d29-0577-5be5-3bd3-b6bdab9ab307}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{9f7b5df4-b902-48bc-bc94-95068c6c7d26}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{b99317e5-89b7-4c0d-abd1-6e705f7912dc}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{c18672d1-dc18-4dfd-91e4-170cf37160cf}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{ea216962-877b-5b73-f7c5-8aef5375959e}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{ed8cc261-2123-567e-063e-75fc5f8e8a48}|
  

---
<br></br>
#### LwtNetLog

|EnableLevel|Enabled|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: |
|0x04|0x01|0x01|{7868B0D4-1423-4681-AFDF-27913575441E}|
  

---
<br></br>
#### NtfsLog

|EnableFlags|EnableLevel|Enabled|_Description|guid|
| :---: | :---: | :---: | :---: | :---: |
|0x07|0x03|0x01|ReFS WPP Trace|{740f3c34-57df-4bad-8eea-72ac69ad5df5}|
  

---
<br></br>
#### SQMLogger

|EnableLevel|EnableProperty|Enabled|LoggerName|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{017BA13C-9A55-4f1f-8200-323055AAC810}|
  

---
<br></br>
#### WiFiSession

|EnableLevel|Enabled|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: |
|0x05|0x01|0x00|{60523747-6516-48B7-84B1-3264FA2CB359}|
  

---
<br></br>
#### WinPhoneCritical

|EnableLevel|EnableProperty|Enabled|LoggerName|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0x02|0x02|0x01|SmsRouter|0x00|{A9C11050-9E93-4fa4-8FE0-7C4750A345B2}|
  

---
<br></br>  
<br></br>
### <span style="text-align: center; font-size:2em;">Services </span>
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BluetoothUserService Service </span>



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 68 bc a3 2f 02 92 09`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BthEnum Service </span>



##### Service Parameters
  
Policy  
PM_AllowBluetooth : `0x02`  
PM_AllowDiscoverableMode : `0x01`  
PM_AllowConnectableMode : `0x01`  
PM_AllowAdvertising : `0x01`  
PM_AllowOutOfBandPairing : `0x01`  
PM_LinkSecurityLevel : `0x00`  
PM_LocalDeviceName : ``  
PM_DevicesAllowedList : `00`  
PM_ServicesAllowedList : `00`  
PM_RequireRestrictedMode : `0x00`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BthLEEnum Service </span>



##### Service Parameters
  
Policy  
PM_AllowBluetooth : `0x02`  
PM_AllowDiscoverableMode : `0x01`  
PM_AllowConnectableMode : `0x01`  
PM_AllowAdvertising : `0x01`  
PM_AllowOutOfBandPairing : `0x01`  
PM_LinkSecurityLevel : `0x00`  
PM_LocalDeviceName : ``  
PM_DevicesAllowedList : `00`  
PM_ServicesAllowedList : `00`  
PM_RequireRestrictedMode : `0x00`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BTHPORT Service </span>



##### Service Parameters
  
Policy  
PM_AllowBluetooth : `0x02`  
PM_AllowDiscoverableMode : `0x01`  
PM_AllowConnectableMode : `0x01`  
PM_AllowAdvertising : `0x01`  
PM_AllowOutOfBandPairing : `0x01`  
PM_LinkSecurityLevel : `0x00`  
PM_LocalDeviceName : ``  
PM_DevicesAllowedList : `00`  
PM_ServicesAllowedList : `00`  
PM_RequireRestrictedMode : `0x00`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">dmwappushservice Service </span>

|RequiredPrivileges|
| :---: |
|`['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege', 'SeIncreaseWorkingSetPrivilege']`|



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`0a0db614-e9fb-48cf-9143-7ae718ff2c83`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 90 bc a3 28 00 92 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Eaphost Service </span>

|DependOnService|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`RPCSSKeyIso`|`@%systemroot%\system32\eapsvc.dll,-2`|`@%systemroot%\system32\eapsvc.dll,-1`|`SERVICE_ERROR_NORMAL`|`80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 c0 d4 01 00 00 00 00 00 00 00 00 00`|`%SystemRoot%\System32\svchost.exe -k netsvcs -p`|`localSystem`|`['SeTcbPrivilege', 'SeDebugPrivilege', 'SeImpersonatePrivilege']`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_SHARE_PROCESS`|
  
Methods : `{'311': {'Name': 'Microsoft', '18': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '21': {'PeerConfigUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\TtlsAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\TtlsCfg.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 389863599, 'WLANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames></ServerNames></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}, '23': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1002', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '254': {'14122': {'1': {'PeerDllPath': '%SystemRoot%\\System32\\WcnEapPeerProxy.dll', 'PeerFriendlyName': 'Windows Connect Now EAP Peer', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 8683520}}}, '50': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1003', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '55': {'PeerConfigUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerDllPath': '%SystemRoot%\\System32\\EapTeapAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\EapTeapAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'Properties': 1065154751}}}`


##### Service Parameters
  
PeerInstalled : `0x01`  
ServiceDll : `%SystemRoot%\System32\eapsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
EapProvPlugin : `{'(Default)': '%SystemRoot%\\System32\\eapprovp.dll', 'DllEntryPoint': 'EapProvPlugGetInfo'}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">EventLog Service </span>

|SvcMemHardLimitInMB|SvcMemMidLimitInMB|SvcMemSoftLimitInMB|Application|System|
| :---: | :---: | :---: | :---: | :---: |
|`0x14`|`0x0f`|`0x0b`|`{'LoadPerf': {'ProviderGuid': '{122EE297-BB47-41AE-B265-1CA8D1886D40}'}, 'Microsoft-Windows-PerfCtrs': {'ProviderGuid': '{973143dd-f3c7-4ef5-b156-544ac38c39b6}', 'EventMessageFile': '%SystemRoot%\\system32\\perfctrs.dll'}, 'PDH': {'ProviderGuid': '{04D66358-C4A1-419B-8023-23B73902DE2C}'}, 'PerfCtrs': {'ProviderGuid': '{973143DD-F3C7-4EF5-B156-544AC38C39B6}'}, 'PerfDisk': {'ProviderGuid': '{7F9D83DE-8ABB-457F-98E8-4AD161449ECC}'}, 'Perflib': {'ProviderGuid': '{13B197BD-7CEE-4B4E-8DD0-59314CE374CE}'}, 'PerfNet': {'ProviderGuid': '{CAB2B8A5-49B9-4EEC-B1B0-FAC21DA05A3B}'}, 'PerfOs': {'ProviderGuid': '{F82FB576-E941-4956-A2C7-A0CF83F6450A}'}, 'PerfProc': {'ProviderGuid': '{72D211E1-4C54-4A93-9520-4901681B2271}'}}`|`{'eventlog': {'EventMessageFile': '%SystemRoot%\\System32\\netevent.dll', 'TypesSupported': 7}, 'LSI_SSS': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'megasas': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'Microsoft-Antimalware-ShieldProvider': {'ProviderGuid': '{928f7d29-0577-5be5-3bd3-b6bdab9ab307}', 'EventMessageFile': '%SystemRoot%\\System32\\SecurityHealthService.exe'}}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">FrameServer Service </span>



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 21 bc a3 2e 0f 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`773732e5-76f9-5b4f-9b55-b94699c46e44`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`d752e524-2365-f747-a647-d3465bf1f5ca`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HomeGroupListener Service </span>

|SvcMemHardLimitInMB|SvcMemMidLimitInMB|SvcMemSoftLimitInMB|ApprovedListeners|
| :---: | :---: | :---: | :---: |
|`0xbd`|`0x7e`|`0x40`|`{'{125B0F61-0EC3-4f07-9A49-AFB340D9E57F}': {'(Default)': 'File History Hosted Listener', 'SupportedRecordTypes': {'GUID_DPListenerRecordType': '{ADBCFEA5-D8FC-4a46-B12B-EB1FFE39BF17}'}}, '{517F6AA6-D6FA-46D0-8094-17FF17E4CCF4}': {'(Default)': 'Security Hosted Listener', 'SupportedRecordTypes': {'GUID_SecurityListener_SigningKeys': '{CA328F46-E759-4399-82AB-FA92651D1ED2}'}}, '{5255EFED-103A-4444-B124-F88F99E4EF8D}': {'(Default)': 'Printer Hosted Listener'}, '{8ADD018C-5C5F-43C5-BE1E-07BAE85593B7}': {'(Default)': 'Alpha Hosted Listener', 'SupportedRecordTypes': {'GUID_AlphaListener_AlphaAccount': '{929CB323-C5EA-48E7-A6D0-193DD432E769}'}}, '{DE9C1288-0F09-40ff-BA84-7F19279FA74B}': {'(Default)': 'Identity Hosted Listener', 'SupportedRecordTypes': {'GUID_IdentityListenerRecordType': '{07004F5D-93A5-4b6c-B851-E2C9BBFD923D}', 'GUID_IdentityMachineCertRecordType': '{07004F5E-93A5-4b6c-B851-E2C9BBFD923E}'}}, '{EB6B4457-F013-4E5A-9B05-1D44E4D6FAEB}': {'(Default)': 'Sharing Hosted Listener', 'SupportedRecordTypes': {'GUID_SharingListener_MACAddresses': '{A7BC622E-8238-4E38-9C88-34153B7D9AB1}'}}}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\ListSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ListenerServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HomeGroupProvider Service </span>

|ServiceData|
| :---: |
|`{'LocalJoiningUser': '', 'Password': b'\x00'}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\provsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ProviderServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">hvservice Service </span>

|Description|Group|
| :---: | :---: |
|`@%SystemRoot%\system32\drivers\hvservice.sys,-17`|`Extended Base`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Lsa Service </span>

|Performance|
| :---: |
|`{'Close': 'CloseLsaPerformanceData', 'Collect': 'CollectLsaPerformanceData', 'Library': 'X:\\Windows\\System32\\Secur32.dll', 'Object List': '1570 1670', 'Open': 'OpenLsaPerformanceData'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">LSI_SSS Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\lsi_sss.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`SCSI Miniport`|`0x0c`|`lsi_sss.inf`|



##### Service Parameters
  
BusType : `0x0a`  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">megasas Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\megasas.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`SCSI Miniport`|`0x0d`|`megasas.inf`|



##### Service Parameters
  
BusType : `0x08`  
IoTimeoutValue : `0x3c`  
Device : `{'DriverParameter': 'nobusywait=1', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mshidkmdf Service </span>

|Description|Group|
| :---: | :---: |
|`@%SystemRoot%\system32\drivers\mshidkmdf.sys,-101`|`Base`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MSSCNTRS Service </span>

|Performance|
| :---: |
|`{'Close': 'Close', 'Collect': 'Collect', 'Library': '%systemroot%\\system32\\msscntrs.dll', 'Open': 'Open'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NlaSvc Service </span>

|DependOnService|FailureActions|
| :---: | :---: |
|`NSIRpcSsTcpIpDhcpEventlog`|`80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 64 00 00 00 01 00 00 00 64 00 00 00 00 00 00 00 00 00 00 00`|



##### Service Parameters
  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2001d
    SID: S-1-0-80-3141615172-2057878085-1754447212-2405740020-3916490453

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RFCOMM Service </span>



##### Service Parameters
  
Policy  
PM_AllowBluetooth : `0x02`  
PM_AllowDiscoverableMode : `0x01`  
PM_AllowConnectableMode : `0x01`  
PM_AllowAdvertising : `0x01`  
PM_AllowOutOfBandPairing : `0x01`  
PM_LinkSecurityLevel : `0x00`  
PM_LocalDeviceName : ``  
PM_DevicesAllowedList : `00`  
PM_ServicesAllowedList : `00`  
PM_RequireRestrictedMode : `0x00`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SensorService Service </span>



##### Service Parameters
  
Sensors : `{'{0D49D945-FA83-4630-A22C-01387F906DE6}': {'PersistentUniqueId': '{934F17E7-42EF-470B-BE7C-1AD0983C9E6C}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}}`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|1||||`D09BDEB5-6171-4A34-BFE2-06FA82652568:8489BE1C-80A4-48BC-901A-AA91BD827A7C`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2||||`DB2CE634-191D-42AF-A28C-16BE97924CA7`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3||||`97BE9507-17DA-4999-87D7-66C0B2D83CC7`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SharedAccess Service </span>

|Defaults|
| :---: |
|`{'FirewallPolicy': {'FirewallRules': {'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-In': 'v2.30\|Action=Allow\|Active=FALSE\|Dir=In\|Protocol=6\|Profile=Private\|LPort=3587\|RA4=LocalSubnet\|RA6=LocalSubnet\|App=%systemroot%\\system32\\svchost.exe\|Svc=p2psvc\|Name=@%systemroot%\\system32\\provsvc.dll,-200\|Desc=@%systemroot%\\system32\\provsvc.dll,-201\|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202\|', 'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-Out': 'v2.30\|Action=Allow\|Active=FALSE\|Dir=Out\|Protocol=6\|Profile=Private\|RPort=3587\|RA4=LocalSubnet\|RA6=LocalSubnet\|App=%systemroot%\\system32\\svchost.exe\|Svc=p2psvc\|Name=@%systemroot%\\system32\\provsvc.dll,-203\|Desc=@%systemroot%\\system32\\provsvc.dll,-204\|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202\|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-In': 'v2.30\|Action=Allow\|Active=FALSE\|Dir=In\|Protocol=17\|Profile=Private\|LPort=3540\|RA4=LocalSubnet\|RA6=LocalSubnet\|App=%systemroot%\\system32\\svchost.exe\|Svc=pnrpsvc\|Name=@%systemroot%\\system32\\provsvc.dll,-205\|Desc=@%systemroot%\\system32\\provsvc.dll,-206\|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202\|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-Out': 'v2.30\|Action=Allow\|Active=FALSE\|Dir=Out\|Protocol=17\|Profile=Private\|RPort=3540\|RA4=LocalSubnet\|RA6=LocalSubnet\|App=%systemroot%\\system32\\svchost.exe\|Svc=pnrpsvc\|Name=@%systemroot%\\system32\\provsvc.dll,-207\|Desc=@%systemroot%\\system32\\provsvc.dll,-208\|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202\|'}}}`|



##### Service Parameters
  
FirewallPolicy : `{'FirewallRules': {'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=6|Profile=Private|LPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-200|Desc=@%systemroot%\\system32\\provsvc.dll,-201|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=6|Profile=Private|RPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-203|Desc=@%systemroot%\\system32\\provsvc.dll,-204|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=17|Profile=Private|LPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-205|Desc=@%systemroot%\\system32\\provsvc.dll,-206|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=17|Profile=Private|RPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-207|Desc=@%systemroot%\\system32\\provsvc.dll,-208|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|'}, 'RestrictedServices': {'Static': {'System': {'HomeGroup Allow In': 'v2.0|Action=Allow|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|LPort=3587|Protocol=6|Name=Allow Grouping to receive from port 3587|', 'HomeGroup Allow In (PRNP)': 'v2.0|Action=Allow|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|LPort=3540|Protocol=17|Name=Allow PNRP to receive from port 3540|', 'HomeGroup Allow Out': 'v2.0|Action=Allow|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|RPort=3587|Protocol=6|Name=Allow Grouping to send to port 3587|', 'HomeGroup Allow Out (PRNP)': 'v2.0|Action=Allow|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|RPort=3540|Protocol=17|Name=Allow PNRP to send from port 3540|', 'HomeGroup Block In': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|Name=Block homegroup incoming|', 'HomeGroup Block Out': 'V2.0|Action=Block|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|Name=Block homegroup outgoing|', 'HomeGroup Listener Block In': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupListener|Name=Block all incoming|', 'HomeGroup Listener Block Out': 'V2.0|Action=Block|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupListener|Name=Block all outgoing|', 'SettingSyncHost': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\settingsynchost.exe|Name=Block IP traffic to SettingSyncHost|'}}}}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SNMPTRAP Service </span>

|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@firewallapi.dll,-50324`|`@firewallapi.dll,-50323`|`SERVICE_ERROR_NORMAL`|`ff ff ff ff 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 60 ea 00 00 00 00 00 00 00 00 00 00`|`%SystemRoot%\System32\snmptrap.exe`|`NT AUTHORITY\LocalService`|`['SeChangeNotifyPrivilege']`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">stisvc Service </span>

|DependOnService|Description|DisplayName|ErrorControl|ImagePath|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`RpcSs`|`@%SystemRoot%\system32\wiaservc.dll,-10`|`@%SystemRoot%\system32\wiaservc.dll,-9`|`SERVICE_ERROR_NORMAL`|`%SystemRoot%\system32\svchost.exe -k imgsvc`|`NT Authority\LocalService`|`['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege']`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wiaservc.dll`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x100
    SID: S-1-0-11
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Synth3dVsc Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\Synth3dVsc.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Video Init`|`0x01`|`wsynth3dvsc.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TapiSrv Service </span>

|Performance|
| :---: |
|`{'ObjectList': '1150'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Telemetry Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\IntelTA.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`Core Security Extensions`|`0x02`|`@intelta.inf,%Telemetry.SVCDESC%;Intel(R) Telemetry Service`|`intelta.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wcnfs Service </span>

|DependOnService|Description|DisplayName|ErrorControl|Group|ImagePath|Start|SupportedFeatures|Type|Instances|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`FltMgr`|`@%systemroot%\system32\drivers\wcnfs.sys,-101`|`@%systemroot%\system32\drivers\wcnfs.sys,-100`|`SERVICE_ERROR_NORMAL`|`FSFilter Top`|`\SystemRoot\system32\drivers\wcnfs.sys`|`SERVICE_DEMAND_START`|`0x07`|`SERVICE_FILE_SYSTEM_DRIVER`|`{'DefaultInstance': 'wcnfs Instance', 'wcnfs Instance': {'Altitude': '409900', 'Flags': 0}}`|



##### Service Parameters
  
DebugOptions : `0x00`  
<br></br>  

---
<br></br>  
<br></br>