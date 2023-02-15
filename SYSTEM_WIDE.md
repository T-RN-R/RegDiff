
804bab7d-450d-4a8d-a315-52601d77d322 348cc840-2674-4338-96eb-39824bfa447b Diff
==============================================================================

Table of contents
=================

* [Core](#core)
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
		* [Services](#services)
			* [ACPI](#acpi)
				* [Service Parameters](#service-parameters)
			* [Appinfo](#appinfo)
				* [Service Triggers](#service-triggers)
			* [AppleSSD](#applessd)
				* [Service Parameters](#service-parameters)
			* [BFE](#bfe)
				* [Service Parameters](#service-parameters)
			* [cbdhsvc](#cbdhsvc)
			* [CldFlt](#cldflt)
				* [Service Parameters](#service-parameters)
			* [dcsvc](#dcsvc)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [DeviceInstall](#deviceinstall)
				* [Service Parameters](#service-parameters)
			* [disk](#disk)
				* [Service Parameters](#service-parameters)
			* [Dnscache](#dnscache)
				* [Service Parameters](#service-parameters)
			* [EapHost](#eaphost)
				* [Service Parameters](#service-parameters)
			* [ebdrv0](#ebdrv0)
			* [EhStorClass](#ehstorclass)
				* [Service Parameters](#service-parameters)
			* [EventLog](#eventlog)
			* [ExecutionContext](#executioncontext)
			* [FrameServerMonitor](#frameservermonitor)
				* [Service Triggers](#service-triggers)
			* [fvevol](#fvevol)
				* [Service Parameters](#service-parameters)
			* [hidspi](#hidspi)
			* [HidSpiCx](#hidspicx)
			* [Hsp](#hsp)
				* [Service Parameters](#service-parameters)
			* [hvservice](#hvservice)
			* [IntelPMT](#intelpmt)
			* [iorate](#iorate)
				* [Service Parameters](#service-parameters)
			* [lfsvc](#lfsvc)
			* [McpManagementService](#mcpmanagementservice)
				* [Service Parameters](#service-parameters)
			* [mpi3drvi](#mpi3drvi)
				* [Service Parameters](#service-parameters)
			* [NDIS](#ndis)
				* [Service Parameters](#service-parameters)
			* [NDKPerf](#ndkperf)
			* [NPSMSvc](#npsmsvc)
				* [Service Parameters](#service-parameters)
			* [nvmedisk](#nvmedisk)
			* [P9NP](#p9np)
			* [P9Rdr](#p9rdr)
			* [P9RdrService](#p9rdrservice)
				* [Service Triggers](#service-triggers)
			* [partmgr](#partmgr)
				* [Service Parameters](#service-parameters)
			* [PcaSvc](#pcasvc)
				* [Service Triggers](#service-triggers)
			* [pci](#pci)
				* [Service Parameters](#service-parameters)
			* [PenService](#penservice)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [PerfDisk](#perfdisk)
			* [PerfNet](#perfnet)
			* [PerfOS](#perfos)
			* [PerfProc](#perfproc)
			* [PrintWorkflowUserSvc](#printworkflowusersvc)
				* [Service Triggers](#service-triggers)
			* [PRM](#prm)
			* [RasMan](#rasman)
			* [rdyboost](#rdyboost)
				* [Service Parameters](#service-parameters)
			* [RemoteAccess](#remoteaccess)
			* [RetailDemo](#retaildemo)
			* [SecurityHealthService](#securityhealthservice)
			* [SensorService](#sensorservice)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [SNMPTrap](#snmptrap)
			* [StiSvc](#stisvc)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [stornvme](#stornvme)
				* [Service Parameters](#service-parameters)
			* [TapiSrv](#tapisrv)
			* [TermService](#termservice)
			* [TPM](#tpm)
				* [Service Parameters](#service-parameters)
			* [tzautoupdate](#tzautoupdate)
				* [Service Triggers](#service-triggers)
			* [UGatherer](#ugatherer)
			* [UGTHRSVC](#ugthrsvc)
			* [Usb4DeviceRouter](#usb4devicerouter)
				* [Service Parameters](#service-parameters)
			* [Usb4HostRouter](#usb4hostrouter)
				* [Service Parameters](#service-parameters)
			* [usbhub](#usbhub)
			* [volmgr](#volmgr)
				* [Service Parameters](#service-parameters)
			* [volsnap](#volsnap)
				* [Service Parameters](#service-parameters)
			* [volume](#volume)
				* [Service Parameters](#service-parameters)
			* [WifiCx](#wificx)
			* [XblGameSave](#xblgamesave)
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
		* [Services](#services)
			* [BluetoothUserService](#bluetoothuserservice)
				* [Service Triggers](#service-triggers)
			* [BthEnum](#bthenum)
				* [Service Parameters](#service-parameters)
			* [BthLEEnum](#bthleenum)
				* [Service Parameters](#service-parameters)
			* [BTHPORT](#bthport)
				* [Service Parameters](#service-parameters)
			* [dmwappushservice](#dmwappushservice)
				* [Service Triggers](#service-triggers)
			* [Eaphost](#eaphost)
				* [Service Parameters](#service-parameters)
			* [EventLog](#eventlog)
			* [FrameServer](#frameserver)
				* [Service Triggers](#service-triggers)
			* [HomeGroupListener](#homegrouplistener)
				* [Service Parameters](#service-parameters)
			* [HomeGroupProvider](#homegroupprovider)
				* [Service Parameters](#service-parameters)
			* [hvservice](#hvservice)
			* [Lsa](#lsa)
			* [LSI_SSS](#lsi_sss)
				* [Service Parameters](#service-parameters)
			* [megasas](#megasas)
				* [Service Parameters](#service-parameters)
			* [mshidkmdf](#mshidkmdf)
			* [MSSCNTRS](#msscntrs)
			* [NlaSvc](#nlasvc)
				* [Service Parameters](#service-parameters)
			* [RFCOMM](#rfcomm)
				* [Service Parameters](#service-parameters)
			* [SensorService](#sensorservice)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [SharedAccess](#sharedaccess)
				* [Service Parameters](#service-parameters)
			* [SNMPTRAP](#snmptrap)
			* [stisvc](#stisvc)
				* [Service Parameters](#service-parameters)
			* [Synth3dVsc](#synth3dvsc)
			* [TapiSrv](#tapisrv)
			* [Telemetry](#telemetry)
			* [wcnfs](#wcnfs)
				* [Service Parameters](#service-parameters)
* [CoreN](#coren)
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
		* [Services](#services)
			* [ACPI](#acpi)
				* [Service Parameters](#service-parameters)
			* [Appinfo](#appinfo)
				* [Service Triggers](#service-triggers)
			* [AppleSSD](#applessd)
				* [Service Parameters](#service-parameters)
			* [BFE](#bfe)
				* [Service Parameters](#service-parameters)
			* [cbdhsvc](#cbdhsvc)
			* [CldFlt](#cldflt)
				* [Service Parameters](#service-parameters)
			* [dcsvc](#dcsvc)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [DeviceInstall](#deviceinstall)
				* [Service Parameters](#service-parameters)
			* [disk](#disk)
				* [Service Parameters](#service-parameters)
			* [Dnscache](#dnscache)
				* [Service Parameters](#service-parameters)
			* [EapHost](#eaphost)
				* [Service Parameters](#service-parameters)
			* [ebdrv0](#ebdrv0)
			* [EhStorClass](#ehstorclass)
				* [Service Parameters](#service-parameters)
			* [EventLog](#eventlog)
			* [ExecutionContext](#executioncontext)
			* [FrameServerMonitor](#frameservermonitor)
				* [Service Triggers](#service-triggers)
			* [fvevol](#fvevol)
				* [Service Parameters](#service-parameters)
			* [hidspi](#hidspi)
			* [HidSpiCx](#hidspicx)
			* [Hsp](#hsp)
				* [Service Parameters](#service-parameters)
			* [hvservice](#hvservice)
			* [IntelPMT](#intelpmt)
			* [iorate](#iorate)
				* [Service Parameters](#service-parameters)
			* [lfsvc](#lfsvc)
			* [McpManagementService](#mcpmanagementservice)
				* [Service Parameters](#service-parameters)
			* [mpi3drvi](#mpi3drvi)
				* [Service Parameters](#service-parameters)
			* [NDIS](#ndis)
				* [Service Parameters](#service-parameters)
			* [NDKPerf](#ndkperf)
			* [NPSMSvc](#npsmsvc)
				* [Service Parameters](#service-parameters)
			* [nvmedisk](#nvmedisk)
			* [P9NP](#p9np)
			* [P9Rdr](#p9rdr)
			* [P9RdrService](#p9rdrservice)
				* [Service Triggers](#service-triggers)
			* [partmgr](#partmgr)
				* [Service Parameters](#service-parameters)
			* [PcaSvc](#pcasvc)
				* [Service Triggers](#service-triggers)
			* [pci](#pci)
				* [Service Parameters](#service-parameters)
			* [PenService](#penservice)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [PerfDisk](#perfdisk)
			* [PerfNet](#perfnet)
			* [PerfOS](#perfos)
			* [PerfProc](#perfproc)
			* [PrintWorkflowUserSvc](#printworkflowusersvc)
				* [Service Triggers](#service-triggers)
			* [PRM](#prm)
			* [RasMan](#rasman)
			* [rdyboost](#rdyboost)
				* [Service Parameters](#service-parameters)
			* [RemoteAccess](#remoteaccess)
			* [RetailDemo](#retaildemo)
			* [SecurityHealthService](#securityhealthservice)
			* [SensorService](#sensorservice)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [SNMPTrap](#snmptrap)
			* [StiSvc](#stisvc)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [stornvme](#stornvme)
				* [Service Parameters](#service-parameters)
			* [TapiSrv](#tapisrv)
			* [TermService](#termservice)
			* [TPM](#tpm)
				* [Service Parameters](#service-parameters)
			* [tzautoupdate](#tzautoupdate)
				* [Service Triggers](#service-triggers)
			* [UGatherer](#ugatherer)
			* [UGTHRSVC](#ugthrsvc)
			* [Usb4DeviceRouter](#usb4devicerouter)
				* [Service Parameters](#service-parameters)
			* [Usb4HostRouter](#usb4hostrouter)
				* [Service Parameters](#service-parameters)
			* [usbhub](#usbhub)
			* [volmgr](#volmgr)
				* [Service Parameters](#service-parameters)
			* [volsnap](#volsnap)
				* [Service Parameters](#service-parameters)
			* [volume](#volume)
				* [Service Parameters](#service-parameters)
			* [WifiCx](#wificx)
			* [XblGameSave](#xblgamesave)
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
		* [Services](#services)
			* [BluetoothUserService](#bluetoothuserservice)
				* [Service Triggers](#service-triggers)
			* [BthEnum](#bthenum)
				* [Service Parameters](#service-parameters)
			* [BthLEEnum](#bthleenum)
				* [Service Parameters](#service-parameters)
			* [BTHPORT](#bthport)
				* [Service Parameters](#service-parameters)
			* [dmwappushservice](#dmwappushservice)
				* [Service Triggers](#service-triggers)
			* [Eaphost](#eaphost)
				* [Service Parameters](#service-parameters)
			* [EventLog](#eventlog)
			* [FrameServer](#frameserver)
				* [Service Triggers](#service-triggers)
			* [HomeGroupListener](#homegrouplistener)
				* [Service Parameters](#service-parameters)
			* [HomeGroupProvider](#homegroupprovider)
				* [Service Parameters](#service-parameters)
			* [hvservice](#hvservice)
			* [Lsa](#lsa)
			* [LSI_SSS](#lsi_sss)
				* [Service Parameters](#service-parameters)
			* [megasas](#megasas)
				* [Service Parameters](#service-parameters)
			* [mshidkmdf](#mshidkmdf)
			* [MSSCNTRS](#msscntrs)
			* [NlaSvc](#nlasvc)
				* [Service Parameters](#service-parameters)
			* [RFCOMM](#rfcomm)
				* [Service Parameters](#service-parameters)
			* [SensorService](#sensorservice)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [SharedAccess](#sharedaccess)
				* [Service Parameters](#service-parameters)
			* [SNMPTRAP](#snmptrap)
			* [stisvc](#stisvc)
				* [Service Parameters](#service-parameters)
			* [Synth3dVsc](#synth3dvsc)
			* [TapiSrv](#tapisrv)
			* [Telemetry](#telemetry)
			* [wcnfs](#wcnfs)
				* [Service Parameters](#service-parameters)
* [Professional](#professional)
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
		* [Services](#services)
			* [ACPI](#acpi)
				* [Service Parameters](#service-parameters)
			* [Appinfo](#appinfo)
				* [Service Triggers](#service-triggers)
			* [AppleSSD](#applessd)
				* [Service Parameters](#service-parameters)
			* [BFE](#bfe)
				* [Service Parameters](#service-parameters)
			* [cbdhsvc](#cbdhsvc)
			* [CldFlt](#cldflt)
				* [Service Parameters](#service-parameters)
			* [dcsvc](#dcsvc)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [DeviceInstall](#deviceinstall)
				* [Service Parameters](#service-parameters)
			* [disk](#disk)
				* [Service Parameters](#service-parameters)
			* [Dnscache](#dnscache)
				* [Service Parameters](#service-parameters)
			* [EapHost](#eaphost)
				* [Service Parameters](#service-parameters)
			* [ebdrv0](#ebdrv0)
			* [EhStorClass](#ehstorclass)
				* [Service Parameters](#service-parameters)
			* [EventLog](#eventlog)
			* [ExecutionContext](#executioncontext)
			* [FrameServerMonitor](#frameservermonitor)
				* [Service Triggers](#service-triggers)
			* [fvevol](#fvevol)
				* [Service Parameters](#service-parameters)
			* [hidspi](#hidspi)
			* [HidSpiCx](#hidspicx)
			* [Hsp](#hsp)
				* [Service Parameters](#service-parameters)
			* [hvservice](#hvservice)
			* [IntelPMT](#intelpmt)
			* [iorate](#iorate)
				* [Service Parameters](#service-parameters)
			* [lfsvc](#lfsvc)
			* [McpManagementService](#mcpmanagementservice)
				* [Service Parameters](#service-parameters)
			* [mpi3drvi](#mpi3drvi)
				* [Service Parameters](#service-parameters)
			* [NDIS](#ndis)
				* [Service Parameters](#service-parameters)
			* [NDKPerf](#ndkperf)
			* [NPSMSvc](#npsmsvc)
				* [Service Parameters](#service-parameters)
			* [nvmedisk](#nvmedisk)
			* [P9NP](#p9np)
			* [P9Rdr](#p9rdr)
			* [P9RdrService](#p9rdrservice)
				* [Service Triggers](#service-triggers)
			* [partmgr](#partmgr)
				* [Service Parameters](#service-parameters)
			* [PcaSvc](#pcasvc)
				* [Service Triggers](#service-triggers)
			* [pci](#pci)
				* [Service Parameters](#service-parameters)
			* [PenService](#penservice)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [PerfDisk](#perfdisk)
			* [PerfNet](#perfnet)
			* [PerfOS](#perfos)
			* [PerfProc](#perfproc)
			* [PrintWorkflowUserSvc](#printworkflowusersvc)
				* [Service Triggers](#service-triggers)
			* [PRM](#prm)
			* [RasMan](#rasman)
			* [rdyboost](#rdyboost)
				* [Service Parameters](#service-parameters)
			* [RemoteAccess](#remoteaccess)
			* [RetailDemo](#retaildemo)
			* [SecurityHealthService](#securityhealthservice)
			* [SensorService](#sensorservice)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [SNMPTrap](#snmptrap)
			* [StiSvc](#stisvc)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [stornvme](#stornvme)
				* [Service Parameters](#service-parameters)
			* [TapiSrv](#tapisrv)
			* [TermService](#termservice)
			* [TPM](#tpm)
				* [Service Parameters](#service-parameters)
			* [tzautoupdate](#tzautoupdate)
				* [Service Triggers](#service-triggers)
			* [UGatherer](#ugatherer)
			* [UGTHRSVC](#ugthrsvc)
			* [Usb4DeviceRouter](#usb4devicerouter)
				* [Service Parameters](#service-parameters)
			* [Usb4HostRouter](#usb4hostrouter)
				* [Service Parameters](#service-parameters)
			* [usbhub](#usbhub)
			* [volmgr](#volmgr)
				* [Service Parameters](#service-parameters)
			* [volsnap](#volsnap)
				* [Service Parameters](#service-parameters)
			* [volume](#volume)
				* [Service Parameters](#service-parameters)
			* [WifiCx](#wificx)
			* [XblGameSave](#xblgamesave)
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
		* [Services](#services)
			* [BluetoothUserService](#bluetoothuserservice)
				* [Service Triggers](#service-triggers)
			* [BthEnum](#bthenum)
				* [Service Parameters](#service-parameters)
			* [BthLEEnum](#bthleenum)
				* [Service Parameters](#service-parameters)
			* [BTHPORT](#bthport)
				* [Service Parameters](#service-parameters)
			* [dmwappushservice](#dmwappushservice)
				* [Service Triggers](#service-triggers)
			* [Eaphost](#eaphost)
				* [Service Parameters](#service-parameters)
			* [EventLog](#eventlog)
			* [FrameServer](#frameserver)
				* [Service Triggers](#service-triggers)
			* [HomeGroupListener](#homegrouplistener)
				* [Service Parameters](#service-parameters)
			* [HomeGroupProvider](#homegroupprovider)
				* [Service Parameters](#service-parameters)
			* [hvservice](#hvservice)
			* [Lsa](#lsa)
			* [LSI_SSS](#lsi_sss)
				* [Service Parameters](#service-parameters)
			* [megasas](#megasas)
				* [Service Parameters](#service-parameters)
			* [mshidkmdf](#mshidkmdf)
			* [MSSCNTRS](#msscntrs)
			* [NlaSvc](#nlasvc)
				* [Service Parameters](#service-parameters)
			* [RFCOMM](#rfcomm)
				* [Service Parameters](#service-parameters)
			* [SensorService](#sensorservice)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [SharedAccess](#sharedaccess)
				* [Service Parameters](#service-parameters)
			* [SNMPTRAP](#snmptrap)
			* [stisvc](#stisvc)
				* [Service Parameters](#service-parameters)
			* [Synth3dVsc](#synth3dvsc)
			* [TapiSrv](#tapisrv)
			* [Telemetry](#telemetry)
			* [wcnfs](#wcnfs)
				* [Service Parameters](#service-parameters)
* [ProfessionalN](#professionaln)
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
		* [Services](#services)
			* [ACPI](#acpi)
				* [Service Parameters](#service-parameters)
			* [Appinfo](#appinfo)
				* [Service Triggers](#service-triggers)
			* [AppleSSD](#applessd)
				* [Service Parameters](#service-parameters)
			* [BFE](#bfe)
				* [Service Parameters](#service-parameters)
			* [cbdhsvc](#cbdhsvc)
			* [CldFlt](#cldflt)
				* [Service Parameters](#service-parameters)
			* [dcsvc](#dcsvc)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [DeviceInstall](#deviceinstall)
				* [Service Parameters](#service-parameters)
			* [disk](#disk)
				* [Service Parameters](#service-parameters)
			* [Dnscache](#dnscache)
				* [Service Parameters](#service-parameters)
			* [EapHost](#eaphost)
				* [Service Parameters](#service-parameters)
			* [ebdrv0](#ebdrv0)
			* [EhStorClass](#ehstorclass)
				* [Service Parameters](#service-parameters)
			* [EventLog](#eventlog)
			* [ExecutionContext](#executioncontext)
			* [FrameServerMonitor](#frameservermonitor)
				* [Service Triggers](#service-triggers)
			* [fvevol](#fvevol)
				* [Service Parameters](#service-parameters)
			* [hidspi](#hidspi)
			* [HidSpiCx](#hidspicx)
			* [Hsp](#hsp)
				* [Service Parameters](#service-parameters)
			* [hvservice](#hvservice)
			* [IntelPMT](#intelpmt)
			* [iorate](#iorate)
				* [Service Parameters](#service-parameters)
			* [lfsvc](#lfsvc)
			* [McpManagementService](#mcpmanagementservice)
				* [Service Parameters](#service-parameters)
			* [mpi3drvi](#mpi3drvi)
				* [Service Parameters](#service-parameters)
			* [NDIS](#ndis)
				* [Service Parameters](#service-parameters)
			* [NDKPerf](#ndkperf)
			* [NPSMSvc](#npsmsvc)
				* [Service Parameters](#service-parameters)
			* [nvmedisk](#nvmedisk)
			* [P9NP](#p9np)
			* [P9Rdr](#p9rdr)
			* [P9RdrService](#p9rdrservice)
				* [Service Triggers](#service-triggers)
			* [partmgr](#partmgr)
				* [Service Parameters](#service-parameters)
			* [PcaSvc](#pcasvc)
				* [Service Triggers](#service-triggers)
			* [pci](#pci)
				* [Service Parameters](#service-parameters)
			* [PenService](#penservice)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [PerfDisk](#perfdisk)
			* [PerfNet](#perfnet)
			* [PerfOS](#perfos)
			* [PerfProc](#perfproc)
			* [PrintWorkflowUserSvc](#printworkflowusersvc)
				* [Service Triggers](#service-triggers)
			* [PRM](#prm)
			* [RasMan](#rasman)
			* [rdyboost](#rdyboost)
				* [Service Parameters](#service-parameters)
			* [RemoteAccess](#remoteaccess)
			* [RetailDemo](#retaildemo)
			* [SecurityHealthService](#securityhealthservice)
			* [SensorService](#sensorservice)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [SNMPTrap](#snmptrap)
			* [StiSvc](#stisvc)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [stornvme](#stornvme)
				* [Service Parameters](#service-parameters)
			* [TapiSrv](#tapisrv)
			* [TermService](#termservice)
			* [TPM](#tpm)
				* [Service Parameters](#service-parameters)
			* [tzautoupdate](#tzautoupdate)
				* [Service Triggers](#service-triggers)
			* [UGatherer](#ugatherer)
			* [UGTHRSVC](#ugthrsvc)
			* [Usb4DeviceRouter](#usb4devicerouter)
				* [Service Parameters](#service-parameters)
			* [Usb4HostRouter](#usb4hostrouter)
				* [Service Parameters](#service-parameters)
			* [usbhub](#usbhub)
			* [volmgr](#volmgr)
				* [Service Parameters](#service-parameters)
			* [volsnap](#volsnap)
				* [Service Parameters](#service-parameters)
			* [volume](#volume)
				* [Service Parameters](#service-parameters)
			* [WifiCx](#wificx)
			* [XblGameSave](#xblgamesave)
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
		* [Services](#services)
			* [BluetoothUserService](#bluetoothuserservice)
				* [Service Triggers](#service-triggers)
			* [BthEnum](#bthenum)
				* [Service Parameters](#service-parameters)
			* [BthLEEnum](#bthleenum)
				* [Service Parameters](#service-parameters)
			* [BTHPORT](#bthport)
				* [Service Parameters](#service-parameters)
			* [dmwappushservice](#dmwappushservice)
				* [Service Triggers](#service-triggers)
			* [Eaphost](#eaphost)
				* [Service Parameters](#service-parameters)
			* [EventLog](#eventlog)
			* [FrameServer](#frameserver)
				* [Service Triggers](#service-triggers)
			* [HomeGroupListener](#homegrouplistener)
				* [Service Parameters](#service-parameters)
			* [HomeGroupProvider](#homegroupprovider)
				* [Service Parameters](#service-parameters)
			* [hvservice](#hvservice)
			* [Lsa](#lsa)
			* [LSI_SSS](#lsi_sss)
				* [Service Parameters](#service-parameters)
			* [megasas](#megasas)
				* [Service Parameters](#service-parameters)
			* [mshidkmdf](#mshidkmdf)
			* [MSSCNTRS](#msscntrs)
			* [NlaSvc](#nlasvc)
				* [Service Parameters](#service-parameters)
			* [RFCOMM](#rfcomm)
				* [Service Parameters](#service-parameters)
			* [SensorService](#sensorservice)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [SharedAccess](#sharedaccess)
				* [Service Parameters](#service-parameters)
			* [SNMPTRAP](#snmptrap)
			* [stisvc](#stisvc)
				* [Service Parameters](#service-parameters)
			* [Synth3dVsc](#synth3dvsc)
			* [TapiSrv](#tapisrv)
			* [Telemetry](#telemetry)
			* [wcnfs](#wcnfs)
				* [Service Parameters](#service-parameters)

# Core

## SYSTEM
  

<details>
  
<summary> Added </summary>
### WMI AutoLoggers

#### BioEnrollment
  
Start : `0x00`  
{4b8b1947-ae4d-54e2-826a-1aee78ef05b2} : `{'Enabled': 0}`  
{a55d5a23-1a5b-580a-2be5-d7188f43fae1} : `{'Enabled': 0}`
|guid|
| :---: |
|Start|
|{4b8b1947-ae4d-54e2-826a-1aee78ef05b2}|
|{a55d5a23-1a5b-580a-2be5-d7188f43fae1}|
  
<br></br>
#### EventLog-Application
  
{04d66358-c4a1-419b-8023-23b73902de2c} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{15f4cd44-ca53-5422-db17-4e76821b5a69} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{7628e972-6d6f-4974-b58f-6428622ec09a} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{7d44233d-3055-4b9c-ba64-0d47ca40a232} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 2305843009213693952, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9068a924-f97e-5506-c3a3-5c020c00e8e0} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{a70ff94f-570b-4979-ba5c-e59c9feab61b} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{ad8aa069-a01b-40a0-ba40-948d1d8dedc5} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{04d66358-c4a1-419b-8023-23b73902de2c}|
|{15f4cd44-ca53-5422-db17-4e76821b5a69}|
|{7628e972-6d6f-4974-b58f-6428622ec09a}|
|{7d44233d-3055-4b9c-ba64-0d47ca40a232}|
|{9068a924-f97e-5506-c3a3-5c020c00e8e0}|
|{a70ff94f-570b-4979-ba5c-e59c9feab61b}|
|{ad8aa069-a01b-40a0-ba40-948d1d8dedc5}|
  
<br></br>
#### EventLog-System
  
{0075e1ab-e1d1-5d1f-35f5-da36fb4f41b1} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{17d2a329-4539-5f4d-3435-f510634ce3b9} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{5bcf2a5c-2e90-5a03-aa4e-2e459bae21b4} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{6600e712-c3b6-44a2-8a48-935c511f28c8} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 2305843009213693952, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{7f54ca8a-6c72-5cbc-b96f-d0ef905b8bce} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{87a623f0-8db5-5c11-7c80-a2ebbcbe5189} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{93db76c2-63ab-5de1-88b3-c068686675b8} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9799276c-fb04-47e8-845e-36946045c218} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 2305843009213693952, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{a2d34bf1-70ab-5b21-c819-5a0dd42748fd} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{b931ed29-66f4-576e-0579-0b8818a5dc6b} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{bcf0c6a7-6130-5208-f27d-fa77a91f12df} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{d07e8c3f-78fb-4c22-b77c-2203d00bfdf3} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{f6cf91be-e7d7-57d6-2a3d-278ca406d190} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{0075e1ab-e1d1-5d1f-35f5-da36fb4f41b1}|
|{17d2a329-4539-5f4d-3435-f510634ce3b9}|
|{5bcf2a5c-2e90-5a03-aa4e-2e459bae21b4}|
|{6600e712-c3b6-44a2-8a48-935c511f28c8}|
|{7f54ca8a-6c72-5cbc-b96f-d0ef905b8bce}|
|{87a623f0-8db5-5c11-7c80-a2ebbcbe5189}|
|{93db76c2-63ab-5de1-88b3-c068686675b8}|
|{9799276c-fb04-47e8-845e-36946045c218}|
|{a2d34bf1-70ab-5b21-c819-5a0dd42748fd}|
|{b931ed29-66f4-576e-0579-0b8818a5dc6b}|
|{bcf0c6a7-6130-5208-f27d-fa77a91f12df}|
|{d07e8c3f-78fb-4c22-b77c-2203d00bfdf3}|
|{f6cf91be-e7d7-57d6-2a3d-278ca406d190}|
  
<br></br>
#### FaceCredProv
  
Start : `0x00`  
{1D480C11-3870-4B19-9144-47A53CD973BD} : `{'Enabled': 0}`
|guid|
| :---: |
|Start|
|{1D480C11-3870-4B19-9144-47A53CD973BD}|
  
<br></br>
#### FaceTel
  
Start : `0x00`  
{22eb0808-0b6c-5cd4-5511-6a77e6e73a93} : `{'Enabled': 0}`
|guid|
| :---: |
|Start|
|{22eb0808-0b6c-5cd4-5511-6a77e6e73a93}|
  
<br></br>
#### NetCore
  
{923C0FFD-7933-4B52-8A49-121ABF2DC357} : `{'@': 'triage_routepolicymanagement_tracelogging', 'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{923C0FFD-7933-4B52-8A49-121ABF2DC357}|
  
<br></br>
#### NtfsLog
  
{aa381297-bccb-4569-8e39-bbbb3b400893} : `{'_Description': 'TmLog Trace Provider', 'Enabled': 1, 'EnableFlags': 15, 'EnableLevel': 5}`
|guid|
| :---: |
|{aa381297-bccb-4569-8e39-bbbb3b400893}|
  
<br></br>
#### ReFSLog
  
ClockType : `0x02`  
GUID : `{81a69395-9f48-48f2-b88c-2401db1e3a91}`  
Start : `0x01`  
{740f3c34-57df-4bad-8eea-72ac69ad5df5} : `{'_Description': 'ReFS WPP Trace', 'Enabled': 1, 'EnableFlags': 7, 'EnableLevel': 3}`
|guid|
| :---: |
|ClockType|
|GUID|
|Start|
|{740f3c34-57df-4bad-8eea-72ac69ad5df5}|
  
<br></br>
#### SetupPlatformTel
  
{D2F37B94-92A5-44E2-AFC9-2F4489D39268} : `{'Enabled': 1, 'EnableLevel': 255}`
|guid|
| :---: |
|{D2F37B94-92A5-44E2-AFC9-2F4489D39268}|
  
<br></br>
#### SpoolerLogger
  
{ba4936a1-31db-4edc-89ce-9190e3c0653b} : `{'Enabled': 1, 'EnableFlags': 0, 'EnableLevel': 5}`
|guid|
| :---: |
|{ba4936a1-31db-4edc-89ce-9190e3c0653b}|
  
<br></br>
#### WiFiSession
  
{745976be-5e09-5c76-eabd-76c93c9212d2} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`  
{ae164ede-2246-5b24-c145-29c484f7362a} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`  
{EA893635-5AB7-562B-75A2-A22107D8058F} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{745976be-5e09-5c76-eabd-76c93c9212d2}|
|{ae164ede-2246-5b24-c145-29c484f7362a}|
|{EA893635-5AB7-562B-75A2-A22107D8058F}|
  
<br></br>  
<br></br>
### Services

#### ACPI



##### Service Parameters
  
PnpAsyncNewDevices : `0x01`  
<br></br>
#### Appinfo



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 66 00 37 00 33 00 38 00 65 00 32 00 30 00 2d 00 37 00 33 00 63 00 30 00 2d 00 34 00 63 00 61 00 38 00 2d 00 61 00 61 00 36 00 61 00 2d 00 38 00 64 00 66 00 65 00 66 00 35 00 34 00 35 00 66 00 65 00 61 00 38 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### AppleSSD
  
ImagePath : `System32\drivers\AppleSSD.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x01`  
DisplayName : `@AppleSSD.inf,%DevDesc1%;Apple Solid State Drive Device`  
Owners : `41 00 70 00 70 00 6c 00 65 00 53 00 53 00 44 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x01`  
Device : `{'MaxTranLenInPages': 64}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### BFE



##### Service Parameters
  
Policy  
Persistent  
ProviderContext
|GUID|Data|
| :---: | :---: |
|{30433c31-b05f-421f-8fde-018ea4c68af4}|`01 10 08 00 cc cc cc cc 10 01 00 00 00 00 00 00 00 00 02 00 01 00 00 00 f0 00 00 00 04 00 02 00 00 00 00 00 00 00 00 00 f0 00 00 00 01 10 08 00 cc cc cc cc e0 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 31 3c 43 30 5f b0 1f 42 8f de 01 8e a4 c6 8a f4 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 00 00 00 00 00 00 00 00 08 00 00 00 08 00 00 00 10 00 02 00 00 00 00 00 05 00 00 00 00 00 00 80 07 00 00 00 00 00 00 00 07 00 00 00 4d 00 50 00 53 00 53 00 56 00 43 00 00 00 00 00 15 00 00 00 00 00 00 00 15 00 00 00 53 00 74 00 6f 00 72 00 65 00 73 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 20 00 6f 00 72 00 69 00 67 00 69 00 6e 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 26 00 00 00 14 00 02 00 26 00 00 00 51 00 75 00 61 00 72 00 61 00 6e 00 74 00 69 00 6e 00 65 00 20 00 44 00 65 00 66 00 61 00 75 00 6c 00 74 00 00 00 00 00 00 00 00 00`|
|{93132c36-6e06-4e6f-a10b-218787cd49cf}|`01 10 08 00 cc cc cc cc 10 01 00 00 00 00 00 00 00 00 02 00 01 00 00 00 f0 00 00 00 04 00 02 00 00 00 00 00 00 00 00 00 f0 00 00 00 01 10 08 00 cc cc cc cc e0 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 36 2c 13 93 06 6e 6f 4e a1 0b 21 87 87 cd 49 cf 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 00 00 00 00 00 00 00 00 08 00 00 00 08 00 00 00 10 00 02 00 00 00 00 00 06 00 00 00 00 00 00 80 07 00 00 00 00 00 00 00 07 00 00 00 4d 00 50 00 53 00 53 00 56 00 43 00 00 00 00 00 15 00 00 00 00 00 00 00 15 00 00 00 53 00 74 00 6f 00 72 00 65 00 73 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 20 00 6f 00 72 00 69 00 67 00 69 00 6e 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 22 00 00 00 14 00 02 00 22 00 00 00 42 00 6f 00 6f 00 74 00 74 00 69 00 6d 00 65 00 20 00 44 00 65 00 66 00 61 00 75 00 6c 00 74 00 00 00 00 00 00 00 00 00 00 00 00 00`|
  
<br></br>
#### cbdhsvc
  
DelayedAutoStart : `0x01`
#### CldFlt



##### Service Parameters
  
USMsgTimeoutMillis : `0x3e8`  
<br></br>
#### dcsvc
  
DelayedAutoStart : `0x01`  
DependOnService : `rpcss`  
Description : `@%systemroot%\system32\dcsvc.dll,-101`  
DisplayName : `@%systemroot%\system32\dcsvc,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 04 00 00 00 14 00 00 00 01 00 00 00 10 27 00 00 01 00 00 00 10 27 00 00 01 00 00 00 10 27 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%systemroot%\system32\svchost.exe -k netsvcs -p`  
ObjectName : `LocalSystem`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`


##### Service Parameters
  
IdleTimeout(sec) : `0x78`  
ServiceDll : `%SystemRoot%\system32\dcsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`35 00 39 00 62 00 65 00 62 00 39 00 37 00 37 00 2d 00 64 00 30 00 33 00 37 00 2d 00 34 00 38 00 66 00 34 00 2d 00 61 00 66 00 37 00 34 00 2d 00 63 00 61 00 30 00 37 00 35 00 34 00 39 00 33 00 61 00 35 00 32 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 61 00 30 00 64 00 62 00 36 00 31 00 34 00 2d 00 65 00 39 00 66 00 62 00 2d 00 34 00 38 00 63 00 66 00 2d 00 39 00 31 00 34 00 33 00 2d 00 37 00 61 00 65 00 37 00 31 00 38 00 66 00 66 00 32 00 63 00 38 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### DeviceInstall



##### Service Parameters
  
DeviceInstallMode : `0x01`  
<br></br>
#### disk



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### Dnscache



##### Service Parameters
  
DohWellKnownServers : `{'1.0.0.1': {'Template': 'https://cloudflare-dns.com/dns-query'}, '1.1.1.1': {'Template': 'https://cloudflare-dns.com/dns-query'}, '149.112.112.112': {'Template': 'https://dns.quad9.net/dns-query'}, '2001:4860:4860::8844': {'Template': 'https://dns.google/dns-query'}, '2001:4860:4860::8888': {'Template': 'https://dns.google/dns-query'}, '2606:4700:4700::1001': {'Template': 'https://cloudflare-dns.com/dns-query'}, '2606:4700:4700::1111': {'Template': 'https://cloudflare-dns.com/dns-query'}, '2620:fe::fe': {'Template': 'https://dns.quad9.net/dns-query'}, '2620:fe::fe:9': {'Template': 'https://dns.quad9.net/dns-query'}, '8.8.4.4': {'Template': 'https://dns.google/dns-query'}, '8.8.8.8': {'Template': 'https://dns.google/dns-query'}, '9.9.9.9': {'Template': 'https://dns.quad9.net/dns-query'}}`  
<br></br>
#### EapHost
  
DependOnService : `RPCSSKeyIso`  
Description : `@%systemroot%\system32\eapsvc.dll,-2`  
DisplayName : `@%systemroot%\system32\eapsvc.dll,-1`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 c0 d4 01 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\svchost.exe -k netsvcs -p`  
ObjectName : `localSystem`  
RequiredPrivileges : `['SeTcbPrivilege', 'SeDebugPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_SHARE_PROCESS`  
Methods : `{'311': {'Name': 'Microsoft', '18': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '21': {'PeerConfigUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\TtlsAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\TtlsCfg.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 389863599, 'LANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}, 'WLANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}, '23': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1002', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '254': {'14122': {'1': {'PeerDllPath': '%SystemRoot%\\System32\\WcnEapPeerProxy.dll', 'PeerFriendlyName': 'Windows Connect Now EAP Peer', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 8683520}}}, '50': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1003', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '55': {'PeerConfigUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerDllPath': '%SystemRoot%\\System32\\EapTeapAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\EapTeapAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'Properties': 1065154751, 'LANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}, 'WLANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="utf-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><TrustedRootCAHash></TrustedRootCAHash></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection> </CertificateStore> </CredentialsSource><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="utf-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><TrustedRootCAHash></TrustedRootCAHash></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}}}`


##### Service Parameters
  
PeerInstalled : `0x01`  
ServiceDll : `%SystemRoot%\System32\eapsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
EapProvPlugin : `{'(Default)': '%SystemRoot%\\System32\\eapprovp.dll', 'DllEntryPoint': 'EapProvPlugGetInfo'}`  
<br></br>
#### ebdrv0
  
ImagePath : `System32\drivers\evbd0a.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `System Bus Extender`  
Tag : `0x03`  
DisplayName : `@netevbd0a.inf,%vbd_srv_desc%;QLogic Legacy Ethernet Adapter VBD`  
Owners : `6e 00 65 00 74 00 65 00 76 00 62 00 64 00 30 00 61 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### EhStorClass



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### EventLog
  
Application : `{'Microsoft-Windows-PDH': {'ProviderGuid': '{04d66358-c4a1-419b-8023-23b73902de2c}', 'EventMessageFile': '%SystemRoot%\\system32\\pdh.dll'}, 'Universal Print': {'EventMessageFile': '%SystemRoot%\\System32\\McpManagementService.dll', 'TypesSupported': 7}}`  
System : `{'AppleSSD': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'ebdrv0': {'eventmessagefile': '%SystemRoot%\\System32\\drivers\\evbd0a.sys;%SystemRoot%\\System32\\iologmsg.dll', 'typessupported': 7}, 'EventLog': {'EventMessageFile': '%SystemRoot%\\System32\\netevent.dll', 'TypesSupported': 7}, 'hvservice': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'Microsoft-Windows-Iphlpsvc-Trace': {'ProviderGuid': '{6600e712-c3b6-44a2-8a48-935c511f28c8}', 'EventMessageFile': '%windir%\\system32\\iphlpsvc.dll'}, 'Microsoft-Windows-Network-ExecutionContext': {'ProviderGuid': '{0075e1ab-e1d1-5d1f-35f5-da36fb4f41b1}', 'EventMessageFile': '%SystemRoot%\\system32\\drivers\\ExecutionContext.sys'}, 'Microsoft-Windows-USB-USB4DeviceRouter-EventLogs': {'ProviderGuid': '{d07e8c3f-78fb-4c22-b77c-2203d00bfdf3}', 'EventMessageFile': '%SystemRoot%\\System32\\DriverStore\\FileRepository\\usb4devicerouter.inf_amd64_3bffb5f5105936e5\\Usb4DeviceRouter.sys'}, 'mpi3drvi': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'nvmedisk': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll;%SystemRoot%\\System32\\drivers\\nvmedisk.sys', 'TypesSupported': 7}}`
#### ExecutionContext
  
DisplayName : `@%SystemRoot%\System32\Drivers\ExecutionContext.sys,-101`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `System`  
ImagePath : `System32\Drivers\ExecutionContext.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### FrameServerMonitor
  
DependOnService : `rpcss`  
Description : `@%systemroot%\system32\FrameServerMonitor.dll,-101`  
DisplayName : `@%systemroot%\system32\FrameServerMonitor.dll,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 20 bf 02 00`  
ImagePath : `%SystemRoot%\System32\svchost.exe -k CameraMonitor`  
ObjectName : `LocalSystem`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`  
parameters : `{'ServiceDll': '%SystemRoot%\\system32\\FrameServerMonitor.dll', 'ServiceDllUnloadOnStop': 1}`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`42 00 45 00 30 00 44 00 39 00 35 00 42 00 41 00 2d 00 32 00 31 00 41 00 35 00 2d 00 34 00 41 00 35 00 46 00 2d 00 41 00 31 00 46 00 30 00 2d 00 39 00 41 00 44 00 41 00 38 00 34 00 41 00 43 00 31 00 31 00 34 00 34 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 26 1d 90 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 21 bc a3 2e 0f 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`773732e5-76f9-5b4f-9b55-b94699c46e44`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`d752e524-2365-f747-a647-d3465bf1f5ca`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 b8 bc a3 3d 01 c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### fvevol



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### hidspi
  
DependOnService : `HidSpiCx`
#### HidSpiCx
  
DisplayName : `HidSpi KMDF Class Extension`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `system32\drivers\HidSpiCx.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### Hsp
  
ImagePath : `\SystemRoot\System32\drivers\Hsp.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@hsp.inf,%Hsp.SVCDESC%;Microsoft Pluton Service`  
Owners : `68 00 73 00 70 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
Wdf : `{'KmdfLibraryVersion': '1.15'}`  
<br></br>
#### hvservice
  
Owners : `68 00 76 00 73 00 65 00 72 00 76 00 69 00 63 00 65 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### IntelPMT
  
ImagePath : `System32\drivers\IntelPMT.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Core Security Extensions`  
Tag : `0x02`  
DisplayName : `@intelpmt.inf,%IntelPMT.SVCDESC%;Intel(R) Platform Monitoring Technology Service`  
Owners : `69 00 6e 00 74 00 65 00 6c 00 70 00 6d 00 74 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### iorate



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### lfsvc
  
Settings : `{'LocationWebServiceProxy': {'USE_CLIENT_PROXY_INFERENCE_ONLY': 0}}`
#### McpManagementService
  
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


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\McpManagementService.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>
#### mpi3drvi
  
ImagePath : `System32\drivers\mpi3drvi.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x10`  
Owners : `6d 00 70 00 69 00 33 00 64 00 72 00 76 00 69 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x08`  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### NDIS



##### Service Parameters
  
Reserved : `{'ExecutionContextProfiles': {'Balanced': {'DpcWatchdogTimerThreshold': 80, 'Flags': 0, 'MaxPacketsReceiveAtDispatch': 64, 'MaxPacketsReceiveAtPassive': 64, 'MaxPacketsReceiveCompleteAtDispatch': 64, 'MaxPacketsReceiveCompleteAtPassive': 64, 'MaxPacketsSendAtDispatch': 64, 'MaxPacketsSendAtPassive': 64, 'MaxPacketsSendCompleteAtDispatch': 64, 'MaxPacketsSendCompleteAtPassive': 64, 'MaxTimeAtDispatch': 0, 'WorkerThreadPriority': 10}}}`  
<br></br>
#### NDKPerf
  
DisplayName : `NDKPerf Driver`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `system32\drivers\NDKPerf.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### NPSMSvc
  
Description : `@%SystemRoot%\system32\npsm.dll,-101`  
DisplayName : `@%SystemRoot%\system32\npsm.dll,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 b8 0b 00 00 01 00 00 00 b8 0b 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k LocalService -p`  
ObjectName : `NT AUTHORITY\LocalService`  
RequiredPrivileges : `['SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `96`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\npsm.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  
Security : `01 00 14 80 a0 00 00 00 ac 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 01 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 70 00 05 00 00 00 00 00 14 00 fd 01 02 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 14 00 00 01 00 00 01 01 00 00 00 00 00 05 0b 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### nvmedisk
  
ImagePath : `System32\drivers\nvmedisk.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@nvmedisk.inf,%nvmedisk.SvcDesc%;Microsoft NVMe disk driver`  
Owners : `6e 00 76 00 6d 00 65 00 64 00 69 00 73 00 6b 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### P9NP
  
Description : `@%systemroot%\system32\p9np.dll,-101`  
DisplayName : `@%systemroot%\system32\p9np.dll,-100`  
NetworkProvider : `{'DeviceName': '\\Device\\P9Rdr', 'DisplayName': '@%systemroot%\\system32\\p9np.dll,-100', 'Name': 'Plan 9 Network Provider', 'ProviderPath': '%SystemRoot%\\System32\\p9np.dll', 'TriggerStartCompleteNotification': b'u\x10\xbc\xa3T\x1e\xc6A', 'TriggerStartNotification': b'u\x08\xbc\xa3T\x1e\xc6A', 'TriggerStartPrefix': b'w\x00s\x00l\x00.\x00l\x00o\x00c\x00a\x00l\x00h\x00o\x00s\x00t\x00\x00\x00w\x00s\x00l\x00$\x00\x00\x00\x00\x00'}`
#### P9Rdr
  
DependOnService : `RDBSS`  
Description : `@%SystemRoot%\System32\drivers\p9rdr.sys,-101`  
DisplayName : `@%SystemRoot%\System32\drivers\p9rdr.sys,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `System32\drivers\p9rdr.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### P9RdrService
  
DependOnService : `P9RdrRPCSS`  
Description : `@%systemroot%\system32\p9rdrservice.dll,-101`  
DisplayName : `@%systemroot%\system32\p9rdrservice.dll,-102`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 b8 0b 00 00 01 00 00 00 b8 0b 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%systemroot%\system32\svchost.exe -k P9RdrService -p`  
ObjectName : `LocalSystem`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `96`  
UserServiceFlags : `0x03`  
parameters : `{'ServiceDll': '%SystemRoot%\\system32\\p9rdrservice.dll', 'ServiceDllUnloadOnStop': 1}`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 54 1e c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### partmgr



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### PcaSvc



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 d0 be a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 18 bc a3 2e 07 c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 2e 03 96 15`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### pci



##### Service Parameters
  
PnpAsyncNewDevices : `0x01`  
<br></br>
#### PenService
  
Description : `@%SystemRoot%\system32\PenService.dll,-101`  
DisplayName : `@%SystemRoot%\system32\PenService.dll,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 02 00 00 00 14 00 00 00 01 00 00 00 10 27 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k PenService`  
Start : `SERVICE_DEMAND_START`  
Type : `96`  
UserServiceFlags : `0x02`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\PenService.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|Data1|Data2|Data3|DataType0|DataType1|DataType2|DataType3|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`b2551e4d-6ff1-cf11-88cb-001111000030`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 31 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 32 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 33 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 46 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### PerfDisk
  
Performance : `{'Collect Supports Metadata': 1}`
#### PerfNet
  
Performance : `{'Collect Supports Metadata': 1}`
#### PerfOS
  
Performance : `{'Collect Supports Metadata': 1}`
#### PerfProc
  
Performance : `{'Collect Supports Metadata': 1}`
#### PrintWorkflowUserSvc



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 3d 0a 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### PRM
  
ImagePath : `System32\DriverStore\FileRepository\prm.inf_amd64_7fc9bb8ba2b73803\PRM.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@prm.inf,%PRM.SvcDesc%;Microsoft PRM Driver`  
Owners : `70 00 72 00 6d 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### RasMan
  
PPP : `{'EAP': {'13': {'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '25': {'LANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">25</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>25</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV1"><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><FastReconnect>true</FastReconnect><InnerEapOptional>false</InnerEapOptional><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap><EnableQuarantineChecks>false</EnableQuarantineChecks><RequireCryptoBinding>false</RequireCryptoBinding><PeapExtensions><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</AcceptServerName><IdentityPrivacy xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2"><EnableIdentityPrivacy>true</EnableIdentityPrivacy><AnonymousUserName>anonymous</AnonymousUserName></IdentityPrivacy></PeapExtensions></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">25</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>25</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV1"><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><FastReconnect>true</FastReconnect><InnerEapOptional>false</InnerEapOptional><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap><EnableQuarantineChecks>false</EnableQuarantineChecks><RequireCryptoBinding>false</RequireCryptoBinding><PeapExtensions><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</AcceptServerName><IdentityPrivacy xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2"><EnableIdentityPrivacy>true</EnableIdentityPrivacy><AnonymousUserName>anonymous</AnonymousUserName></IdentityPrivacy></PeapExtensions></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}}}}`
#### rdyboost



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### RemoteAccess
  
Performance : `{'Object List': '7584 7620'}`
#### RetailDemo
  
StateFlags : `0x01`
#### SecurityHealthService
  
Security : `01 00 14 80 a4 00 00 00 b0 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 00 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 74 00 05 00 00 00 00 00 14 00 9d 00 02 00 01 01 00 00 00 00 00 05 0b 00 00 00 00 00 18 00 9d 00 02 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 9d 00 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 18 00 9d 00 02 00 01 02 00 00 00 00 00 0f 02 00 00 00 01 00 00 00 00 00 14 00 ff 01 0f 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### SensorService



##### Service Parameters
  
Sensors : `{'{934F17E7-42EF-470B-BE7C-1AD0983C9E6C}': {'RequiredHingeJointsCount': 1, 'RequiredPanelGroupsCount': 2, 'SensorType': '{0D49D945-FA83-4630-A22C-01387F906DE6}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}, '{AEDD7472-297F-4285-B2FB-9422731BCDA6}': {'RequiredHingeJointsCount': 2, 'RequiredPanelGroupsCount': 3, 'SensorType': '{0D49D945-FA83-4630-A22C-01387F906DE6}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}}`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 38 00 34 00 38 00 39 00 42 00 45 00 31 00 43 00 2d 00 38 00 30 00 41 00 34 00 2d 00 34 00 38 00 42 00 43 00 2d 00 39 00 30 00 31 00 41 00 2d 00 41 00 41 00 39 00 31 00 42 00 44 00 38 00 32 00 37 00 41 00 37 00 43 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 42 00 32 00 43 00 45 00 36 00 33 00 34 00 2d 00 31 00 39 00 31 00 44 00 2d 00 34 00 32 00 41 00 46 00 2d 00 41 00 32 00 38 00 43 00 2d 00 31 00 36 00 42 00 45 00 39 00 37 00 39 00 32 00 34 00 43 00 41 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|6|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`39 00 37 00 42 00 45 00 39 00 35 00 30 00 37 00 2d 00 31 00 37 00 44 00 41 00 2d 00 34 00 39 00 39 00 39 00 2d 00 38 00 37 00 44 00 37 00 2d 00 36 00 36 00 43 00 30 00 42 00 32 00 44 00 38 00 33 00 43 00 43 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|7|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`36 00 33 00 32 00 38 00 44 00 43 00 43 00 34 00 2d 00 31 00 36 00 35 00 38 00 2d 00 34 00 31 00 33 00 33 00 2d 00 38 00 30 00 36 00 32 00 2d 00 41 00 39 00 39 00 34 00 33 00 44 00 41 00 43 00 32 00 30 00 39 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### SNMPTrap
  
Description : `@firewallapi.dll,-50324`  
DisplayName : `@firewallapi.dll,-50323`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `ff ff ff ff 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 60 ea 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\snmptrap.exe`  
ObjectName : `NT AUTHORITY\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`
#### StiSvc
  
DependOnService : `RpcSs`  
Description : `@%SystemRoot%\system32\wiaservc.dll,-10`  
DisplayName : `@%SystemRoot%\system32\wiaservc.dll,-9`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k imgsvc`  
ObjectName : `NT Authority\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wiaservc.dll`  
<br></br>  
Security : `01 00 14 80 a0 00 00 00 ac 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 01 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 70 00 05 00 00 00 00 00 14 00 fd 01 02 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 14 00 00 01 00 00 01 01 00 00 00 00 00 05 0b 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`c61fdd6b-0f81-d011-bec7-08002be2092f`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>
#### stornvme



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### TapiSrv
  
Performance : `{'Object List': '1150'}`
#### TermService
  
Performance : `{'Collect Supports Metadata': 1}`
#### TPM



##### Service Parameters
  
KsrGuid : `{F141DC89-3D00-450A-B2D2-AD995267F8FC}`  
<br></br>
#### tzautoupdate
  
StateFlags : `0x01`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 58 bc a3 3e 06 83 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 30 bc a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|6|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 d0 be a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### UGatherer
  
Performance : `{'Object List': '7654'}`
#### UGTHRSVC
  
Performance : `{'Object List': '7760'}`
#### Usb4DeviceRouter
  
ImagePath : `\SystemRoot\System32\DriverStore\FileRepository\usb4devicerouter.inf_amd64_3bffb5f5105936e5\Usb4DeviceRouter.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Base`  
Tag : `0x15`  
DisplayName : `@Usb4DeviceRouter.inf,%Usb4DeviceRouter.SVCDESC%;USB4 Device Router Service`  
Owners : `55 00 73 00 62 00 34 00 44 00 65 00 76 00 69 00 63 00 65 00 52 00 6f 00 75 00 74 00 65 00 72 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
ForceLogsInMiniDump : `0x01`  
<br></br>
#### Usb4HostRouter
  
ImagePath : `\SystemRoot\System32\DriverStore\FileRepository\usb4hostrouter.inf_amd64_dd61aa4ab70fa4fb\Usb4HostRouter.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@Usb4HostRouter.inf,%Usb4HostRouter.SVCDESC%;USB4 Host Router Service`  
Owners : `55 00 73 00 62 00 34 00 48 00 6f 00 73 00 74 00 52 00 6f 00 75 00 74 00 65 00 72 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
DmaRemappingCompatible : `0x01`  
ForceLogsInMiniDump : `0x01`  
<br></br>
#### usbhub
  
Performance : `{'Object List': '9956'}`
#### volmgr



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### volsnap



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### volume



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### WifiCx
  
DependOnService : `NetAdapterCx`  
DisplayName : `Wifi Network Adapter Class Extension`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `system32\drivers\WifiCx.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### XblGameSave



##### Service Parameters
  
FeatureLevel : `0x01`  
<br></br>  
<br></br>  

</details>
  

<details>
  
<summary> Removed </summary>
### WMI AutoLoggers

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
{B1D067C7-2F8C-436E-9E82-C5C2C22229D5} : `{'Enabled': 0, 'EnableLevel': 4, 'MatchAnyKeyword': 18374686479671623680}`
|guid|
| :---: |
|BufferSize|
|ClockType|
|FileMax|
|FileName|
|Guid|
|LogFileMode|
|MaxFileSize|
|MaximumBuffers|
|MinimumBuffers|
|Start|
|{B1D067C7-2F8C-436E-9E82-C5C2C22229D5}|
  
<br></br>
#### EventLog-Application
  
{28e25b07-c47f-473d-8b24-2e171cca808a} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{579402a2-883c-45d8-b70a-9bc856407751} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{83d6e83b-900b-48a3-9835-57656b6f6474} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{973143dd-f3c7-4ef5-b156-544ac38c39b6} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9f973c1d-d056-4e38-84a5-7be81cdd6ab6} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{af0a5a6d-e009-46d4-8867-42f2240f8a72} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{f43c3c35-22e2-53eb-f169-07594054779e} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{28e25b07-c47f-473d-8b24-2e171cca808a}|
|{579402a2-883c-45d8-b70a-9bc856407751}|
|{5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0}|
|{83d6e83b-900b-48a3-9835-57656b6f6474}|
|{973143dd-f3c7-4ef5-b156-544ac38c39b6}|
|{9f973c1d-d056-4e38-84a5-7be81cdd6ab6}|
|{af0a5a6d-e009-46d4-8867-42f2240f8a72}|
|{c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef}|
|{f43c3c35-22e2-53eb-f169-07594054779e}|
  
<br></br>
#### EventLog-System
  
{3903d5b9-988d-4c31-9ccd-4022f96703f0} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{928f7d29-0577-5be5-3bd3-b6bdab9ab307} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9f7b5df4-b902-48bc-bc94-95068c6c7d26} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{b99317e5-89b7-4c0d-abd1-6e705f7912dc} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{c18672d1-dc18-4dfd-91e4-170cf37160cf} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{ea216962-877b-5b73-f7c5-8aef5375959e} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{3903d5b9-988d-4c31-9ccd-4022f96703f0}|
|{928f7d29-0577-5be5-3bd3-b6bdab9ab307}|
|{9f7b5df4-b902-48bc-bc94-95068c6c7d26}|
|{b99317e5-89b7-4c0d-abd1-6e705f7912dc}|
|{c18672d1-dc18-4dfd-91e4-170cf37160cf}|
|{ea216962-877b-5b73-f7c5-8aef5375959e}|
  
<br></br>
#### LwtNetLog
  
{7868B0D4-1423-4681-AFDF-27913575441E} : `{'Enabled': 1, 'EnableLevel': 4, 'MatchAnyKeyword': 1}`
|guid|
| :---: |
|{7868B0D4-1423-4681-AFDF-27913575441E}|
  
<br></br>
#### NtfsLog
  
{740f3c34-57df-4bad-8eea-72ac69ad5df5} : `{'_Description': 'ReFS WPP Trace', 'Enabled': 1, 'EnableFlags': 7, 'EnableLevel': 3}`
|guid|
| :---: |
|{740f3c34-57df-4bad-8eea-72ac69ad5df5}|
  
<br></br>
#### SQMLogger
  
{017BA13C-9A55-4f1f-8200-323055AAC810} : `{'Enabled': 1, 'EnableLevel': 4, 'EnableProperty': 2, 'LoggerName': 'SQMLogger', 'MatchAnyKeyword': 2251799813685248}`
|guid|
| :---: |
|{017BA13C-9A55-4f1f-8200-323055AAC810}|
  
<br></br>
#### WiFiSession
  
{60523747-6516-48B7-84B1-3264FA2CB359} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{60523747-6516-48B7-84B1-3264FA2CB359}|
  
<br></br>
#### WinPhoneCritical
  
{A9C11050-9E93-4fa4-8FE0-7C4750A345B2} : `{'Enabled': 1, 'EnableLevel': 2, 'EnableProperty': 2, 'LoggerName': 'SmsRouter', 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{A9C11050-9E93-4fa4-8FE0-7C4750A345B2}|
  
<br></br>  
<br></br>
### Services

#### BluetoothUserService



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 68 bc a3 2f 02 92 09`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### BthEnum



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
#### BthLEEnum



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
#### BTHPORT



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
#### dmwappushservice
  
RequiredPrivileges : `['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege', 'SeIncreaseWorkingSetPrivilege']`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 61 00 30 00 64 00 62 00 36 00 31 00 34 00 2d 00 65 00 39 00 66 00 62 00 2d 00 34 00 38 00 63 00 66 00 2d 00 39 00 31 00 34 00 33 00 2d 00 37 00 61 00 65 00 37 00 31 00 38 00 66 00 66 00 32 00 63 00 38 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 90 bc a3 28 00 92 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### Eaphost
  
DependOnService : `RPCSSKeyIso`  
Description : `@%systemroot%\system32\eapsvc.dll,-2`  
DisplayName : `@%systemroot%\system32\eapsvc.dll,-1`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 c0 d4 01 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\svchost.exe -k netsvcs -p`  
ObjectName : `localSystem`  
RequiredPrivileges : `['SeTcbPrivilege', 'SeDebugPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_SHARE_PROCESS`  
Methods : `{'311': {'Name': 'Microsoft', '18': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '21': {'PeerConfigUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\TtlsAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\TtlsCfg.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 389863599, 'WLANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames></ServerNames></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}, '23': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1002', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '254': {'14122': {'1': {'PeerDllPath': '%SystemRoot%\\System32\\WcnEapPeerProxy.dll', 'PeerFriendlyName': 'Windows Connect Now EAP Peer', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 8683520}}}, '50': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1003', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '55': {'PeerConfigUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerDllPath': '%SystemRoot%\\System32\\EapTeapAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\EapTeapAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'Properties': 1065154751}}}`


##### Service Parameters
  
PeerInstalled : `0x01`  
ServiceDll : `%SystemRoot%\System32\eapsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
EapProvPlugin : `{'(Default)': '%SystemRoot%\\System32\\eapprovp.dll', 'DllEntryPoint': 'EapProvPlugGetInfo'}`  
<br></br>
#### EventLog
  
SvcMemHardLimitInMB : `0x14`  
SvcMemMidLimitInMB : `0x0f`  
SvcMemSoftLimitInMB : `0x0b`  
Application : `{'LoadPerf': {'ProviderGuid': '{122EE297-BB47-41AE-B265-1CA8D1886D40}'}, 'Microsoft-Windows-PerfCtrs': {'ProviderGuid': '{973143dd-f3c7-4ef5-b156-544ac38c39b6}', 'EventMessageFile': '%SystemRoot%\\system32\\perfctrs.dll'}, 'PDH': {'ProviderGuid': '{04D66358-C4A1-419B-8023-23B73902DE2C}'}, 'PerfCtrs': {'ProviderGuid': '{973143DD-F3C7-4EF5-B156-544AC38C39B6}'}, 'PerfDisk': {'ProviderGuid': '{7F9D83DE-8ABB-457F-98E8-4AD161449ECC}'}, 'Perflib': {'ProviderGuid': '{13B197BD-7CEE-4B4E-8DD0-59314CE374CE}'}, 'PerfNet': {'ProviderGuid': '{CAB2B8A5-49B9-4EEC-B1B0-FAC21DA05A3B}'}, 'PerfOs': {'ProviderGuid': '{F82FB576-E941-4956-A2C7-A0CF83F6450A}'}, 'PerfProc': {'ProviderGuid': '{72D211E1-4C54-4A93-9520-4901681B2271}'}}`  
System : `{'eventlog': {'EventMessageFile': '%SystemRoot%\\System32\\netevent.dll', 'TypesSupported': 7}, 'LSI_SSS': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'megasas': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'Microsoft-Antimalware-ShieldProvider': {'ProviderGuid': '{928f7d29-0577-5be5-3bd3-b6bdab9ab307}', 'EventMessageFile': '%SystemRoot%\\System32\\SecurityHealthService.exe'}}`
#### FrameServer



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 21 bc a3 2e 0f 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`773732e5-76f9-5b4f-9b55-b94699c46e44`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`d752e524-2365-f747-a647-d3465bf1f5ca`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
  
<br></br>
#### HomeGroupListener
  
SvcMemHardLimitInMB : `0xbd`  
SvcMemMidLimitInMB : `0x7e`  
SvcMemSoftLimitInMB : `0x40`  
ApprovedListeners : `{'{125B0F61-0EC3-4f07-9A49-AFB340D9E57F}': {'(Default)': 'File History Hosted Listener', 'SupportedRecordTypes': {'GUID_DPListenerRecordType': '{ADBCFEA5-D8FC-4a46-B12B-EB1FFE39BF17}'}}, '{517F6AA6-D6FA-46D0-8094-17FF17E4CCF4}': {'(Default)': 'Security Hosted Listener', 'SupportedRecordTypes': {'GUID_SecurityListener_SigningKeys': '{CA328F46-E759-4399-82AB-FA92651D1ED2}'}}, '{5255EFED-103A-4444-B124-F88F99E4EF8D}': {'(Default)': 'Printer Hosted Listener'}, '{8ADD018C-5C5F-43C5-BE1E-07BAE85593B7}': {'(Default)': 'Alpha Hosted Listener', 'SupportedRecordTypes': {'GUID_AlphaListener_AlphaAccount': '{929CB323-C5EA-48E7-A6D0-193DD432E769}'}}, '{DE9C1288-0F09-40ff-BA84-7F19279FA74B}': {'(Default)': 'Identity Hosted Listener', 'SupportedRecordTypes': {'GUID_IdentityListenerRecordType': '{07004F5D-93A5-4b6c-B851-E2C9BBFD923D}', 'GUID_IdentityMachineCertRecordType': '{07004F5E-93A5-4b6c-B851-E2C9BBFD923E}'}}, '{EB6B4457-F013-4E5A-9B05-1D44E4D6FAEB}': {'(Default)': 'Sharing Hosted Listener', 'SupportedRecordTypes': {'GUID_SharingListener_MACAddresses': '{A7BC622E-8238-4E38-9C88-34153B7D9AB1}'}}}`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\ListSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ListenerServiceMain`  
<br></br>
#### HomeGroupProvider



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\provsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ProviderServiceMain`  
<br></br>  
ServiceData : `{'LocalJoiningUser': '', 'Password': b'\x00'}`
#### hvservice
  
Description : `@%SystemRoot%\system32\drivers\hvservice.sys,-17`  
Group : `Extended Base`
#### Lsa
  
Performance : `{'Close': 'CloseLsaPerformanceData', 'Collect': 'CollectLsaPerformanceData', 'Library': 'X:\\Windows\\System32\\Secur32.dll', 'Object List': '1570 1670', 'Open': 'OpenLsaPerformanceData'}`
#### LSI_SSS
  
ImagePath : `System32\drivers\lsi_sss.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x0c`  
Owners : `6c 00 73 00 69 00 5f 00 73 00 73 00 73 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x0a`  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### megasas
  
ImagePath : `System32\drivers\megasas.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x0d`  
Owners : `6d 00 65 00 67 00 61 00 73 00 61 00 73 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x08`  
IoTimeoutValue : `0x3c`  
Device : `{'DriverParameter': 'nobusywait=1', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### mshidkmdf
  
Description : `@%SystemRoot%\system32\drivers\mshidkmdf.sys,-101`  
Group : `Base`
#### MSSCNTRS
  
Performance : `{'Close': 'Close', 'Collect': 'Collect', 'Library': '%systemroot%\\system32\\msscntrs.dll', 'Open': 'Open'}`
#### NlaSvc
  
DependOnService : `NSIRpcSsTcpIpDhcpEventlog`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 64 00 00 00 01 00 00 00 64 00 00 00 00 00 00 00 00 00 00 00`


##### Service Parameters
  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  
Security : `01 00 04 80 98 00 00 00 a4 00 00 00 00 00 00 00 14 00 00 00 02 00 84 00 05 00 00 00 00 02 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 02 14 00 ff 01 0f 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 14 00 9d 00 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 28 00 1d 00 02 00 01 06 00 00 00 00 00 05 50 00 00 00 44 3e 41 bb 45 ba a8 7a 6c bd 92 68 f4 ad 64 8f d5 e6 70 e9 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### RFCOMM



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
#### SensorService



##### Service Parameters
  
Sensors : `{'{0D49D945-FA83-4630-A22C-01387F906DE6}': {'PersistentUniqueId': '{934F17E7-42EF-470B-BE7C-1AD0983C9E6C}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}}`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|1||||`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 38 00 34 00 38 00 39 00 42 00 45 00 31 00 43 00 2d 00 38 00 30 00 41 00 34 00 2d 00 34 00 38 00 42 00 43 00 2d 00 39 00 30 00 31 00 41 00 2d 00 41 00 41 00 39 00 31 00 42 00 44 00 38 00 32 00 37 00 41 00 37 00 43 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2||||`44 00 42 00 32 00 43 00 45 00 36 00 33 00 34 00 2d 00 31 00 39 00 31 00 44 00 2d 00 34 00 32 00 41 00 46 00 2d 00 41 00 32 00 38 00 43 00 2d 00 31 00 36 00 42 00 45 00 39 00 37 00 39 00 32 00 34 00 43 00 41 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3||||`39 00 37 00 42 00 45 00 39 00 35 00 30 00 37 00 2d 00 31 00 37 00 44 00 41 00 2d 00 34 00 39 00 39 00 39 00 2d 00 38 00 37 00 44 00 37 00 2d 00 36 00 36 00 43 00 30 00 42 00 32 00 44 00 38 00 33 00 43 00 43 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### SharedAccess
  
Defaults : `{'FirewallPolicy': {'FirewallRules': {'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=6|Profile=Private|LPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-200|Desc=@%systemroot%\\system32\\provsvc.dll,-201|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=6|Profile=Private|RPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-203|Desc=@%systemroot%\\system32\\provsvc.dll,-204|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=17|Profile=Private|LPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-205|Desc=@%systemroot%\\system32\\provsvc.dll,-206|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=17|Profile=Private|RPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-207|Desc=@%systemroot%\\system32\\provsvc.dll,-208|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|'}}}`


##### Service Parameters
  
FirewallPolicy : `{'FirewallRules': {'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=6|Profile=Private|LPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-200|Desc=@%systemroot%\\system32\\provsvc.dll,-201|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=6|Profile=Private|RPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-203|Desc=@%systemroot%\\system32\\provsvc.dll,-204|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=17|Profile=Private|LPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-205|Desc=@%systemroot%\\system32\\provsvc.dll,-206|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=17|Profile=Private|RPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-207|Desc=@%systemroot%\\system32\\provsvc.dll,-208|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|'}, 'RestrictedServices': {'Static': {'System': {'HomeGroup Allow In': 'v2.0|Action=Allow|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|LPort=3587|Protocol=6|Name=Allow Grouping to receive from port 3587|', 'HomeGroup Allow In (PRNP)': 'v2.0|Action=Allow|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|LPort=3540|Protocol=17|Name=Allow PNRP to receive from port 3540|', 'HomeGroup Allow Out': 'v2.0|Action=Allow|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|RPort=3587|Protocol=6|Name=Allow Grouping to send to port 3587|', 'HomeGroup Allow Out (PRNP)': 'v2.0|Action=Allow|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|RPort=3540|Protocol=17|Name=Allow PNRP to send from port 3540|', 'HomeGroup Block In': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|Name=Block homegroup incoming|', 'HomeGroup Block Out': 'V2.0|Action=Block|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|Name=Block homegroup outgoing|', 'HomeGroup Listener Block In': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupListener|Name=Block all incoming|', 'HomeGroup Listener Block Out': 'V2.0|Action=Block|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupListener|Name=Block all outgoing|', 'SettingSyncHost': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\settingsynchost.exe|Name=Block IP traffic to SettingSyncHost|'}}}}`  
<br></br>
#### SNMPTRAP
  
Description : `@firewallapi.dll,-50324`  
DisplayName : `@firewallapi.dll,-50323`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `ff ff ff ff 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 60 ea 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\snmptrap.exe`  
ObjectName : `NT AUTHORITY\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`
#### stisvc
  
DependOnService : `RpcSs`  
Description : `@%SystemRoot%\system32\wiaservc.dll,-10`  
DisplayName : `@%SystemRoot%\system32\wiaservc.dll,-9`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k imgsvc`  
ObjectName : `NT Authority\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wiaservc.dll`  
<br></br>  
Security : `01 00 14 80 a0 00 00 00 ac 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 01 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 70 00 05 00 00 00 00 00 14 00 fd 01 02 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 14 00 00 01 00 00 01 01 00 00 00 00 00 05 0b 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### Synth3dVsc
  
ImagePath : `\SystemRoot\System32\drivers\Synth3dVsc.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Video Init`  
Tag : `0x01`  
Owners : `77 00 73 00 79 00 6e 00 74 00 68 00 33 00 64 00 76 00 73 00 63 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### TapiSrv
  
Performance : `{'ObjectList': '1150'}`
#### Telemetry
  
ImagePath : `System32\drivers\IntelTA.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Core Security Extensions`  
Tag : `0x02`  
DisplayName : `@intelta.inf,%Telemetry.SVCDESC%;Intel(R) Telemetry Service`  
Owners : `69 00 6e 00 74 00 65 00 6c 00 74 00 61 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### wcnfs
  
DependOnService : `FltMgr`  
Description : `@%systemroot%\system32\drivers\wcnfs.sys,-101`  
DisplayName : `@%systemroot%\system32\drivers\wcnfs.sys,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `FSFilter Top`  
ImagePath : `\SystemRoot\system32\drivers\wcnfs.sys`  
Start : `SERVICE_DEMAND_START`  
SupportedFeatures : `0x07`  
Type : `SERVICE_FILE_SYSTEM_DRIVER`  
Instances : `{'DefaultInstance': 'wcnfs Instance', 'wcnfs Instance': {'Altitude': '409900', 'Flags': 0}}`


##### Service Parameters
  
DebugOptions : `0x00`  
<br></br>  
<br></br>  

</details>

# CoreN

## SYSTEM
  

<details>
  
<summary> Added </summary>
### WMI AutoLoggers

#### BioEnrollment
  
Start : `0x00`  
{4b8b1947-ae4d-54e2-826a-1aee78ef05b2} : `{'Enabled': 0}`  
{a55d5a23-1a5b-580a-2be5-d7188f43fae1} : `{'Enabled': 0}`
|guid|
| :---: |
|Start|
|{4b8b1947-ae4d-54e2-826a-1aee78ef05b2}|
|{a55d5a23-1a5b-580a-2be5-d7188f43fae1}|
  
<br></br>
#### EventLog-Application
  
{04d66358-c4a1-419b-8023-23b73902de2c} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{15f4cd44-ca53-5422-db17-4e76821b5a69} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{7628e972-6d6f-4974-b58f-6428622ec09a} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{7d44233d-3055-4b9c-ba64-0d47ca40a232} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 2305843009213693952, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9068a924-f97e-5506-c3a3-5c020c00e8e0} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{a70ff94f-570b-4979-ba5c-e59c9feab61b} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{ad8aa069-a01b-40a0-ba40-948d1d8dedc5} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{04d66358-c4a1-419b-8023-23b73902de2c}|
|{15f4cd44-ca53-5422-db17-4e76821b5a69}|
|{7628e972-6d6f-4974-b58f-6428622ec09a}|
|{7d44233d-3055-4b9c-ba64-0d47ca40a232}|
|{9068a924-f97e-5506-c3a3-5c020c00e8e0}|
|{a70ff94f-570b-4979-ba5c-e59c9feab61b}|
|{ad8aa069-a01b-40a0-ba40-948d1d8dedc5}|
  
<br></br>
#### EventLog-System
  
{0075e1ab-e1d1-5d1f-35f5-da36fb4f41b1} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{17d2a329-4539-5f4d-3435-f510634ce3b9} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{5bcf2a5c-2e90-5a03-aa4e-2e459bae21b4} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{6600e712-c3b6-44a2-8a48-935c511f28c8} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 2305843009213693952, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{7f54ca8a-6c72-5cbc-b96f-d0ef905b8bce} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{87a623f0-8db5-5c11-7c80-a2ebbcbe5189} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{93db76c2-63ab-5de1-88b3-c068686675b8} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9799276c-fb04-47e8-845e-36946045c218} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 2305843009213693952, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{a2d34bf1-70ab-5b21-c819-5a0dd42748fd} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{b931ed29-66f4-576e-0579-0b8818a5dc6b} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{bcf0c6a7-6130-5208-f27d-fa77a91f12df} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{d07e8c3f-78fb-4c22-b77c-2203d00bfdf3} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{f6cf91be-e7d7-57d6-2a3d-278ca406d190} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{0075e1ab-e1d1-5d1f-35f5-da36fb4f41b1}|
|{17d2a329-4539-5f4d-3435-f510634ce3b9}|
|{5bcf2a5c-2e90-5a03-aa4e-2e459bae21b4}|
|{6600e712-c3b6-44a2-8a48-935c511f28c8}|
|{7f54ca8a-6c72-5cbc-b96f-d0ef905b8bce}|
|{87a623f0-8db5-5c11-7c80-a2ebbcbe5189}|
|{93db76c2-63ab-5de1-88b3-c068686675b8}|
|{9799276c-fb04-47e8-845e-36946045c218}|
|{a2d34bf1-70ab-5b21-c819-5a0dd42748fd}|
|{b931ed29-66f4-576e-0579-0b8818a5dc6b}|
|{bcf0c6a7-6130-5208-f27d-fa77a91f12df}|
|{d07e8c3f-78fb-4c22-b77c-2203d00bfdf3}|
|{f6cf91be-e7d7-57d6-2a3d-278ca406d190}|
  
<br></br>
#### FaceCredProv
  
Start : `0x00`  
{1D480C11-3870-4B19-9144-47A53CD973BD} : `{'Enabled': 0}`
|guid|
| :---: |
|Start|
|{1D480C11-3870-4B19-9144-47A53CD973BD}|
  
<br></br>
#### FaceTel
  
Start : `0x00`  
{22eb0808-0b6c-5cd4-5511-6a77e6e73a93} : `{'Enabled': 0}`
|guid|
| :---: |
|Start|
|{22eb0808-0b6c-5cd4-5511-6a77e6e73a93}|
  
<br></br>
#### NetCore
  
{923C0FFD-7933-4B52-8A49-121ABF2DC357} : `{'@': 'triage_routepolicymanagement_tracelogging', 'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{923C0FFD-7933-4B52-8A49-121ABF2DC357}|
  
<br></br>
#### NtfsLog
  
{aa381297-bccb-4569-8e39-bbbb3b400893} : `{'_Description': 'TmLog Trace Provider', 'Enabled': 1, 'EnableFlags': 15, 'EnableLevel': 5}`
|guid|
| :---: |
|{aa381297-bccb-4569-8e39-bbbb3b400893}|
  
<br></br>
#### ReFSLog
  
ClockType : `0x02`  
GUID : `{81a69395-9f48-48f2-b88c-2401db1e3a91}`  
Start : `0x01`  
{740f3c34-57df-4bad-8eea-72ac69ad5df5} : `{'_Description': 'ReFS WPP Trace', 'Enabled': 1, 'EnableFlags': 7, 'EnableLevel': 3}`
|guid|
| :---: |
|ClockType|
|GUID|
|Start|
|{740f3c34-57df-4bad-8eea-72ac69ad5df5}|
  
<br></br>
#### SetupPlatformTel
  
{D2F37B94-92A5-44E2-AFC9-2F4489D39268} : `{'Enabled': 1, 'EnableLevel': 255}`
|guid|
| :---: |
|{D2F37B94-92A5-44E2-AFC9-2F4489D39268}|
  
<br></br>
#### SpoolerLogger
  
{ba4936a1-31db-4edc-89ce-9190e3c0653b} : `{'Enabled': 1, 'EnableFlags': 0, 'EnableLevel': 5}`
|guid|
| :---: |
|{ba4936a1-31db-4edc-89ce-9190e3c0653b}|
  
<br></br>
#### WiFiSession
  
{745976be-5e09-5c76-eabd-76c93c9212d2} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`  
{ae164ede-2246-5b24-c145-29c484f7362a} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`  
{EA893635-5AB7-562B-75A2-A22107D8058F} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{745976be-5e09-5c76-eabd-76c93c9212d2}|
|{ae164ede-2246-5b24-c145-29c484f7362a}|
|{EA893635-5AB7-562B-75A2-A22107D8058F}|
  
<br></br>  
<br></br>
### Services

#### ACPI



##### Service Parameters
  
PnpAsyncNewDevices : `0x01`  
<br></br>
#### Appinfo



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 66 00 37 00 33 00 38 00 65 00 32 00 30 00 2d 00 37 00 33 00 63 00 30 00 2d 00 34 00 63 00 61 00 38 00 2d 00 61 00 61 00 36 00 61 00 2d 00 38 00 64 00 66 00 65 00 66 00 35 00 34 00 35 00 66 00 65 00 61 00 38 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### AppleSSD
  
ImagePath : `System32\drivers\AppleSSD.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x01`  
DisplayName : `@AppleSSD.inf,%DevDesc1%;Apple Solid State Drive Device`  
Owners : `41 00 70 00 70 00 6c 00 65 00 53 00 53 00 44 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x01`  
Device : `{'MaxTranLenInPages': 64}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### BFE



##### Service Parameters
  
Policy  
Persistent  
ProviderContext
|GUID|Data|
| :---: | :---: |
|{30433c31-b05f-421f-8fde-018ea4c68af4}|`01 10 08 00 cc cc cc cc 10 01 00 00 00 00 00 00 00 00 02 00 01 00 00 00 f0 00 00 00 04 00 02 00 00 00 00 00 00 00 00 00 f0 00 00 00 01 10 08 00 cc cc cc cc e0 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 31 3c 43 30 5f b0 1f 42 8f de 01 8e a4 c6 8a f4 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 00 00 00 00 00 00 00 00 08 00 00 00 08 00 00 00 10 00 02 00 00 00 00 00 05 00 00 00 00 00 00 80 07 00 00 00 00 00 00 00 07 00 00 00 4d 00 50 00 53 00 53 00 56 00 43 00 00 00 00 00 15 00 00 00 00 00 00 00 15 00 00 00 53 00 74 00 6f 00 72 00 65 00 73 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 20 00 6f 00 72 00 69 00 67 00 69 00 6e 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 26 00 00 00 14 00 02 00 26 00 00 00 51 00 75 00 61 00 72 00 61 00 6e 00 74 00 69 00 6e 00 65 00 20 00 44 00 65 00 66 00 61 00 75 00 6c 00 74 00 00 00 00 00 00 00 00 00`|
|{93132c36-6e06-4e6f-a10b-218787cd49cf}|`01 10 08 00 cc cc cc cc 10 01 00 00 00 00 00 00 00 00 02 00 01 00 00 00 f0 00 00 00 04 00 02 00 00 00 00 00 00 00 00 00 f0 00 00 00 01 10 08 00 cc cc cc cc e0 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 36 2c 13 93 06 6e 6f 4e a1 0b 21 87 87 cd 49 cf 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 00 00 00 00 00 00 00 00 08 00 00 00 08 00 00 00 10 00 02 00 00 00 00 00 06 00 00 00 00 00 00 80 07 00 00 00 00 00 00 00 07 00 00 00 4d 00 50 00 53 00 53 00 56 00 43 00 00 00 00 00 15 00 00 00 00 00 00 00 15 00 00 00 53 00 74 00 6f 00 72 00 65 00 73 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 20 00 6f 00 72 00 69 00 67 00 69 00 6e 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 22 00 00 00 14 00 02 00 22 00 00 00 42 00 6f 00 6f 00 74 00 74 00 69 00 6d 00 65 00 20 00 44 00 65 00 66 00 61 00 75 00 6c 00 74 00 00 00 00 00 00 00 00 00 00 00 00 00`|
  
<br></br>
#### cbdhsvc
  
DelayedAutoStart : `0x01`
#### CldFlt



##### Service Parameters
  
USMsgTimeoutMillis : `0x3e8`  
<br></br>
#### dcsvc
  
DelayedAutoStart : `0x01`  
DependOnService : `rpcss`  
Description : `@%systemroot%\system32\dcsvc.dll,-101`  
DisplayName : `@%systemroot%\system32\dcsvc,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 04 00 00 00 14 00 00 00 01 00 00 00 10 27 00 00 01 00 00 00 10 27 00 00 01 00 00 00 10 27 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%systemroot%\system32\svchost.exe -k netsvcs -p`  
ObjectName : `LocalSystem`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`


##### Service Parameters
  
IdleTimeout(sec) : `0x78`  
ServiceDll : `%SystemRoot%\system32\dcsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`35 00 39 00 62 00 65 00 62 00 39 00 37 00 37 00 2d 00 64 00 30 00 33 00 37 00 2d 00 34 00 38 00 66 00 34 00 2d 00 61 00 66 00 37 00 34 00 2d 00 63 00 61 00 30 00 37 00 35 00 34 00 39 00 33 00 61 00 35 00 32 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 61 00 30 00 64 00 62 00 36 00 31 00 34 00 2d 00 65 00 39 00 66 00 62 00 2d 00 34 00 38 00 63 00 66 00 2d 00 39 00 31 00 34 00 33 00 2d 00 37 00 61 00 65 00 37 00 31 00 38 00 66 00 66 00 32 00 63 00 38 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### DeviceInstall



##### Service Parameters
  
DeviceInstallMode : `0x01`  
<br></br>
#### disk



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### Dnscache



##### Service Parameters
  
DohWellKnownServers : `{'1.0.0.1': {'Template': 'https://cloudflare-dns.com/dns-query'}, '1.1.1.1': {'Template': 'https://cloudflare-dns.com/dns-query'}, '149.112.112.112': {'Template': 'https://dns.quad9.net/dns-query'}, '2001:4860:4860::8844': {'Template': 'https://dns.google/dns-query'}, '2001:4860:4860::8888': {'Template': 'https://dns.google/dns-query'}, '2606:4700:4700::1001': {'Template': 'https://cloudflare-dns.com/dns-query'}, '2606:4700:4700::1111': {'Template': 'https://cloudflare-dns.com/dns-query'}, '2620:fe::fe': {'Template': 'https://dns.quad9.net/dns-query'}, '2620:fe::fe:9': {'Template': 'https://dns.quad9.net/dns-query'}, '8.8.4.4': {'Template': 'https://dns.google/dns-query'}, '8.8.8.8': {'Template': 'https://dns.google/dns-query'}, '9.9.9.9': {'Template': 'https://dns.quad9.net/dns-query'}}`  
<br></br>
#### EapHost
  
DependOnService : `RPCSSKeyIso`  
Description : `@%systemroot%\system32\eapsvc.dll,-2`  
DisplayName : `@%systemroot%\system32\eapsvc.dll,-1`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 c0 d4 01 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\svchost.exe -k netsvcs -p`  
ObjectName : `localSystem`  
RequiredPrivileges : `['SeTcbPrivilege', 'SeDebugPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_SHARE_PROCESS`  
Methods : `{'311': {'Name': 'Microsoft', '18': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '21': {'PeerConfigUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\TtlsAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\TtlsCfg.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 389863599, 'LANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}, 'WLANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}, '23': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1002', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '254': {'14122': {'1': {'PeerDllPath': '%SystemRoot%\\System32\\WcnEapPeerProxy.dll', 'PeerFriendlyName': 'Windows Connect Now EAP Peer', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 8683520}}}, '50': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1003', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '55': {'PeerConfigUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerDllPath': '%SystemRoot%\\System32\\EapTeapAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\EapTeapAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'Properties': 1065154751, 'LANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}, 'WLANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="utf-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><TrustedRootCAHash></TrustedRootCAHash></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection> </CertificateStore> </CredentialsSource><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="utf-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><TrustedRootCAHash></TrustedRootCAHash></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}}}`


##### Service Parameters
  
PeerInstalled : `0x01`  
ServiceDll : `%SystemRoot%\System32\eapsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
EapProvPlugin : `{'(Default)': '%SystemRoot%\\System32\\eapprovp.dll', 'DllEntryPoint': 'EapProvPlugGetInfo'}`  
<br></br>
#### ebdrv0
  
ImagePath : `System32\drivers\evbd0a.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `System Bus Extender`  
Tag : `0x03`  
DisplayName : `@netevbd0a.inf,%vbd_srv_desc%;QLogic Legacy Ethernet Adapter VBD`  
Owners : `6e 00 65 00 74 00 65 00 76 00 62 00 64 00 30 00 61 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### EhStorClass



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### EventLog
  
Application : `{'Microsoft-Windows-PDH': {'ProviderGuid': '{04d66358-c4a1-419b-8023-23b73902de2c}', 'EventMessageFile': '%SystemRoot%\\system32\\pdh.dll'}, 'Universal Print': {'EventMessageFile': '%SystemRoot%\\System32\\McpManagementService.dll', 'TypesSupported': 7}}`  
System : `{'AppleSSD': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'ebdrv0': {'eventmessagefile': '%SystemRoot%\\System32\\drivers\\evbd0a.sys;%SystemRoot%\\System32\\iologmsg.dll', 'typessupported': 7}, 'EventLog': {'EventMessageFile': '%SystemRoot%\\System32\\netevent.dll', 'TypesSupported': 7}, 'hvservice': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'Microsoft-Windows-Iphlpsvc-Trace': {'ProviderGuid': '{6600e712-c3b6-44a2-8a48-935c511f28c8}', 'EventMessageFile': '%windir%\\system32\\iphlpsvc.dll'}, 'Microsoft-Windows-Network-ExecutionContext': {'ProviderGuid': '{0075e1ab-e1d1-5d1f-35f5-da36fb4f41b1}', 'EventMessageFile': '%SystemRoot%\\system32\\drivers\\ExecutionContext.sys'}, 'Microsoft-Windows-USB-USB4DeviceRouter-EventLogs': {'ProviderGuid': '{d07e8c3f-78fb-4c22-b77c-2203d00bfdf3}', 'EventMessageFile': '%SystemRoot%\\System32\\DriverStore\\FileRepository\\usb4devicerouter.inf_amd64_3bffb5f5105936e5\\Usb4DeviceRouter.sys'}, 'mpi3drvi': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'nvmedisk': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll;%SystemRoot%\\System32\\drivers\\nvmedisk.sys', 'TypesSupported': 7}}`
#### ExecutionContext
  
DisplayName : `@%SystemRoot%\System32\Drivers\ExecutionContext.sys,-101`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `System`  
ImagePath : `System32\Drivers\ExecutionContext.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### FrameServerMonitor
  
DependOnService : `rpcss`  
Description : `@%systemroot%\system32\FrameServerMonitor.dll,-101`  
DisplayName : `@%systemroot%\system32\FrameServerMonitor.dll,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 20 bf 02 00`  
ImagePath : `%SystemRoot%\System32\svchost.exe -k CameraMonitor`  
ObjectName : `LocalSystem`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`  
parameters : `{'ServiceDll': '%SystemRoot%\\system32\\FrameServerMonitor.dll', 'ServiceDllUnloadOnStop': 1}`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`42 00 45 00 30 00 44 00 39 00 35 00 42 00 41 00 2d 00 32 00 31 00 41 00 35 00 2d 00 34 00 41 00 35 00 46 00 2d 00 41 00 31 00 46 00 30 00 2d 00 39 00 41 00 44 00 41 00 38 00 34 00 41 00 43 00 31 00 31 00 34 00 34 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 26 1d 90 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 21 bc a3 2e 0f 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`773732e5-76f9-5b4f-9b55-b94699c46e44`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`d752e524-2365-f747-a647-d3465bf1f5ca`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 b8 bc a3 3d 01 c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### fvevol



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### hidspi
  
DependOnService : `HidSpiCx`
#### HidSpiCx
  
DisplayName : `HidSpi KMDF Class Extension`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `system32\drivers\HidSpiCx.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### Hsp
  
ImagePath : `\SystemRoot\System32\drivers\Hsp.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@hsp.inf,%Hsp.SVCDESC%;Microsoft Pluton Service`  
Owners : `68 00 73 00 70 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
Wdf : `{'KmdfLibraryVersion': '1.15'}`  
<br></br>
#### hvservice
  
Owners : `68 00 76 00 73 00 65 00 72 00 76 00 69 00 63 00 65 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### IntelPMT
  
ImagePath : `System32\drivers\IntelPMT.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Core Security Extensions`  
Tag : `0x02`  
DisplayName : `@intelpmt.inf,%IntelPMT.SVCDESC%;Intel(R) Platform Monitoring Technology Service`  
Owners : `69 00 6e 00 74 00 65 00 6c 00 70 00 6d 00 74 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### iorate



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### lfsvc
  
Settings : `{'LocationWebServiceProxy': {'USE_CLIENT_PROXY_INFERENCE_ONLY': 0}}`
#### McpManagementService
  
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


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\McpManagementService.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>
#### mpi3drvi
  
ImagePath : `System32\drivers\mpi3drvi.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x10`  
Owners : `6d 00 70 00 69 00 33 00 64 00 72 00 76 00 69 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x08`  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### NDIS



##### Service Parameters
  
Reserved : `{'ExecutionContextProfiles': {'Balanced': {'DpcWatchdogTimerThreshold': 80, 'Flags': 0, 'MaxPacketsReceiveAtDispatch': 64, 'MaxPacketsReceiveAtPassive': 64, 'MaxPacketsReceiveCompleteAtDispatch': 64, 'MaxPacketsReceiveCompleteAtPassive': 64, 'MaxPacketsSendAtDispatch': 64, 'MaxPacketsSendAtPassive': 64, 'MaxPacketsSendCompleteAtDispatch': 64, 'MaxPacketsSendCompleteAtPassive': 64, 'MaxTimeAtDispatch': 0, 'WorkerThreadPriority': 10}}}`  
<br></br>
#### NDKPerf
  
DisplayName : `NDKPerf Driver`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `system32\drivers\NDKPerf.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### NPSMSvc
  
Description : `@%SystemRoot%\system32\npsm.dll,-101`  
DisplayName : `@%SystemRoot%\system32\npsm.dll,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 b8 0b 00 00 01 00 00 00 b8 0b 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k LocalService -p`  
ObjectName : `NT AUTHORITY\LocalService`  
RequiredPrivileges : `['SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `96`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\npsm.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  
Security : `01 00 14 80 a0 00 00 00 ac 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 01 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 70 00 05 00 00 00 00 00 14 00 fd 01 02 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 14 00 00 01 00 00 01 01 00 00 00 00 00 05 0b 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### nvmedisk
  
ImagePath : `System32\drivers\nvmedisk.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@nvmedisk.inf,%nvmedisk.SvcDesc%;Microsoft NVMe disk driver`  
Owners : `6e 00 76 00 6d 00 65 00 64 00 69 00 73 00 6b 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### P9NP
  
Description : `@%systemroot%\system32\p9np.dll,-101`  
DisplayName : `@%systemroot%\system32\p9np.dll,-100`  
NetworkProvider : `{'DeviceName': '\\Device\\P9Rdr', 'DisplayName': '@%systemroot%\\system32\\p9np.dll,-100', 'Name': 'Plan 9 Network Provider', 'ProviderPath': '%SystemRoot%\\System32\\p9np.dll', 'TriggerStartCompleteNotification': b'u\x10\xbc\xa3T\x1e\xc6A', 'TriggerStartNotification': b'u\x08\xbc\xa3T\x1e\xc6A', 'TriggerStartPrefix': b'w\x00s\x00l\x00.\x00l\x00o\x00c\x00a\x00l\x00h\x00o\x00s\x00t\x00\x00\x00w\x00s\x00l\x00$\x00\x00\x00\x00\x00'}`
#### P9Rdr
  
DependOnService : `RDBSS`  
Description : `@%SystemRoot%\System32\drivers\p9rdr.sys,-101`  
DisplayName : `@%SystemRoot%\System32\drivers\p9rdr.sys,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `System32\drivers\p9rdr.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### P9RdrService
  
DependOnService : `P9RdrRPCSS`  
Description : `@%systemroot%\system32\p9rdrservice.dll,-101`  
DisplayName : `@%systemroot%\system32\p9rdrservice.dll,-102`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 b8 0b 00 00 01 00 00 00 b8 0b 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%systemroot%\system32\svchost.exe -k P9RdrService -p`  
ObjectName : `LocalSystem`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `96`  
UserServiceFlags : `0x03`  
parameters : `{'ServiceDll': '%SystemRoot%\\system32\\p9rdrservice.dll', 'ServiceDllUnloadOnStop': 1}`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 54 1e c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### partmgr



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### PcaSvc



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 d0 be a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 18 bc a3 2e 07 c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 2e 03 96 15`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### pci



##### Service Parameters
  
PnpAsyncNewDevices : `0x01`  
<br></br>
#### PenService
  
Description : `@%SystemRoot%\system32\PenService.dll,-101`  
DisplayName : `@%SystemRoot%\system32\PenService.dll,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 02 00 00 00 14 00 00 00 01 00 00 00 10 27 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k PenService`  
Start : `SERVICE_DEMAND_START`  
Type : `96`  
UserServiceFlags : `0x02`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\PenService.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|Data1|Data2|Data3|DataType0|DataType1|DataType2|DataType3|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`b2551e4d-6ff1-cf11-88cb-001111000030`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 31 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 32 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 33 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 46 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### PerfDisk
  
Performance : `{'Collect Supports Metadata': 1}`
#### PerfNet
  
Performance : `{'Collect Supports Metadata': 1}`
#### PerfOS
  
Performance : `{'Collect Supports Metadata': 1}`
#### PerfProc
  
Performance : `{'Collect Supports Metadata': 1}`
#### PrintWorkflowUserSvc



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 3d 0a 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### PRM
  
ImagePath : `System32\DriverStore\FileRepository\prm.inf_amd64_7fc9bb8ba2b73803\PRM.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@prm.inf,%PRM.SvcDesc%;Microsoft PRM Driver`  
Owners : `70 00 72 00 6d 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### RasMan
  
PPP : `{'EAP': {'13': {'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '25': {'LANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">25</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>25</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV1"><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><FastReconnect>true</FastReconnect><InnerEapOptional>false</InnerEapOptional><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap><EnableQuarantineChecks>false</EnableQuarantineChecks><RequireCryptoBinding>false</RequireCryptoBinding><PeapExtensions><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</AcceptServerName><IdentityPrivacy xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2"><EnableIdentityPrivacy>true</EnableIdentityPrivacy><AnonymousUserName>anonymous</AnonymousUserName></IdentityPrivacy></PeapExtensions></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">25</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>25</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV1"><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><FastReconnect>true</FastReconnect><InnerEapOptional>false</InnerEapOptional><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap><EnableQuarantineChecks>false</EnableQuarantineChecks><RequireCryptoBinding>false</RequireCryptoBinding><PeapExtensions><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</AcceptServerName><IdentityPrivacy xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2"><EnableIdentityPrivacy>true</EnableIdentityPrivacy><AnonymousUserName>anonymous</AnonymousUserName></IdentityPrivacy></PeapExtensions></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}}}}`
#### rdyboost



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### RemoteAccess
  
Performance : `{'Object List': '7106 7142'}`
#### RetailDemo
  
StateFlags : `0x01`
#### SecurityHealthService
  
Security : `01 00 14 80 a4 00 00 00 b0 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 00 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 74 00 05 00 00 00 00 00 14 00 9d 00 02 00 01 01 00 00 00 00 00 05 0b 00 00 00 00 00 18 00 9d 00 02 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 9d 00 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 18 00 9d 00 02 00 01 02 00 00 00 00 00 0f 02 00 00 00 01 00 00 00 00 00 14 00 ff 01 0f 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### SensorService



##### Service Parameters
  
Sensors : `{'{934F17E7-42EF-470B-BE7C-1AD0983C9E6C}': {'RequiredHingeJointsCount': 1, 'RequiredPanelGroupsCount': 2, 'SensorType': '{0D49D945-FA83-4630-A22C-01387F906DE6}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}, '{AEDD7472-297F-4285-B2FB-9422731BCDA6}': {'RequiredHingeJointsCount': 2, 'RequiredPanelGroupsCount': 3, 'SensorType': '{0D49D945-FA83-4630-A22C-01387F906DE6}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}}`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 38 00 34 00 38 00 39 00 42 00 45 00 31 00 43 00 2d 00 38 00 30 00 41 00 34 00 2d 00 34 00 38 00 42 00 43 00 2d 00 39 00 30 00 31 00 41 00 2d 00 41 00 41 00 39 00 31 00 42 00 44 00 38 00 32 00 37 00 41 00 37 00 43 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 42 00 32 00 43 00 45 00 36 00 33 00 34 00 2d 00 31 00 39 00 31 00 44 00 2d 00 34 00 32 00 41 00 46 00 2d 00 41 00 32 00 38 00 43 00 2d 00 31 00 36 00 42 00 45 00 39 00 37 00 39 00 32 00 34 00 43 00 41 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|6|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`39 00 37 00 42 00 45 00 39 00 35 00 30 00 37 00 2d 00 31 00 37 00 44 00 41 00 2d 00 34 00 39 00 39 00 39 00 2d 00 38 00 37 00 44 00 37 00 2d 00 36 00 36 00 43 00 30 00 42 00 32 00 44 00 38 00 33 00 43 00 43 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|7|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`36 00 33 00 32 00 38 00 44 00 43 00 43 00 34 00 2d 00 31 00 36 00 35 00 38 00 2d 00 34 00 31 00 33 00 33 00 2d 00 38 00 30 00 36 00 32 00 2d 00 41 00 39 00 39 00 34 00 33 00 44 00 41 00 43 00 32 00 30 00 39 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### SNMPTrap
  
Description : `@firewallapi.dll,-50324`  
DisplayName : `@firewallapi.dll,-50323`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `ff ff ff ff 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 60 ea 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\snmptrap.exe`  
ObjectName : `NT AUTHORITY\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`
#### StiSvc
  
DependOnService : `RpcSs`  
Description : `@%SystemRoot%\system32\wiaservc.dll,-10`  
DisplayName : `@%SystemRoot%\system32\wiaservc.dll,-9`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k imgsvc`  
ObjectName : `NT Authority\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wiaservc.dll`  
<br></br>  
Security : `01 00 14 80 a0 00 00 00 ac 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 01 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 70 00 05 00 00 00 00 00 14 00 fd 01 02 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 14 00 00 01 00 00 01 01 00 00 00 00 00 05 0b 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`c61fdd6b-0f81-d011-bec7-08002be2092f`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>
#### stornvme



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### TapiSrv
  
Performance : `{'Object List': '1150'}`
#### TermService
  
Performance : `{'Collect Supports Metadata': 1}`
#### TPM



##### Service Parameters
  
KsrGuid : `{F141DC89-3D00-450A-B2D2-AD995267F8FC}`  
<br></br>
#### tzautoupdate
  
StateFlags : `0x01`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 58 bc a3 3e 06 83 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 30 bc a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|6|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 d0 be a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### UGatherer
  
Performance : `{'Object List': '7146'}`
#### UGTHRSVC
  
Performance : `{'Object List': '7252'}`
#### Usb4DeviceRouter
  
ImagePath : `\SystemRoot\System32\DriverStore\FileRepository\usb4devicerouter.inf_amd64_3bffb5f5105936e5\Usb4DeviceRouter.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Base`  
Tag : `0x15`  
DisplayName : `@Usb4DeviceRouter.inf,%Usb4DeviceRouter.SVCDESC%;USB4 Device Router Service`  
Owners : `55 00 73 00 62 00 34 00 44 00 65 00 76 00 69 00 63 00 65 00 52 00 6f 00 75 00 74 00 65 00 72 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
ForceLogsInMiniDump : `0x01`  
<br></br>
#### Usb4HostRouter
  
ImagePath : `\SystemRoot\System32\DriverStore\FileRepository\usb4hostrouter.inf_amd64_dd61aa4ab70fa4fb\Usb4HostRouter.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@Usb4HostRouter.inf,%Usb4HostRouter.SVCDESC%;USB4 Host Router Service`  
Owners : `55 00 73 00 62 00 34 00 48 00 6f 00 73 00 74 00 52 00 6f 00 75 00 74 00 65 00 72 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
DmaRemappingCompatible : `0x01`  
ForceLogsInMiniDump : `0x01`  
<br></br>
#### usbhub
  
Performance : `{'Object List': '7468'}`
#### volmgr



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### volsnap



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### volume



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### WifiCx
  
DependOnService : `NetAdapterCx`  
DisplayName : `Wifi Network Adapter Class Extension`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `system32\drivers\WifiCx.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### XblGameSave



##### Service Parameters
  
FeatureLevel : `0x01`  
<br></br>  
<br></br>  

</details>
  

<details>
  
<summary> Removed </summary>
### WMI AutoLoggers

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
{B1D067C7-2F8C-436E-9E82-C5C2C22229D5} : `{'Enabled': 0, 'EnableLevel': 4, 'MatchAnyKeyword': 18374686479671623680}`
|guid|
| :---: |
|BufferSize|
|ClockType|
|FileMax|
|FileName|
|Guid|
|LogFileMode|
|MaxFileSize|
|MaximumBuffers|
|MinimumBuffers|
|Start|
|{B1D067C7-2F8C-436E-9E82-C5C2C22229D5}|
  
<br></br>
#### EventLog-Application
  
{28e25b07-c47f-473d-8b24-2e171cca808a} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{579402a2-883c-45d8-b70a-9bc856407751} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{83d6e83b-900b-48a3-9835-57656b6f6474} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{973143dd-f3c7-4ef5-b156-544ac38c39b6} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9f973c1d-d056-4e38-84a5-7be81cdd6ab6} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{af0a5a6d-e009-46d4-8867-42f2240f8a72} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{f43c3c35-22e2-53eb-f169-07594054779e} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{28e25b07-c47f-473d-8b24-2e171cca808a}|
|{579402a2-883c-45d8-b70a-9bc856407751}|
|{5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0}|
|{83d6e83b-900b-48a3-9835-57656b6f6474}|
|{973143dd-f3c7-4ef5-b156-544ac38c39b6}|
|{9f973c1d-d056-4e38-84a5-7be81cdd6ab6}|
|{af0a5a6d-e009-46d4-8867-42f2240f8a72}|
|{c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef}|
|{f43c3c35-22e2-53eb-f169-07594054779e}|
  
<br></br>
#### EventLog-System
  
{3903d5b9-988d-4c31-9ccd-4022f96703f0} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{928f7d29-0577-5be5-3bd3-b6bdab9ab307} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9f7b5df4-b902-48bc-bc94-95068c6c7d26} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{b99317e5-89b7-4c0d-abd1-6e705f7912dc} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{c18672d1-dc18-4dfd-91e4-170cf37160cf} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{ea216962-877b-5b73-f7c5-8aef5375959e} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{3903d5b9-988d-4c31-9ccd-4022f96703f0}|
|{928f7d29-0577-5be5-3bd3-b6bdab9ab307}|
|{9f7b5df4-b902-48bc-bc94-95068c6c7d26}|
|{b99317e5-89b7-4c0d-abd1-6e705f7912dc}|
|{c18672d1-dc18-4dfd-91e4-170cf37160cf}|
|{ea216962-877b-5b73-f7c5-8aef5375959e}|
  
<br></br>
#### LwtNetLog
  
{7868B0D4-1423-4681-AFDF-27913575441E} : `{'Enabled': 1, 'EnableLevel': 4, 'MatchAnyKeyword': 1}`
|guid|
| :---: |
|{7868B0D4-1423-4681-AFDF-27913575441E}|
  
<br></br>
#### NtfsLog
  
{740f3c34-57df-4bad-8eea-72ac69ad5df5} : `{'_Description': 'ReFS WPP Trace', 'Enabled': 1, 'EnableFlags': 7, 'EnableLevel': 3}`
|guid|
| :---: |
|{740f3c34-57df-4bad-8eea-72ac69ad5df5}|
  
<br></br>
#### SQMLogger
  
{017BA13C-9A55-4f1f-8200-323055AAC810} : `{'Enabled': 1, 'EnableLevel': 4, 'EnableProperty': 2, 'LoggerName': 'SQMLogger', 'MatchAnyKeyword': 2251799813685248}`
|guid|
| :---: |
|{017BA13C-9A55-4f1f-8200-323055AAC810}|
  
<br></br>
#### WiFiSession
  
{60523747-6516-48B7-84B1-3264FA2CB359} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{60523747-6516-48B7-84B1-3264FA2CB359}|
  
<br></br>
#### WinPhoneCritical
  
{A9C11050-9E93-4fa4-8FE0-7C4750A345B2} : `{'Enabled': 1, 'EnableLevel': 2, 'EnableProperty': 2, 'LoggerName': 'SmsRouter', 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{A9C11050-9E93-4fa4-8FE0-7C4750A345B2}|
  
<br></br>  
<br></br>
### Services

#### BluetoothUserService



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 68 bc a3 2f 02 92 09`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### BthEnum



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
#### BthLEEnum



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
#### BTHPORT



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
#### dmwappushservice
  
RequiredPrivileges : `['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege', 'SeIncreaseWorkingSetPrivilege']`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 61 00 30 00 64 00 62 00 36 00 31 00 34 00 2d 00 65 00 39 00 66 00 62 00 2d 00 34 00 38 00 63 00 66 00 2d 00 39 00 31 00 34 00 33 00 2d 00 37 00 61 00 65 00 37 00 31 00 38 00 66 00 66 00 32 00 63 00 38 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 90 bc a3 28 00 92 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### Eaphost
  
DependOnService : `RPCSSKeyIso`  
Description : `@%systemroot%\system32\eapsvc.dll,-2`  
DisplayName : `@%systemroot%\system32\eapsvc.dll,-1`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 c0 d4 01 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\svchost.exe -k netsvcs -p`  
ObjectName : `localSystem`  
RequiredPrivileges : `['SeTcbPrivilege', 'SeDebugPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_SHARE_PROCESS`  
Methods : `{'311': {'Name': 'Microsoft', '18': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '21': {'PeerConfigUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\TtlsAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\TtlsCfg.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 389863599, 'WLANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames></ServerNames></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}, '23': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1002', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '254': {'14122': {'1': {'PeerDllPath': '%SystemRoot%\\System32\\WcnEapPeerProxy.dll', 'PeerFriendlyName': 'Windows Connect Now EAP Peer', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 8683520}}}, '50': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1003', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '55': {'PeerConfigUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerDllPath': '%SystemRoot%\\System32\\EapTeapAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\EapTeapAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'Properties': 1065154751}}}`


##### Service Parameters
  
PeerInstalled : `0x01`  
ServiceDll : `%SystemRoot%\System32\eapsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
EapProvPlugin : `{'(Default)': '%SystemRoot%\\System32\\eapprovp.dll', 'DllEntryPoint': 'EapProvPlugGetInfo'}`  
<br></br>
#### EventLog
  
SvcMemHardLimitInMB : `0x14`  
SvcMemMidLimitInMB : `0x0f`  
SvcMemSoftLimitInMB : `0x0b`  
Application : `{'LoadPerf': {'ProviderGuid': '{122EE297-BB47-41AE-B265-1CA8D1886D40}'}, 'Microsoft-Windows-PerfCtrs': {'ProviderGuid': '{973143dd-f3c7-4ef5-b156-544ac38c39b6}', 'EventMessageFile': '%SystemRoot%\\system32\\perfctrs.dll'}, 'PDH': {'ProviderGuid': '{04D66358-C4A1-419B-8023-23B73902DE2C}'}, 'PerfCtrs': {'ProviderGuid': '{973143DD-F3C7-4EF5-B156-544AC38C39B6}'}, 'PerfDisk': {'ProviderGuid': '{7F9D83DE-8ABB-457F-98E8-4AD161449ECC}'}, 'Perflib': {'ProviderGuid': '{13B197BD-7CEE-4B4E-8DD0-59314CE374CE}'}, 'PerfNet': {'ProviderGuid': '{CAB2B8A5-49B9-4EEC-B1B0-FAC21DA05A3B}'}, 'PerfOs': {'ProviderGuid': '{F82FB576-E941-4956-A2C7-A0CF83F6450A}'}, 'PerfProc': {'ProviderGuid': '{72D211E1-4C54-4A93-9520-4901681B2271}'}}`  
System : `{'eventlog': {'EventMessageFile': '%SystemRoot%\\System32\\netevent.dll', 'TypesSupported': 7}, 'LSI_SSS': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'megasas': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'Microsoft-Antimalware-ShieldProvider': {'ProviderGuid': '{928f7d29-0577-5be5-3bd3-b6bdab9ab307}', 'EventMessageFile': '%SystemRoot%\\System32\\SecurityHealthService.exe'}}`
#### FrameServer



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 21 bc a3 2e 0f 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`773732e5-76f9-5b4f-9b55-b94699c46e44`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`d752e524-2365-f747-a647-d3465bf1f5ca`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
  
<br></br>
#### HomeGroupListener
  
SvcMemHardLimitInMB : `0xbd`  
SvcMemMidLimitInMB : `0x7e`  
SvcMemSoftLimitInMB : `0x40`  
ApprovedListeners : `{'{125B0F61-0EC3-4f07-9A49-AFB340D9E57F}': {'(Default)': 'File History Hosted Listener', 'SupportedRecordTypes': {'GUID_DPListenerRecordType': '{ADBCFEA5-D8FC-4a46-B12B-EB1FFE39BF17}'}}, '{517F6AA6-D6FA-46D0-8094-17FF17E4CCF4}': {'(Default)': 'Security Hosted Listener', 'SupportedRecordTypes': {'GUID_SecurityListener_SigningKeys': '{CA328F46-E759-4399-82AB-FA92651D1ED2}'}}, '{5255EFED-103A-4444-B124-F88F99E4EF8D}': {'(Default)': 'Printer Hosted Listener'}, '{8ADD018C-5C5F-43C5-BE1E-07BAE85593B7}': {'(Default)': 'Alpha Hosted Listener', 'SupportedRecordTypes': {'GUID_AlphaListener_AlphaAccount': '{929CB323-C5EA-48E7-A6D0-193DD432E769}'}}, '{DE9C1288-0F09-40ff-BA84-7F19279FA74B}': {'(Default)': 'Identity Hosted Listener', 'SupportedRecordTypes': {'GUID_IdentityListenerRecordType': '{07004F5D-93A5-4b6c-B851-E2C9BBFD923D}', 'GUID_IdentityMachineCertRecordType': '{07004F5E-93A5-4b6c-B851-E2C9BBFD923E}'}}, '{EB6B4457-F013-4E5A-9B05-1D44E4D6FAEB}': {'(Default)': 'Sharing Hosted Listener', 'SupportedRecordTypes': {'GUID_SharingListener_MACAddresses': '{A7BC622E-8238-4E38-9C88-34153B7D9AB1}'}}}`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\ListSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ListenerServiceMain`  
<br></br>
#### HomeGroupProvider



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\provsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ProviderServiceMain`  
<br></br>  
ServiceData : `{'LocalJoiningUser': '', 'Password': b'\x00'}`
#### hvservice
  
Description : `@%SystemRoot%\system32\drivers\hvservice.sys,-17`  
Group : `Extended Base`
#### Lsa
  
Performance : `{'Close': 'CloseLsaPerformanceData', 'Collect': 'CollectLsaPerformanceData', 'Library': 'X:\\Windows\\System32\\Secur32.dll', 'Object List': '1570 1670', 'Open': 'OpenLsaPerformanceData'}`
#### LSI_SSS
  
ImagePath : `System32\drivers\lsi_sss.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x0c`  
Owners : `6c 00 73 00 69 00 5f 00 73 00 73 00 73 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x0a`  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### megasas
  
ImagePath : `System32\drivers\megasas.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x0d`  
Owners : `6d 00 65 00 67 00 61 00 73 00 61 00 73 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x08`  
IoTimeoutValue : `0x3c`  
Device : `{'DriverParameter': 'nobusywait=1', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### mshidkmdf
  
Description : `@%SystemRoot%\system32\drivers\mshidkmdf.sys,-101`  
Group : `Base`
#### MSSCNTRS
  
Performance : `{'Close': 'Close', 'Collect': 'Collect', 'Library': '%systemroot%\\system32\\msscntrs.dll', 'Open': 'Open'}`
#### NlaSvc
  
DependOnService : `NSIRpcSsTcpIpDhcpEventlog`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 64 00 00 00 01 00 00 00 64 00 00 00 00 00 00 00 00 00 00 00`


##### Service Parameters
  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  
Security : `01 00 04 80 98 00 00 00 a4 00 00 00 00 00 00 00 14 00 00 00 02 00 84 00 05 00 00 00 00 02 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 02 14 00 ff 01 0f 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 14 00 9d 00 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 28 00 1d 00 02 00 01 06 00 00 00 00 00 05 50 00 00 00 44 3e 41 bb 45 ba a8 7a 6c bd 92 68 f4 ad 64 8f d5 e6 70 e9 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### RFCOMM



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
#### SensorService



##### Service Parameters
  
Sensors : `{'{0D49D945-FA83-4630-A22C-01387F906DE6}': {'PersistentUniqueId': '{934F17E7-42EF-470B-BE7C-1AD0983C9E6C}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}}`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|1||||`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 38 00 34 00 38 00 39 00 42 00 45 00 31 00 43 00 2d 00 38 00 30 00 41 00 34 00 2d 00 34 00 38 00 42 00 43 00 2d 00 39 00 30 00 31 00 41 00 2d 00 41 00 41 00 39 00 31 00 42 00 44 00 38 00 32 00 37 00 41 00 37 00 43 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2||||`44 00 42 00 32 00 43 00 45 00 36 00 33 00 34 00 2d 00 31 00 39 00 31 00 44 00 2d 00 34 00 32 00 41 00 46 00 2d 00 41 00 32 00 38 00 43 00 2d 00 31 00 36 00 42 00 45 00 39 00 37 00 39 00 32 00 34 00 43 00 41 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3||||`39 00 37 00 42 00 45 00 39 00 35 00 30 00 37 00 2d 00 31 00 37 00 44 00 41 00 2d 00 34 00 39 00 39 00 39 00 2d 00 38 00 37 00 44 00 37 00 2d 00 36 00 36 00 43 00 30 00 42 00 32 00 44 00 38 00 33 00 43 00 43 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### SharedAccess
  
Defaults : `{'FirewallPolicy': {'FirewallRules': {'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=6|Profile=Private|LPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-200|Desc=@%systemroot%\\system32\\provsvc.dll,-201|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=6|Profile=Private|RPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-203|Desc=@%systemroot%\\system32\\provsvc.dll,-204|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=17|Profile=Private|LPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-205|Desc=@%systemroot%\\system32\\provsvc.dll,-206|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=17|Profile=Private|RPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-207|Desc=@%systemroot%\\system32\\provsvc.dll,-208|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|'}}}`


##### Service Parameters
  
FirewallPolicy : `{'FirewallRules': {'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=6|Profile=Private|LPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-200|Desc=@%systemroot%\\system32\\provsvc.dll,-201|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=6|Profile=Private|RPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-203|Desc=@%systemroot%\\system32\\provsvc.dll,-204|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=17|Profile=Private|LPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-205|Desc=@%systemroot%\\system32\\provsvc.dll,-206|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=17|Profile=Private|RPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-207|Desc=@%systemroot%\\system32\\provsvc.dll,-208|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|'}, 'RestrictedServices': {'Static': {'System': {'HomeGroup Allow In': 'v2.0|Action=Allow|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|LPort=3587|Protocol=6|Name=Allow Grouping to receive from port 3587|', 'HomeGroup Allow In (PRNP)': 'v2.0|Action=Allow|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|LPort=3540|Protocol=17|Name=Allow PNRP to receive from port 3540|', 'HomeGroup Allow Out': 'v2.0|Action=Allow|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|RPort=3587|Protocol=6|Name=Allow Grouping to send to port 3587|', 'HomeGroup Allow Out (PRNP)': 'v2.0|Action=Allow|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|RPort=3540|Protocol=17|Name=Allow PNRP to send from port 3540|', 'HomeGroup Block In': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|Name=Block homegroup incoming|', 'HomeGroup Block Out': 'V2.0|Action=Block|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|Name=Block homegroup outgoing|', 'HomeGroup Listener Block In': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupListener|Name=Block all incoming|', 'HomeGroup Listener Block Out': 'V2.0|Action=Block|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupListener|Name=Block all outgoing|', 'SettingSyncHost': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\settingsynchost.exe|Name=Block IP traffic to SettingSyncHost|'}}}}`  
<br></br>
#### SNMPTRAP
  
Description : `@firewallapi.dll,-50324`  
DisplayName : `@firewallapi.dll,-50323`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `ff ff ff ff 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 60 ea 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\snmptrap.exe`  
ObjectName : `NT AUTHORITY\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`
#### stisvc
  
DependOnService : `RpcSs`  
Description : `@%SystemRoot%\system32\wiaservc.dll,-10`  
DisplayName : `@%SystemRoot%\system32\wiaservc.dll,-9`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k imgsvc`  
ObjectName : `NT Authority\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wiaservc.dll`  
<br></br>  
Security : `01 00 14 80 a0 00 00 00 ac 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 01 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 70 00 05 00 00 00 00 00 14 00 fd 01 02 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 14 00 00 01 00 00 01 01 00 00 00 00 00 05 0b 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### Synth3dVsc
  
ImagePath : `\SystemRoot\System32\drivers\Synth3dVsc.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Video Init`  
Tag : `0x01`  
Owners : `77 00 73 00 79 00 6e 00 74 00 68 00 33 00 64 00 76 00 73 00 63 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### TapiSrv
  
Performance : `{'ObjectList': '1150'}`
#### Telemetry
  
ImagePath : `System32\drivers\IntelTA.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Core Security Extensions`  
Tag : `0x02`  
DisplayName : `@intelta.inf,%Telemetry.SVCDESC%;Intel(R) Telemetry Service`  
Owners : `69 00 6e 00 74 00 65 00 6c 00 74 00 61 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### wcnfs
  
DependOnService : `FltMgr`  
Description : `@%systemroot%\system32\drivers\wcnfs.sys,-101`  
DisplayName : `@%systemroot%\system32\drivers\wcnfs.sys,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `FSFilter Top`  
ImagePath : `\SystemRoot\system32\drivers\wcnfs.sys`  
Start : `SERVICE_DEMAND_START`  
SupportedFeatures : `0x07`  
Type : `SERVICE_FILE_SYSTEM_DRIVER`  
Instances : `{'DefaultInstance': 'wcnfs Instance', 'wcnfs Instance': {'Altitude': '409900', 'Flags': 0}}`


##### Service Parameters
  
DebugOptions : `0x00`  
<br></br>  
<br></br>  

</details>

# Professional

## SYSTEM
  

<details>
  
<summary> Added </summary>
### WMI AutoLoggers

#### BioEnrollment
  
Start : `0x00`  
{4b8b1947-ae4d-54e2-826a-1aee78ef05b2} : `{'Enabled': 0}`  
{a55d5a23-1a5b-580a-2be5-d7188f43fae1} : `{'Enabled': 0}`
|guid|
| :---: |
|Start|
|{4b8b1947-ae4d-54e2-826a-1aee78ef05b2}|
|{a55d5a23-1a5b-580a-2be5-d7188f43fae1}|
  
<br></br>
#### EventLog-Application
  
{04d66358-c4a1-419b-8023-23b73902de2c} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{15f4cd44-ca53-5422-db17-4e76821b5a69} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{6e0df32c-7f11-54f7-e8ee-5ad4032727ce} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 2305843009213693952, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{7628e972-6d6f-4974-b58f-6428622ec09a} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{7d44233d-3055-4b9c-ba64-0d47ca40a232} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 2305843009213693952, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9068a924-f97e-5506-c3a3-5c020c00e8e0} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{a70ff94f-570b-4979-ba5c-e59c9feab61b} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{ad8aa069-a01b-40a0-ba40-948d1d8dedc5} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{04d66358-c4a1-419b-8023-23b73902de2c}|
|{15f4cd44-ca53-5422-db17-4e76821b5a69}|
|{6e0df32c-7f11-54f7-e8ee-5ad4032727ce}|
|{7628e972-6d6f-4974-b58f-6428622ec09a}|
|{7d44233d-3055-4b9c-ba64-0d47ca40a232}|
|{9068a924-f97e-5506-c3a3-5c020c00e8e0}|
|{a70ff94f-570b-4979-ba5c-e59c9feab61b}|
|{ad8aa069-a01b-40a0-ba40-948d1d8dedc5}|
  
<br></br>
#### EventLog-System
  
{0075e1ab-e1d1-5d1f-35f5-da36fb4f41b1} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{17d2a329-4539-5f4d-3435-f510634ce3b9} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{5bcf2a5c-2e90-5a03-aa4e-2e459bae21b4} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{6600e712-c3b6-44a2-8a48-935c511f28c8} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 2305843009213693952, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{7f54ca8a-6c72-5cbc-b96f-d0ef905b8bce} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{87a623f0-8db5-5c11-7c80-a2ebbcbe5189} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{93db76c2-63ab-5de1-88b3-c068686675b8} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9799276c-fb04-47e8-845e-36946045c218} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 2305843009213693952, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{a2d34bf1-70ab-5b21-c819-5a0dd42748fd} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{b931ed29-66f4-576e-0579-0b8818a5dc6b} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{bcf0c6a7-6130-5208-f27d-fa77a91f12df} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{d07e8c3f-78fb-4c22-b77c-2203d00bfdf3} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{f6cf91be-e7d7-57d6-2a3d-278ca406d190} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{0075e1ab-e1d1-5d1f-35f5-da36fb4f41b1}|
|{17d2a329-4539-5f4d-3435-f510634ce3b9}|
|{5bcf2a5c-2e90-5a03-aa4e-2e459bae21b4}|
|{6600e712-c3b6-44a2-8a48-935c511f28c8}|
|{7f54ca8a-6c72-5cbc-b96f-d0ef905b8bce}|
|{87a623f0-8db5-5c11-7c80-a2ebbcbe5189}|
|{93db76c2-63ab-5de1-88b3-c068686675b8}|
|{9799276c-fb04-47e8-845e-36946045c218}|
|{a2d34bf1-70ab-5b21-c819-5a0dd42748fd}|
|{b931ed29-66f4-576e-0579-0b8818a5dc6b}|
|{bcf0c6a7-6130-5208-f27d-fa77a91f12df}|
|{d07e8c3f-78fb-4c22-b77c-2203d00bfdf3}|
|{f6cf91be-e7d7-57d6-2a3d-278ca406d190}|
  
<br></br>
#### FaceCredProv
  
Start : `0x00`  
{1D480C11-3870-4B19-9144-47A53CD973BD} : `{'Enabled': 0}`
|guid|
| :---: |
|Start|
|{1D480C11-3870-4B19-9144-47A53CD973BD}|
  
<br></br>
#### FaceTel
  
Start : `0x00`  
{22eb0808-0b6c-5cd4-5511-6a77e6e73a93} : `{'Enabled': 0}`
|guid|
| :---: |
|Start|
|{22eb0808-0b6c-5cd4-5511-6a77e6e73a93}|
  
<br></br>
#### NetCore
  
{923C0FFD-7933-4B52-8A49-121ABF2DC357} : `{'@': 'triage_routepolicymanagement_tracelogging', 'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{923C0FFD-7933-4B52-8A49-121ABF2DC357}|
  
<br></br>
#### NtfsLog
  
{aa381297-bccb-4569-8e39-bbbb3b400893} : `{'_Description': 'TmLog Trace Provider', 'Enabled': 1, 'EnableFlags': 15, 'EnableLevel': 5}`
|guid|
| :---: |
|{aa381297-bccb-4569-8e39-bbbb3b400893}|
  
<br></br>
#### ReFSLog
  
ClockType : `0x02`  
GUID : `{81a69395-9f48-48f2-b88c-2401db1e3a91}`  
Start : `0x01`  
{740f3c34-57df-4bad-8eea-72ac69ad5df5} : `{'_Description': 'ReFS WPP Trace', 'Enabled': 1, 'EnableFlags': 7, 'EnableLevel': 3}`
|guid|
| :---: |
|ClockType|
|GUID|
|Start|
|{740f3c34-57df-4bad-8eea-72ac69ad5df5}|
  
<br></br>
#### SetupPlatformTel
  
{D2F37B94-92A5-44E2-AFC9-2F4489D39268} : `{'Enabled': 1, 'EnableLevel': 255}`
|guid|
| :---: |
|{D2F37B94-92A5-44E2-AFC9-2F4489D39268}|
  
<br></br>
#### SpoolerLogger
  
{ba4936a1-31db-4edc-89ce-9190e3c0653b} : `{'Enabled': 1, 'EnableFlags': 0, 'EnableLevel': 5}`
|guid|
| :---: |
|{ba4936a1-31db-4edc-89ce-9190e3c0653b}|
  
<br></br>
#### WiFiSession
  
{745976be-5e09-5c76-eabd-76c93c9212d2} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`  
{ae164ede-2246-5b24-c145-29c484f7362a} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`  
{EA893635-5AB7-562B-75A2-A22107D8058F} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{745976be-5e09-5c76-eabd-76c93c9212d2}|
|{ae164ede-2246-5b24-c145-29c484f7362a}|
|{EA893635-5AB7-562B-75A2-A22107D8058F}|
  
<br></br>  
<br></br>
### Services

#### ACPI



##### Service Parameters
  
PnpAsyncNewDevices : `0x01`  
<br></br>
#### Appinfo



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 66 00 37 00 33 00 38 00 65 00 32 00 30 00 2d 00 37 00 33 00 63 00 30 00 2d 00 34 00 63 00 61 00 38 00 2d 00 61 00 61 00 36 00 61 00 2d 00 38 00 64 00 66 00 65 00 66 00 35 00 34 00 35 00 66 00 65 00 61 00 38 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### AppleSSD
  
ImagePath : `System32\drivers\AppleSSD.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x01`  
DisplayName : `@AppleSSD.inf,%DevDesc1%;Apple Solid State Drive Device`  
Owners : `41 00 70 00 70 00 6c 00 65 00 53 00 53 00 44 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x01`  
Device : `{'MaxTranLenInPages': 64}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### BFE



##### Service Parameters
  
Policy  
Persistent  
ProviderContext
|GUID|Data|
| :---: | :---: |
|{30433c31-b05f-421f-8fde-018ea4c68af4}|`01 10 08 00 cc cc cc cc 10 01 00 00 00 00 00 00 00 00 02 00 01 00 00 00 f0 00 00 00 04 00 02 00 00 00 00 00 00 00 00 00 f0 00 00 00 01 10 08 00 cc cc cc cc e0 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 31 3c 43 30 5f b0 1f 42 8f de 01 8e a4 c6 8a f4 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 00 00 00 00 00 00 00 00 08 00 00 00 08 00 00 00 10 00 02 00 00 00 00 00 05 00 00 00 00 00 00 80 07 00 00 00 00 00 00 00 07 00 00 00 4d 00 50 00 53 00 53 00 56 00 43 00 00 00 00 00 15 00 00 00 00 00 00 00 15 00 00 00 53 00 74 00 6f 00 72 00 65 00 73 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 20 00 6f 00 72 00 69 00 67 00 69 00 6e 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 26 00 00 00 14 00 02 00 26 00 00 00 51 00 75 00 61 00 72 00 61 00 6e 00 74 00 69 00 6e 00 65 00 20 00 44 00 65 00 66 00 61 00 75 00 6c 00 74 00 00 00 00 00 00 00 00 00`|
|{93132c36-6e06-4e6f-a10b-218787cd49cf}|`01 10 08 00 cc cc cc cc 10 01 00 00 00 00 00 00 00 00 02 00 01 00 00 00 f0 00 00 00 04 00 02 00 00 00 00 00 00 00 00 00 f0 00 00 00 01 10 08 00 cc cc cc cc e0 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 36 2c 13 93 06 6e 6f 4e a1 0b 21 87 87 cd 49 cf 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 00 00 00 00 00 00 00 00 08 00 00 00 08 00 00 00 10 00 02 00 00 00 00 00 06 00 00 00 00 00 00 80 07 00 00 00 00 00 00 00 07 00 00 00 4d 00 50 00 53 00 53 00 56 00 43 00 00 00 00 00 15 00 00 00 00 00 00 00 15 00 00 00 53 00 74 00 6f 00 72 00 65 00 73 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 20 00 6f 00 72 00 69 00 67 00 69 00 6e 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 22 00 00 00 14 00 02 00 22 00 00 00 42 00 6f 00 6f 00 74 00 74 00 69 00 6d 00 65 00 20 00 44 00 65 00 66 00 61 00 75 00 6c 00 74 00 00 00 00 00 00 00 00 00 00 00 00 00`|
  
<br></br>
#### cbdhsvc
  
DelayedAutoStart : `0x01`
#### CldFlt



##### Service Parameters
  
USMsgTimeoutMillis : `0x3e8`  
<br></br>
#### dcsvc
  
DelayedAutoStart : `0x01`  
DependOnService : `rpcss`  
Description : `@%systemroot%\system32\dcsvc.dll,-101`  
DisplayName : `@%systemroot%\system32\dcsvc,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 04 00 00 00 14 00 00 00 01 00 00 00 10 27 00 00 01 00 00 00 10 27 00 00 01 00 00 00 10 27 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%systemroot%\system32\svchost.exe -k netsvcs -p`  
ObjectName : `LocalSystem`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`


##### Service Parameters
  
IdleTimeout(sec) : `0x78`  
ServiceDll : `%SystemRoot%\system32\dcsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`35 00 39 00 62 00 65 00 62 00 39 00 37 00 37 00 2d 00 64 00 30 00 33 00 37 00 2d 00 34 00 38 00 66 00 34 00 2d 00 61 00 66 00 37 00 34 00 2d 00 63 00 61 00 30 00 37 00 35 00 34 00 39 00 33 00 61 00 35 00 32 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 61 00 30 00 64 00 62 00 36 00 31 00 34 00 2d 00 65 00 39 00 66 00 62 00 2d 00 34 00 38 00 63 00 66 00 2d 00 39 00 31 00 34 00 33 00 2d 00 37 00 61 00 65 00 37 00 31 00 38 00 66 00 66 00 32 00 63 00 38 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### DeviceInstall



##### Service Parameters
  
DeviceInstallMode : `0x01`  
<br></br>
#### disk



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### Dnscache



##### Service Parameters
  
DohWellKnownServers : `{'1.0.0.1': {'Template': 'https://cloudflare-dns.com/dns-query'}, '1.1.1.1': {'Template': 'https://cloudflare-dns.com/dns-query'}, '149.112.112.112': {'Template': 'https://dns.quad9.net/dns-query'}, '2001:4860:4860::8844': {'Template': 'https://dns.google/dns-query'}, '2001:4860:4860::8888': {'Template': 'https://dns.google/dns-query'}, '2606:4700:4700::1001': {'Template': 'https://cloudflare-dns.com/dns-query'}, '2606:4700:4700::1111': {'Template': 'https://cloudflare-dns.com/dns-query'}, '2620:fe::fe': {'Template': 'https://dns.quad9.net/dns-query'}, '2620:fe::fe:9': {'Template': 'https://dns.quad9.net/dns-query'}, '8.8.4.4': {'Template': 'https://dns.google/dns-query'}, '8.8.8.8': {'Template': 'https://dns.google/dns-query'}, '9.9.9.9': {'Template': 'https://dns.quad9.net/dns-query'}}`  
<br></br>
#### EapHost
  
DependOnService : `RPCSSKeyIso`  
Description : `@%systemroot%\system32\eapsvc.dll,-2`  
DisplayName : `@%systemroot%\system32\eapsvc.dll,-1`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 c0 d4 01 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\svchost.exe -k netsvcs -p`  
ObjectName : `localSystem`  
RequiredPrivileges : `['SeTcbPrivilege', 'SeDebugPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_SHARE_PROCESS`  
Methods : `{'311': {'Name': 'Microsoft', '18': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '21': {'PeerConfigUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\TtlsAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\TtlsCfg.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 389863599, 'LANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}, 'WLANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}, '23': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1002', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '254': {'14122': {'1': {'PeerDllPath': '%SystemRoot%\\System32\\WcnEapPeerProxy.dll', 'PeerFriendlyName': 'Windows Connect Now EAP Peer', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 8683520}}}, '50': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1003', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '55': {'PeerConfigUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerDllPath': '%SystemRoot%\\System32\\EapTeapAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\EapTeapAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'Properties': 1065154751, 'LANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}, 'WLANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="utf-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><TrustedRootCAHash></TrustedRootCAHash></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection> </CertificateStore> </CredentialsSource><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="utf-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><TrustedRootCAHash></TrustedRootCAHash></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}}}`


##### Service Parameters
  
PeerInstalled : `0x01`  
ServiceDll : `%SystemRoot%\System32\eapsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
EapProvPlugin : `{'(Default)': '%SystemRoot%\\System32\\eapprovp.dll', 'DllEntryPoint': 'EapProvPlugGetInfo'}`  
<br></br>
#### ebdrv0
  
ImagePath : `System32\drivers\evbd0a.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `System Bus Extender`  
Tag : `0x03`  
DisplayName : `@netevbd0a.inf,%vbd_srv_desc%;QLogic Legacy Ethernet Adapter VBD`  
Owners : `6e 00 65 00 74 00 65 00 76 00 62 00 64 00 30 00 61 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### EhStorClass



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### EventLog
  
Application : `{'Microsoft-Windows-PDH': {'ProviderGuid': '{04d66358-c4a1-419b-8023-23b73902de2c}', 'EventMessageFile': '%SystemRoot%\\system32\\pdh.dll'}, 'Universal Print': {'EventMessageFile': '%SystemRoot%\\System32\\McpManagementService.dll', 'TypesSupported': 7}}`  
System : `{'AppleSSD': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'ebdrv0': {'eventmessagefile': '%SystemRoot%\\System32\\drivers\\evbd0a.sys;%SystemRoot%\\System32\\iologmsg.dll', 'typessupported': 7}, 'EventLog': {'EventMessageFile': '%SystemRoot%\\System32\\netevent.dll', 'TypesSupported': 7}, 'hvservice': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'Microsoft-Windows-Iphlpsvc-Trace': {'ProviderGuid': '{6600e712-c3b6-44a2-8a48-935c511f28c8}', 'EventMessageFile': '%windir%\\system32\\iphlpsvc.dll'}, 'Microsoft-Windows-Network-ExecutionContext': {'ProviderGuid': '{0075e1ab-e1d1-5d1f-35f5-da36fb4f41b1}', 'EventMessageFile': '%SystemRoot%\\system32\\drivers\\ExecutionContext.sys'}, 'Microsoft-Windows-USB-USB4DeviceRouter-EventLogs': {'ProviderGuid': '{d07e8c3f-78fb-4c22-b77c-2203d00bfdf3}', 'EventMessageFile': '%SystemRoot%\\System32\\DriverStore\\FileRepository\\usb4devicerouter.inf_amd64_3bffb5f5105936e5\\Usb4DeviceRouter.sys'}, 'mpi3drvi': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'nvmedisk': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll;%SystemRoot%\\System32\\drivers\\nvmedisk.sys', 'TypesSupported': 7}}`
#### ExecutionContext
  
DisplayName : `@%SystemRoot%\System32\Drivers\ExecutionContext.sys,-101`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `System`  
ImagePath : `System32\Drivers\ExecutionContext.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### FrameServerMonitor
  
DependOnService : `rpcss`  
Description : `@%systemroot%\system32\FrameServerMonitor.dll,-101`  
DisplayName : `@%systemroot%\system32\FrameServerMonitor.dll,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 20 bf 02 00`  
ImagePath : `%SystemRoot%\System32\svchost.exe -k CameraMonitor`  
ObjectName : `LocalSystem`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`  
parameters : `{'ServiceDll': '%SystemRoot%\\system32\\FrameServerMonitor.dll', 'ServiceDllUnloadOnStop': 1}`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`42 00 45 00 30 00 44 00 39 00 35 00 42 00 41 00 2d 00 32 00 31 00 41 00 35 00 2d 00 34 00 41 00 35 00 46 00 2d 00 41 00 31 00 46 00 30 00 2d 00 39 00 41 00 44 00 41 00 38 00 34 00 41 00 43 00 31 00 31 00 34 00 34 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 26 1d 90 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 21 bc a3 2e 0f 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`773732e5-76f9-5b4f-9b55-b94699c46e44`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`d752e524-2365-f747-a647-d3465bf1f5ca`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 b8 bc a3 3d 01 c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### fvevol



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### hidspi
  
DependOnService : `HidSpiCx`
#### HidSpiCx
  
DisplayName : `HidSpi KMDF Class Extension`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `system32\drivers\HidSpiCx.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### Hsp
  
ImagePath : `\SystemRoot\System32\drivers\Hsp.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@hsp.inf,%Hsp.SVCDESC%;Microsoft Pluton Service`  
Owners : `68 00 73 00 70 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
Wdf : `{'KmdfLibraryVersion': '1.15'}`  
<br></br>
#### hvservice
  
Owners : `68 00 76 00 73 00 65 00 72 00 76 00 69 00 63 00 65 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### IntelPMT
  
ImagePath : `System32\drivers\IntelPMT.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Core Security Extensions`  
Tag : `0x02`  
DisplayName : `@intelpmt.inf,%IntelPMT.SVCDESC%;Intel(R) Platform Monitoring Technology Service`  
Owners : `69 00 6e 00 74 00 65 00 6c 00 70 00 6d 00 74 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### iorate



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### lfsvc
  
Settings : `{'LocationWebServiceProxy': {'USE_CLIENT_PROXY_INFERENCE_ONLY': 0}}`
#### McpManagementService
  
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


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\McpManagementService.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>
#### mpi3drvi
  
ImagePath : `System32\drivers\mpi3drvi.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x10`  
Owners : `6d 00 70 00 69 00 33 00 64 00 72 00 76 00 69 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x08`  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### NDIS



##### Service Parameters
  
Reserved : `{'ExecutionContextProfiles': {'Balanced': {'DpcWatchdogTimerThreshold': 80, 'Flags': 0, 'MaxPacketsReceiveAtDispatch': 64, 'MaxPacketsReceiveAtPassive': 64, 'MaxPacketsReceiveCompleteAtDispatch': 64, 'MaxPacketsReceiveCompleteAtPassive': 64, 'MaxPacketsSendAtDispatch': 64, 'MaxPacketsSendAtPassive': 64, 'MaxPacketsSendCompleteAtDispatch': 64, 'MaxPacketsSendCompleteAtPassive': 64, 'MaxTimeAtDispatch': 0, 'WorkerThreadPriority': 10}}}`  
<br></br>
#### NDKPerf
  
DisplayName : `NDKPerf Driver`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `system32\drivers\NDKPerf.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### NPSMSvc
  
Description : `@%SystemRoot%\system32\npsm.dll,-101`  
DisplayName : `@%SystemRoot%\system32\npsm.dll,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 b8 0b 00 00 01 00 00 00 b8 0b 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k LocalService -p`  
ObjectName : `NT AUTHORITY\LocalService`  
RequiredPrivileges : `['SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `96`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\npsm.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  
Security : `01 00 14 80 a0 00 00 00 ac 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 01 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 70 00 05 00 00 00 00 00 14 00 fd 01 02 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 14 00 00 01 00 00 01 01 00 00 00 00 00 05 0b 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### nvmedisk
  
ImagePath : `System32\drivers\nvmedisk.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@nvmedisk.inf,%nvmedisk.SvcDesc%;Microsoft NVMe disk driver`  
Owners : `6e 00 76 00 6d 00 65 00 64 00 69 00 73 00 6b 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### P9NP
  
Description : `@%systemroot%\system32\p9np.dll,-101`  
DisplayName : `@%systemroot%\system32\p9np.dll,-100`  
NetworkProvider : `{'DeviceName': '\\Device\\P9Rdr', 'DisplayName': '@%systemroot%\\system32\\p9np.dll,-100', 'Name': 'Plan 9 Network Provider', 'ProviderPath': '%SystemRoot%\\System32\\p9np.dll', 'TriggerStartCompleteNotification': b'u\x10\xbc\xa3T\x1e\xc6A', 'TriggerStartNotification': b'u\x08\xbc\xa3T\x1e\xc6A', 'TriggerStartPrefix': b'w\x00s\x00l\x00.\x00l\x00o\x00c\x00a\x00l\x00h\x00o\x00s\x00t\x00\x00\x00w\x00s\x00l\x00$\x00\x00\x00\x00\x00'}`
#### P9Rdr
  
DependOnService : `RDBSS`  
Description : `@%SystemRoot%\System32\drivers\p9rdr.sys,-101`  
DisplayName : `@%SystemRoot%\System32\drivers\p9rdr.sys,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `System32\drivers\p9rdr.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### P9RdrService
  
DependOnService : `P9RdrRPCSS`  
Description : `@%systemroot%\system32\p9rdrservice.dll,-101`  
DisplayName : `@%systemroot%\system32\p9rdrservice.dll,-102`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 b8 0b 00 00 01 00 00 00 b8 0b 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%systemroot%\system32\svchost.exe -k P9RdrService -p`  
ObjectName : `LocalSystem`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `96`  
UserServiceFlags : `0x03`  
parameters : `{'ServiceDll': '%SystemRoot%\\system32\\p9rdrservice.dll', 'ServiceDllUnloadOnStop': 1}`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 54 1e c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### partmgr



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### PcaSvc



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 d0 be a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 18 bc a3 2e 07 c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 2e 03 96 15`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### pci



##### Service Parameters
  
PnpAsyncNewDevices : `0x01`  
<br></br>
#### PenService
  
Description : `@%SystemRoot%\system32\PenService.dll,-101`  
DisplayName : `@%SystemRoot%\system32\PenService.dll,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 02 00 00 00 14 00 00 00 01 00 00 00 10 27 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k PenService`  
Start : `SERVICE_DEMAND_START`  
Type : `96`  
UserServiceFlags : `0x02`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\PenService.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|Data1|Data2|Data3|DataType0|DataType1|DataType2|DataType3|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`b2551e4d-6ff1-cf11-88cb-001111000030`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 31 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 32 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 33 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 46 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### PerfDisk
  
Performance : `{'Collect Supports Metadata': 1}`
#### PerfNet
  
Performance : `{'Collect Supports Metadata': 1}`
#### PerfOS
  
Performance : `{'Collect Supports Metadata': 1}`
#### PerfProc
  
Performance : `{'Collect Supports Metadata': 1}`
#### PrintWorkflowUserSvc



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 3d 0a 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### PRM
  
ImagePath : `System32\DriverStore\FileRepository\prm.inf_amd64_7fc9bb8ba2b73803\PRM.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@prm.inf,%PRM.SvcDesc%;Microsoft PRM Driver`  
Owners : `70 00 72 00 6d 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### RasMan
  
PPP : `{'EAP': {'13': {'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '25': {'LANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">25</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>25</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV1"><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><FastReconnect>true</FastReconnect><InnerEapOptional>false</InnerEapOptional><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap><EnableQuarantineChecks>false</EnableQuarantineChecks><RequireCryptoBinding>false</RequireCryptoBinding><PeapExtensions><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</AcceptServerName><IdentityPrivacy xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2"><EnableIdentityPrivacy>true</EnableIdentityPrivacy><AnonymousUserName>anonymous</AnonymousUserName></IdentityPrivacy></PeapExtensions></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">25</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>25</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV1"><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><FastReconnect>true</FastReconnect><InnerEapOptional>false</InnerEapOptional><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap><EnableQuarantineChecks>false</EnableQuarantineChecks><RequireCryptoBinding>false</RequireCryptoBinding><PeapExtensions><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</AcceptServerName><IdentityPrivacy xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2"><EnableIdentityPrivacy>true</EnableIdentityPrivacy><AnonymousUserName>anonymous</AnonymousUserName></IdentityPrivacy></PeapExtensions></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}}}}`
#### rdyboost



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### RemoteAccess
  
Performance : `{'Object List': '7584 7620'}`
#### RetailDemo
  
StateFlags : `0x01`
#### SecurityHealthService
  
Security : `01 00 14 80 a4 00 00 00 b0 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 00 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 74 00 05 00 00 00 00 00 14 00 9d 00 02 00 01 01 00 00 00 00 00 05 0b 00 00 00 00 00 18 00 9d 00 02 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 9d 00 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 18 00 9d 00 02 00 01 02 00 00 00 00 00 0f 02 00 00 00 01 00 00 00 00 00 14 00 ff 01 0f 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### SensorService



##### Service Parameters
  
Sensors : `{'{934F17E7-42EF-470B-BE7C-1AD0983C9E6C}': {'RequiredHingeJointsCount': 1, 'RequiredPanelGroupsCount': 2, 'SensorType': '{0D49D945-FA83-4630-A22C-01387F906DE6}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}, '{AEDD7472-297F-4285-B2FB-9422731BCDA6}': {'RequiredHingeJointsCount': 2, 'RequiredPanelGroupsCount': 3, 'SensorType': '{0D49D945-FA83-4630-A22C-01387F906DE6}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}}`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 38 00 34 00 38 00 39 00 42 00 45 00 31 00 43 00 2d 00 38 00 30 00 41 00 34 00 2d 00 34 00 38 00 42 00 43 00 2d 00 39 00 30 00 31 00 41 00 2d 00 41 00 41 00 39 00 31 00 42 00 44 00 38 00 32 00 37 00 41 00 37 00 43 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 42 00 32 00 43 00 45 00 36 00 33 00 34 00 2d 00 31 00 39 00 31 00 44 00 2d 00 34 00 32 00 41 00 46 00 2d 00 41 00 32 00 38 00 43 00 2d 00 31 00 36 00 42 00 45 00 39 00 37 00 39 00 32 00 34 00 43 00 41 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|6|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`39 00 37 00 42 00 45 00 39 00 35 00 30 00 37 00 2d 00 31 00 37 00 44 00 41 00 2d 00 34 00 39 00 39 00 39 00 2d 00 38 00 37 00 44 00 37 00 2d 00 36 00 36 00 43 00 30 00 42 00 32 00 44 00 38 00 33 00 43 00 43 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|7|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`36 00 33 00 32 00 38 00 44 00 43 00 43 00 34 00 2d 00 31 00 36 00 35 00 38 00 2d 00 34 00 31 00 33 00 33 00 2d 00 38 00 30 00 36 00 32 00 2d 00 41 00 39 00 39 00 34 00 33 00 44 00 41 00 43 00 32 00 30 00 39 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### SNMPTrap
  
Description : `@firewallapi.dll,-50324`  
DisplayName : `@firewallapi.dll,-50323`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `ff ff ff ff 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 60 ea 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\snmptrap.exe`  
ObjectName : `NT AUTHORITY\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`
#### StiSvc
  
DependOnService : `RpcSs`  
Description : `@%SystemRoot%\system32\wiaservc.dll,-10`  
DisplayName : `@%SystemRoot%\system32\wiaservc.dll,-9`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k imgsvc`  
ObjectName : `NT Authority\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wiaservc.dll`  
<br></br>  
Security : `01 00 14 80 a0 00 00 00 ac 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 01 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 70 00 05 00 00 00 00 00 14 00 fd 01 02 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 14 00 00 01 00 00 01 01 00 00 00 00 00 05 0b 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`c61fdd6b-0f81-d011-bec7-08002be2092f`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>
#### stornvme



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### TapiSrv
  
Performance : `{'Object List': '1150'}`
#### TermService
  
Performance : `{'Collect Supports Metadata': 1}`
#### TPM



##### Service Parameters
  
KsrGuid : `{F141DC89-3D00-450A-B2D2-AD995267F8FC}`  
<br></br>
#### tzautoupdate
  
StateFlags : `0x01`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 58 bc a3 3e 06 83 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 30 bc a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|6|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 d0 be a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### UGatherer
  
Performance : `{'Object List': '7654'}`
#### UGTHRSVC
  
Performance : `{'Object List': '7760'}`
#### Usb4DeviceRouter
  
ImagePath : `\SystemRoot\System32\DriverStore\FileRepository\usb4devicerouter.inf_amd64_3bffb5f5105936e5\Usb4DeviceRouter.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Base`  
Tag : `0x15`  
DisplayName : `@Usb4DeviceRouter.inf,%Usb4DeviceRouter.SVCDESC%;USB4 Device Router Service`  
Owners : `55 00 73 00 62 00 34 00 44 00 65 00 76 00 69 00 63 00 65 00 52 00 6f 00 75 00 74 00 65 00 72 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
ForceLogsInMiniDump : `0x01`  
<br></br>
#### Usb4HostRouter
  
ImagePath : `\SystemRoot\System32\DriverStore\FileRepository\usb4hostrouter.inf_amd64_dd61aa4ab70fa4fb\Usb4HostRouter.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@Usb4HostRouter.inf,%Usb4HostRouter.SVCDESC%;USB4 Host Router Service`  
Owners : `55 00 73 00 62 00 34 00 48 00 6f 00 73 00 74 00 52 00 6f 00 75 00 74 00 65 00 72 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
DmaRemappingCompatible : `0x01`  
ForceLogsInMiniDump : `0x01`  
<br></br>
#### usbhub
  
Performance : `{'Object List': '9956'}`
#### volmgr



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### volsnap



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### volume



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### WifiCx
  
DependOnService : `NetAdapterCx`  
DisplayName : `Wifi Network Adapter Class Extension`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `system32\drivers\WifiCx.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### XblGameSave



##### Service Parameters
  
FeatureLevel : `0x01`  
<br></br>  
<br></br>  

</details>
  

<details>
  
<summary> Removed </summary>
### WMI AutoLoggers

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
{B1D067C7-2F8C-436E-9E82-C5C2C22229D5} : `{'Enabled': 0, 'EnableLevel': 4, 'MatchAnyKeyword': 18374686479671623680}`
|guid|
| :---: |
|BufferSize|
|ClockType|
|FileMax|
|FileName|
|Guid|
|LogFileMode|
|MaxFileSize|
|MaximumBuffers|
|MinimumBuffers|
|Start|
|{B1D067C7-2F8C-436E-9E82-C5C2C22229D5}|
  
<br></br>
#### EventLog-Application
  
{28e25b07-c47f-473d-8b24-2e171cca808a} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{579402a2-883c-45d8-b70a-9bc856407751} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{83d6e83b-900b-48a3-9835-57656b6f6474} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{973143dd-f3c7-4ef5-b156-544ac38c39b6} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9f973c1d-d056-4e38-84a5-7be81cdd6ab6} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{af0a5a6d-e009-46d4-8867-42f2240f8a72} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{f43c3c35-22e2-53eb-f169-07594054779e} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{28e25b07-c47f-473d-8b24-2e171cca808a}|
|{579402a2-883c-45d8-b70a-9bc856407751}|
|{5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0}|
|{83d6e83b-900b-48a3-9835-57656b6f6474}|
|{973143dd-f3c7-4ef5-b156-544ac38c39b6}|
|{9f973c1d-d056-4e38-84a5-7be81cdd6ab6}|
|{af0a5a6d-e009-46d4-8867-42f2240f8a72}|
|{c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef}|
|{f43c3c35-22e2-53eb-f169-07594054779e}|
  
<br></br>
#### EventLog-System
  
{2bef5442-d402-5a72-58e1-cb7e491bf179} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{3903d5b9-988d-4c31-9ccd-4022f96703f0} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{928f7d29-0577-5be5-3bd3-b6bdab9ab307} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9f7b5df4-b902-48bc-bc94-95068c6c7d26} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{b99317e5-89b7-4c0d-abd1-6e705f7912dc} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{c18672d1-dc18-4dfd-91e4-170cf37160cf} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{ea216962-877b-5b73-f7c5-8aef5375959e} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{ed8cc261-2123-567e-063e-75fc5f8e8a48} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{2bef5442-d402-5a72-58e1-cb7e491bf179}|
|{3903d5b9-988d-4c31-9ccd-4022f96703f0}|
|{928f7d29-0577-5be5-3bd3-b6bdab9ab307}|
|{9f7b5df4-b902-48bc-bc94-95068c6c7d26}|
|{b99317e5-89b7-4c0d-abd1-6e705f7912dc}|
|{c18672d1-dc18-4dfd-91e4-170cf37160cf}|
|{ea216962-877b-5b73-f7c5-8aef5375959e}|
|{ed8cc261-2123-567e-063e-75fc5f8e8a48}|
  
<br></br>
#### LwtNetLog
  
{7868B0D4-1423-4681-AFDF-27913575441E} : `{'Enabled': 1, 'EnableLevel': 4, 'MatchAnyKeyword': 1}`
|guid|
| :---: |
|{7868B0D4-1423-4681-AFDF-27913575441E}|
  
<br></br>
#### NtfsLog
  
{740f3c34-57df-4bad-8eea-72ac69ad5df5} : `{'_Description': 'ReFS WPP Trace', 'Enabled': 1, 'EnableFlags': 7, 'EnableLevel': 3}`
|guid|
| :---: |
|{740f3c34-57df-4bad-8eea-72ac69ad5df5}|
  
<br></br>
#### SQMLogger
  
{017BA13C-9A55-4f1f-8200-323055AAC810} : `{'Enabled': 1, 'EnableLevel': 4, 'EnableProperty': 2, 'LoggerName': 'SQMLogger', 'MatchAnyKeyword': 2251799813685248}`
|guid|
| :---: |
|{017BA13C-9A55-4f1f-8200-323055AAC810}|
  
<br></br>
#### WiFiSession
  
{60523747-6516-48B7-84B1-3264FA2CB359} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{60523747-6516-48B7-84B1-3264FA2CB359}|
  
<br></br>
#### WinPhoneCritical
  
{A9C11050-9E93-4fa4-8FE0-7C4750A345B2} : `{'Enabled': 1, 'EnableLevel': 2, 'EnableProperty': 2, 'LoggerName': 'SmsRouter', 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{A9C11050-9E93-4fa4-8FE0-7C4750A345B2}|
  
<br></br>  
<br></br>
### Services

#### BluetoothUserService



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 68 bc a3 2f 02 92 09`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### BthEnum



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
#### BthLEEnum



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
#### BTHPORT



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
#### dmwappushservice
  
RequiredPrivileges : `['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege', 'SeIncreaseWorkingSetPrivilege']`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 61 00 30 00 64 00 62 00 36 00 31 00 34 00 2d 00 65 00 39 00 66 00 62 00 2d 00 34 00 38 00 63 00 66 00 2d 00 39 00 31 00 34 00 33 00 2d 00 37 00 61 00 65 00 37 00 31 00 38 00 66 00 66 00 32 00 63 00 38 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 90 bc a3 28 00 92 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### Eaphost
  
DependOnService : `RPCSSKeyIso`  
Description : `@%systemroot%\system32\eapsvc.dll,-2`  
DisplayName : `@%systemroot%\system32\eapsvc.dll,-1`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 c0 d4 01 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\svchost.exe -k netsvcs -p`  
ObjectName : `localSystem`  
RequiredPrivileges : `['SeTcbPrivilege', 'SeDebugPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_SHARE_PROCESS`  
Methods : `{'311': {'Name': 'Microsoft', '18': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '21': {'PeerConfigUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\TtlsAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\TtlsCfg.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 389863599, 'WLANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames></ServerNames></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}, '23': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1002', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '254': {'14122': {'1': {'PeerDllPath': '%SystemRoot%\\System32\\WcnEapPeerProxy.dll', 'PeerFriendlyName': 'Windows Connect Now EAP Peer', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 8683520}}}, '50': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1003', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '55': {'PeerConfigUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerDllPath': '%SystemRoot%\\System32\\EapTeapAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\EapTeapAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'Properties': 1065154751}}}`


##### Service Parameters
  
PeerInstalled : `0x01`  
ServiceDll : `%SystemRoot%\System32\eapsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
EapProvPlugin : `{'(Default)': '%SystemRoot%\\System32\\eapprovp.dll', 'DllEntryPoint': 'EapProvPlugGetInfo'}`  
<br></br>
#### EventLog
  
SvcMemHardLimitInMB : `0x14`  
SvcMemMidLimitInMB : `0x0f`  
SvcMemSoftLimitInMB : `0x0b`  
Application : `{'LoadPerf': {'ProviderGuid': '{122EE297-BB47-41AE-B265-1CA8D1886D40}'}, 'Microsoft-Windows-PerfCtrs': {'ProviderGuid': '{973143dd-f3c7-4ef5-b156-544ac38c39b6}', 'EventMessageFile': '%SystemRoot%\\system32\\perfctrs.dll'}, 'PDH': {'ProviderGuid': '{04D66358-C4A1-419B-8023-23B73902DE2C}'}, 'PerfCtrs': {'ProviderGuid': '{973143DD-F3C7-4EF5-B156-544AC38C39B6}'}, 'PerfDisk': {'ProviderGuid': '{7F9D83DE-8ABB-457F-98E8-4AD161449ECC}'}, 'Perflib': {'ProviderGuid': '{13B197BD-7CEE-4B4E-8DD0-59314CE374CE}'}, 'PerfNet': {'ProviderGuid': '{CAB2B8A5-49B9-4EEC-B1B0-FAC21DA05A3B}'}, 'PerfOs': {'ProviderGuid': '{F82FB576-E941-4956-A2C7-A0CF83F6450A}'}, 'PerfProc': {'ProviderGuid': '{72D211E1-4C54-4A93-9520-4901681B2271}'}}`  
System : `{'eventlog': {'EventMessageFile': '%SystemRoot%\\System32\\netevent.dll', 'TypesSupported': 7}, 'LSI_SSS': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'megasas': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'Microsoft-Antimalware-ShieldProvider': {'ProviderGuid': '{928f7d29-0577-5be5-3bd3-b6bdab9ab307}', 'EventMessageFile': '%SystemRoot%\\System32\\SecurityHealthService.exe'}}`
#### FrameServer



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 21 bc a3 2e 0f 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`773732e5-76f9-5b4f-9b55-b94699c46e44`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`d752e524-2365-f747-a647-d3465bf1f5ca`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
  
<br></br>
#### HomeGroupListener
  
SvcMemHardLimitInMB : `0xbd`  
SvcMemMidLimitInMB : `0x7e`  
SvcMemSoftLimitInMB : `0x40`  
ApprovedListeners : `{'{125B0F61-0EC3-4f07-9A49-AFB340D9E57F}': {'(Default)': 'File History Hosted Listener', 'SupportedRecordTypes': {'GUID_DPListenerRecordType': '{ADBCFEA5-D8FC-4a46-B12B-EB1FFE39BF17}'}}, '{517F6AA6-D6FA-46D0-8094-17FF17E4CCF4}': {'(Default)': 'Security Hosted Listener', 'SupportedRecordTypes': {'GUID_SecurityListener_SigningKeys': '{CA328F46-E759-4399-82AB-FA92651D1ED2}'}}, '{5255EFED-103A-4444-B124-F88F99E4EF8D}': {'(Default)': 'Printer Hosted Listener'}, '{8ADD018C-5C5F-43C5-BE1E-07BAE85593B7}': {'(Default)': 'Alpha Hosted Listener', 'SupportedRecordTypes': {'GUID_AlphaListener_AlphaAccount': '{929CB323-C5EA-48E7-A6D0-193DD432E769}'}}, '{DE9C1288-0F09-40ff-BA84-7F19279FA74B}': {'(Default)': 'Identity Hosted Listener', 'SupportedRecordTypes': {'GUID_IdentityListenerRecordType': '{07004F5D-93A5-4b6c-B851-E2C9BBFD923D}', 'GUID_IdentityMachineCertRecordType': '{07004F5E-93A5-4b6c-B851-E2C9BBFD923E}'}}, '{EB6B4457-F013-4E5A-9B05-1D44E4D6FAEB}': {'(Default)': 'Sharing Hosted Listener', 'SupportedRecordTypes': {'GUID_SharingListener_MACAddresses': '{A7BC622E-8238-4E38-9C88-34153B7D9AB1}'}}}`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\ListSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ListenerServiceMain`  
<br></br>
#### HomeGroupProvider



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\provsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ProviderServiceMain`  
<br></br>  
ServiceData : `{'LocalJoiningUser': '', 'Password': b'\x00'}`
#### hvservice
  
Description : `@%SystemRoot%\system32\drivers\hvservice.sys,-17`  
Group : `Extended Base`
#### Lsa
  
Performance : `{'Close': 'CloseLsaPerformanceData', 'Collect': 'CollectLsaPerformanceData', 'Library': 'X:\\Windows\\System32\\Secur32.dll', 'Object List': '1570 1670', 'Open': 'OpenLsaPerformanceData'}`
#### LSI_SSS
  
ImagePath : `System32\drivers\lsi_sss.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x0c`  
Owners : `6c 00 73 00 69 00 5f 00 73 00 73 00 73 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x0a`  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### megasas
  
ImagePath : `System32\drivers\megasas.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x0d`  
Owners : `6d 00 65 00 67 00 61 00 73 00 61 00 73 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x08`  
IoTimeoutValue : `0x3c`  
Device : `{'DriverParameter': 'nobusywait=1', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### mshidkmdf
  
Description : `@%SystemRoot%\system32\drivers\mshidkmdf.sys,-101`  
Group : `Base`
#### MSSCNTRS
  
Performance : `{'Close': 'Close', 'Collect': 'Collect', 'Library': '%systemroot%\\system32\\msscntrs.dll', 'Open': 'Open'}`
#### NlaSvc
  
DependOnService : `NSIRpcSsTcpIpDhcpEventlog`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 64 00 00 00 01 00 00 00 64 00 00 00 00 00 00 00 00 00 00 00`


##### Service Parameters
  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  
Security : `01 00 04 80 98 00 00 00 a4 00 00 00 00 00 00 00 14 00 00 00 02 00 84 00 05 00 00 00 00 02 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 02 14 00 ff 01 0f 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 14 00 9d 00 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 28 00 1d 00 02 00 01 06 00 00 00 00 00 05 50 00 00 00 44 3e 41 bb 45 ba a8 7a 6c bd 92 68 f4 ad 64 8f d5 e6 70 e9 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### RFCOMM



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
#### SensorService



##### Service Parameters
  
Sensors : `{'{0D49D945-FA83-4630-A22C-01387F906DE6}': {'PersistentUniqueId': '{934F17E7-42EF-470B-BE7C-1AD0983C9E6C}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}}`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|1||||`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 38 00 34 00 38 00 39 00 42 00 45 00 31 00 43 00 2d 00 38 00 30 00 41 00 34 00 2d 00 34 00 38 00 42 00 43 00 2d 00 39 00 30 00 31 00 41 00 2d 00 41 00 41 00 39 00 31 00 42 00 44 00 38 00 32 00 37 00 41 00 37 00 43 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2||||`44 00 42 00 32 00 43 00 45 00 36 00 33 00 34 00 2d 00 31 00 39 00 31 00 44 00 2d 00 34 00 32 00 41 00 46 00 2d 00 41 00 32 00 38 00 43 00 2d 00 31 00 36 00 42 00 45 00 39 00 37 00 39 00 32 00 34 00 43 00 41 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3||||`39 00 37 00 42 00 45 00 39 00 35 00 30 00 37 00 2d 00 31 00 37 00 44 00 41 00 2d 00 34 00 39 00 39 00 39 00 2d 00 38 00 37 00 44 00 37 00 2d 00 36 00 36 00 43 00 30 00 42 00 32 00 44 00 38 00 33 00 43 00 43 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### SharedAccess
  
Defaults : `{'FirewallPolicy': {'FirewallRules': {'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=6|Profile=Private|LPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-200|Desc=@%systemroot%\\system32\\provsvc.dll,-201|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=6|Profile=Private|RPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-203|Desc=@%systemroot%\\system32\\provsvc.dll,-204|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=17|Profile=Private|LPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-205|Desc=@%systemroot%\\system32\\provsvc.dll,-206|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=17|Profile=Private|RPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-207|Desc=@%systemroot%\\system32\\provsvc.dll,-208|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|'}}}`


##### Service Parameters
  
FirewallPolicy : `{'FirewallRules': {'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=6|Profile=Private|LPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-200|Desc=@%systemroot%\\system32\\provsvc.dll,-201|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=6|Profile=Private|RPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-203|Desc=@%systemroot%\\system32\\provsvc.dll,-204|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=17|Profile=Private|LPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-205|Desc=@%systemroot%\\system32\\provsvc.dll,-206|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=17|Profile=Private|RPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-207|Desc=@%systemroot%\\system32\\provsvc.dll,-208|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|'}, 'RestrictedServices': {'Static': {'System': {'HomeGroup Allow In': 'v2.0|Action=Allow|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|LPort=3587|Protocol=6|Name=Allow Grouping to receive from port 3587|', 'HomeGroup Allow In (PRNP)': 'v2.0|Action=Allow|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|LPort=3540|Protocol=17|Name=Allow PNRP to receive from port 3540|', 'HomeGroup Allow Out': 'v2.0|Action=Allow|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|RPort=3587|Protocol=6|Name=Allow Grouping to send to port 3587|', 'HomeGroup Allow Out (PRNP)': 'v2.0|Action=Allow|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|RPort=3540|Protocol=17|Name=Allow PNRP to send from port 3540|', 'HomeGroup Block In': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|Name=Block homegroup incoming|', 'HomeGroup Block Out': 'V2.0|Action=Block|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|Name=Block homegroup outgoing|', 'HomeGroup Listener Block In': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupListener|Name=Block all incoming|', 'HomeGroup Listener Block Out': 'V2.0|Action=Block|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupListener|Name=Block all outgoing|', 'SettingSyncHost': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\settingsynchost.exe|Name=Block IP traffic to SettingSyncHost|'}}}}`  
<br></br>
#### SNMPTRAP
  
Description : `@firewallapi.dll,-50324`  
DisplayName : `@firewallapi.dll,-50323`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `ff ff ff ff 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 60 ea 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\snmptrap.exe`  
ObjectName : `NT AUTHORITY\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`
#### stisvc
  
DependOnService : `RpcSs`  
Description : `@%SystemRoot%\system32\wiaservc.dll,-10`  
DisplayName : `@%SystemRoot%\system32\wiaservc.dll,-9`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k imgsvc`  
ObjectName : `NT Authority\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wiaservc.dll`  
<br></br>  
Security : `01 00 14 80 a0 00 00 00 ac 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 01 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 70 00 05 00 00 00 00 00 14 00 fd 01 02 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 14 00 00 01 00 00 01 01 00 00 00 00 00 05 0b 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### Synth3dVsc
  
ImagePath : `\SystemRoot\System32\drivers\Synth3dVsc.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Video Init`  
Tag : `0x01`  
Owners : `77 00 73 00 79 00 6e 00 74 00 68 00 33 00 64 00 76 00 73 00 63 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### TapiSrv
  
Performance : `{'ObjectList': '1150'}`
#### Telemetry
  
ImagePath : `System32\drivers\IntelTA.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Core Security Extensions`  
Tag : `0x02`  
DisplayName : `@intelta.inf,%Telemetry.SVCDESC%;Intel(R) Telemetry Service`  
Owners : `69 00 6e 00 74 00 65 00 6c 00 74 00 61 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### wcnfs
  
DependOnService : `FltMgr`  
Description : `@%systemroot%\system32\drivers\wcnfs.sys,-101`  
DisplayName : `@%systemroot%\system32\drivers\wcnfs.sys,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `FSFilter Top`  
ImagePath : `\SystemRoot\system32\drivers\wcnfs.sys`  
Start : `SERVICE_DEMAND_START`  
SupportedFeatures : `0x07`  
Type : `SERVICE_FILE_SYSTEM_DRIVER`  
Instances : `{'DefaultInstance': 'wcnfs Instance', 'wcnfs Instance': {'Altitude': '409900', 'Flags': 0}}`


##### Service Parameters
  
DebugOptions : `0x00`  
<br></br>  
<br></br>  

</details>

# ProfessionalN

## SYSTEM
  

<details>
  
<summary> Added </summary>
### WMI AutoLoggers

#### BioEnrollment
  
Start : `0x00`  
{4b8b1947-ae4d-54e2-826a-1aee78ef05b2} : `{'Enabled': 0}`  
{a55d5a23-1a5b-580a-2be5-d7188f43fae1} : `{'Enabled': 0}`
|guid|
| :---: |
|Start|
|{4b8b1947-ae4d-54e2-826a-1aee78ef05b2}|
|{a55d5a23-1a5b-580a-2be5-d7188f43fae1}|
  
<br></br>
#### EventLog-Application
  
{04d66358-c4a1-419b-8023-23b73902de2c} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{15f4cd44-ca53-5422-db17-4e76821b5a69} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{6e0df32c-7f11-54f7-e8ee-5ad4032727ce} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 2305843009213693952, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{7628e972-6d6f-4974-b58f-6428622ec09a} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{7d44233d-3055-4b9c-ba64-0d47ca40a232} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 2305843009213693952, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9068a924-f97e-5506-c3a3-5c020c00e8e0} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{a70ff94f-570b-4979-ba5c-e59c9feab61b} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{ad8aa069-a01b-40a0-ba40-948d1d8dedc5} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{04d66358-c4a1-419b-8023-23b73902de2c}|
|{15f4cd44-ca53-5422-db17-4e76821b5a69}|
|{6e0df32c-7f11-54f7-e8ee-5ad4032727ce}|
|{7628e972-6d6f-4974-b58f-6428622ec09a}|
|{7d44233d-3055-4b9c-ba64-0d47ca40a232}|
|{9068a924-f97e-5506-c3a3-5c020c00e8e0}|
|{a70ff94f-570b-4979-ba5c-e59c9feab61b}|
|{ad8aa069-a01b-40a0-ba40-948d1d8dedc5}|
  
<br></br>
#### EventLog-System
  
{0075e1ab-e1d1-5d1f-35f5-da36fb4f41b1} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{17d2a329-4539-5f4d-3435-f510634ce3b9} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{5bcf2a5c-2e90-5a03-aa4e-2e459bae21b4} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{6600e712-c3b6-44a2-8a48-935c511f28c8} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 2305843009213693952, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{7f54ca8a-6c72-5cbc-b96f-d0ef905b8bce} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{87a623f0-8db5-5c11-7c80-a2ebbcbe5189} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{93db76c2-63ab-5de1-88b3-c068686675b8} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9799276c-fb04-47e8-845e-36946045c218} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 2305843009213693952, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{a2d34bf1-70ab-5b21-c819-5a0dd42748fd} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{b931ed29-66f4-576e-0579-0b8818a5dc6b} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{bcf0c6a7-6130-5208-f27d-fa77a91f12df} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{d07e8c3f-78fb-4c22-b77c-2203d00bfdf3} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{f6cf91be-e7d7-57d6-2a3d-278ca406d190} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{0075e1ab-e1d1-5d1f-35f5-da36fb4f41b1}|
|{17d2a329-4539-5f4d-3435-f510634ce3b9}|
|{5bcf2a5c-2e90-5a03-aa4e-2e459bae21b4}|
|{6600e712-c3b6-44a2-8a48-935c511f28c8}|
|{7f54ca8a-6c72-5cbc-b96f-d0ef905b8bce}|
|{87a623f0-8db5-5c11-7c80-a2ebbcbe5189}|
|{93db76c2-63ab-5de1-88b3-c068686675b8}|
|{9799276c-fb04-47e8-845e-36946045c218}|
|{a2d34bf1-70ab-5b21-c819-5a0dd42748fd}|
|{b931ed29-66f4-576e-0579-0b8818a5dc6b}|
|{bcf0c6a7-6130-5208-f27d-fa77a91f12df}|
|{d07e8c3f-78fb-4c22-b77c-2203d00bfdf3}|
|{f6cf91be-e7d7-57d6-2a3d-278ca406d190}|
  
<br></br>
#### FaceCredProv
  
Start : `0x00`  
{1D480C11-3870-4B19-9144-47A53CD973BD} : `{'Enabled': 0}`
|guid|
| :---: |
|Start|
|{1D480C11-3870-4B19-9144-47A53CD973BD}|
  
<br></br>
#### FaceTel
  
Start : `0x00`  
{22eb0808-0b6c-5cd4-5511-6a77e6e73a93} : `{'Enabled': 0}`
|guid|
| :---: |
|Start|
|{22eb0808-0b6c-5cd4-5511-6a77e6e73a93}|
  
<br></br>
#### NetCore
  
{923C0FFD-7933-4B52-8A49-121ABF2DC357} : `{'@': 'triage_routepolicymanagement_tracelogging', 'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{923C0FFD-7933-4B52-8A49-121ABF2DC357}|
  
<br></br>
#### NtfsLog
  
{aa381297-bccb-4569-8e39-bbbb3b400893} : `{'_Description': 'TmLog Trace Provider', 'Enabled': 1, 'EnableFlags': 15, 'EnableLevel': 5}`
|guid|
| :---: |
|{aa381297-bccb-4569-8e39-bbbb3b400893}|
  
<br></br>
#### ReFSLog
  
ClockType : `0x02`  
GUID : `{81a69395-9f48-48f2-b88c-2401db1e3a91}`  
Start : `0x01`  
{740f3c34-57df-4bad-8eea-72ac69ad5df5} : `{'_Description': 'ReFS WPP Trace', 'Enabled': 1, 'EnableFlags': 7, 'EnableLevel': 3}`
|guid|
| :---: |
|ClockType|
|GUID|
|Start|
|{740f3c34-57df-4bad-8eea-72ac69ad5df5}|
  
<br></br>
#### SetupPlatformTel
  
{D2F37B94-92A5-44E2-AFC9-2F4489D39268} : `{'Enabled': 1, 'EnableLevel': 255}`
|guid|
| :---: |
|{D2F37B94-92A5-44E2-AFC9-2F4489D39268}|
  
<br></br>
#### SpoolerLogger
  
{ba4936a1-31db-4edc-89ce-9190e3c0653b} : `{'Enabled': 1, 'EnableFlags': 0, 'EnableLevel': 5}`
|guid|
| :---: |
|{ba4936a1-31db-4edc-89ce-9190e3c0653b}|
  
<br></br>
#### WiFiSession
  
{745976be-5e09-5c76-eabd-76c93c9212d2} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`  
{ae164ede-2246-5b24-c145-29c484f7362a} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`  
{EA893635-5AB7-562B-75A2-A22107D8058F} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{745976be-5e09-5c76-eabd-76c93c9212d2}|
|{ae164ede-2246-5b24-c145-29c484f7362a}|
|{EA893635-5AB7-562B-75A2-A22107D8058F}|
  
<br></br>  
<br></br>
### Services

#### ACPI



##### Service Parameters
  
PnpAsyncNewDevices : `0x01`  
<br></br>
#### Appinfo



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 66 00 37 00 33 00 38 00 65 00 32 00 30 00 2d 00 37 00 33 00 63 00 30 00 2d 00 34 00 63 00 61 00 38 00 2d 00 61 00 61 00 36 00 61 00 2d 00 38 00 64 00 66 00 65 00 66 00 35 00 34 00 35 00 66 00 65 00 61 00 38 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### AppleSSD
  
ImagePath : `System32\drivers\AppleSSD.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x01`  
DisplayName : `@AppleSSD.inf,%DevDesc1%;Apple Solid State Drive Device`  
Owners : `41 00 70 00 70 00 6c 00 65 00 53 00 53 00 44 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x01`  
Device : `{'MaxTranLenInPages': 64}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### BFE



##### Service Parameters
  
Policy  
Persistent  
ProviderContext
|GUID|Data|
| :---: | :---: |
|{30433c31-b05f-421f-8fde-018ea4c68af4}|`01 10 08 00 cc cc cc cc 10 01 00 00 00 00 00 00 00 00 02 00 01 00 00 00 f0 00 00 00 04 00 02 00 00 00 00 00 00 00 00 00 f0 00 00 00 01 10 08 00 cc cc cc cc e0 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 31 3c 43 30 5f b0 1f 42 8f de 01 8e a4 c6 8a f4 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 00 00 00 00 00 00 00 00 08 00 00 00 08 00 00 00 10 00 02 00 00 00 00 00 05 00 00 00 00 00 00 80 07 00 00 00 00 00 00 00 07 00 00 00 4d 00 50 00 53 00 53 00 56 00 43 00 00 00 00 00 15 00 00 00 00 00 00 00 15 00 00 00 53 00 74 00 6f 00 72 00 65 00 73 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 20 00 6f 00 72 00 69 00 67 00 69 00 6e 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 26 00 00 00 14 00 02 00 26 00 00 00 51 00 75 00 61 00 72 00 61 00 6e 00 74 00 69 00 6e 00 65 00 20 00 44 00 65 00 66 00 61 00 75 00 6c 00 74 00 00 00 00 00 00 00 00 00`|
|{93132c36-6e06-4e6f-a10b-218787cd49cf}|`01 10 08 00 cc cc cc cc 10 01 00 00 00 00 00 00 00 00 02 00 01 00 00 00 f0 00 00 00 04 00 02 00 00 00 00 00 00 00 00 00 f0 00 00 00 01 10 08 00 cc cc cc cc e0 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 36 2c 13 93 06 6e 6f 4e a1 0b 21 87 87 cd 49 cf 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 00 00 00 00 00 00 00 00 08 00 00 00 08 00 00 00 10 00 02 00 00 00 00 00 06 00 00 00 00 00 00 80 07 00 00 00 00 00 00 00 07 00 00 00 4d 00 50 00 53 00 53 00 56 00 43 00 00 00 00 00 15 00 00 00 00 00 00 00 15 00 00 00 53 00 74 00 6f 00 72 00 65 00 73 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 20 00 6f 00 72 00 69 00 67 00 69 00 6e 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 22 00 00 00 14 00 02 00 22 00 00 00 42 00 6f 00 6f 00 74 00 74 00 69 00 6d 00 65 00 20 00 44 00 65 00 66 00 61 00 75 00 6c 00 74 00 00 00 00 00 00 00 00 00 00 00 00 00`|
  
<br></br>
#### cbdhsvc
  
DelayedAutoStart : `0x01`
#### CldFlt



##### Service Parameters
  
USMsgTimeoutMillis : `0x3e8`  
<br></br>
#### dcsvc
  
DelayedAutoStart : `0x01`  
DependOnService : `rpcss`  
Description : `@%systemroot%\system32\dcsvc.dll,-101`  
DisplayName : `@%systemroot%\system32\dcsvc,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 04 00 00 00 14 00 00 00 01 00 00 00 10 27 00 00 01 00 00 00 10 27 00 00 01 00 00 00 10 27 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%systemroot%\system32\svchost.exe -k netsvcs -p`  
ObjectName : `LocalSystem`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`


##### Service Parameters
  
IdleTimeout(sec) : `0x78`  
ServiceDll : `%SystemRoot%\system32\dcsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`35 00 39 00 62 00 65 00 62 00 39 00 37 00 37 00 2d 00 64 00 30 00 33 00 37 00 2d 00 34 00 38 00 66 00 34 00 2d 00 61 00 66 00 37 00 34 00 2d 00 63 00 61 00 30 00 37 00 35 00 34 00 39 00 33 00 61 00 35 00 32 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 61 00 30 00 64 00 62 00 36 00 31 00 34 00 2d 00 65 00 39 00 66 00 62 00 2d 00 34 00 38 00 63 00 66 00 2d 00 39 00 31 00 34 00 33 00 2d 00 37 00 61 00 65 00 37 00 31 00 38 00 66 00 66 00 32 00 63 00 38 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### DeviceInstall



##### Service Parameters
  
DeviceInstallMode : `0x01`  
<br></br>
#### disk



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### Dnscache



##### Service Parameters
  
DohWellKnownServers : `{'1.0.0.1': {'Template': 'https://cloudflare-dns.com/dns-query'}, '1.1.1.1': {'Template': 'https://cloudflare-dns.com/dns-query'}, '149.112.112.112': {'Template': 'https://dns.quad9.net/dns-query'}, '2001:4860:4860::8844': {'Template': 'https://dns.google/dns-query'}, '2001:4860:4860::8888': {'Template': 'https://dns.google/dns-query'}, '2606:4700:4700::1001': {'Template': 'https://cloudflare-dns.com/dns-query'}, '2606:4700:4700::1111': {'Template': 'https://cloudflare-dns.com/dns-query'}, '2620:fe::fe': {'Template': 'https://dns.quad9.net/dns-query'}, '2620:fe::fe:9': {'Template': 'https://dns.quad9.net/dns-query'}, '8.8.4.4': {'Template': 'https://dns.google/dns-query'}, '8.8.8.8': {'Template': 'https://dns.google/dns-query'}, '9.9.9.9': {'Template': 'https://dns.quad9.net/dns-query'}}`  
<br></br>
#### EapHost
  
DependOnService : `RPCSSKeyIso`  
Description : `@%systemroot%\system32\eapsvc.dll,-2`  
DisplayName : `@%systemroot%\system32\eapsvc.dll,-1`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 c0 d4 01 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\svchost.exe -k netsvcs -p`  
ObjectName : `localSystem`  
RequiredPrivileges : `['SeTcbPrivilege', 'SeDebugPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_SHARE_PROCESS`  
Methods : `{'311': {'Name': 'Microsoft', '18': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '21': {'PeerConfigUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\TtlsAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\TtlsCfg.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 389863599, 'LANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}, 'WLANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication /></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}, '23': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1002', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '254': {'14122': {'1': {'PeerDllPath': '%SystemRoot%\\System32\\WcnEapPeerProxy.dll', 'PeerFriendlyName': 'Windows Connect Now EAP Peer', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 8683520}}}, '50': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1003', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName /><Realm Enabled="true" /></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '55': {'PeerConfigUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerDllPath': '%SystemRoot%\\System32\\EapTeapAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\EapTeapAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'Properties': 1065154751, 'LANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames /><TrustedRootCAHash /></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}, 'WLANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0" encoding="utf-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><TrustedRootCAHash></TrustedRootCAHash></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection> </CertificateStore> </CredentialsSource><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0" encoding="utf-8"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>machineOrUser</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><TrustedRootCAHash></TrustedRootCAHash></ServerValidation><Phase2Authentication><InnerMethodConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></InnerMethodConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>someone@example.com</AnonymousIdentity></Phase1Identity></EapTeap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}}}`


##### Service Parameters
  
PeerInstalled : `0x01`  
ServiceDll : `%SystemRoot%\System32\eapsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
EapProvPlugin : `{'(Default)': '%SystemRoot%\\System32\\eapprovp.dll', 'DllEntryPoint': 'EapProvPlugGetInfo'}`  
<br></br>
#### ebdrv0
  
ImagePath : `System32\drivers\evbd0a.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `System Bus Extender`  
Tag : `0x03`  
DisplayName : `@netevbd0a.inf,%vbd_srv_desc%;QLogic Legacy Ethernet Adapter VBD`  
Owners : `6e 00 65 00 74 00 65 00 76 00 62 00 64 00 30 00 61 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### EhStorClass



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### EventLog
  
Application : `{'Microsoft-Windows-PDH': {'ProviderGuid': '{04d66358-c4a1-419b-8023-23b73902de2c}', 'EventMessageFile': '%SystemRoot%\\system32\\pdh.dll'}, 'Universal Print': {'EventMessageFile': '%SystemRoot%\\System32\\McpManagementService.dll', 'TypesSupported': 7}}`  
System : `{'AppleSSD': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'ebdrv0': {'eventmessagefile': '%SystemRoot%\\System32\\drivers\\evbd0a.sys;%SystemRoot%\\System32\\iologmsg.dll', 'typessupported': 7}, 'EventLog': {'EventMessageFile': '%SystemRoot%\\System32\\netevent.dll', 'TypesSupported': 7}, 'hvservice': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'Microsoft-Windows-Iphlpsvc-Trace': {'ProviderGuid': '{6600e712-c3b6-44a2-8a48-935c511f28c8}', 'EventMessageFile': '%windir%\\system32\\iphlpsvc.dll'}, 'Microsoft-Windows-Network-ExecutionContext': {'ProviderGuid': '{0075e1ab-e1d1-5d1f-35f5-da36fb4f41b1}', 'EventMessageFile': '%SystemRoot%\\system32\\drivers\\ExecutionContext.sys'}, 'Microsoft-Windows-USB-USB4DeviceRouter-EventLogs': {'ProviderGuid': '{d07e8c3f-78fb-4c22-b77c-2203d00bfdf3}', 'EventMessageFile': '%SystemRoot%\\System32\\DriverStore\\FileRepository\\usb4devicerouter.inf_amd64_3bffb5f5105936e5\\Usb4DeviceRouter.sys'}, 'mpi3drvi': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'nvmedisk': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll;%SystemRoot%\\System32\\drivers\\nvmedisk.sys', 'TypesSupported': 7}}`
#### ExecutionContext
  
DisplayName : `@%SystemRoot%\System32\Drivers\ExecutionContext.sys,-101`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `System`  
ImagePath : `System32\Drivers\ExecutionContext.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### FrameServerMonitor
  
DependOnService : `rpcss`  
Description : `@%systemroot%\system32\FrameServerMonitor.dll,-101`  
DisplayName : `@%systemroot%\system32\FrameServerMonitor.dll,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 20 bf 02 00`  
ImagePath : `%SystemRoot%\System32\svchost.exe -k CameraMonitor`  
ObjectName : `LocalSystem`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`  
parameters : `{'ServiceDll': '%SystemRoot%\\system32\\FrameServerMonitor.dll', 'ServiceDllUnloadOnStop': 1}`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`42 00 45 00 30 00 44 00 39 00 35 00 42 00 41 00 2d 00 32 00 31 00 41 00 35 00 2d 00 34 00 41 00 35 00 46 00 2d 00 41 00 31 00 46 00 30 00 2d 00 39 00 41 00 44 00 41 00 38 00 34 00 41 00 43 00 31 00 31 00 34 00 34 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 26 1d 90 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 21 bc a3 2e 0f 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`773732e5-76f9-5b4f-9b55-b94699c46e44`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`d752e524-2365-f747-a647-d3465bf1f5ca`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 b8 bc a3 3d 01 c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### fvevol



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### hidspi
  
DependOnService : `HidSpiCx`
#### HidSpiCx
  
DisplayName : `HidSpi KMDF Class Extension`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `system32\drivers\HidSpiCx.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### Hsp
  
ImagePath : `\SystemRoot\System32\drivers\Hsp.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@hsp.inf,%Hsp.SVCDESC%;Microsoft Pluton Service`  
Owners : `68 00 73 00 70 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
Wdf : `{'KmdfLibraryVersion': '1.15'}`  
<br></br>
#### hvservice
  
Owners : `68 00 76 00 73 00 65 00 72 00 76 00 69 00 63 00 65 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### IntelPMT
  
ImagePath : `System32\drivers\IntelPMT.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Core Security Extensions`  
Tag : `0x02`  
DisplayName : `@intelpmt.inf,%IntelPMT.SVCDESC%;Intel(R) Platform Monitoring Technology Service`  
Owners : `69 00 6e 00 74 00 65 00 6c 00 70 00 6d 00 74 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### iorate



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### lfsvc
  
Settings : `{'LocationWebServiceProxy': {'USE_CLIENT_PROXY_INFERENCE_ONLY': 0}}`
#### McpManagementService
  
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


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\McpManagementService.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>
#### mpi3drvi
  
ImagePath : `System32\drivers\mpi3drvi.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x10`  
Owners : `6d 00 70 00 69 00 33 00 64 00 72 00 76 00 69 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x08`  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### NDIS



##### Service Parameters
  
Reserved : `{'ExecutionContextProfiles': {'Balanced': {'DpcWatchdogTimerThreshold': 80, 'Flags': 0, 'MaxPacketsReceiveAtDispatch': 64, 'MaxPacketsReceiveAtPassive': 64, 'MaxPacketsReceiveCompleteAtDispatch': 64, 'MaxPacketsReceiveCompleteAtPassive': 64, 'MaxPacketsSendAtDispatch': 64, 'MaxPacketsSendAtPassive': 64, 'MaxPacketsSendCompleteAtDispatch': 64, 'MaxPacketsSendCompleteAtPassive': 64, 'MaxTimeAtDispatch': 0, 'WorkerThreadPriority': 10}}}`  
<br></br>
#### NDKPerf
  
DisplayName : `NDKPerf Driver`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `system32\drivers\NDKPerf.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### NPSMSvc
  
Description : `@%SystemRoot%\system32\npsm.dll,-101`  
DisplayName : `@%SystemRoot%\system32\npsm.dll,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 b8 0b 00 00 01 00 00 00 b8 0b 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k LocalService -p`  
ObjectName : `NT AUTHORITY\LocalService`  
RequiredPrivileges : `['SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `96`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\npsm.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  
Security : `01 00 14 80 a0 00 00 00 ac 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 01 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 70 00 05 00 00 00 00 00 14 00 fd 01 02 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 14 00 00 01 00 00 01 01 00 00 00 00 00 05 0b 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### nvmedisk
  
ImagePath : `System32\drivers\nvmedisk.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@nvmedisk.inf,%nvmedisk.SvcDesc%;Microsoft NVMe disk driver`  
Owners : `6e 00 76 00 6d 00 65 00 64 00 69 00 73 00 6b 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### P9NP
  
Description : `@%systemroot%\system32\p9np.dll,-101`  
DisplayName : `@%systemroot%\system32\p9np.dll,-100`  
NetworkProvider : `{'DeviceName': '\\Device\\P9Rdr', 'DisplayName': '@%systemroot%\\system32\\p9np.dll,-100', 'Name': 'Plan 9 Network Provider', 'ProviderPath': '%SystemRoot%\\System32\\p9np.dll', 'TriggerStartCompleteNotification': b'u\x10\xbc\xa3T\x1e\xc6A', 'TriggerStartNotification': b'u\x08\xbc\xa3T\x1e\xc6A', 'TriggerStartPrefix': b'w\x00s\x00l\x00.\x00l\x00o\x00c\x00a\x00l\x00h\x00o\x00s\x00t\x00\x00\x00w\x00s\x00l\x00$\x00\x00\x00\x00\x00'}`
#### P9Rdr
  
DependOnService : `RDBSS`  
Description : `@%SystemRoot%\System32\drivers\p9rdr.sys,-101`  
DisplayName : `@%SystemRoot%\System32\drivers\p9rdr.sys,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `System32\drivers\p9rdr.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### P9RdrService
  
DependOnService : `P9RdrRPCSS`  
Description : `@%systemroot%\system32\p9rdrservice.dll,-101`  
DisplayName : `@%systemroot%\system32\p9rdrservice.dll,-102`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 b8 0b 00 00 01 00 00 00 b8 0b 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%systemroot%\system32\svchost.exe -k P9RdrService -p`  
ObjectName : `LocalSystem`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `96`  
UserServiceFlags : `0x03`  
parameters : `{'ServiceDll': '%SystemRoot%\\system32\\p9rdrservice.dll', 'ServiceDllUnloadOnStop': 1}`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 54 1e c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### partmgr



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### PcaSvc



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 d0 be a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 18 bc a3 2e 07 c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 2e 03 96 15`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### pci



##### Service Parameters
  
PnpAsyncNewDevices : `0x01`  
<br></br>
#### PenService
  
Description : `@%SystemRoot%\system32\PenService.dll,-101`  
DisplayName : `@%SystemRoot%\system32\PenService.dll,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 02 00 00 00 14 00 00 00 01 00 00 00 10 27 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k PenService`  
Start : `SERVICE_DEMAND_START`  
Type : `96`  
UserServiceFlags : `0x02`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\PenService.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|Data1|Data2|Data3|DataType0|DataType1|DataType2|DataType3|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`b2551e4d-6ff1-cf11-88cb-001111000030`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 31 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 32 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 33 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 46 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### PerfDisk
  
Performance : `{'Collect Supports Metadata': 1}`
#### PerfNet
  
Performance : `{'Collect Supports Metadata': 1}`
#### PerfOS
  
Performance : `{'Collect Supports Metadata': 1}`
#### PerfProc
  
Performance : `{'Collect Supports Metadata': 1}`
#### PrintWorkflowUserSvc



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 3d 0a 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### PRM
  
ImagePath : `System32\DriverStore\FileRepository\prm.inf_amd64_7fc9bb8ba2b73803\PRM.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@prm.inf,%PRM.SvcDesc%;Microsoft PRM Driver`  
Owners : `70 00 72 00 6d 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### RasMan
  
PPP : `{'EAP': {'13': {'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '25': {'LANProfileCreationUXAuth': {'13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">25</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>25</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV1"><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><FastReconnect>true</FastReconnect><InnerEapOptional>false</InnerEapOptional><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true</AcceptServerName></EapType></Eap><EnableQuarantineChecks>false</EnableQuarantineChecks><RequireCryptoBinding>false</RequireCryptoBinding><PeapExtensions><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</AcceptServerName><IdentityPrivacy xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2"><EnableIdentityPrivacy>true</EnableIdentityPrivacy><AnonymousUserName>anonymous</AnonymousUserName></IdentityPrivacy></PeapExtensions></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'LANProfileTemplate': '<?xml version="1.0" encoding="UTF-8"?><LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1"><MSM><security><OneXEnforced>false</OneXEnforced><OneXEnabled>true</OneXEnabled><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">25</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>25</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV1"><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames /><TrustedRootCA /></ServerValidation><FastReconnect>true</FastReconnect><InnerEapOptional>false</InnerEapOptional><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap><EnableQuarantineChecks>false</EnableQuarantineChecks><RequireCryptoBinding>false</RequireCryptoBinding><PeapExtensions><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2">true</AcceptServerName><IdentityPrivacy xmlns="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV2"><EnableIdentityPrivacy>true</EnableIdentityPrivacy><AnonymousUserName>anonymous</AnonymousUserName></IdentityPrivacy></PeapExtensions></EapType></Eap></Config></EapHostConfig></EAPConfig></OneX></security></MSM></LANProfile>'}}}}}`
#### rdyboost



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### RemoteAccess
  
Performance : `{'Object List': '7106 7142'}`
#### RetailDemo
  
StateFlags : `0x01`
#### SecurityHealthService
  
Security : `01 00 14 80 a4 00 00 00 b0 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 00 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 74 00 05 00 00 00 00 00 14 00 9d 00 02 00 01 01 00 00 00 00 00 05 0b 00 00 00 00 00 18 00 9d 00 02 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 9d 00 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 18 00 9d 00 02 00 01 02 00 00 00 00 00 0f 02 00 00 00 01 00 00 00 00 00 14 00 ff 01 0f 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### SensorService



##### Service Parameters
  
Sensors : `{'{934F17E7-42EF-470B-BE7C-1AD0983C9E6C}': {'RequiredHingeJointsCount': 1, 'RequiredPanelGroupsCount': 2, 'SensorType': '{0D49D945-FA83-4630-A22C-01387F906DE6}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}, '{AEDD7472-297F-4285-B2FB-9422731BCDA6}': {'RequiredHingeJointsCount': 2, 'RequiredPanelGroupsCount': 3, 'SensorType': '{0D49D945-FA83-4630-A22C-01387F906DE6}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}}`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 38 00 34 00 38 00 39 00 42 00 45 00 31 00 43 00 2d 00 38 00 30 00 41 00 34 00 2d 00 34 00 38 00 42 00 43 00 2d 00 39 00 30 00 31 00 41 00 2d 00 41 00 41 00 39 00 31 00 42 00 44 00 38 00 32 00 37 00 41 00 37 00 43 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 42 00 32 00 43 00 45 00 36 00 33 00 34 00 2d 00 31 00 39 00 31 00 44 00 2d 00 34 00 32 00 41 00 46 00 2d 00 41 00 32 00 38 00 43 00 2d 00 31 00 36 00 42 00 45 00 39 00 37 00 39 00 32 00 34 00 43 00 41 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|6|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`39 00 37 00 42 00 45 00 39 00 35 00 30 00 37 00 2d 00 31 00 37 00 44 00 41 00 2d 00 34 00 39 00 39 00 39 00 2d 00 38 00 37 00 44 00 37 00 2d 00 36 00 36 00 43 00 30 00 42 00 32 00 44 00 38 00 33 00 43 00 43 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|7|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`36 00 33 00 32 00 38 00 44 00 43 00 43 00 34 00 2d 00 31 00 36 00 35 00 38 00 2d 00 34 00 31 00 33 00 33 00 2d 00 38 00 30 00 36 00 32 00 2d 00 41 00 39 00 39 00 34 00 33 00 44 00 41 00 43 00 32 00 30 00 39 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### SNMPTrap
  
Description : `@firewallapi.dll,-50324`  
DisplayName : `@firewallapi.dll,-50323`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `ff ff ff ff 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 60 ea 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\snmptrap.exe`  
ObjectName : `NT AUTHORITY\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`
#### StiSvc
  
DependOnService : `RpcSs`  
Description : `@%SystemRoot%\system32\wiaservc.dll,-10`  
DisplayName : `@%SystemRoot%\system32\wiaservc.dll,-9`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k imgsvc`  
ObjectName : `NT Authority\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wiaservc.dll`  
<br></br>  
Security : `01 00 14 80 a0 00 00 00 ac 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 01 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 70 00 05 00 00 00 00 00 14 00 fd 01 02 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 14 00 00 01 00 00 01 01 00 00 00 00 00 05 0b 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`c61fdd6b-0f81-d011-bec7-08002be2092f`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>
#### stornvme



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### TapiSrv
  
Performance : `{'Object List': '1150'}`
#### TermService
  
Performance : `{'Collect Supports Metadata': 1}`
#### TPM



##### Service Parameters
  
KsrGuid : `{F141DC89-3D00-450A-B2D2-AD995267F8FC}`  
<br></br>
#### tzautoupdate
  
StateFlags : `0x01`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 58 bc a3 3e 06 83 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 30 bc a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|6|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 d0 be a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### UGatherer
  
Performance : `{'Object List': '7146'}`
#### UGTHRSVC
  
Performance : `{'Object List': '7252'}`
#### Usb4DeviceRouter
  
ImagePath : `\SystemRoot\System32\DriverStore\FileRepository\usb4devicerouter.inf_amd64_3bffb5f5105936e5\Usb4DeviceRouter.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Base`  
Tag : `0x15`  
DisplayName : `@Usb4DeviceRouter.inf,%Usb4DeviceRouter.SVCDESC%;USB4 Device Router Service`  
Owners : `55 00 73 00 62 00 34 00 44 00 65 00 76 00 69 00 63 00 65 00 52 00 6f 00 75 00 74 00 65 00 72 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
ForceLogsInMiniDump : `0x01`  
<br></br>
#### Usb4HostRouter
  
ImagePath : `\SystemRoot\System32\DriverStore\FileRepository\usb4hostrouter.inf_amd64_dd61aa4ab70fa4fb\Usb4HostRouter.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
DisplayName : `@Usb4HostRouter.inf,%Usb4HostRouter.SVCDESC%;USB4 Host Router Service`  
Owners : `55 00 73 00 62 00 34 00 48 00 6f 00 73 00 74 00 52 00 6f 00 75 00 74 00 65 00 72 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
DmaRemappingCompatible : `0x01`  
ForceLogsInMiniDump : `0x01`  
<br></br>
#### usbhub
  
Performance : `{'Object List': '7468'}`
#### volmgr



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### volsnap



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### volume



##### Service Parameters
  
StorageSupportedFeatures : `0x01`  
<br></br>
#### WifiCx
  
DependOnService : `NetAdapterCx`  
DisplayName : `Wifi Network Adapter Class Extension`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `system32\drivers\WifiCx.sys`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_KERNEL_DRIVER`
#### XblGameSave



##### Service Parameters
  
FeatureLevel : `0x01`  
<br></br>  
<br></br>  

</details>
  

<details>
  
<summary> Removed </summary>
### WMI AutoLoggers

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
{B1D067C7-2F8C-436E-9E82-C5C2C22229D5} : `{'Enabled': 0, 'EnableLevel': 4, 'MatchAnyKeyword': 18374686479671623680}`
|guid|
| :---: |
|BufferSize|
|ClockType|
|FileMax|
|FileName|
|Guid|
|LogFileMode|
|MaxFileSize|
|MaximumBuffers|
|MinimumBuffers|
|Start|
|{B1D067C7-2F8C-436E-9E82-C5C2C22229D5}|
  
<br></br>
#### EventLog-Application
  
{28e25b07-c47f-473d-8b24-2e171cca808a} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{579402a2-883c-45d8-b70a-9bc856407751} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{83d6e83b-900b-48a3-9835-57656b6f6474} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{973143dd-f3c7-4ef5-b156-544ac38c39b6} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9f973c1d-d056-4e38-84a5-7be81cdd6ab6} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{af0a5a6d-e009-46d4-8867-42f2240f8a72} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{f43c3c35-22e2-53eb-f169-07594054779e} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-Application', 'MatchAnyKeyword': 13835058055282163712, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{28e25b07-c47f-473d-8b24-2e171cca808a}|
|{579402a2-883c-45d8-b70a-9bc856407751}|
|{5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0}|
|{83d6e83b-900b-48a3-9835-57656b6f6474}|
|{973143dd-f3c7-4ef5-b156-544ac38c39b6}|
|{9f973c1d-d056-4e38-84a5-7be81cdd6ab6}|
|{af0a5a6d-e009-46d4-8867-42f2240f8a72}|
|{c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef}|
|{f43c3c35-22e2-53eb-f169-07594054779e}|
  
<br></br>
#### EventLog-System
  
{2bef5442-d402-5a72-58e1-cb7e491bf179} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{3903d5b9-988d-4c31-9ccd-4022f96703f0} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{928f7d29-0577-5be5-3bd3-b6bdab9ab307} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{9f7b5df4-b902-48bc-bc94-95068c6c7d26} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{b99317e5-89b7-4c0d-abd1-6e705f7912dc} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{c18672d1-dc18-4dfd-91e4-170cf37160cf} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 4611686018427387904, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{ea216962-877b-5b73-f7c5-8aef5375959e} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`  
{ed8cc261-2123-567e-063e-75fc5f8e8a48} : `{'Enabled': 1, 'EnableLevel': 0, 'LoggerName': 'EventLog-System', 'MatchAnyKeyword': 9223372036854775808, 'MatchAllKeyword': 0, 'EnableProperty': 1}`
|guid|
| :---: |
|{2bef5442-d402-5a72-58e1-cb7e491bf179}|
|{3903d5b9-988d-4c31-9ccd-4022f96703f0}|
|{928f7d29-0577-5be5-3bd3-b6bdab9ab307}|
|{9f7b5df4-b902-48bc-bc94-95068c6c7d26}|
|{b99317e5-89b7-4c0d-abd1-6e705f7912dc}|
|{c18672d1-dc18-4dfd-91e4-170cf37160cf}|
|{ea216962-877b-5b73-f7c5-8aef5375959e}|
|{ed8cc261-2123-567e-063e-75fc5f8e8a48}|
  
<br></br>
#### LwtNetLog
  
{7868B0D4-1423-4681-AFDF-27913575441E} : `{'Enabled': 1, 'EnableLevel': 4, 'MatchAnyKeyword': 1}`
|guid|
| :---: |
|{7868B0D4-1423-4681-AFDF-27913575441E}|
  
<br></br>
#### NtfsLog
  
{740f3c34-57df-4bad-8eea-72ac69ad5df5} : `{'_Description': 'ReFS WPP Trace', 'Enabled': 1, 'EnableFlags': 7, 'EnableLevel': 3}`
|guid|
| :---: |
|{740f3c34-57df-4bad-8eea-72ac69ad5df5}|
  
<br></br>
#### SQMLogger
  
{017BA13C-9A55-4f1f-8200-323055AAC810} : `{'Enabled': 1, 'EnableLevel': 4, 'EnableProperty': 2, 'LoggerName': 'SQMLogger', 'MatchAnyKeyword': 2251799813685248}`
|guid|
| :---: |
|{017BA13C-9A55-4f1f-8200-323055AAC810}|
  
<br></br>
#### WiFiSession
  
{60523747-6516-48B7-84B1-3264FA2CB359} : `{'Enabled': 1, 'EnableLevel': 5, 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{60523747-6516-48B7-84B1-3264FA2CB359}|
  
<br></br>
#### WinPhoneCritical
  
{A9C11050-9E93-4fa4-8FE0-7C4750A345B2} : `{'Enabled': 1, 'EnableLevel': 2, 'EnableProperty': 2, 'LoggerName': 'SmsRouter', 'MatchAnyKeyword': 0}`
|guid|
| :---: |
|{A9C11050-9E93-4fa4-8FE0-7C4750A345B2}|
  
<br></br>  
<br></br>
### Services

#### BluetoothUserService



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 68 bc a3 2f 02 92 09`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### BthEnum



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
#### BthLEEnum



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
#### BTHPORT



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
#### dmwappushservice
  
RequiredPrivileges : `['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege', 'SeIncreaseWorkingSetPrivilege']`


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 61 00 30 00 64 00 62 00 36 00 31 00 34 00 2d 00 65 00 39 00 66 00 62 00 2d 00 34 00 38 00 63 00 66 00 2d 00 39 00 31 00 34 00 33 00 2d 00 37 00 61 00 65 00 37 00 31 00 38 00 66 00 66 00 32 00 63 00 38 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 90 bc a3 28 00 92 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>
#### Eaphost
  
DependOnService : `RPCSSKeyIso`  
Description : `@%systemroot%\system32\eapsvc.dll,-2`  
DisplayName : `@%systemroot%\system32\eapsvc.dll,-1`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 c0 d4 01 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\svchost.exe -k netsvcs -p`  
ObjectName : `localSystem`  
RequiredPrivileges : `['SeTcbPrivilege', 'SeDebugPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_SHARE_PROCESS`  
Methods : `{'311': {'Name': 'Microsoft', '18': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">18</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapSim xmlns="http://www.microsoft.com/provisioning/EapSimConnectionPropertiesV1"><UseStrongCipherKeys>false</UseStrongCipherKeys><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapSim></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '21': {'PeerConfigUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\TtlsAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\TtlsCfg.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\TtlsCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 389863599, 'WLANProfileCreationUXAuth': {'1025': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3000', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><PAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1026': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3001', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><CHAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1027': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3002', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPAuthentication/></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '1028': {'FriendlyName': '@%SystemRoot%\\system32\\TtlsCfg.dll,-3003', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><MSCHAPv2Authentication><UseWinlogonCredentials>false</UseWinlogonCredentials></MSCHAPv2Authentication></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '13': {'FriendlyName': '@%SystemRoot%\\system32\\rastls.dll,-2001', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>auto</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><cacheUserData>true</cacheUserData><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>13</Type><EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1"><CredentialsSource><CertificateStore><SimpleCertSelection>true</SimpleCertSelection></CertificateStore></CredentialsSource><ServerValidation><DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation><ServerNames></ServerNames></ServerValidation><DifferentUsername>false</DifferentUsername><PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation><AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</AcceptServerName></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '26': {'FriendlyName': '@%SystemRoot%\\system32\\raschap.dll,-2002', 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><authMode>user</authMode><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">21</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapTtls xmlns="http://www.microsoft.com/provisioning/EapTtlsConnectionPropertiesV1"><ServerValidation><ServerNames></ServerNames><DisablePrompt>false</DisablePrompt></ServerValidation><Phase2Authentication><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">26</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"><Type>26</Type><EapType xmlns="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1"><UseWinLogonCredentials>false</UseWinLogonCredentials></EapType></Eap></Config></EapHostConfig></Phase2Authentication><Phase1Identity><IdentityPrivacy>true</IdentityPrivacy><AnonymousIdentity>anonymous</AnonymousIdentity></Phase1Identity></EapTtls></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}}}, '23': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1002', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1"><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAka></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '254': {'14122': {'1': {'PeerDllPath': '%SystemRoot%\\System32\\WcnEapPeerProxy.dll', 'PeerFriendlyName': 'Windows Connect Now EAP Peer', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 8683520}}}, '50': {'PeerConfigUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerDllPath': '%SystemRoot%\\System32\\SimAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\SimAuth.dll,-1003', 'PeerIdentityPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\SimCfg.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'PeerRequireConfigUI': 1, 'Properties': 376195262, 'WLANProfileTemplate': '<?xml version="1.0"?><WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"><name>placeholder</name><SSIDConfig><SSID><hex>706C616365686F6C646572</hex><name>placeholder</name></SSID><nonBroadcast>false</nonBroadcast></SSIDConfig><connectionType>ESS</connectionType><connectionMode>manual</connectionMode><autoSwitch>false</autoSwitch><MSM><security><authEncryption><authentication>WPA2</authentication><encryption>AES</encryption><useOneX>true</useOneX></authEncryption><OneX xmlns="http://www.microsoft.com/networking/OneX/v1"><EAPConfig><EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapMethod><Type xmlns="http://www.microsoft.com/provisioning/EapCommon">50</Type><VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId><VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType><AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId></EapMethod><Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig"><EapAkaPrime xmlns="http://www.microsoft.com/provisioning/EapAkaPrimeConnectionPropertiesV1"><IgnoreNetworkNameMismatch>true</IgnoreNetworkNameMismatch><EnableFastReauth>false</EnableFastReauth><DontRevealPermanentID>false</DontRevealPermanentID><ProviderName></ProviderName><Realm Enabled="true"></Realm></EapAkaPrime></Config></EapHostConfig></EAPConfig></OneX></security></MSM></WLANProfile>'}, '55': {'PeerConfigUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerDllPath': '%SystemRoot%\\System32\\EapTeapAuth.dll', 'PeerFriendlyName': '@%SystemRoot%\\System32\\EapTeapAuth.dll,-1001', 'PeerIdentityPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInteractiveUIPath': '%SystemRoot%\\System32\\EapTeapConfig.dll', 'PeerInvokePasswordDialog': 0, 'PeerInvokeUsernameDialog': 0, 'Properties': 1065154751}}}`


##### Service Parameters
  
PeerInstalled : `0x01`  
ServiceDll : `%SystemRoot%\System32\eapsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
EapProvPlugin : `{'(Default)': '%SystemRoot%\\System32\\eapprovp.dll', 'DllEntryPoint': 'EapProvPlugGetInfo'}`  
<br></br>
#### EventLog
  
SvcMemHardLimitInMB : `0x14`  
SvcMemMidLimitInMB : `0x0f`  
SvcMemSoftLimitInMB : `0x0b`  
Application : `{'LoadPerf': {'ProviderGuid': '{122EE297-BB47-41AE-B265-1CA8D1886D40}'}, 'Microsoft-Windows-PerfCtrs': {'ProviderGuid': '{973143dd-f3c7-4ef5-b156-544ac38c39b6}', 'EventMessageFile': '%SystemRoot%\\system32\\perfctrs.dll'}, 'PDH': {'ProviderGuid': '{04D66358-C4A1-419B-8023-23B73902DE2C}'}, 'PerfCtrs': {'ProviderGuid': '{973143DD-F3C7-4EF5-B156-544AC38C39B6}'}, 'PerfDisk': {'ProviderGuid': '{7F9D83DE-8ABB-457F-98E8-4AD161449ECC}'}, 'Perflib': {'ProviderGuid': '{13B197BD-7CEE-4B4E-8DD0-59314CE374CE}'}, 'PerfNet': {'ProviderGuid': '{CAB2B8A5-49B9-4EEC-B1B0-FAC21DA05A3B}'}, 'PerfOs': {'ProviderGuid': '{F82FB576-E941-4956-A2C7-A0CF83F6450A}'}, 'PerfProc': {'ProviderGuid': '{72D211E1-4C54-4A93-9520-4901681B2271}'}}`  
System : `{'eventlog': {'EventMessageFile': '%SystemRoot%\\System32\\netevent.dll', 'TypesSupported': 7}, 'LSI_SSS': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'megasas': {'EventMessageFile': '%SystemRoot%\\System32\\IoLogMsg.dll', 'TypesSupported': 7}, 'Microsoft-Antimalware-ShieldProvider': {'ProviderGuid': '{928f7d29-0577-5be5-3bd3-b6bdab9ab307}', 'EventMessageFile': '%SystemRoot%\\System32\\SecurityHealthService.exe'}}`
#### FrameServer



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 21 bc a3 2e 0f 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`773732e5-76f9-5b4f-9b55-b94699c46e44`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`d752e524-2365-f747-a647-d3465bf1f5ca`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
  
<br></br>
#### HomeGroupListener
  
SvcMemHardLimitInMB : `0xbd`  
SvcMemMidLimitInMB : `0x7e`  
SvcMemSoftLimitInMB : `0x40`  
ApprovedListeners : `{'{125B0F61-0EC3-4f07-9A49-AFB340D9E57F}': {'(Default)': 'File History Hosted Listener', 'SupportedRecordTypes': {'GUID_DPListenerRecordType': '{ADBCFEA5-D8FC-4a46-B12B-EB1FFE39BF17}'}}, '{517F6AA6-D6FA-46D0-8094-17FF17E4CCF4}': {'(Default)': 'Security Hosted Listener', 'SupportedRecordTypes': {'GUID_SecurityListener_SigningKeys': '{CA328F46-E759-4399-82AB-FA92651D1ED2}'}}, '{5255EFED-103A-4444-B124-F88F99E4EF8D}': {'(Default)': 'Printer Hosted Listener'}, '{8ADD018C-5C5F-43C5-BE1E-07BAE85593B7}': {'(Default)': 'Alpha Hosted Listener', 'SupportedRecordTypes': {'GUID_AlphaListener_AlphaAccount': '{929CB323-C5EA-48E7-A6D0-193DD432E769}'}}, '{DE9C1288-0F09-40ff-BA84-7F19279FA74B}': {'(Default)': 'Identity Hosted Listener', 'SupportedRecordTypes': {'GUID_IdentityListenerRecordType': '{07004F5D-93A5-4b6c-B851-E2C9BBFD923D}', 'GUID_IdentityMachineCertRecordType': '{07004F5E-93A5-4b6c-B851-E2C9BBFD923E}'}}, '{EB6B4457-F013-4E5A-9B05-1D44E4D6FAEB}': {'(Default)': 'Sharing Hosted Listener', 'SupportedRecordTypes': {'GUID_SharingListener_MACAddresses': '{A7BC622E-8238-4E38-9C88-34153B7D9AB1}'}}}`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\ListSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ListenerServiceMain`  
<br></br>
#### HomeGroupProvider



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\provsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ProviderServiceMain`  
<br></br>  
ServiceData : `{'LocalJoiningUser': '', 'Password': b'\x00'}`
#### hvservice
  
Description : `@%SystemRoot%\system32\drivers\hvservice.sys,-17`  
Group : `Extended Base`
#### Lsa
  
Performance : `{'Close': 'CloseLsaPerformanceData', 'Collect': 'CollectLsaPerformanceData', 'Library': 'X:\\Windows\\System32\\Secur32.dll', 'Object List': '1570 1670', 'Open': 'OpenLsaPerformanceData'}`
#### LSI_SSS
  
ImagePath : `System32\drivers\lsi_sss.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x0c`  
Owners : `6c 00 73 00 69 00 5f 00 73 00 73 00 73 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x0a`  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### megasas
  
ImagePath : `System32\drivers\megasas.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `SCSI Miniport`  
Tag : `0x0d`  
Owners : `6d 00 65 00 67 00 61 00 73 00 61 00 73 00 2e 00 69 00 6e 00 66 00 00 00 00 00`


##### Service Parameters
  
BusType : `0x08`  
IoTimeoutValue : `0x3c`  
Device : `{'DriverParameter': 'nobusywait=1', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>
#### mshidkmdf
  
Description : `@%SystemRoot%\system32\drivers\mshidkmdf.sys,-101`  
Group : `Base`
#### MSSCNTRS
  
Performance : `{'Close': 'Close', 'Collect': 'Collect', 'Library': '%systemroot%\\system32\\msscntrs.dll', 'Open': 'Open'}`
#### NlaSvc
  
DependOnService : `NSIRpcSsTcpIpDhcpEventlog`  
FailureActions : `80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 64 00 00 00 01 00 00 00 64 00 00 00 00 00 00 00 00 00 00 00`


##### Service Parameters
  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  
Security : `01 00 04 80 98 00 00 00 a4 00 00 00 00 00 00 00 14 00 00 00 02 00 84 00 05 00 00 00 00 02 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 02 14 00 ff 01 0f 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 14 00 9d 00 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 28 00 1d 00 02 00 01 06 00 00 00 00 00 05 50 00 00 00 44 3e 41 bb 45 ba a8 7a 6c bd 92 68 f4 ad 64 8f d5 e6 70 e9 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### RFCOMM



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
#### SensorService



##### Service Parameters
  
Sensors : `{'{0D49D945-FA83-4630-A22C-01387F906DE6}': {'PersistentUniqueId': '{934F17E7-42EF-470B-BE7C-1AD0983C9E6C}', '{82358065-F4C4-4DA1-B272-13C23332A207}': None}}`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|1||||`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 38 00 34 00 38 00 39 00 42 00 45 00 31 00 43 00 2d 00 38 00 30 00 41 00 34 00 2d 00 34 00 38 00 42 00 43 00 2d 00 39 00 30 00 31 00 41 00 2d 00 41 00 41 00 39 00 31 00 42 00 44 00 38 00 32 00 37 00 41 00 37 00 43 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2||||`44 00 42 00 32 00 43 00 45 00 36 00 33 00 34 00 2d 00 31 00 39 00 31 00 44 00 2d 00 34 00 32 00 41 00 46 00 2d 00 41 00 32 00 38 00 43 00 2d 00 31 00 36 00 42 00 45 00 39 00 37 00 39 00 32 00 34 00 43 00 41 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3||||`39 00 37 00 42 00 45 00 39 00 35 00 30 00 37 00 2d 00 31 00 37 00 44 00 41 00 2d 00 34 00 39 00 39 00 39 00 2d 00 38 00 37 00 44 00 37 00 2d 00 36 00 36 00 43 00 30 00 42 00 32 00 44 00 38 00 33 00 43 00 43 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>
#### SharedAccess
  
Defaults : `{'FirewallPolicy': {'FirewallRules': {'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=6|Profile=Private|LPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-200|Desc=@%systemroot%\\system32\\provsvc.dll,-201|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=6|Profile=Private|RPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-203|Desc=@%systemroot%\\system32\\provsvc.dll,-204|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=17|Profile=Private|LPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-205|Desc=@%systemroot%\\system32\\provsvc.dll,-206|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=17|Profile=Private|RPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-207|Desc=@%systemroot%\\system32\\provsvc.dll,-208|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|'}}}`


##### Service Parameters
  
FirewallPolicy : `{'FirewallRules': {'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=6|Profile=Private|LPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-200|Desc=@%systemroot%\\system32\\provsvc.dll,-201|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-TCP3587-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=6|Profile=Private|RPort=3587|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=p2psvc|Name=@%systemroot%\\system32\\provsvc.dll,-203|Desc=@%systemroot%\\system32\\provsvc.dll,-204|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-In': 'v2.30|Action=Allow|Active=FALSE|Dir=In|Protocol=17|Profile=Private|LPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-205|Desc=@%systemroot%\\system32\\provsvc.dll,-206|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|', 'Microsoft-Windows-HomeGroup-ProvSvc-UDP3540-Out': 'v2.30|Action=Allow|Active=FALSE|Dir=Out|Protocol=17|Profile=Private|RPort=3540|RA4=LocalSubnet|RA6=LocalSubnet|App=%systemroot%\\system32\\svchost.exe|Svc=pnrpsvc|Name=@%systemroot%\\system32\\provsvc.dll,-207|Desc=@%systemroot%\\system32\\provsvc.dll,-208|EmbedCtxt=@%systemroot%\\system32\\provsvc.dll,-202|'}, 'RestrictedServices': {'Static': {'System': {'HomeGroup Allow In': 'v2.0|Action=Allow|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|LPort=3587|Protocol=6|Name=Allow Grouping to receive from port 3587|', 'HomeGroup Allow In (PRNP)': 'v2.0|Action=Allow|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|LPort=3540|Protocol=17|Name=Allow PNRP to receive from port 3540|', 'HomeGroup Allow Out': 'v2.0|Action=Allow|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|RPort=3587|Protocol=6|Name=Allow Grouping to send to port 3587|', 'HomeGroup Allow Out (PRNP)': 'v2.0|Action=Allow|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|RPort=3540|Protocol=17|Name=Allow PNRP to send from port 3540|', 'HomeGroup Block In': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|Name=Block homegroup incoming|', 'HomeGroup Block Out': 'V2.0|Action=Block|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupProvider|Name=Block homegroup outgoing|', 'HomeGroup Listener Block In': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupListener|Name=Block all incoming|', 'HomeGroup Listener Block Out': 'V2.0|Action=Block|Dir=Out|App=%SystemRoot%\\system32\\svchost.exe|Svc=HomeGroupListener|Name=Block all outgoing|', 'SettingSyncHost': 'V2.0|Action=Block|Dir=In|App=%SystemRoot%\\system32\\settingsynchost.exe|Name=Block IP traffic to SettingSyncHost|'}}}}`  
<br></br>
#### SNMPTRAP
  
Description : `@firewallapi.dll,-50324`  
DisplayName : `@firewallapi.dll,-50323`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
FailureActions : `ff ff ff ff 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 60 ea 00 00 00 00 00 00 00 00 00 00`  
ImagePath : `%SystemRoot%\System32\snmptrap.exe`  
ObjectName : `NT AUTHORITY\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`
#### stisvc
  
DependOnService : `RpcSs`  
Description : `@%SystemRoot%\system32\wiaservc.dll,-10`  
DisplayName : `@%SystemRoot%\system32\wiaservc.dll,-9`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
ImagePath : `%SystemRoot%\system32\svchost.exe -k imgsvc`  
ObjectName : `NT Authority\LocalService`  
RequiredPrivileges : `['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege']`  
ServiceSidType: `SERVICE_SID_TYPE_UNRESTRICTED`  
Start : `SERVICE_DEMAND_START`  
Type : `SERVICE_WIN32_OWN_PROCESS`


##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wiaservc.dll`  
<br></br>  
Security : `01 00 14 80 a0 00 00 00 ac 00 00 00 14 00 00 00 30 00 00 00 02 00 1c 00 01 00 00 00 02 80 14 00 ff 01 0f 00 01 01 00 00 00 00 00 01 00 00 00 00 02 00 70 00 05 00 00 00 00 00 14 00 fd 01 02 00 01 01 00 00 00 00 00 05 12 00 00 00 00 00 18 00 ff 01 0f 00 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 8d 01 02 00 01 01 00 00 00 00 00 05 06 00 00 00 00 00 14 00 00 01 00 00 01 01 00 00 00 00 00 05 0b 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00`
#### Synth3dVsc
  
ImagePath : `\SystemRoot\System32\drivers\Synth3dVsc.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_DEMAND_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Video Init`  
Tag : `0x01`  
Owners : `77 00 73 00 79 00 6e 00 74 00 68 00 33 00 64 00 76 00 73 00 63 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### TapiSrv
  
Performance : `{'ObjectList': '1150'}`
#### Telemetry
  
ImagePath : `System32\drivers\IntelTA.sys`  
Type : `SERVICE_KERNEL_DRIVER`  
Start : `SERVICE_BOOT_START`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `Core Security Extensions`  
Tag : `0x02`  
DisplayName : `@intelta.inf,%Telemetry.SVCDESC%;Intel(R) Telemetry Service`  
Owners : `69 00 6e 00 74 00 65 00 6c 00 74 00 61 00 2e 00 69 00 6e 00 66 00 00 00 00 00`
#### wcnfs
  
DependOnService : `FltMgr`  
Description : `@%systemroot%\system32\drivers\wcnfs.sys,-101`  
DisplayName : `@%systemroot%\system32\drivers\wcnfs.sys,-100`  
ErrorControl : `SERVICE_ERROR_NORMAL`  
Group : `FSFilter Top`  
ImagePath : `\SystemRoot\system32\drivers\wcnfs.sys`  
Start : `SERVICE_DEMAND_START`  
SupportedFeatures : `0x07`  
Type : `SERVICE_FILE_SYSTEM_DRIVER`  
Instances : `{'DefaultInstance': 'wcnfs Instance', 'wcnfs Instance': {'Altitude': '409900', 'Flags': 0}}`


##### Service Parameters
  
DebugOptions : `0x00`  
<br></br>  
<br></br>  

</details>
