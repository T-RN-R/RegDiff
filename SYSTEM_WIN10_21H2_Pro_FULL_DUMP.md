
Win10 (21H2 19044.1706)
=======================

Table of contents
=================

* [Full Dump](#full-dump)
	* [SYSTEM](#system)
		* [WMI AutoLoggers](#wmi-autologgers)
			* [Cellcore](#cellcore)
			* [Circular Kernel Context Logger](#circular-kernel-context-logger)
			* [CloudExperienceHostOobe](#cloudexperiencehostoobe)
			* [DataMarket](#datamarket)
			* [DefenderApiLogger](#defenderapilogger)
			* [DefenderAuditLogger](#defenderauditlogger)
			* [DiagLog](#diaglog)
			* [Diagtrack-Listener](#diagtrack-listener)
			* [EventLog-Application](#eventlog-application)
			* [EventLog-Security](#eventlog-security)
			* [EventLog-System](#eventlog-system)
			* [HolographicDevice](#holographicdevice)
			* [LwtNetLog](#lwtnetlog)
			* [Mellanox-Kernel](#mellanox-kernel)
			* [Microsoft-Windows-AssignedAccess-Trace](#microsoft-windows-assignedaccess-trace)
			* [Microsoft-Windows-Rdp-Graphics-RdpIdd-Trace](#microsoft-windows-rdp-graphics-rdpidd-trace)
			* [Microsoft-Windows-Setup](#microsoft-windows-setup)
			* [NBSMBLOGGER](#nbsmblogger)
			* [NetCore](#netcore)
			* [NtfsLog](#ntfslog)
			* [PEAuthLog](#peauthlog)
			* [RadioMgr](#radiomgr)
			* [RdrLog](#rdrlog)
			* [ReadyBoot](#readyboot)
			* [SetupPlatform](#setupplatform)
			* [SetupPlatformTel](#setupplatformtel)
			* [SpoolerLogger](#spoolerlogger)
			* [SQMLogger](#sqmlogger)
			* [TCPIPLOGGER](#tcpiplogger)
			* [TileStore](#tilestore)
			* [Tpm](#tpm)
			* [UBPM](#ubpm)
			* [WdiContextLog](#wdicontextlog)
			* [WFP-IPsec Trace](#wfp-ipsec-trace)
			* [WiFiDriverIHVSession](#wifidriverihvsession)
			* [WiFiDriverIHVSessionRepro](#wifidriverihvsessionrepro)
			* [WiFiSession](#wifisession)
			* [WinPhoneCritical](#winphonecritical)
		* [<span style="text-align: center; font-size:2em;">Services </span>](#span-styletext-align-center-font-size2emservices-span)
			* [<span style="text-align: center; font-size:2em;">.NET CLR Data Service </span>](#span-styletext-align-center-font-size2emnet-clr-data-service-span)
			* [<span style="text-align: center; font-size:2em;">.NET CLR Networking Service </span>](#span-styletext-align-center-font-size2emnet-clr-networking-service-span)
			* [<span style="text-align: center; font-size:2em;">.NET CLR Networking 4.0.0.0 Service </span>](#span-styletext-align-center-font-size2emnet-clr-networking-4000-service-span)
			* [<span style="text-align: center; font-size:2em;">.NET Data Provider for Oracle Service </span>](#span-styletext-align-center-font-size2emnet-data-provider-for-oracle-service-span)
			* [<span style="text-align: center; font-size:2em;">.NET Data Provider for SqlServer Service </span>](#span-styletext-align-center-font-size2emnet-data-provider-for-sqlserver-service-span)
			* [<span style="text-align: center; font-size:2em;">.NET Memory Cache 4.0 Service </span>](#span-styletext-align-center-font-size2emnet-memory-cache-40-service-span)
			* [<span style="text-align: center; font-size:2em;">.NETFramework Service </span>](#span-styletext-align-center-font-size2emnetframework-service-span)
			* [<span style="text-align: center; font-size:2em;">1394ohci Service </span>](#span-styletext-align-center-font-size2em1394ohci-service-span)
			* [<span style="text-align: center; font-size:2em;">3ware Service </span>](#span-styletext-align-center-font-size2em3ware-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">AarSvc Service </span>](#span-styletext-align-center-font-size2emaarsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">ACPI Service </span>](#span-styletext-align-center-font-size2emacpi-service-span)
			* [<span style="text-align: center; font-size:2em;">AcpiDev Service </span>](#span-styletext-align-center-font-size2emacpidev-service-span)
			* [<span style="text-align: center; font-size:2em;">acpiex Service </span>](#span-styletext-align-center-font-size2emacpiex-service-span)
			* [<span style="text-align: center; font-size:2em;">acpipagr Service </span>](#span-styletext-align-center-font-size2emacpipagr-service-span)
			* [<span style="text-align: center; font-size:2em;">AcpiPmi Service </span>](#span-styletext-align-center-font-size2emacpipmi-service-span)
			* [<span style="text-align: center; font-size:2em;">acpitime Service </span>](#span-styletext-align-center-font-size2emacpitime-service-span)
			* [<span style="text-align: center; font-size:2em;">Acx01000 Service </span>](#span-styletext-align-center-font-size2emacx01000-service-span)
			* [<span style="text-align: center; font-size:2em;">ADOVMPPackage Service </span>](#span-styletext-align-center-font-size2emadovmppackage-service-span)
			* [<span style="text-align: center; font-size:2em;">ADP80XX Service </span>](#span-styletext-align-center-font-size2emadp80xx-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">adsi Service </span>](#span-styletext-align-center-font-size2emadsi-service-span)
			* [<span style="text-align: center; font-size:2em;">AFD Service </span>](#span-styletext-align-center-font-size2emafd-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">afunix Service </span>](#span-styletext-align-center-font-size2emafunix-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">ahcache Service </span>](#span-styletext-align-center-font-size2emahcache-service-span)
			* [<span style="text-align: center; font-size:2em;">AJRouter Service </span>](#span-styletext-align-center-font-size2emajrouter-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">ALG Service </span>](#span-styletext-align-center-font-size2emalg-service-span)
			* [<span style="text-align: center; font-size:2em;">amdgpio2 Service </span>](#span-styletext-align-center-font-size2emamdgpio2-service-span)
			* [<span style="text-align: center; font-size:2em;">amdi2c Service </span>](#span-styletext-align-center-font-size2emamdi2c-service-span)
			* [<span style="text-align: center; font-size:2em;">AmdK8 Service </span>](#span-styletext-align-center-font-size2emamdk8-service-span)
			* [<span style="text-align: center; font-size:2em;">AmdPPM Service </span>](#span-styletext-align-center-font-size2emamdppm-service-span)
			* [<span style="text-align: center; font-size:2em;">amdsata Service </span>](#span-styletext-align-center-font-size2emamdsata-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">amdsbs Service </span>](#span-styletext-align-center-font-size2emamdsbs-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">amdxata Service </span>](#span-styletext-align-center-font-size2emamdxata-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">AppID Service </span>](#span-styletext-align-center-font-size2emappid-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">AppIDSvc Service </span>](#span-styletext-align-center-font-size2emappidsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">Appinfo Service </span>](#span-styletext-align-center-font-size2emappinfo-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">applockerfltr Service </span>](#span-styletext-align-center-font-size2emapplockerfltr-service-span)
			* [<span style="text-align: center; font-size:2em;">AppMgmt Service </span>](#span-styletext-align-center-font-size2emappmgmt-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">AppReadiness Service </span>](#span-styletext-align-center-font-size2emappreadiness-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">AppVClient Service </span>](#span-styletext-align-center-font-size2emappvclient-service-span)
			* [<span style="text-align: center; font-size:2em;">AppvStrm Service </span>](#span-styletext-align-center-font-size2emappvstrm-service-span)
			* [<span style="text-align: center; font-size:2em;">AppvVemgr Service </span>](#span-styletext-align-center-font-size2emappvvemgr-service-span)
			* [<span style="text-align: center; font-size:2em;">AppvVfs Service </span>](#span-styletext-align-center-font-size2emappvvfs-service-span)
			* [<span style="text-align: center; font-size:2em;">AppXSvc Service </span>](#span-styletext-align-center-font-size2emappxsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">arcsas Service </span>](#span-styletext-align-center-font-size2emarcsas-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">AssignedAccessManagerSvc Service </span>](#span-styletext-align-center-font-size2emassignedaccessmanagersvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">AsyncMac Service </span>](#span-styletext-align-center-font-size2emasyncmac-service-span)
			* [<span style="text-align: center; font-size:2em;">atapi Service </span>](#span-styletext-align-center-font-size2ematapi-service-span)
			* [<span style="text-align: center; font-size:2em;">AudioEndpointBuilder Service </span>](#span-styletext-align-center-font-size2emaudioendpointbuilder-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Audiosrv Service </span>](#span-styletext-align-center-font-size2emaudiosrv-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">autotimesvc Service </span>](#span-styletext-align-center-font-size2emautotimesvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">AxInstSV Service </span>](#span-styletext-align-center-font-size2emaxinstsv-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">b06bdrv Service </span>](#span-styletext-align-center-font-size2emb06bdrv-service-span)
			* [<span style="text-align: center; font-size:2em;">bam Service </span>](#span-styletext-align-center-font-size2embam-service-span)
			* [<span style="text-align: center; font-size:2em;">BasicDisplay Service </span>](#span-styletext-align-center-font-size2embasicdisplay-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">BasicRender Service </span>](#span-styletext-align-center-font-size2embasicrender-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">BattC Service </span>](#span-styletext-align-center-font-size2embattc-service-span)
			* [<span style="text-align: center; font-size:2em;">BcastDVRUserService Service </span>](#span-styletext-align-center-font-size2embcastdvruserservice-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">bcmfn2 Service </span>](#span-styletext-align-center-font-size2embcmfn2-service-span)
			* [<span style="text-align: center; font-size:2em;">BDESVC Service </span>](#span-styletext-align-center-font-size2embdesvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">Beep Service </span>](#span-styletext-align-center-font-size2embeep-service-span)
			* [<span style="text-align: center; font-size:2em;">BFE Service </span>](#span-styletext-align-center-font-size2embfe-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">bindflt Service </span>](#span-styletext-align-center-font-size2embindflt-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">BITS Service </span>](#span-styletext-align-center-font-size2embits-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">BluetoothUserService Service </span>](#span-styletext-align-center-font-size2embluetoothuserservice-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">bowser Service </span>](#span-styletext-align-center-font-size2embowser-service-span)
			* [<span style="text-align: center; font-size:2em;">BrokerInfrastructure Service </span>](#span-styletext-align-center-font-size2embrokerinfrastructure-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Browser Service </span>](#span-styletext-align-center-font-size2embrowser-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">BTAGService Service </span>](#span-styletext-align-center-font-size2embtagservice-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">BthA2dp Service </span>](#span-styletext-align-center-font-size2embtha2dp-service-span)
			* [<span style="text-align: center; font-size:2em;">BthAvctpSvc Service </span>](#span-styletext-align-center-font-size2embthavctpsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">BthEnum Service </span>](#span-styletext-align-center-font-size2embthenum-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">BthHFEnum Service </span>](#span-styletext-align-center-font-size2embthhfenum-service-span)
			* [<span style="text-align: center; font-size:2em;">BthLEEnum Service </span>](#span-styletext-align-center-font-size2embthleenum-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">BthMini Service </span>](#span-styletext-align-center-font-size2embthmini-service-span)
			* [<span style="text-align: center; font-size:2em;">BTHMODEM Service </span>](#span-styletext-align-center-font-size2embthmodem-service-span)
			* [<span style="text-align: center; font-size:2em;">BTHPORT Service </span>](#span-styletext-align-center-font-size2embthport-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">bthserv Service </span>](#span-styletext-align-center-font-size2embthserv-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">BTHUSB Service </span>](#span-styletext-align-center-font-size2embthusb-service-span)
			* [<span style="text-align: center; font-size:2em;">bttflt Service </span>](#span-styletext-align-center-font-size2embttflt-service-span)
			* [<span style="text-align: center; font-size:2em;">buttonconverter Service </span>](#span-styletext-align-center-font-size2embuttonconverter-service-span)
			* [<span style="text-align: center; font-size:2em;">CAD Service </span>](#span-styletext-align-center-font-size2emcad-service-span)
			* [<span style="text-align: center; font-size:2em;">camsvc Service </span>](#span-styletext-align-center-font-size2emcamsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">CaptureService Service </span>](#span-styletext-align-center-font-size2emcaptureservice-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">cbdhsvc Service </span>](#span-styletext-align-center-font-size2emcbdhsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">cdfs Service </span>](#span-styletext-align-center-font-size2emcdfs-service-span)
			* [<span style="text-align: center; font-size:2em;">CDPSvc Service </span>](#span-styletext-align-center-font-size2emcdpsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">CDPUserSvc Service </span>](#span-styletext-align-center-font-size2emcdpusersvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">cdrom Service </span>](#span-styletext-align-center-font-size2emcdrom-service-span)
			* [<span style="text-align: center; font-size:2em;">CertPropSvc Service </span>](#span-styletext-align-center-font-size2emcertpropsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">cht4iscsi Service </span>](#span-styletext-align-center-font-size2emcht4iscsi-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">cht4vbd Service </span>](#span-styletext-align-center-font-size2emcht4vbd-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">CimFS Service </span>](#span-styletext-align-center-font-size2emcimfs-service-span)
			* [<span style="text-align: center; font-size:2em;">circlass Service </span>](#span-styletext-align-center-font-size2emcirclass-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">CldFlt Service </span>](#span-styletext-align-center-font-size2emcldflt-service-span)
			* [<span style="text-align: center; font-size:2em;">CLFS Service </span>](#span-styletext-align-center-font-size2emclfs-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">ClipSVC Service </span>](#span-styletext-align-center-font-size2emclipsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">cloudidsvc Service </span>](#span-styletext-align-center-font-size2emcloudidsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">clr_optimization_v4.0.30319_32 Service </span>](#span-styletext-align-center-font-size2emclr_optimization_v4030319_32-service-span)
			* [<span style="text-align: center; font-size:2em;">clr_optimization_v4.0.30319_64 Service </span>](#span-styletext-align-center-font-size2emclr_optimization_v4030319_64-service-span)
			* [<span style="text-align: center; font-size:2em;">CmBatt Service </span>](#span-styletext-align-center-font-size2emcmbatt-service-span)
			* [<span style="text-align: center; font-size:2em;">CNG Service </span>](#span-styletext-align-center-font-size2emcng-service-span)
			* [<span style="text-align: center; font-size:2em;">cnghwassist Service </span>](#span-styletext-align-center-font-size2emcnghwassist-service-span)
			* [<span style="text-align: center; font-size:2em;">CompositeBus Service </span>](#span-styletext-align-center-font-size2emcompositebus-service-span)
			* [<span style="text-align: center; font-size:2em;">COMSysApp Service </span>](#span-styletext-align-center-font-size2emcomsysapp-service-span)
			* [<span style="text-align: center; font-size:2em;">condrv Service </span>](#span-styletext-align-center-font-size2emcondrv-service-span)
			* [<span style="text-align: center; font-size:2em;">ConsentUxUserSvc Service </span>](#span-styletext-align-center-font-size2emconsentuxusersvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">CoreMessagingRegistrar Service </span>](#span-styletext-align-center-font-size2emcoremessagingregistrar-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">CoreUI Service </span>](#span-styletext-align-center-font-size2emcoreui-service-span)
			* [<span style="text-align: center; font-size:2em;">CredentialEnrollmentManagerUserSvc Service </span>](#span-styletext-align-center-font-size2emcredentialenrollmentmanagerusersvc-service-span)
			* [<span style="text-align: center; font-size:2em;">CryptSvc Service </span>](#span-styletext-align-center-font-size2emcryptsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">CSC Service </span>](#span-styletext-align-center-font-size2emcsc-service-span)
			* [<span style="text-align: center; font-size:2em;">CscService Service </span>](#span-styletext-align-center-font-size2emcscservice-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">dam Service </span>](#span-styletext-align-center-font-size2emdam-service-span)
			* [<span style="text-align: center; font-size:2em;">DCLocator Service </span>](#span-styletext-align-center-font-size2emdclocator-service-span)
			* [<span style="text-align: center; font-size:2em;">DcomLaunch Service </span>](#span-styletext-align-center-font-size2emdcomlaunch-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">defragsvc Service </span>](#span-styletext-align-center-font-size2emdefragsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">DeviceAssociationBrokerSvc Service </span>](#span-styletext-align-center-font-size2emdeviceassociationbrokersvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">DeviceAssociationService Service </span>](#span-styletext-align-center-font-size2emdeviceassociationservice-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">DeviceInstall Service </span>](#span-styletext-align-center-font-size2emdeviceinstall-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">DevicePickerUserSvc Service </span>](#span-styletext-align-center-font-size2emdevicepickerusersvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">DevicesFlowUserSvc Service </span>](#span-styletext-align-center-font-size2emdevicesflowusersvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">DevQueryBroker Service </span>](#span-styletext-align-center-font-size2emdevquerybroker-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">Dfsc Service </span>](#span-styletext-align-center-font-size2emdfsc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Dhcp Service </span>](#span-styletext-align-center-font-size2emdhcp-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">diagnosticshub.standardcollector.service Service </span>](#span-styletext-align-center-font-size2emdiagnosticshubstandardcollectorservice-service-span)
			* [<span style="text-align: center; font-size:2em;">diagsvc Service </span>](#span-styletext-align-center-font-size2emdiagsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">DiagTrack Service </span>](#span-styletext-align-center-font-size2emdiagtrack-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">DialogBlockingService Service </span>](#span-styletext-align-center-font-size2emdialogblockingservice-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">disk Service </span>](#span-styletext-align-center-font-size2emdisk-service-span)
			* [<span style="text-align: center; font-size:2em;">DispBrokerDesktopSvc Service </span>](#span-styletext-align-center-font-size2emdispbrokerdesktopsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">DisplayEnhancementService Service </span>](#span-styletext-align-center-font-size2emdisplayenhancementservice-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">DmEnrollmentSvc Service </span>](#span-styletext-align-center-font-size2emdmenrollmentsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">dmvsc Service </span>](#span-styletext-align-center-font-size2emdmvsc-service-span)
			* [<span style="text-align: center; font-size:2em;">dmwappushservice Service </span>](#span-styletext-align-center-font-size2emdmwappushservice-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">Dnscache Service </span>](#span-styletext-align-center-font-size2emdnscache-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">DoSvc Service </span>](#span-styletext-align-center-font-size2emdosvc-service-span)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">dot3svc Service </span>](#span-styletext-align-center-font-size2emdot3svc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">DPS Service </span>](#span-styletext-align-center-font-size2emdps-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">drmkaud Service </span>](#span-styletext-align-center-font-size2emdrmkaud-service-span)
			* [<span style="text-align: center; font-size:2em;">DsmSvc Service </span>](#span-styletext-align-center-font-size2emdsmsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">DsSvc Service </span>](#span-styletext-align-center-font-size2emdssvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">DusmSvc Service </span>](#span-styletext-align-center-font-size2emdusmsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">DXGKrnl Service </span>](#span-styletext-align-center-font-size2emdxgkrnl-service-span)
			* [<span style="text-align: center; font-size:2em;">Eaphost Service </span>](#span-styletext-align-center-font-size2emeaphost-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">ebdrv Service </span>](#span-styletext-align-center-font-size2emebdrv-service-span)
			* [<span style="text-align: center; font-size:2em;">edgeupdate Service </span>](#span-styletext-align-center-font-size2emedgeupdate-service-span)
			* [<span style="text-align: center; font-size:2em;">edgeupdatem Service </span>](#span-styletext-align-center-font-size2emedgeupdatem-service-span)
			* [<span style="text-align: center; font-size:2em;">EFS Service </span>](#span-styletext-align-center-font-size2emefs-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">EhStorClass Service </span>](#span-styletext-align-center-font-size2emehstorclass-service-span)
			* [<span style="text-align: center; font-size:2em;">EhStorTcgDrv Service </span>](#span-styletext-align-center-font-size2emehstortcgdrv-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">embeddedmode Service </span>](#span-styletext-align-center-font-size2emembeddedmode-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">EntAppSvc Service </span>](#span-styletext-align-center-font-size2ementappsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">ErrDev Service </span>](#span-styletext-align-center-font-size2emerrdev-service-span)
			* [<span style="text-align: center; font-size:2em;">ESENT Service </span>](#span-styletext-align-center-font-size2emesent-service-span)
			* [<span style="text-align: center; font-size:2em;">EventLog Service </span>](#span-styletext-align-center-font-size2emeventlog-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">EventSystem Service </span>](#span-styletext-align-center-font-size2emeventsystem-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">exfat Service </span>](#span-styletext-align-center-font-size2emexfat-service-span)
			* [<span style="text-align: center; font-size:2em;">fastfat Service </span>](#span-styletext-align-center-font-size2emfastfat-service-span)
			* [<span style="text-align: center; font-size:2em;">Fax Service </span>](#span-styletext-align-center-font-size2emfax-service-span)
			* [<span style="text-align: center; font-size:2em;">fdc Service </span>](#span-styletext-align-center-font-size2emfdc-service-span)
			* [<span style="text-align: center; font-size:2em;">fdPHost Service </span>](#span-styletext-align-center-font-size2emfdphost-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">FDResPub Service </span>](#span-styletext-align-center-font-size2emfdrespub-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">fhsvc Service </span>](#span-styletext-align-center-font-size2emfhsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">FileCrypt Service </span>](#span-styletext-align-center-font-size2emfilecrypt-service-span)
			* [<span style="text-align: center; font-size:2em;">FileInfo Service </span>](#span-styletext-align-center-font-size2emfileinfo-service-span)
			* [<span style="text-align: center; font-size:2em;">Filetrace Service </span>](#span-styletext-align-center-font-size2emfiletrace-service-span)
			* [<span style="text-align: center; font-size:2em;">flpydisk Service </span>](#span-styletext-align-center-font-size2emflpydisk-service-span)
			* [<span style="text-align: center; font-size:2em;">FltMgr Service </span>](#span-styletext-align-center-font-size2emfltmgr-service-span)
			* [<span style="text-align: center; font-size:2em;">FontCache Service </span>](#span-styletext-align-center-font-size2emfontcache-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">FrameServer Service </span>](#span-styletext-align-center-font-size2emframeserver-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">FsDepends Service </span>](#span-styletext-align-center-font-size2emfsdepends-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Fs_Rec Service </span>](#span-styletext-align-center-font-size2emfs_rec-service-span)
			* [<span style="text-align: center; font-size:2em;">fvevol Service </span>](#span-styletext-align-center-font-size2emfvevol-service-span)
			* [<span style="text-align: center; font-size:2em;">gencounter Service </span>](#span-styletext-align-center-font-size2emgencounter-service-span)
			* [<span style="text-align: center; font-size:2em;">genericusbfn Service </span>](#span-styletext-align-center-font-size2emgenericusbfn-service-span)
			* [<span style="text-align: center; font-size:2em;">GPIOClx0101 Service </span>](#span-styletext-align-center-font-size2emgpioclx0101-service-span)
			* [<span style="text-align: center; font-size:2em;">gpsvc Service </span>](#span-styletext-align-center-font-size2emgpsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">GpuEnergyDrv Service </span>](#span-styletext-align-center-font-size2emgpuenergydrv-service-span)
			* [<span style="text-align: center; font-size:2em;">GraphicsPerfSvc Service </span>](#span-styletext-align-center-font-size2emgraphicsperfsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">HdAudAddService Service </span>](#span-styletext-align-center-font-size2emhdaudaddservice-service-span)
			* [<span style="text-align: center; font-size:2em;">HDAudBus Service </span>](#span-styletext-align-center-font-size2emhdaudbus-service-span)
			* [<span style="text-align: center; font-size:2em;">HidBatt Service </span>](#span-styletext-align-center-font-size2emhidbatt-service-span)
			* [<span style="text-align: center; font-size:2em;">HidBth Service </span>](#span-styletext-align-center-font-size2emhidbth-service-span)
			* [<span style="text-align: center; font-size:2em;">hidi2c Service </span>](#span-styletext-align-center-font-size2emhidi2c-service-span)
			* [<span style="text-align: center; font-size:2em;">hidinterrupt Service </span>](#span-styletext-align-center-font-size2emhidinterrupt-service-span)
			* [<span style="text-align: center; font-size:2em;">HidIr Service </span>](#span-styletext-align-center-font-size2emhidir-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">hidserv Service </span>](#span-styletext-align-center-font-size2emhidserv-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">hidspi Service </span>](#span-styletext-align-center-font-size2emhidspi-service-span)
			* [<span style="text-align: center; font-size:2em;">HidUsb Service </span>](#span-styletext-align-center-font-size2emhidusb-service-span)
			* [<span style="text-align: center; font-size:2em;">HomeGroupListener Service </span>](#span-styletext-align-center-font-size2emhomegrouplistener-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">HomeGroupProvider Service </span>](#span-styletext-align-center-font-size2emhomegroupprovider-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">HpSAMD Service </span>](#span-styletext-align-center-font-size2emhpsamd-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">HTTP Service </span>](#span-styletext-align-center-font-size2emhttp-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">hvcrash Service </span>](#span-styletext-align-center-font-size2emhvcrash-service-span)
			* [<span style="text-align: center; font-size:2em;">HvHost Service </span>](#span-styletext-align-center-font-size2emhvhost-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">hvservice Service </span>](#span-styletext-align-center-font-size2emhvservice-service-span)
			* [<span style="text-align: center; font-size:2em;">HwNClx0101 Service </span>](#span-styletext-align-center-font-size2emhwnclx0101-service-span)
			* [<span style="text-align: center; font-size:2em;">hwpolicy Service </span>](#span-styletext-align-center-font-size2emhwpolicy-service-span)
			* [<span style="text-align: center; font-size:2em;">hyperkbd Service </span>](#span-styletext-align-center-font-size2emhyperkbd-service-span)
			* [<span style="text-align: center; font-size:2em;">HyperVideo Service </span>](#span-styletext-align-center-font-size2emhypervideo-service-span)
			* [<span style="text-align: center; font-size:2em;">i8042prt Service </span>](#span-styletext-align-center-font-size2emi8042prt-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">iagpio Service </span>](#span-styletext-align-center-font-size2emiagpio-service-span)
			* [<span style="text-align: center; font-size:2em;">iai2c Service </span>](#span-styletext-align-center-font-size2emiai2c-service-span)
			* [<span style="text-align: center; font-size:2em;">iaLPSS2i_GPIO2 Service </span>](#span-styletext-align-center-font-size2emialpss2i_gpio2-service-span)
			* [<span style="text-align: center; font-size:2em;">iaLPSS2i_GPIO2_BXT_P Service </span>](#span-styletext-align-center-font-size2emialpss2i_gpio2_bxt_p-service-span)
			* [<span style="text-align: center; font-size:2em;">iaLPSS2i_GPIO2_CNL Service </span>](#span-styletext-align-center-font-size2emialpss2i_gpio2_cnl-service-span)
			* [<span style="text-align: center; font-size:2em;">iaLPSS2i_GPIO2_GLK Service </span>](#span-styletext-align-center-font-size2emialpss2i_gpio2_glk-service-span)
			* [<span style="text-align: center; font-size:2em;">iaLPSS2i_I2C Service </span>](#span-styletext-align-center-font-size2emialpss2i_i2c-service-span)
			* [<span style="text-align: center; font-size:2em;">iaLPSS2i_I2C_BXT_P Service </span>](#span-styletext-align-center-font-size2emialpss2i_i2c_bxt_p-service-span)
			* [<span style="text-align: center; font-size:2em;">iaLPSS2i_I2C_CNL Service </span>](#span-styletext-align-center-font-size2emialpss2i_i2c_cnl-service-span)
			* [<span style="text-align: center; font-size:2em;">iaLPSS2i_I2C_GLK Service </span>](#span-styletext-align-center-font-size2emialpss2i_i2c_glk-service-span)
			* [<span style="text-align: center; font-size:2em;">iaLPSSi_GPIO Service </span>](#span-styletext-align-center-font-size2emialpssi_gpio-service-span)
			* [<span style="text-align: center; font-size:2em;">iaLPSSi_I2C Service </span>](#span-styletext-align-center-font-size2emialpssi_i2c-service-span)
			* [<span style="text-align: center; font-size:2em;">iaStorAV Service </span>](#span-styletext-align-center-font-size2emiastorav-service-span)
			* [<span style="text-align: center; font-size:2em;">iaStorAVC Service </span>](#span-styletext-align-center-font-size2emiastoravc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">iaStorV Service </span>](#span-styletext-align-center-font-size2emiastorv-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">ibbus Service </span>](#span-styletext-align-center-font-size2emibbus-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">icssvc Service </span>](#span-styletext-align-center-font-size2emicssvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">IKEEXT Service </span>](#span-styletext-align-center-font-size2emikeext-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">IndirectKmd Service </span>](#span-styletext-align-center-font-size2emindirectkmd-service-span)
			* [<span style="text-align: center; font-size:2em;">inetaccs Service </span>](#span-styletext-align-center-font-size2eminetaccs-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">InstallService Service </span>](#span-styletext-align-center-font-size2eminstallservice-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">intelide Service </span>](#span-styletext-align-center-font-size2emintelide-service-span)
			* [<span style="text-align: center; font-size:2em;">intelpep Service </span>](#span-styletext-align-center-font-size2emintelpep-service-span)
			* [<span style="text-align: center; font-size:2em;">intelpmax Service </span>](#span-styletext-align-center-font-size2emintelpmax-service-span)
			* [<span style="text-align: center; font-size:2em;">intelppm Service </span>](#span-styletext-align-center-font-size2emintelppm-service-span)
			* [<span style="text-align: center; font-size:2em;">iorate Service </span>](#span-styletext-align-center-font-size2emiorate-service-span)
			* [<span style="text-align: center; font-size:2em;">IpFilterDriver Service </span>](#span-styletext-align-center-font-size2emipfilterdriver-service-span)
			* [<span style="text-align: center; font-size:2em;">iphlpsvc Service </span>](#span-styletext-align-center-font-size2emiphlpsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">IPMIDRV Service </span>](#span-styletext-align-center-font-size2emipmidrv-service-span)
			* [<span style="text-align: center; font-size:2em;">IPNAT Service </span>](#span-styletext-align-center-font-size2emipnat-service-span)
			* [<span style="text-align: center; font-size:2em;">IPT Service </span>](#span-styletext-align-center-font-size2emipt-service-span)
			* [<span style="text-align: center; font-size:2em;">IpxlatCfgSvc Service </span>](#span-styletext-align-center-font-size2emipxlatcfgsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">isapnp Service </span>](#span-styletext-align-center-font-size2emisapnp-service-span)
			* [<span style="text-align: center; font-size:2em;">iScsiPrt Service </span>](#span-styletext-align-center-font-size2emiscsiprt-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">ItSas35i Service </span>](#span-styletext-align-center-font-size2emitsas35i-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">kbdclass Service </span>](#span-styletext-align-center-font-size2emkbdclass-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">kbdhid Service </span>](#span-styletext-align-center-font-size2emkbdhid-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">kbldfltr Service </span>](#span-styletext-align-center-font-size2emkbldfltr-service-span)
			* [<span style="text-align: center; font-size:2em;">kdnic Service </span>](#span-styletext-align-center-font-size2emkdnic-service-span)
			* [<span style="text-align: center; font-size:2em;">KeyIso Service </span>](#span-styletext-align-center-font-size2emkeyiso-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">KSecDD Service </span>](#span-styletext-align-center-font-size2emksecdd-service-span)
			* [<span style="text-align: center; font-size:2em;">KSecPkg Service </span>](#span-styletext-align-center-font-size2emksecpkg-service-span)
			* [<span style="text-align: center; font-size:2em;">ksthunk Service </span>](#span-styletext-align-center-font-size2emksthunk-service-span)
			* [<span style="text-align: center; font-size:2em;">KtmRm Service </span>](#span-styletext-align-center-font-size2emktmrm-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">LanmanServer Service </span>](#span-styletext-align-center-font-size2emlanmanserver-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">LanmanWorkstation Service </span>](#span-styletext-align-center-font-size2emlanmanworkstation-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">ldap Service </span>](#span-styletext-align-center-font-size2emldap-service-span)
			* [<span style="text-align: center; font-size:2em;">lfsvc Service </span>](#span-styletext-align-center-font-size2emlfsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">LicenseManager Service </span>](#span-styletext-align-center-font-size2emlicensemanager-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">lltdio Service </span>](#span-styletext-align-center-font-size2emlltdio-service-span)
			* [<span style="text-align: center; font-size:2em;">lltdsvc Service </span>](#span-styletext-align-center-font-size2emlltdsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">lmhosts Service </span>](#span-styletext-align-center-font-size2emlmhosts-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">Lsa Service </span>](#span-styletext-align-center-font-size2emlsa-service-span)
			* [<span style="text-align: center; font-size:2em;">LSI_SAS Service </span>](#span-styletext-align-center-font-size2emlsi_sas-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">LSI_SAS2i Service </span>](#span-styletext-align-center-font-size2emlsi_sas2i-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">LSI_SAS3i Service </span>](#span-styletext-align-center-font-size2emlsi_sas3i-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">LSI_SSS Service </span>](#span-styletext-align-center-font-size2emlsi_sss-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">LSM Service </span>](#span-styletext-align-center-font-size2emlsm-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">luafv Service </span>](#span-styletext-align-center-font-size2emluafv-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">LxpSvc Service </span>](#span-styletext-align-center-font-size2emlxpsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">MapsBroker Service </span>](#span-styletext-align-center-font-size2emmapsbroker-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">mausbhost Service </span>](#span-styletext-align-center-font-size2emmausbhost-service-span)
			* [<span style="text-align: center; font-size:2em;">mausbip Service </span>](#span-styletext-align-center-font-size2emmausbip-service-span)
			* [<span style="text-align: center; font-size:2em;">MbbCx Service </span>](#span-styletext-align-center-font-size2emmbbcx-service-span)
			* [<span style="text-align: center; font-size:2em;">megasas Service </span>](#span-styletext-align-center-font-size2emmegasas-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">megasas2i Service </span>](#span-styletext-align-center-font-size2emmegasas2i-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">megasas35i Service </span>](#span-styletext-align-center-font-size2emmegasas35i-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">megasr Service </span>](#span-styletext-align-center-font-size2emmegasr-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">MessagingService Service </span>](#span-styletext-align-center-font-size2emmessagingservice-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">Microsoft_Bluetooth_AvrcpTransport Service </span>](#span-styletext-align-center-font-size2emmicrosoft_bluetooth_avrcptransport-service-span)
			* [<span style="text-align: center; font-size:2em;">MixedRealityOpenXRSvc Service </span>](#span-styletext-align-center-font-size2emmixedrealityopenxrsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">mlx4_bus Service </span>](#span-styletext-align-center-font-size2emmlx4_bus-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">MMCSS Service </span>](#span-styletext-align-center-font-size2emmmcss-service-span)
			* [<span style="text-align: center; font-size:2em;">Modem Service </span>](#span-styletext-align-center-font-size2emmodem-service-span)
			* [<span style="text-align: center; font-size:2em;">monitor Service </span>](#span-styletext-align-center-font-size2emmonitor-service-span)
			* [<span style="text-align: center; font-size:2em;">mouclass Service </span>](#span-styletext-align-center-font-size2emmouclass-service-span)
			* [<span style="text-align: center; font-size:2em;">mouhid Service </span>](#span-styletext-align-center-font-size2emmouhid-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">mountmgr Service </span>](#span-styletext-align-center-font-size2emmountmgr-service-span)
			* [<span style="text-align: center; font-size:2em;">mpsdrv Service </span>](#span-styletext-align-center-font-size2emmpsdrv-service-span)
			* [<span style="text-align: center; font-size:2em;">mpssvc Service </span>](#span-styletext-align-center-font-size2emmpssvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">MRxDAV Service </span>](#span-styletext-align-center-font-size2emmrxdav-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">mrxsmb Service </span>](#span-styletext-align-center-font-size2emmrxsmb-service-span)
			* [<span style="text-align: center; font-size:2em;">mrxsmb10 Service </span>](#span-styletext-align-center-font-size2emmrxsmb10-service-span)
			* [<span style="text-align: center; font-size:2em;">mrxsmb20 Service </span>](#span-styletext-align-center-font-size2emmrxsmb20-service-span)
			* [<span style="text-align: center; font-size:2em;">MsBridge Service </span>](#span-styletext-align-center-font-size2emmsbridge-service-span)
			* [<span style="text-align: center; font-size:2em;">MSDTC Service </span>](#span-styletext-align-center-font-size2emmsdtc-service-span)
			* [<span style="text-align: center; font-size:2em;">MSDTC Bridge 4.0.0.0 Service </span>](#span-styletext-align-center-font-size2emmsdtc-bridge-4000-service-span)
			* [<span style="text-align: center; font-size:2em;">Msfs Service </span>](#span-styletext-align-center-font-size2emmsfs-service-span)
			* [<span style="text-align: center; font-size:2em;">msgpiowin32 Service </span>](#span-styletext-align-center-font-size2emmsgpiowin32-service-span)
			* [<span style="text-align: center; font-size:2em;">mshidkmdf Service </span>](#span-styletext-align-center-font-size2emmshidkmdf-service-span)
			* [<span style="text-align: center; font-size:2em;">mshidumdf Service </span>](#span-styletext-align-center-font-size2emmshidumdf-service-span)
			* [<span style="text-align: center; font-size:2em;">msisadrv Service </span>](#span-styletext-align-center-font-size2emmsisadrv-service-span)
			* [<span style="text-align: center; font-size:2em;">MSiSCSI Service </span>](#span-styletext-align-center-font-size2emmsiscsi-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">msiserver Service </span>](#span-styletext-align-center-font-size2emmsiserver-service-span)
			* [<span style="text-align: center; font-size:2em;">MsKeyboardFilter Service </span>](#span-styletext-align-center-font-size2emmskeyboardfilter-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">MSKSSRV Service </span>](#span-styletext-align-center-font-size2emmskssrv-service-span)
			* [<span style="text-align: center; font-size:2em;">MsLldp Service </span>](#span-styletext-align-center-font-size2emmslldp-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">MSPCLOCK Service </span>](#span-styletext-align-center-font-size2emmspclock-service-span)
			* [<span style="text-align: center; font-size:2em;">MSPQM Service </span>](#span-styletext-align-center-font-size2emmspqm-service-span)
			* [<span style="text-align: center; font-size:2em;">MsQuic Service </span>](#span-styletext-align-center-font-size2emmsquic-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">MsRPC Service </span>](#span-styletext-align-center-font-size2emmsrpc-service-span)
			* [<span style="text-align: center; font-size:2em;">MSSCNTRS Service </span>](#span-styletext-align-center-font-size2emmsscntrs-service-span)
			* [<span style="text-align: center; font-size:2em;">MsSecFlt Service </span>](#span-styletext-align-center-font-size2emmssecflt-service-span)
			* [<span style="text-align: center; font-size:2em;">mssmbios Service </span>](#span-styletext-align-center-font-size2emmssmbios-service-span)
			* [<span style="text-align: center; font-size:2em;">MSTEE Service </span>](#span-styletext-align-center-font-size2emmstee-service-span)
			* [<span style="text-align: center; font-size:2em;">MTConfig Service </span>](#span-styletext-align-center-font-size2emmtconfig-service-span)
			* [<span style="text-align: center; font-size:2em;">Mup Service </span>](#span-styletext-align-center-font-size2emmup-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">mvumis Service </span>](#span-styletext-align-center-font-size2emmvumis-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">napagent Service </span>](#span-styletext-align-center-font-size2emnapagent-service-span)
			* [<span style="text-align: center; font-size:2em;">NativeWifiP Service </span>](#span-styletext-align-center-font-size2emnativewifip-service-span)
			* [<span style="text-align: center; font-size:2em;">NaturalAuthentication Service </span>](#span-styletext-align-center-font-size2emnaturalauthentication-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">NcaSvc Service </span>](#span-styletext-align-center-font-size2emncasvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">NcbService Service </span>](#span-styletext-align-center-font-size2emncbservice-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">NcdAutoSetup Service </span>](#span-styletext-align-center-font-size2emncdautosetup-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">ndfltr Service </span>](#span-styletext-align-center-font-size2emndfltr-service-span)
			* [<span style="text-align: center; font-size:2em;">NDIS Service </span>](#span-styletext-align-center-font-size2emndis-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">NdisCap Service </span>](#span-styletext-align-center-font-size2emndiscap-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">NdisImPlatform Service </span>](#span-styletext-align-center-font-size2emndisimplatform-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">NdisTapi Service </span>](#span-styletext-align-center-font-size2emndistapi-service-span)
			* [<span style="text-align: center; font-size:2em;">Ndisuio Service </span>](#span-styletext-align-center-font-size2emndisuio-service-span)
			* [<span style="text-align: center; font-size:2em;">NdisVirtualBus Service </span>](#span-styletext-align-center-font-size2emndisvirtualbus-service-span)
			* [<span style="text-align: center; font-size:2em;">NdisWan Service </span>](#span-styletext-align-center-font-size2emndiswan-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">ndiswanlegacy Service </span>](#span-styletext-align-center-font-size2emndiswanlegacy-service-span)
			* [<span style="text-align: center; font-size:2em;">NDKPing Service </span>](#span-styletext-align-center-font-size2emndkping-service-span)
			* [<span style="text-align: center; font-size:2em;">ndproxy Service </span>](#span-styletext-align-center-font-size2emndproxy-service-span)
			* [<span style="text-align: center; font-size:2em;">Ndu Service </span>](#span-styletext-align-center-font-size2emndu-service-span)
			* [<span style="text-align: center; font-size:2em;">NetAdapterCx Service </span>](#span-styletext-align-center-font-size2emnetadaptercx-service-span)
			* [<span style="text-align: center; font-size:2em;">NetBIOS Service </span>](#span-styletext-align-center-font-size2emnetbios-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">NetbiosSmb Service </span>](#span-styletext-align-center-font-size2emnetbiossmb-service-span)
			* [<span style="text-align: center; font-size:2em;">NetBT Service </span>](#span-styletext-align-center-font-size2emnetbt-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Netlogon Service </span>](#span-styletext-align-center-font-size2emnetlogon-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Netman Service </span>](#span-styletext-align-center-font-size2emnetman-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">netprofm Service </span>](#span-styletext-align-center-font-size2emnetprofm-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">NetSetupSvc Service </span>](#span-styletext-align-center-font-size2emnetsetupsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">NetTcpPortSharing Service </span>](#span-styletext-align-center-font-size2emnettcpportsharing-service-span)
			* [<span style="text-align: center; font-size:2em;">netvsc Service </span>](#span-styletext-align-center-font-size2emnetvsc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">NgcCtnrSvc Service </span>](#span-styletext-align-center-font-size2emngcctnrsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">NgcSvc Service </span>](#span-styletext-align-center-font-size2emngcsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">NlaSvc Service </span>](#span-styletext-align-center-font-size2emnlasvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Npfs Service </span>](#span-styletext-align-center-font-size2emnpfs-service-span)
			* [<span style="text-align: center; font-size:2em;">npsvctrig Service </span>](#span-styletext-align-center-font-size2emnpsvctrig-service-span)
			* [<span style="text-align: center; font-size:2em;">nsi Service </span>](#span-styletext-align-center-font-size2emnsi-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">nsiproxy Service </span>](#span-styletext-align-center-font-size2emnsiproxy-service-span)
			* [<span style="text-align: center; font-size:2em;">NTDS Service </span>](#span-styletext-align-center-font-size2emntds-service-span)
			* [<span style="text-align: center; font-size:2em;">Ntfs Service </span>](#span-styletext-align-center-font-size2emntfs-service-span)
			* [<span style="text-align: center; font-size:2em;">Null Service </span>](#span-styletext-align-center-font-size2emnull-service-span)
			* [<span style="text-align: center; font-size:2em;">nvdimm Service </span>](#span-styletext-align-center-font-size2emnvdimm-service-span)
			* [<span style="text-align: center; font-size:2em;">nvraid Service </span>](#span-styletext-align-center-font-size2emnvraid-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">nvstor Service </span>](#span-styletext-align-center-font-size2emnvstor-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">OneSyncSvc Service </span>](#span-styletext-align-center-font-size2emonesyncsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">p2pimsvc Service </span>](#span-styletext-align-center-font-size2emp2pimsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">p2psvc Service </span>](#span-styletext-align-center-font-size2emp2psvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Parport Service </span>](#span-styletext-align-center-font-size2emparport-service-span)
			* [<span style="text-align: center; font-size:2em;">partmgr Service </span>](#span-styletext-align-center-font-size2empartmgr-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">PcaSvc Service </span>](#span-styletext-align-center-font-size2empcasvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">pci Service </span>](#span-styletext-align-center-font-size2empci-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">pciide Service </span>](#span-styletext-align-center-font-size2empciide-service-span)
			* [<span style="text-align: center; font-size:2em;">pcmcia Service </span>](#span-styletext-align-center-font-size2empcmcia-service-span)
			* [<span style="text-align: center; font-size:2em;">pcw Service </span>](#span-styletext-align-center-font-size2empcw-service-span)
			* [<span style="text-align: center; font-size:2em;">pdc Service </span>](#span-styletext-align-center-font-size2empdc-service-span)
			* [<span style="text-align: center; font-size:2em;">PEAUTH Service </span>](#span-styletext-align-center-font-size2empeauth-service-span)
			* [<span style="text-align: center; font-size:2em;">PeerDistSvc Service </span>](#span-styletext-align-center-font-size2empeerdistsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">perceptionsimulation Service </span>](#span-styletext-align-center-font-size2emperceptionsimulation-service-span)
			* [<span style="text-align: center; font-size:2em;">percsas2i Service </span>](#span-styletext-align-center-font-size2empercsas2i-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">percsas3i Service </span>](#span-styletext-align-center-font-size2empercsas3i-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">PerfDisk Service </span>](#span-styletext-align-center-font-size2emperfdisk-service-span)
			* [<span style="text-align: center; font-size:2em;">PerfHost Service </span>](#span-styletext-align-center-font-size2emperfhost-service-span)
			* [<span style="text-align: center; font-size:2em;">PerfNet Service </span>](#span-styletext-align-center-font-size2emperfnet-service-span)
			* [<span style="text-align: center; font-size:2em;">PerfOS Service </span>](#span-styletext-align-center-font-size2emperfos-service-span)
			* [<span style="text-align: center; font-size:2em;">PerfProc Service </span>](#span-styletext-align-center-font-size2emperfproc-service-span)
			* [<span style="text-align: center; font-size:2em;">PhoneSvc Service </span>](#span-styletext-align-center-font-size2emphonesvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">PimIndexMaintenanceSvc Service </span>](#span-styletext-align-center-font-size2empimindexmaintenancesvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">PktMon Service </span>](#span-styletext-align-center-font-size2empktmon-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">pla Service </span>](#span-styletext-align-center-font-size2empla-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">PlugPlay Service </span>](#span-styletext-align-center-font-size2emplugplay-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">pmem Service </span>](#span-styletext-align-center-font-size2empmem-service-span)
			* [<span style="text-align: center; font-size:2em;">PNPMEM Service </span>](#span-styletext-align-center-font-size2empnpmem-service-span)
			* [<span style="text-align: center; font-size:2em;">PNRPAutoReg Service </span>](#span-styletext-align-center-font-size2empnrpautoreg-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">PNRPsvc Service </span>](#span-styletext-align-center-font-size2empnrpsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">PolicyAgent Service </span>](#span-styletext-align-center-font-size2empolicyagent-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">portcfg Service </span>](#span-styletext-align-center-font-size2emportcfg-service-span)
			* [<span style="text-align: center; font-size:2em;">PortProxy Service </span>](#span-styletext-align-center-font-size2emportproxy-service-span)
			* [<span style="text-align: center; font-size:2em;">Power Service </span>](#span-styletext-align-center-font-size2empower-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">PptpMiniport Service </span>](#span-styletext-align-center-font-size2empptpminiport-service-span)
			* [<span style="text-align: center; font-size:2em;">PrintWorkflowUserSvc Service </span>](#span-styletext-align-center-font-size2emprintworkflowusersvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Processor Service </span>](#span-styletext-align-center-font-size2emprocessor-service-span)
			* [<span style="text-align: center; font-size:2em;">ProfSvc Service </span>](#span-styletext-align-center-font-size2emprofsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Psched Service </span>](#span-styletext-align-center-font-size2empsched-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">PushToInstall Service </span>](#span-styletext-align-center-font-size2empushtoinstall-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">QWAVE Service </span>](#span-styletext-align-center-font-size2emqwave-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">QWAVEdrv Service </span>](#span-styletext-align-center-font-size2emqwavedrv-service-span)
			* [<span style="text-align: center; font-size:2em;">Ramdisk Service </span>](#span-styletext-align-center-font-size2emramdisk-service-span)
			* [<span style="text-align: center; font-size:2em;">RasAcd Service </span>](#span-styletext-align-center-font-size2emrasacd-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">RasAgileVpn Service </span>](#span-styletext-align-center-font-size2emrasagilevpn-service-span)
			* [<span style="text-align: center; font-size:2em;">RasAuto Service </span>](#span-styletext-align-center-font-size2emrasauto-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Rasl2tp Service </span>](#span-styletext-align-center-font-size2emrasl2tp-service-span)
			* [<span style="text-align: center; font-size:2em;">RasMan Service </span>](#span-styletext-align-center-font-size2emrasman-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">RasPppoe Service </span>](#span-styletext-align-center-font-size2emraspppoe-service-span)
			* [<span style="text-align: center; font-size:2em;">RasSstp Service </span>](#span-styletext-align-center-font-size2emrassstp-service-span)
			* [<span style="text-align: center; font-size:2em;">rdbss Service </span>](#span-styletext-align-center-font-size2emrdbss-service-span)
			* [<span style="text-align: center; font-size:2em;">rdpbus Service </span>](#span-styletext-align-center-font-size2emrdpbus-service-span)
			* [<span style="text-align: center; font-size:2em;">RDPDR Service </span>](#span-styletext-align-center-font-size2emrdpdr-service-span)
			* [<span style="text-align: center; font-size:2em;">RDPNP Service </span>](#span-styletext-align-center-font-size2emrdpnp-service-span)
			* [<span style="text-align: center; font-size:2em;">RDPUDD Service </span>](#span-styletext-align-center-font-size2emrdpudd-service-span)
			* [<span style="text-align: center; font-size:2em;">RdpVideoMiniport Service </span>](#span-styletext-align-center-font-size2emrdpvideominiport-service-span)
			* [<span style="text-align: center; font-size:2em;">rdyboost Service </span>](#span-styletext-align-center-font-size2emrdyboost-service-span)
			* [<span style="text-align: center; font-size:2em;">ReFS Service </span>](#span-styletext-align-center-font-size2emrefs-service-span)
			* [<span style="text-align: center; font-size:2em;">ReFSv1 Service </span>](#span-styletext-align-center-font-size2emrefsv1-service-span)
			* [<span style="text-align: center; font-size:2em;">RemoteAccess Service </span>](#span-styletext-align-center-font-size2emremoteaccess-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">RemoteRegistry Service </span>](#span-styletext-align-center-font-size2emremoteregistry-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">RetailDemo Service </span>](#span-styletext-align-center-font-size2emretaildemo-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">RFCOMM Service </span>](#span-styletext-align-center-font-size2emrfcomm-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">rhproxy Service </span>](#span-styletext-align-center-font-size2emrhproxy-service-span)
			* [<span style="text-align: center; font-size:2em;">RmSvc Service </span>](#span-styletext-align-center-font-size2emrmsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">RpcEptMapper Service </span>](#span-styletext-align-center-font-size2emrpceptmapper-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">RpcLocator Service </span>](#span-styletext-align-center-font-size2emrpclocator-service-span)
			* [<span style="text-align: center; font-size:2em;">RpcSs Service </span>](#span-styletext-align-center-font-size2emrpcss-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">rspndr Service </span>](#span-styletext-align-center-font-size2emrspndr-service-span)
			* [<span style="text-align: center; font-size:2em;">s3cap Service </span>](#span-styletext-align-center-font-size2ems3cap-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">SamSs Service </span>](#span-styletext-align-center-font-size2emsamss-service-span)
			* [<span style="text-align: center; font-size:2em;">sbp2port Service </span>](#span-styletext-align-center-font-size2emsbp2port-service-span)
			* [<span style="text-align: center; font-size:2em;">SCardSvr Service </span>](#span-styletext-align-center-font-size2emscardsvr-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">ScDeviceEnum Service </span>](#span-styletext-align-center-font-size2emscdeviceenum-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">scfilter Service </span>](#span-styletext-align-center-font-size2emscfilter-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Schedule Service </span>](#span-styletext-align-center-font-size2emschedule-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">scmbus Service </span>](#span-styletext-align-center-font-size2emscmbus-service-span)
			* [<span style="text-align: center; font-size:2em;">SCPolicySvc Service </span>](#span-styletext-align-center-font-size2emscpolicysvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">sdbus Service </span>](#span-styletext-align-center-font-size2emsdbus-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">SDFRd Service </span>](#span-styletext-align-center-font-size2emsdfrd-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">SDRSVC Service </span>](#span-styletext-align-center-font-size2emsdrsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">sdstor Service </span>](#span-styletext-align-center-font-size2emsdstor-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">seclogon Service </span>](#span-styletext-align-center-font-size2emseclogon-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">SecurityHealthService Service </span>](#span-styletext-align-center-font-size2emsecurityhealthservice-service-span)
			* [<span style="text-align: center; font-size:2em;">SEMgrSvc Service </span>](#span-styletext-align-center-font-size2emsemgrsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">SENS Service </span>](#span-styletext-align-center-font-size2emsens-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Sense Service </span>](#span-styletext-align-center-font-size2emsense-service-span)
			* [<span style="text-align: center; font-size:2em;">SensorDataService Service </span>](#span-styletext-align-center-font-size2emsensordataservice-service-span)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">SensorService Service </span>](#span-styletext-align-center-font-size2emsensorservice-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">SensrSvc Service </span>](#span-styletext-align-center-font-size2emsensrsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">SerCx Service </span>](#span-styletext-align-center-font-size2emsercx-service-span)
			* [<span style="text-align: center; font-size:2em;">SerCx2 Service </span>](#span-styletext-align-center-font-size2emsercx2-service-span)
			* [<span style="text-align: center; font-size:2em;">Serenum Service </span>](#span-styletext-align-center-font-size2emserenum-service-span)
			* [<span style="text-align: center; font-size:2em;">Serial Service </span>](#span-styletext-align-center-font-size2emserial-service-span)
			* [<span style="text-align: center; font-size:2em;">sermouse Service </span>](#span-styletext-align-center-font-size2emsermouse-service-span)
			* [<span style="text-align: center; font-size:2em;">SessionEnv Service </span>](#span-styletext-align-center-font-size2emsessionenv-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">sfloppy Service </span>](#span-styletext-align-center-font-size2emsfloppy-service-span)
			* [<span style="text-align: center; font-size:2em;">SgrmAgent Service </span>](#span-styletext-align-center-font-size2emsgrmagent-service-span)
			* [<span style="text-align: center; font-size:2em;">SgrmBroker Service </span>](#span-styletext-align-center-font-size2emsgrmbroker-service-span)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">SharedAccess Service </span>](#span-styletext-align-center-font-size2emsharedaccess-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">SharedRealitySvc Service </span>](#span-styletext-align-center-font-size2emsharedrealitysvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">ShellHWDetection Service </span>](#span-styletext-align-center-font-size2emshellhwdetection-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">shpamsvc Service </span>](#span-styletext-align-center-font-size2emshpamsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">SiSRaid2 Service </span>](#span-styletext-align-center-font-size2emsisraid2-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">SiSRaid4 Service </span>](#span-styletext-align-center-font-size2emsisraid4-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">SmartSAMD Service </span>](#span-styletext-align-center-font-size2emsmartsamd-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">smbdirect Service </span>](#span-styletext-align-center-font-size2emsmbdirect-service-span)
			* [<span style="text-align: center; font-size:2em;">smphost Service </span>](#span-styletext-align-center-font-size2emsmphost-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">SmsRouter Service </span>](#span-styletext-align-center-font-size2emsmsrouter-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">SMSvcHost 4.0.0.0 Service </span>](#span-styletext-align-center-font-size2emsmsvchost-4000-service-span)
			* [<span style="text-align: center; font-size:2em;">SNMPTRAP Service </span>](#span-styletext-align-center-font-size2emsnmptrap-service-span)
			* [<span style="text-align: center; font-size:2em;">spaceparser Service </span>](#span-styletext-align-center-font-size2emspaceparser-service-span)
			* [<span style="text-align: center; font-size:2em;">spaceport Service </span>](#span-styletext-align-center-font-size2emspaceport-service-span)
			* [<span style="text-align: center; font-size:2em;">SpatialGraphFilter Service </span>](#span-styletext-align-center-font-size2emspatialgraphfilter-service-span)
			* [<span style="text-align: center; font-size:2em;">SpbCx Service </span>](#span-styletext-align-center-font-size2emspbcx-service-span)
			* [<span style="text-align: center; font-size:2em;">spectrum Service </span>](#span-styletext-align-center-font-size2emspectrum-service-span)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">Spooler Service </span>](#span-styletext-align-center-font-size2emspooler-service-span)
			* [<span style="text-align: center; font-size:2em;">sppsvc Service </span>](#span-styletext-align-center-font-size2emsppsvc-service-span)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">srv2 Service </span>](#span-styletext-align-center-font-size2emsrv2-service-span)
			* [<span style="text-align: center; font-size:2em;">srvnet Service </span>](#span-styletext-align-center-font-size2emsrvnet-service-span)
			* [<span style="text-align: center; font-size:2em;">SSDPSRV Service </span>](#span-styletext-align-center-font-size2emssdpsrv-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">ssh-agent Service </span>](#span-styletext-align-center-font-size2emssh-agent-service-span)
			* [<span style="text-align: center; font-size:2em;">SstpSvc Service </span>](#span-styletext-align-center-font-size2emsstpsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">StateRepository Service </span>](#span-styletext-align-center-font-size2emstaterepository-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">stexstor Service </span>](#span-styletext-align-center-font-size2emstexstor-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">stisvc Service </span>](#span-styletext-align-center-font-size2emstisvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">storahci Service </span>](#span-styletext-align-center-font-size2emstorahci-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">storflt Service </span>](#span-styletext-align-center-font-size2emstorflt-service-span)
			* [<span style="text-align: center; font-size:2em;">stornvme Service </span>](#span-styletext-align-center-font-size2emstornvme-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">storqosflt Service </span>](#span-styletext-align-center-font-size2emstorqosflt-service-span)
			* [<span style="text-align: center; font-size:2em;">StorSvc Service </span>](#span-styletext-align-center-font-size2emstorsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">storufs Service </span>](#span-styletext-align-center-font-size2emstorufs-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">storvsc Service </span>](#span-styletext-align-center-font-size2emstorvsc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">svsvc Service </span>](#span-styletext-align-center-font-size2emsvsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">swenum Service </span>](#span-styletext-align-center-font-size2emswenum-service-span)
			* [<span style="text-align: center; font-size:2em;">swprv Service </span>](#span-styletext-align-center-font-size2emswprv-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Synth3dVsc Service </span>](#span-styletext-align-center-font-size2emsynth3dvsc-service-span)
			* [<span style="text-align: center; font-size:2em;">SysMain Service </span>](#span-styletext-align-center-font-size2emsysmain-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">SystemEventsBroker Service </span>](#span-styletext-align-center-font-size2emsystemeventsbroker-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">TabletInputService Service </span>](#span-styletext-align-center-font-size2emtabletinputservice-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">TapiSrv Service </span>](#span-styletext-align-center-font-size2emtapisrv-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Tcpip Service </span>](#span-styletext-align-center-font-size2emtcpip-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Tcpip6 Service </span>](#span-styletext-align-center-font-size2emtcpip6-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">TCPIP6TUNNEL Service </span>](#span-styletext-align-center-font-size2emtcpip6tunnel-service-span)
			* [<span style="text-align: center; font-size:2em;">tcpipreg Service </span>](#span-styletext-align-center-font-size2emtcpipreg-service-span)
			* [<span style="text-align: center; font-size:2em;">TCPIPTUNNEL Service </span>](#span-styletext-align-center-font-size2emtcpiptunnel-service-span)
			* [<span style="text-align: center; font-size:2em;">tdx Service </span>](#span-styletext-align-center-font-size2emtdx-service-span)
			* [<span style="text-align: center; font-size:2em;">Telemetry Service </span>](#span-styletext-align-center-font-size2emtelemetry-service-span)
			* [<span style="text-align: center; font-size:2em;">terminpt Service </span>](#span-styletext-align-center-font-size2emterminpt-service-span)
			* [<span style="text-align: center; font-size:2em;">TermService Service </span>](#span-styletext-align-center-font-size2emtermservice-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Themes Service </span>](#span-styletext-align-center-font-size2emthemes-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">TieringEngineService Service </span>](#span-styletext-align-center-font-size2emtieringengineservice-service-span)
			* [<span style="text-align: center; font-size:2em;">TimeBrokerSvc Service </span>](#span-styletext-align-center-font-size2emtimebrokersvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">TokenBroker Service </span>](#span-styletext-align-center-font-size2emtokenbroker-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">TPM Service </span>](#span-styletext-align-center-font-size2emtpm-service-span)
			* [<span style="text-align: center; font-size:2em;">TrkWks Service </span>](#span-styletext-align-center-font-size2emtrkwks-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">TroubleshootingSvc Service </span>](#span-styletext-align-center-font-size2emtroubleshootingsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">TrustedInstaller Service </span>](#span-styletext-align-center-font-size2emtrustedinstaller-service-span)
			* [<span style="text-align: center; font-size:2em;">TSDDD Service </span>](#span-styletext-align-center-font-size2emtsddd-service-span)
			* [<span style="text-align: center; font-size:2em;">TsUsbFlt Service </span>](#span-styletext-align-center-font-size2emtsusbflt-service-span)
			* [<span style="text-align: center; font-size:2em;">TsUsbGD Service </span>](#span-styletext-align-center-font-size2emtsusbgd-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">tsusbhub Service </span>](#span-styletext-align-center-font-size2emtsusbhub-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">tunnel Service </span>](#span-styletext-align-center-font-size2emtunnel-service-span)
			* [<span style="text-align: center; font-size:2em;">tzautoupdate Service </span>](#span-styletext-align-center-font-size2emtzautoupdate-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">UASPStor Service </span>](#span-styletext-align-center-font-size2emuaspstor-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">UcmCx0101 Service </span>](#span-styletext-align-center-font-size2emucmcx0101-service-span)
			* [<span style="text-align: center; font-size:2em;">UcmTcpciCx0101 Service </span>](#span-styletext-align-center-font-size2emucmtcpcicx0101-service-span)
			* [<span style="text-align: center; font-size:2em;">UcmUcsiAcpiClient Service </span>](#span-styletext-align-center-font-size2emucmucsiacpiclient-service-span)
			* [<span style="text-align: center; font-size:2em;">UcmUcsiCx0101 Service </span>](#span-styletext-align-center-font-size2emucmucsicx0101-service-span)
			* [<span style="text-align: center; font-size:2em;">Ucx01000 Service </span>](#span-styletext-align-center-font-size2emucx01000-service-span)
			* [<span style="text-align: center; font-size:2em;">UdeCx Service </span>](#span-styletext-align-center-font-size2emudecx-service-span)
			* [<span style="text-align: center; font-size:2em;">udfs Service </span>](#span-styletext-align-center-font-size2emudfs-service-span)
			* [<span style="text-align: center; font-size:2em;">UdkUserSvc Service </span>](#span-styletext-align-center-font-size2emudkusersvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">UEFI Service </span>](#span-styletext-align-center-font-size2emuefi-service-span)
			* [<span style="text-align: center; font-size:2em;">UevAgentDriver Service </span>](#span-styletext-align-center-font-size2emuevagentdriver-service-span)
			* [<span style="text-align: center; font-size:2em;">UevAgentService Service </span>](#span-styletext-align-center-font-size2emuevagentservice-service-span)
			* [<span style="text-align: center; font-size:2em;">Ufx01000 Service </span>](#span-styletext-align-center-font-size2emufx01000-service-span)
			* [<span style="text-align: center; font-size:2em;">UfxChipidea Service </span>](#span-styletext-align-center-font-size2emufxchipidea-service-span)
			* [<span style="text-align: center; font-size:2em;">ufxsynopsys Service </span>](#span-styletext-align-center-font-size2emufxsynopsys-service-span)
			* [<span style="text-align: center; font-size:2em;">UGatherer Service </span>](#span-styletext-align-center-font-size2emugatherer-service-span)
			* [<span style="text-align: center; font-size:2em;">UGTHRSVC Service </span>](#span-styletext-align-center-font-size2emugthrsvc-service-span)
			* [<span style="text-align: center; font-size:2em;">umbus Service </span>](#span-styletext-align-center-font-size2emumbus-service-span)
			* [<span style="text-align: center; font-size:2em;">UmPass Service </span>](#span-styletext-align-center-font-size2emumpass-service-span)
			* [<span style="text-align: center; font-size:2em;">UmRdpService Service </span>](#span-styletext-align-center-font-size2emumrdpservice-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">UnistoreSvc Service </span>](#span-styletext-align-center-font-size2emunistoresvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">upnphost Service </span>](#span-styletext-align-center-font-size2emupnphost-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">UrsChipidea Service </span>](#span-styletext-align-center-font-size2emurschipidea-service-span)
			* [<span style="text-align: center; font-size:2em;">UrsCx01000 Service </span>](#span-styletext-align-center-font-size2emurscx01000-service-span)
			* [<span style="text-align: center; font-size:2em;">UrsSynopsys Service </span>](#span-styletext-align-center-font-size2emurssynopsys-service-span)
			* [<span style="text-align: center; font-size:2em;">usbaudio Service </span>](#span-styletext-align-center-font-size2emusbaudio-service-span)
			* [<span style="text-align: center; font-size:2em;">usbaudio2 Service </span>](#span-styletext-align-center-font-size2emusbaudio2-service-span)
			* [<span style="text-align: center; font-size:2em;">usbccgp Service </span>](#span-styletext-align-center-font-size2emusbccgp-service-span)
			* [<span style="text-align: center; font-size:2em;">usbcir Service </span>](#span-styletext-align-center-font-size2emusbcir-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">usbehci Service </span>](#span-styletext-align-center-font-size2emusbehci-service-span)
			* [<span style="text-align: center; font-size:2em;">usbhub Service </span>](#span-styletext-align-center-font-size2emusbhub-service-span)
			* [<span style="text-align: center; font-size:2em;">USBHUB3 Service </span>](#span-styletext-align-center-font-size2emusbhub3-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">usbohci Service </span>](#span-styletext-align-center-font-size2emusbohci-service-span)
			* [<span style="text-align: center; font-size:2em;">usbprint Service </span>](#span-styletext-align-center-font-size2emusbprint-service-span)
			* [<span style="text-align: center; font-size:2em;">usbser Service </span>](#span-styletext-align-center-font-size2emusbser-service-span)
			* [<span style="text-align: center; font-size:2em;">USBSTOR Service </span>](#span-styletext-align-center-font-size2emusbstor-service-span)
			* [<span style="text-align: center; font-size:2em;">usbuhci Service </span>](#span-styletext-align-center-font-size2emusbuhci-service-span)
			* [<span style="text-align: center; font-size:2em;">USBXHCI Service </span>](#span-styletext-align-center-font-size2emusbxhci-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">UserDataSvc Service </span>](#span-styletext-align-center-font-size2emuserdatasvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">UserManager Service </span>](#span-styletext-align-center-font-size2emusermanager-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">UsoSvc Service </span>](#span-styletext-align-center-font-size2emusosvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">VacSvc Service </span>](#span-styletext-align-center-font-size2emvacsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">VaultSvc Service </span>](#span-styletext-align-center-font-size2emvaultsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">vdrvroot Service </span>](#span-styletext-align-center-font-size2emvdrvroot-service-span)
			* [<span style="text-align: center; font-size:2em;">vds Service </span>](#span-styletext-align-center-font-size2emvds-service-span)
			* [<span style="text-align: center; font-size:2em;">VerifierExt Service </span>](#span-styletext-align-center-font-size2emverifierext-service-span)
			* [<span style="text-align: center; font-size:2em;">vhdmp Service </span>](#span-styletext-align-center-font-size2emvhdmp-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">vhf Service </span>](#span-styletext-align-center-font-size2emvhf-service-span)
			* [<span style="text-align: center; font-size:2em;">Vid Service </span>](#span-styletext-align-center-font-size2emvid-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">VirtualRender Service </span>](#span-styletext-align-center-font-size2emvirtualrender-service-span)
			* [<span style="text-align: center; font-size:2em;">vmbus Service </span>](#span-styletext-align-center-font-size2emvmbus-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">VMBusHID Service </span>](#span-styletext-align-center-font-size2emvmbushid-service-span)
			* [<span style="text-align: center; font-size:2em;">vmgid Service </span>](#span-styletext-align-center-font-size2emvmgid-service-span)
			* [<span style="text-align: center; font-size:2em;">vmicguestinterface Service </span>](#span-styletext-align-center-font-size2emvmicguestinterface-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">vmicheartbeat Service </span>](#span-styletext-align-center-font-size2emvmicheartbeat-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">vmickvpexchange Service </span>](#span-styletext-align-center-font-size2emvmickvpexchange-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">vmicrdv Service </span>](#span-styletext-align-center-font-size2emvmicrdv-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">vmicshutdown Service </span>](#span-styletext-align-center-font-size2emvmicshutdown-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">vmictimesync Service </span>](#span-styletext-align-center-font-size2emvmictimesync-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">vmicvmsession Service </span>](#span-styletext-align-center-font-size2emvmicvmsession-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">vmicvss Service </span>](#span-styletext-align-center-font-size2emvmicvss-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">volmgr Service </span>](#span-styletext-align-center-font-size2emvolmgr-service-span)
			* [<span style="text-align: center; font-size:2em;">volmgrx Service </span>](#span-styletext-align-center-font-size2emvolmgrx-service-span)
			* [<span style="text-align: center; font-size:2em;">volsnap Service </span>](#span-styletext-align-center-font-size2emvolsnap-service-span)
			* [<span style="text-align: center; font-size:2em;">volume Service </span>](#span-styletext-align-center-font-size2emvolume-service-span)
			* [<span style="text-align: center; font-size:2em;">vpci Service </span>](#span-styletext-align-center-font-size2emvpci-service-span)
			* [<span style="text-align: center; font-size:2em;">vsmraid Service </span>](#span-styletext-align-center-font-size2emvsmraid-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">VSS Service </span>](#span-styletext-align-center-font-size2emvss-service-span)
			* [<span style="text-align: center; font-size:2em;">VSTXRAID Service </span>](#span-styletext-align-center-font-size2emvstxraid-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">vwifibus Service </span>](#span-styletext-align-center-font-size2emvwifibus-service-span)
			* [<span style="text-align: center; font-size:2em;">vwififlt Service </span>](#span-styletext-align-center-font-size2emvwififlt-service-span)
			* [<span style="text-align: center; font-size:2em;">W32Time Service </span>](#span-styletext-align-center-font-size2emw32time-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">WaaSMedicSvc Service </span>](#span-styletext-align-center-font-size2emwaasmedicsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WacomPen Service </span>](#span-styletext-align-center-font-size2emwacompen-service-span)
			* [<span style="text-align: center; font-size:2em;">WalletService Service </span>](#span-styletext-align-center-font-size2emwalletservice-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">wanarp Service </span>](#span-styletext-align-center-font-size2emwanarp-service-span)
			* [<span style="text-align: center; font-size:2em;">wanarpv6 Service </span>](#span-styletext-align-center-font-size2emwanarpv6-service-span)
			* [<span style="text-align: center; font-size:2em;">WarpJITSvc Service </span>](#span-styletext-align-center-font-size2emwarpjitsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">wbengine Service </span>](#span-styletext-align-center-font-size2emwbengine-service-span)
			* [<span style="text-align: center; font-size:2em;">WbioSrvc Service </span>](#span-styletext-align-center-font-size2emwbiosrvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">wcifs Service </span>](#span-styletext-align-center-font-size2emwcifs-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Wcmsvc Service </span>](#span-styletext-align-center-font-size2emwcmsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">wcncsvc Service </span>](#span-styletext-align-center-font-size2emwcncsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">wcnfs Service </span>](#span-styletext-align-center-font-size2emwcnfs-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WdBoot Service </span>](#span-styletext-align-center-font-size2emwdboot-service-span)
			* [<span style="text-align: center; font-size:2em;">Wdf01000 Service </span>](#span-styletext-align-center-font-size2emwdf01000-service-span)
			* [<span style="text-align: center; font-size:2em;">WdFilter Service </span>](#span-styletext-align-center-font-size2emwdfilter-service-span)
			* [<span style="text-align: center; font-size:2em;">WdiServiceHost Service </span>](#span-styletext-align-center-font-size2emwdiservicehost-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WdiSystemHost Service </span>](#span-styletext-align-center-font-size2emwdisystemhost-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">wdiwifi Service </span>](#span-styletext-align-center-font-size2emwdiwifi-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WdmCompanionFilter Service </span>](#span-styletext-align-center-font-size2emwdmcompanionfilter-service-span)
			* [<span style="text-align: center; font-size:2em;">WdNisDrv Service </span>](#span-styletext-align-center-font-size2emwdnisdrv-service-span)
			* [<span style="text-align: center; font-size:2em;">WdNisSvc Service </span>](#span-styletext-align-center-font-size2emwdnissvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WebClient Service </span>](#span-styletext-align-center-font-size2emwebclient-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">Wecsvc Service </span>](#span-styletext-align-center-font-size2emwecsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WEPHOSTSVC Service </span>](#span-styletext-align-center-font-size2emwephostsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">wercplsupport Service </span>](#span-styletext-align-center-font-size2emwercplsupport-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WerSvc Service </span>](#span-styletext-align-center-font-size2emwersvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">WFDSConMgrSvc Service </span>](#span-styletext-align-center-font-size2emwfdsconmgrsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">WFPLWFS Service </span>](#span-styletext-align-center-font-size2emwfplwfs-service-span)
			* [<span style="text-align: center; font-size:2em;">WiaRpc Service </span>](#span-styletext-align-center-font-size2emwiarpc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WIMMount Service </span>](#span-styletext-align-center-font-size2emwimmount-service-span)
			* [<span style="text-align: center; font-size:2em;">WinDefend Service </span>](#span-styletext-align-center-font-size2emwindefend-service-span)
			* [<span style="text-align: center; font-size:2em;">Windows Workflow Foundation 4.0.0.0 Service </span>](#span-styletext-align-center-font-size2emwindows-workflow-foundation-4000-service-span)
			* [<span style="text-align: center; font-size:2em;">WindowsTrustedRT Service </span>](#span-styletext-align-center-font-size2emwindowstrustedrt-service-span)
			* [<span style="text-align: center; font-size:2em;">WindowsTrustedRTProxy Service </span>](#span-styletext-align-center-font-size2emwindowstrustedrtproxy-service-span)
			* [<span style="text-align: center; font-size:2em;">WinHttpAutoProxySvc Service </span>](#span-styletext-align-center-font-size2emwinhttpautoproxysvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WinMad Service </span>](#span-styletext-align-center-font-size2emwinmad-service-span)
			* [<span style="text-align: center; font-size:2em;">Winmgmt Service </span>](#span-styletext-align-center-font-size2emwinmgmt-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WinNat Service </span>](#span-styletext-align-center-font-size2emwinnat-service-span)
			* [<span style="text-align: center; font-size:2em;">WinRM Service </span>](#span-styletext-align-center-font-size2emwinrm-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">Winsock Service </span>](#span-styletext-align-center-font-size2emwinsock-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WinSock2 Service </span>](#span-styletext-align-center-font-size2emwinsock2-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WINUSB Service </span>](#span-styletext-align-center-font-size2emwinusb-service-span)
			* [<span style="text-align: center; font-size:2em;">WinVerbs Service </span>](#span-styletext-align-center-font-size2emwinverbs-service-span)
			* [<span style="text-align: center; font-size:2em;">wisvc Service </span>](#span-styletext-align-center-font-size2emwisvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">WlanSvc Service </span>](#span-styletext-align-center-font-size2emwlansvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">wlidsvc Service </span>](#span-styletext-align-center-font-size2emwlidsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">wlpasvc Service </span>](#span-styletext-align-center-font-size2emwlpasvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">WManSvc Service </span>](#span-styletext-align-center-font-size2emwmansvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WmiAcpi Service </span>](#span-styletext-align-center-font-size2emwmiacpi-service-span)
			* [<span style="text-align: center; font-size:2em;">WmiApRpl Service </span>](#span-styletext-align-center-font-size2emwmiaprpl-service-span)
			* [<span style="text-align: center; font-size:2em;">wmiApSrv Service </span>](#span-styletext-align-center-font-size2emwmiapsrv-service-span)
			* [<span style="text-align: center; font-size:2em;">WMPNetworkSvc Service </span>](#span-styletext-align-center-font-size2emwmpnetworksvc-service-span)
			* [<span style="text-align: center; font-size:2em;">Wof Service </span>](#span-styletext-align-center-font-size2emwof-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">workerdd Service </span>](#span-styletext-align-center-font-size2emworkerdd-service-span)
			* [<span style="text-align: center; font-size:2em;">workfolderssvc Service </span>](#span-styletext-align-center-font-size2emworkfolderssvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WpcMonSvc Service </span>](#span-styletext-align-center-font-size2emwpcmonsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WPDBusEnum Service </span>](#span-styletext-align-center-font-size2emwpdbusenum-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">WpdUpFltr Service </span>](#span-styletext-align-center-font-size2emwpdupfltr-service-span)
			* [<span style="text-align: center; font-size:2em;">WpnService Service </span>](#span-styletext-align-center-font-size2emwpnservice-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WpnUserService Service </span>](#span-styletext-align-center-font-size2emwpnuserservice-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">ws2ifsl Service </span>](#span-styletext-align-center-font-size2emws2ifsl-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">wscsvc Service </span>](#span-styletext-align-center-font-size2emwscsvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WSearch Service </span>](#span-styletext-align-center-font-size2emwsearch-service-span)
			* [<span style="text-align: center; font-size:2em;">WSearchIdxPi Service </span>](#span-styletext-align-center-font-size2emwsearchidxpi-service-span)
			* [<span style="text-align: center; font-size:2em;">wuauserv Service </span>](#span-styletext-align-center-font-size2emwuauserv-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">WudfPf Service </span>](#span-styletext-align-center-font-size2emwudfpf-service-span)
			* [<span style="text-align: center; font-size:2em;">WUDFRd Service </span>](#span-styletext-align-center-font-size2emwudfrd-service-span)
			* [<span style="text-align: center; font-size:2em;">WwanSvc Service </span>](#span-styletext-align-center-font-size2emwwansvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">XblAuthManager Service </span>](#span-styletext-align-center-font-size2emxblauthmanager-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">XblGameSave Service </span>](#span-styletext-align-center-font-size2emxblgamesave-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">xboxgip Service </span>](#span-styletext-align-center-font-size2emxboxgip-service-span)
			* [<span style="text-align: center; font-size:2em;">XboxGipSvc Service </span>](#span-styletext-align-center-font-size2emxboxgipsvc-service-span)
				* [Service Parameters](#service-parameters)
				* [Service Triggers](#service-triggers)
			* [<span style="text-align: center; font-size:2em;">XboxNetApiSvc Service </span>](#span-styletext-align-center-font-size2emxboxnetapisvc-service-span)
				* [Service Parameters](#service-parameters)
			* [<span style="text-align: center; font-size:2em;">xinputhid Service </span>](#span-styletext-align-center-font-size2emxinputhid-service-span)
			* [<span style="text-align: center; font-size:2em;">xmlprov Service </span>](#span-styletext-align-center-font-size2emxmlprov-service-span)
				* [Service Parameters](#service-parameters)

# Full Dump

## SYSTEM

### WMI AutoLoggers
  

---
<br></br>
#### Cellcore

|EnableLevel|EnableProperty|Enabled|LoggerName|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0x04|0x02|0x01|SmsRouter|0x00|{A9C11050-9E93-4fa4-8FE0-7C4750A345B2}|
  

---
<br></br>
#### Circular Kernel Context Logger
  
BufferSize : `0x04`  
ClockType : `0x03`  
EnableKernelFlags : `05 20 00 00 80 40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`  
GUID : `{54dea73a-ed1f-42a4-af71-3e63d056f174}`  
LogFileMode : `0x480`  
MaxFileSize : `0x00`  
MaximumBuffers : `0x02`  
MinimumBuffers : `0x02`  
Start : `0x01`  
Status : `0x00`
|guid|
| :---: |
|BufferSize|
|ClockType|
|EnableKernelFlags|
|GUID|
|LogFileMode|
|MaxFileSize|
|MaximumBuffers|
|MinimumBuffers|
|Start|
|Status|
  

---
<br></br>
#### CloudExperienceHostOobe

|EnableLevel|Enabled|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: |
|0x05|0x01|0x00|{17bc862c-6db8-49a7-945d-9f101535416f}|
|0x05|0x01|0xc00000000000|{22eb0808-0b6c-5cd4-5511-6a77e6e73a93}|
|0x05|0x01|0x00|{31059da2-ad95-402a-9076-291886471ed5}|
|0x05|0x01|0x00|{397b9505-a6ba-5951-46ee-84b08fb14812}|
|0x05|0x01|0xc00000000000|{4b8b1947-ae4d-54e2-826a-1aee78ef05b2}|
|0x05|0x01|0x00|{5e586678-8171-5406-e113-c6fbd31535db}|
|0x05|0x01|0x00|{99eb7b56-f3c6-558c-b9f6-09a33abb4c83}|
|0x05|0x01|0xc00000000000|{a55d5a23-1a5b-580a-2be5-d7188f43fae1}|
|0x05|0x01|0xc00000000000|{acc49822-f0b2-49ff-bff2-1092384822b6}|
|0x05|0x01|0x00|{bb8dd8e5-3650-5ca7-4fea-46f75f152414}|
|0x05|0x01|0x00|{d0034f5e-3686-5a74-dc48-5a22dd4f3d5b}|
|0x05|0x01|0x00|{e74efd1a-b62d-4b83-ab00-66f4a166a2d3}|
|0x05|0x01|0x00|{f385e1a5-0346-5411-11a2-e8c8afe3b6ca}|
|0x05|0x01|0x00|{ff91e668-f7be-577e-14a3-44d801cccfa0}|
  

---
<br></br>
#### DataMarket

|EnableLevel|Enabled|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: |
|0x04|0x00|0xff00000000000000|{B1D067C7-2F8C-436E-9E82-C5C2C22229D5}|
  

---
<br></br>
#### DefenderApiLogger
  
{1edeee53-0afe-4609-b846-d8c0b2075b1f} : `{1edeee53-0afe-4609-b846-d8c0b2075b1f}`  
{54849625-5478-4994-a5ba-3e3b0328c30d} : `{54849625-5478-4994-a5ba-3e3b0328c30d}`  
{E02A841C-75A3-4FA7-AFC8-AE09CF9B7F23} : `{E02A841C-75A3-4FA7-AFC8-AE09CF9B7F23}`  
{fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148} : `{fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148}`
|EnableLevel|Enabled|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: |
|None|None|None|{1edeee53-0afe-4609-b846-d8c0b2075b1f}|
|None|None|None|{54849625-5478-4994-a5ba-3e3b0328c30d}|
|0x00|0x01|None|{85a62a0d-7e17-485f-9d4f-749a287193a6}|
|0x00|0x01|0x400|{8c416c79-d49b-4f01-a467-e56d3aa8234c}|
|None|0x01|None|{c688cf83-9945-5ff6-0e1e-1ff1f8a2ec9a}|
|None|None|None|{E02A841C-75A3-4FA7-AFC8-AE09CF9B7F23}|
|0x00|0x01|0x1c085445|{f4e1897c-bb5d-5668-f1d8-040f4d8dd344}|
|None|None|None|{fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148}|
  

---
<br></br>
#### DefenderAuditLogger
  
Age : `0x01`  
BufferSize : `0x40`  
ClockType : `0x02`  
EnableSecurityProvider : `0x01`  
FlushTimer : `0x0a`  
GUID : `{6B4012D0-22B6-464D-A553-20E9618403A1}`  
LogFileMode : `0x180001c0`  
MaximumBuffers : `0x10`  
MinimumBuffers : `0x00`  
Start : `0x01`  
Status : `0x00`
|guid|
| :---: |
|Age|
|BufferSize|
|ClockType|
|EnableSecurityProvider|
|FlushTimer|
|GUID|
|LogFileMode|
|MaximumBuffers|
|MinimumBuffers|
|Start|
|Status|
  

---
<br></br>
#### DiagLog
  
BufferSize : `0x10`  
FlushTimer : `0x01`  
GUID : `{08b524eb-a2bf-47eb-aef1-dbd871741d7a}`  
LogFileMode : `0x10000180`  
MaximumBuffers : `0x16`  
Start : `0x01`  
Status : `0x00`
|guid|
| :---: |
|BufferSize|
|FlushTimer|
|GUID|
|LogFileMode|
|MaximumBuffers|
|Start|
|Status|
  

---
<br></br>
#### Diagtrack-Listener

|EnableLevel|EnableProperty|Enabled|MatchAllKeyword|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0xff|0x3b1|0x01|0x00|0xe00000000000|{4f50731a-89cf-4782-b3e0-dce8c90476ba}|
|0xff|0x3b1|0x01|0x00|0xe00000000000|{780dddc8-18a1-5781-895a-a690464fa89c}|
|0xff|0x3b1|0x01|0x00|0xe0000000|{976a8310-986e-4640-8bfb-7736ee6d9b65}|
|0xff|0x3b1|0x01|0x00|0xe00000000000|{c7de053a-0c2e-4a44-91a2-5222ec2ecdf1}|
  

---
<br></br>
#### EventLog-Application

|EnableLevel|EnableProperty|Enabled|LoggerName|MatchAllKeyword|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{01090065-b467-4503-9b28-533766761087}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{08466062-aed4-4834-8b04-cddb414504e5}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{0888e5ef-9b98-4695-979d-e92ce4247224}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{09608c12-c1da-4104-a6fe-b959cf57560a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{09ac07b9-6ac9-43bc-a50f-58419a797c69}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{09ec9687-d7ad-40ca-9c5e-78a04a5ae993}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{0dd4d48e-2bbf-452f-a7ec-ba3dba8407ae}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{0ff1c24b-7f05-45c0-abdc-3c8521be4f62}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{10a208dd-a372-421c-9d99-4fad6db68b62}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{1139c61b-b549-4251-8ed3-27250a1edec8}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xa000000000000000|{11a75546-3234-465e-bec8-2d301cb501ac}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{126cdb97-d346-4894-8a34-658da5eea1b6}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{134ea407-755d-4a93-b8a6-f290cd155023}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{13b197bd-7cee-4b4e-8dd0-59314ce374ce}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{13bc4371-4e21-4e46-a84f-8c0ffb548ced}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{1418ef04-b0b4-4623-bf7e-d74ab47bbdaa}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{15a7a4f8-0072-4eab-abad-f98a4d666aed}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xe000000000000000|{1b8b402d-78dc-46fb-bf71-46e64aedf165}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{1bd672b8-445e-53fc-35ef-09f53672c385}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{1bda2ab1-bbc1-4acb-a849-c0ef2b249672}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{1db28f2e-8f80-4027-8c5a-a11f7f10f62d}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{1ed6976a-4171-4764-b415-7ea08bc46c51}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{1edeee53-0afe-4609-b846-d8c0b2075b1f}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{21d79db0-8e03-41cd-9589-f3ef7001a92a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{23b8d46b-67dd-40a3-b636-d43e50552c6d}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{23f0f2c7-c77c-51ee-0ac1-5ac7796a85df}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xa000000000000000|{27a8c1e2-eb19-463e-8424-b399df27a216}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{287d59b6-79ba-4741-a08b-2fedeede6435}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{28aa95bb-d444-4719-a36f-40462168127e}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{28e25b07-c47f-473d-8b24-2e171cca808a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{2a45d52e-bbf3-4843-8e18-b356ed5f6a65}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{2cd58181-0bb6-463e-828a-056ff837f966}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{2d318b91-e6e7-4c46-bd04-bfe6db412cf9}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{2ed299d2-2f6b-411d-8d15-f4cc6fde0c70}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{2f94e1cc-a8c5-4fe7-a1c3-53d7bda8e73e}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x7800000000000000|{30336ed4-e327-447c-9de0-51b652c86108}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{314de49f-ce63-4779-ba2b-d616f6963a88}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x6000000000000000|{315a8872-923e-4ea2-9889-33cd4754bf64}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x1000000000000000|{319122a9-1485-4e48-af35-7db2d93b8ad2}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{32254f6c-aa33-46f0-a5e3-1cbcc74bf683}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x9000000000000000|{34a3697e-0f10-4e48-af3c-f869b5babebb}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{34b02aa4-be24-55e0-4eb1-d29469a2d79c}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{3527cb55-1298-49d4-ab94-1243db0fcaff}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{3663a992-84be-40ea-bba9-90c7ed544222}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{36c23e18-0e66-11d9-bbeb-505054503030}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{3a5bef13-d0f7-4e7f-9ec8-5e707df711d0}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{3a718a68-6974-4075-abd3-e8243caef398}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{3ae1ea61-c002-47fb-b06c-4022a8c98929}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{3c088e51-65be-40d1-9b90-62bfec076737}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{3cb40aaa-1145-4fb8-b27b-7e30f0454316}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{3cc2d4af-da5e-4ed4-bcbe-3cf995940483}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{3d42a67d-9ce8-4284-b755-2550672b0ce0}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{3da494e4-0fe2-415c-b895-fb5265c5c83b}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{3e5ac668-af52-4c15-b99b-a3e7a6616ebd}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{3f471139-acb7-4a01-b7a7-ff5da4ba2d43}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{4053fada-178b-5aa8-746b-7cf8538b5118}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{40ab57c2-1c53-4df9-9324-ff7cf898a02c}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{41862974-da3b-4f0b-97d5-bb29fbb9b71e}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{442c11c5-304b-45a4-ae73-dc2194c4e876}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{46098845-8a94-442d-9095-366a6bcfefa9}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{4969de67-439c-516f-f805-a82a4f905730}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{4a104570-ec6d-4560-a40f-858fa955e84f}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{4a933674-fb3d-4e8d-b01d-17ee14e91a3e}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{4afddfde-002d-51ac-c109-c3b7897858d0}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{4cb314df-c11f-47d7-9c04-65fb0051561b}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{4de9bc9c-b27a-43c9-8994-0915f1a5e24f}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{4eacb4d0-263b-4b93-8cd6-778a278e5642}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{50df9e12-a8c4-4939-b281-47e1325ba63e}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{50f99b2d-96d2-421f-be4c-222c4140da9f}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{530fb9b9-c515-4472-9313-fb346f9255e3}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{5402e5ea-1bdd-4390-82be-e108f1e634f5}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{54164045-7c50-4905-963f-e5bc1eef0cca}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{57003e21-269b-4bdc-8434-b3bf8d57d2d5}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{579402a2-883c-45d8-b70a-9bc856407751}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{58980f4b-bd39-4a3e-b344-492ed2254a4e}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{595f33ea-d4af-4f4d-b4dd-9dacdd17fc6e}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xd000000000000000|{5b0a651a-8807-45cc-9656-7579815b6af0}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{5b5ab841-7d2e-4a95-bb4f-095cdf66d8f0}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{5bbca4a8-b209-48dc-a8c7-b23d3e5216fb}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{5d674230-ca9f-11da-a94d-0800200c9a66}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x5000000000000000|{5d896912-022d-40aa-a3a8-4fa5515c76d7}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{5ec13d8e-4b3f-422e-a7e7-3121a1d90c7a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x1000000000000000|{5f0e257f-c224-43e5-9555-2adcb8540a58}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{63b530f8-29c9-4880-a5b4-b8179096e7b8}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{63d2bb1d-e39a-41b8-9a3d-52dd06677588}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{63dd5dfb-2488-5e1f-7895-d49ff5bc7125}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{6489b27f-7c43-5886-1d00-0a61bb2a375b}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{64a98c25-9e00-404e-84ad-6700dfe02529}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{64ef2b1c-4ae1-4e64-8599-1636e441ec88}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{66a5c15c-4f8e-4044-bf6e-71d896038977}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{67d07935-283a-4791-8f8d-fa9117f3e6f2}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{699e309c-e782-4400-98c8-e21d162d7b7b}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{69c8ca7e-1adf-472b-ba4c-a0485986b9f6}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{6a1f2b00-6a90-4c38-95a5-5cab3b056778}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x2000000000000000|{6a2dc7c1-930a-4fb5-bb44-80b30aebed6c}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{6b1ffe48-5b1e-4793-9f7f-ae926454499d}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{6d7662a9-034e-4b1f-a167-67819c401632}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{6d8a3a60-40af-445a-98ca-99359e500146}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{6df57621-e7e4-410f-a7e9-e43eeb61b11f}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xa000000000000000|{6e400999-5b82-475f-b800-cef6fe361539}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{6eb8db94-fe96-443f-a366-5fe0cee7fb1c}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{712abb2d-d806-4b42-9682-26da01d8b307}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{72561cf0-c85c-4f78-9e8d-cba9093df62d}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{72d211e1-4c54-4a93-9520-4901681b2271}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{73370bd6-85e5-430b-b60a-fea1285808a7}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{741bb90c-a7a3-49d6-bd82-1e6b858403f7}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{741fc222-44ed-4ba7-98e3-f405b2d2c4b4}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{747ef6fd-e535-4d16-b510-42c90f6873a1}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{75ebc33e-0870-49e5-bdce-9d7028279489}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{75ebc33e-0936-4a55-9d26-5f298f3180bf}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{75ebc33e-0cc6-49da-8cd9-8903a5222aa0}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{75ebc33e-8670-4eb6-b535-3b9d6bb222fd}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{75ebc33e-997f-49cf-b49f-ecc50184b75d}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{75ebc33e-c8ae-4f93-9ca1-683a53e20cb6}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{76ab12d5-c986-4e60-9d7c-2a092b284cdd}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{777ba8fe-2498-4875-933a-3067de883070}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{7d29d58a-931a-40ac-8743-48c733045548}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{7d7b0c39-93f6-4100-bd96-4dda859652c5}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{7e58e69a-e361-4f06-b880-ad2f4b64c944}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{7e87506f-bace-4bf1-bc09-3a1f37045c71}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{7eafcf79-06a7-460b-8a55-bd0a0c9248aa}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{7f9d83de-8abb-457f-98e8-4ad161449ecc}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{8127f6d4-59f9-4abf-8952-3e3a02073d5f}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{83d6e83b-900b-48a3-9835-57656b6f6474}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{8530db6e-51c0-43d6-9d02-a8c2088526cd}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{85a62a0d-7e17-485f-9d4f-749a287193a6}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{85be49ea-38f1-4547-a604-80060202fb27}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{85fe7609-ff4a-48e9-9d50-12918e43e1da}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{88c09888-118d-48fc-8863-e1c6d39ca4df}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xa000000000000000|{88cd9180-4491-4640-b571-e3bee2527943}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{8939299f-2315-4c5c-9b91-abb86aa0627d}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{89592015-d996-4636-8f61-066b5d4dd739}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{89a2278b-c662-4aff-a06c-46ad3f220bca}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{89b1e9f0-5aff-44a6-9b44-0a07a7ce5845}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x2000000000000000|{8bcdf442-3070-4118-8c94-e8843be363b3}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{8ce93926-bdae-4409-9155-2fe4799ef4d3}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{906b8a99-63ce-58d7-86ab-10989bbd5567}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{91f5fb12-fdea-4095-85d5-614b495cd9de}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{9363ccd9-d429-4452-9adb-2501e704b810}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{93a19ab3-fb2c-46eb-91ef-56b0a318b983}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xa000000000000000|{952773bf-c2b7-49bc-88f4-920744b82c43}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{95353826-4fbe-41d4-9c42-f521c6e86360}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{9580d7dd-0379-4658-9870-d5be7d52d6de}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{968f313b-097f-4e09-9cdd-bc62692d138b}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc00000000000000|{96f4a050-7e31-453c-88be-9634f4e02139}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{973143dd-f3c7-4ef5-b156-544ac38c39b6}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{97ca8142-10b1-4baa-9fbb-70a7d11231c3}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{9803daa0-81ba-483a-986c-f0e395b9f8d1}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{98bf1cd3-583e-4926-95ee-a61bf3f46470}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{98e0765d-8c42-44a3-a57b-760d7f93225a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{9ae87b12-a014-5288-92df-e3030981ebab}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{9c2a37f3-e5fd-5cae-bcd1-43dafeee1ff0}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{9cc0413e-5717-4af5-82eb-6103d8707b45}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{9d55b53d-449b-4824-a637-24f9d69aa02f}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{9f973c1d-d056-4e38-84a5-7be81cdd6ab6}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x9000000000000000|{a0c1853b-5c40-4b15-8766-3cf1c58f985a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{a615acb9-d5a4-4738-b561-1df301d207f8}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{a7975c8f-ac13-49f1-87da-5a984a4ab417}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{a83fa99f-c356-4ded-9fd6-5a5eb8546d68}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{a9c11050-9e93-4fa4-8fe0-7c4750a345b2}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{aa018a01-3747-532b-94ec-5d87dc3a5085}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{aa4c798d-d91b-4b07-a013-787f5803d6fc}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{aabf8b86-7936-4fa2-acb0-63127f879dbf}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{aaeac398-3028-487c-9586-44eacad03637}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{aaf67066-0bf8-469f-ab76-275590c434ee}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{add0de40-32b0-4b58-9d5e-938b2f5c1d1f}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8800000000000000|{ae4bd3be-f36f-45b6-8d21-bdd6fb832853}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{af0a5a6d-e009-46d4-8867-42f2240f8a72}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{b059b83f-d946-4b13-87ca-4292839dc2f2}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x2000000000000000|{b2fcd41f-9a40-4150-8c92-b224b7d8c8aa}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x3000000000000000|{b447b4db-7780-11e0-ada3-18a90531a85a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x2000000000000000|{b447b4de-7780-11e0-ada3-18a90531a85a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x2000000000000000|{b447b4df-7780-11e0-ada3-18a90531a85a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x2000000000000000|{b447b4e1-7780-11e0-ada3-18a90531a85a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x2000000000000000|{b6cc0d55-9ecc-49a8-b929-2b9022426f2a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{b6d775ef-1436-4fe6-bad3-9e436319e218}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{b92cf7fd-dc10-4c6b-a72d-1613bf25e597}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x9000000000000000|{b977cf02-76f6-df84-cc1a-6a4b232322b6}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{b9da9fe6-ae5f-4f3e-b2fa-8e623c11dc75}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{ba093605-3909-4345-990b-26b746adee0a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{ba723d81-0d0c-4f1e-80c8-54740f508ddf}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xd000000000000000|{bab3ad92-fb96-5902-450b-b8421bdec7bd}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{bc1bdb57-71a2-581a-147b-e0b49474a2d4}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{bd12f3b8-fc40-4a61-a307-b7a013a069c1}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{bea18b89-126f-4155-9ee4-d36038b02680}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{bf406804-6afa-46e7-8a48-6c357e1d6d61}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{bff15e13-81bf-45ee-8b16-7cfead00da86}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{c2f36562-a1e4-4bc3-a6f6-01a7adb643e8}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{c4b57d35-0636-4bc3-a262-370f249f9802}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{c4efc9bb-2570-4821-8923-1bad317d2d4b}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{c651f5f6-1c0d-492e-8ae1-b4efd7c9d503}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{c6bf6832-f7bd-4151-ac21-753ce4707453}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x5000000000000000|{c76baa63-ae81-421c-b425-340b4b24157f}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{ca4e628d-8567-4896-ab6b-835b221f373f}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{cab2b8a5-49b9-4eec-b1b0-fac21da05a3b}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{cb070027-1534-4cf3-98ea-b9751f508376}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x5000000000000000|{cbda4dbf-8d5d-4f69-9578-be14aa540d22}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{cd7cf0d0-02cc-4872-9b65-0dba0a90efe8}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{cf3f502e-b40d-4071-996f-00981edf938e}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{cffb980e-327c-5b87-19c6-62c4c3be2290}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x2000000000000000|{d0e22efc-ac66-4b25-a72d-382736b5e940}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8400000000000000|{d1bc9aff-2abf-4d71-9146-ecb2a986eb85}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{d2e990da-8504-4702-a5e5-367fc2f823bf}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{d3610dca-4501-5a5d-21a7-30ca91130711}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{d39b6336-cfcb-483b-8c76-7c3e7d02bcb8}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{d3f29eda-805d-428a-9902-b259b937f84b}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{d67fbb76-d18a-5ae3-24a3-8c1db52d6c62}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{d710d46c-235d-4798-ac20-9f83e1dcd557}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{d8965fcf-7397-4e0e-b750-21a4580bd880}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{dab3b18c-3c0f-43e8-80b1-e44bc0dad901}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{db00dfb6-29f9-4a9c-9b3b-1f4f9e7d9770}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{dbe9b383-7cf3-4331-91cc-a3cb16a3b538}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xa000000000000000|{dcbe5aaa-16e2-457c-9337-366950045f0a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{de095dbe-8667-4168-94c2-48ca61665aca}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{de513a55-c345-438b-9a74-e18cac5c5cc5}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x800000000000000|{de7b24ea-73c8-4a09-985d-5bdadcfa9017}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{e0c6f6de-258a-50e0-ac1a-103482d118bc}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{e1dd7e52-621d-44e3-a1ad-0370c2b25946}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{e23b33b0-c8c9-472c-a5f9-f2bdfea0f156}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{e4d53f84-7de3-11d8-9435-505054503030}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x2000000000000000|{e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{e53df8ba-367a-4406-98d5-709ffb169681}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{e5c16d49-2464-4382-bb20-97a4b5465db9}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{e6307a09-292c-497e-aad6-498f68e2b619}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{e6835967-e0d2-41fb-bcec-58387404e25a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{e7558269-3fa5-46ed-9f4d-3c6e282dde55}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{e8ed09dc-100c-45e2-9fc8-b53399ec1f70}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{e934e6dd-62be-55d8-1cc8-416d0039498b}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{ea8cd8a5-78ff-4418-b292-aadc6a7181df}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{eb65a492-86c0-406a-bace-9912d595bd69}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{ec23f986-ae2d-4269-b52f-4e20765c1a94}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xd000000000000000|{ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x1f00000000000000|{eef54e71-0661-422d-9a98-82fd4940b820}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{f0be35f8-237b-4814-86b5-ade51192e503}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{f0db7ef8-b6f3-4005-9937-feb77b9e1b43}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{f1201b5a-e170-42b6-8d20-b57ac57e6416}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{f1394de0-32c7-4a76-a6de-b245e48f4615}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xa000000000000000|{f1ef270a-0d32-4352-ba52-dbab41e1d859}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{f2311b48-32be-4902-a22a-7240371dbb2c}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{f3f53c76-b06d-4f15-b412-61164a0d2b73}|
|0x00|0x01|0x01|EventLog-Application|0x00|0xc000000000000000|{f43c3c35-22e2-53eb-f169-07594054779e}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{f4aed7c7-a898-4627-b053-44a7caa12fcd}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{f5dbaa02-15d6-4644-a784-7032d508bf64}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{f82fb576-e941-4956-a2c7-a0cf83f6450a}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{f8ad09ba-419c-5134-1750-270f4d0fb889}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x800000000000000|{f9fe3908-44b8-48d9-9a32-5a763ff5ed79}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{fae10392-f0af-4ac0-b8ff-9f4d920c3cdf}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{fae96d09-ade1-5223-0098-af7b67348531}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{fb829150-cd7d-44c3-af5b-711a3c31cedc}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x4000000000000000|{fbcfac3f-8459-419f-8e48-1f0b49cdb85e}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x2000000000000000|{fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148}|
|0x00|0x01|0x01|EventLog-Application|0x00|0x8000000000000000|{ff79a477-c45f-4a52-8ae0-2b324346d4e4}|
  

---
<br></br>
#### EventLog-Security
  
BufferSize : `0x40`  
ClockType : `0x02`  
FlushTimer : `0x01`  
Guid : `{0e66e20b-b802-ba6a-9272-31199d0ed295}`  
LogFileMode : `0x180001c0`  
MaximumBuffers : `0x10`  
MinimumBuffers : `0x00`  
OwningChannel : `Security`  
Start : `0x01`
|guid|
| :---: |
|BufferSize|
|ClockType|
|FlushTimer|
|Guid|
|LogFileMode|
|MaximumBuffers|
|MinimumBuffers|
|OwningChannel|
|Start|
  

---
<br></br>
#### EventLog-System

|EnableLevel|EnableProperty|Enabled|LoggerName|MatchAllKeyword|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{01979c6a-42fa-414c-b8aa-eee2c8202018}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{04268430-d489-424d-b914-0cff741d6684}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{059f0f37-910e-4ff0-a7ee-ae8d49dd319b}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{05f02597-fe85-4e67-8542-69567ab8fd4f}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{06edcfeb-0fd0-4e53-acca-a6f8bbf81bcb}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{0b886108-1899-4d3a-9c0d-42d8fc4b9108}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{0b9fdccc-451c-449c-9bd8-6756fcc6091a}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{0bf2fb94-7b60-4b4d-9766-e82f658df540}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc800000000000000|{0c478c5b-0351-41b1-8c58-4a6737da32e3}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{0d4fdc09-8c27-494a-bda0-505e4fd8adae}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{0f67e49f-fe51-4e9f-b490-6f2948cc6027}|
|0x00|0x01|0x01|EventLog-System|0x00|0x9000000000000000|{0fa2ee03-1feb-5057-3bb3-eb25521b8482}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{11c5d8ad-756a-42c2-8087-eb1b4a72a846}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{11cd958a-c507-4ef3-b3f2-5fd9dfbd2c78}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{125f2cf1-2768-4d33-976e-527137d080f8}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{152fbe4b-c7ad-4f68-bada-a4fcc1464f6c}|
|0x00|0x01|0x01|EventLog-System|0x00|0x2000000000000000|{15a7a4f8-0072-4eab-abad-f98a4d666aed}|
|0x00|0x01|0x01|EventLog-System|0x00|0xa000000000000000|{15ca44ff-4d7a-4baa-bba5-0998955e531e}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{199fe037-2b82-40a9-82ac-e1d46c792b99}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{1b562e86-b7aa-4131-badc-b6f3a001407e}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{1b6b0772-251b-4d42-917d-faca166bc059}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{1c95126e-7eea-49a9-a3fe-a378b03ddb4d}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{1db28f2e-8f80-4027-8c5a-a11f7f10f62d}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{1e9a4978-78c2-441e-8858-75b5d1326bc5}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{1f678132-5938-4686-9fdc-c8ff68f15c85}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{206f6dea-d3c5-4d10-bc72-989f03c8b84b}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{21b7c16e-c5af-4a69-a74a-7245481c1b97}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{2a274310-42d5-4019-b816-e4b8c7abe95c}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{2bef5442-d402-5a72-58e1-cb7e491bf179}|
|0x00|0x01|0x01|EventLog-System|0x00|0x2000000000000000|{2e35aaeb-857f-4beb-a418-2e6c0e54d988}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{2e6cb42e-161d-413b-a6c1-84ca4c1e5890}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{2f07e2ee-15db-40f1-90ef-9d7ba282188a}|
|0x00|0x01|0x01|EventLog-System|0x00|0x2000000000000000|{2ff3e6b7-cb90-4700-9621-443f389734ed}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{306c4e0b-e148-543d-315b-c618eb93157c}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{30e1d284-5d88-459c-83fd-6345b39b19ec}|
|0x00|0x01|0x01|EventLog-System|0x00|0x9000000000000000|{331c3b3a-2005-44c2-ac5e-77220c37d6b4}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{355c44fe-0c8e-4bf8-be28-8bc7b5a42720}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{3629dd4d-d6f1-4302-a623-0768b51501c7}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{36c23e18-0e66-11d9-bbeb-505054503030}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{3903d5b9-988d-4c31-9ccd-4022f96703f0}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{3cb2a168-fe19-4a4e-bdad-dcf422f13473}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{3e59a529-b0b3-4a11-8129-9ffe6bb46eb9}|
|0x00|0x01|0x01|EventLog-System|0x00|0x1000000000000000|{3f471139-acb7-4a01-b7a7-ff5da4ba2d43}|
|0x00|0x01|0x01|EventLog-System|0x00|0xe000000000000000|{3ff37a1c-a68d-4d6e-8c9b-f79e8b16c482}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{40783728-8921-45d0-b231-919037b4b4fd}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{412bdff2-a8c4-470d-8f33-63fe0d8c20e2}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{43e63da5-41d1-4fbf-aded-1bbed98fdd1d}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{45eec9e5-4a1b-5446-7ad8-a4ab1313c437}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{46c78e5c-a213-46a8-8a6b-622f6916201d}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{47bc9477-a8ba-452e-b951-4f2ed3593cf9}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{47bfa2b7-bd54-4fac-b70b-29021084ca8f}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{494e7a3d-8db9-4ec4-b43e-2844af6e38d6}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{4af188ac-e9c4-4c11-b07b-1fabc07dfeb2}|
|0x00|0x01|0x01|EventLog-System|0x00|0x1000000000000000|{4cb314df-c11f-47d7-9c04-65fb0051561b}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{4cec9c95-a65f-4591-b5c4-30100e51d870}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{4ee76bd8-3cf4-44a0-a0ac-3937643e37a3}|
|0x00|0x01|0x01|EventLog-System|0x00|0xe000000000000000|{52fc89f8-995e-434c-a91e-199986449890}|
|0x00|0x01|0x01|EventLog-System|0x00|0x2000000000000000|{530fb9b9-c515-4472-9313-fb346f9255e3}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{538cbbad-4877-4eb2-b26e-7caee8f0f8cb}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{54cb22ff-26b4-4393-a8c2-6b0715912c5f}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{555908d1-a6d7-4695-8e1e-26931d2012f4}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{55ab77f6-fa04-43ef-af45-688fbf500482}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{5931d877-4860-4ee7-a95c-610a5f0d1407}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{595f7f52-c90a-4026-a125-8eb5e083f15e}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{5d674230-ca9f-11da-a94d-0800200c9a66}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{5d896912-022d-40aa-a3a8-4fa5515c76d7}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{5f92bc59-248f-4111-86a9-e393e12c6139}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{62de9e48-90c6-4755-8813-6a7d655b0802}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{632f767e-0ec3-47b9-ba1c-a0e62a74728a}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{63d1e632-95cc-4443-9312-af927761d52a}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{64ef2b1c-4ae1-4e64-8599-1636e441ec88}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{651df93b-5053-4d1e-94c5-f6e6d25908d0}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{66a5c15c-4f8e-4044-bf6e-71d896038977}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{67fe2216-727a-40cb-94b2-c02211edb34a}|
|0x00|0x01|0x01|EventLog-System|0x00|0x2000000000000000|{6a1f2b00-6a90-4c38-95a5-5cab3b056778}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{6a2dc7c1-930a-4fb5-bb44-80b30aebed6c}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{6b93bf66-a922-4c11-a617-cf60d95c133d}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{6bba3851-2c7e-4dea-8f54-31e5afd029e3}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{7237fff9-a08a-4804-9c79-4a8704b70b87}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{72cd9ff7-4af8-4b89-aede-5f26fda13567}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{73a33ab2-1966-4999-8add-868c41415269}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{73e9c9de-a148-41f7-b1db-4da051fdc327}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{74c2135f-cc76-45c3-879a-ef3bb1eeaf86}|
|0x00|0x01|0x01|EventLog-System|0x00|0x2000000000000000|{75ebc33e-997f-49cf-b49f-ecc50184b75d}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{7725b5f9-1f2e-4e21-baeb-b2af4690bc87}|
|0x00|0x01|0x01|EventLog-System|0x00|0xe000000000000000|{7b563579-53c8-44e7-8236-0f87b9fe6594}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{7b6bc78c-898b-4170-bbf8-1a469ea43fc5}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{7d5387b0-cbe0-11da-a94d-0800200c9a66}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{7da4fe0e-fd42-4708-9aa5-89b77a224885}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc00000000000000|{802ec45a-1e99-4b83-9920-87c98277ba9d}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{84de80eb-86e8-4ff6-85a6-9319abd578a4}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{85a62a0d-7e17-485f-9d4f-749a287193a6}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{89203471-d554-47d4-bde4-7552ec219999}|
|0x00|0x01|0x01|EventLog-System|0x00|0x1000000000000000|{89592015-d996-4636-8f61-066b5d4dd739}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{89fe8f40-cdce-464e-8217-15ef97d4c7c3}|
|0x00|0x01|0x01|EventLog-System|0x00|0x100000000000000|{8c416c79-d49b-4f01-a467-e56d3aa8234c}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{8e6a5303-a4ce-498f-afdb-e03a8a82b077}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{928f7d29-0577-5be5-3bd3-b6bdab9ab307}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{945a8954-c147-4acd-923f-40c45405a658}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{951b41ea-c830-44dc-a671-e2c9958809b8}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{95353826-4fbe-41d4-9c42-f521c6e86360}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{9580d7dd-0379-4658-9870-d5be7d52d6de}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{96f4a050-7e31-453c-88be-9634f4e02139}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{9741fd4e-3757-479f-a3c6-fc49f6d5edd0}|
|0x00|0x01|0x01|EventLog-System|0x00|0x2700000000000000|{988c59c5-0a1c-45b6-a555-0c62276e327d}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{991f8fe6-249d-44d6-b93d-5a3060c1dedb}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{9988748e-c2e8-4054-85f6-0c3e1cad2470}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc200000000000000|{9c205a39-1250-487d-abd7-e831c6290539}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{9f650c63-9409-453c-a652-83d7185a2e83}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{9f7b5df4-b902-48bc-bc94-95068c6c7d26}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{a0e3d8ea-c34f-4419-a1db-90435b8b21d0}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{a4445c76-ed85-c8a3-02c1-532a38614a9e}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{a67075c2-3e39-4109-b6cd-6d750058a731}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{a68ca8b7-004f-d7b6-a698-07e2de0f1f5d}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{a6ad76e3-867a-4635-91b3-4904ba6374d7}|
|0x00|0x01|0x01|EventLog-System|0x00|0x9000000000000000|{a7f2235f-be51-51ed-decf-f4498812a9a2}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{a82fda5d-745f-409c-b0fe-18ae0678a0e0}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{a8a1f2f6-a13a-45e9-b1fe-3419569e5ef2}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{a963a23c-0058-521d-71ec-a1cce6173f21}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{abf1f586-2e50-4ba8-928d-49044e6f0db7}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{ac43300d-5fcc-4800-8e99-1bd3f85f0320}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{ac52ad17-cc01-4f85-8df5-4dce4333c99b}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{ad5162d8-daf0-4a25-88a7-01cbeb33902e}|
|0x00|0x01|0x01|EventLog-System|0x00|0x6000000000000000|{ae4bd3be-f36f-45b6-8d21-bdd6fb832853}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{aea1b4fa-97d1-45f2-a64c-4d69fffd92c9}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{aec5c129-7c10-407d-be97-91a042c61aaa}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{b0aa8734-56f7-41cc-b2f4-de228e98b946}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{b2fcd41f-9a40-4150-8c92-b224b7d8c8aa}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{b675ec37-bdb6-4648-bc92-f3fdc74d3ca2}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4800000000000000|{b977cf02-76f6-df84-cc1a-6a4b232322b6}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{b99317e5-89b7-4c0d-abd1-6e705f7912dc}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{ba093605-3909-4345-990b-26b746adee0a}|
|0x00|0x01|0x01|EventLog-System|0x00|0x800000000000000|{ba2ffb5c-e20a-4fb9-91b4-45f61b4b66a0}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{babda89a-4d5e-48eb-af3d-e0e8410207c0}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{bc0669e1-a10d-4a78-834e-1ca3c806c93b}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{bef2aa8e-81cd-11e2-a7bb-5eac6188709b}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{c02afc2b-e24e-4449-ad76-bcc2c2575ead}|
|0x00|0x01|0x01|EventLog-System|0x00|0x3000000000000000|{c03715ce-ea6f-5b67-4449-da1d1e1afeb8}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{c18672d1-dc18-4dfd-91e4-170cf37160cf}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{c26c4f3c-3f66-4e99-8f8a-39405cfed220}|
|0x00|0x01|0x01|EventLog-System|0x00|0xa00000000000000|{c4636a1e-7986-4646-bf10-7bc3b4a76e8e}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{c76baa63-ae81-421c-b425-340b4b24157f}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{c914f0df-835a-4a22-8c70-732c9a80c634}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{cb017cd2-1f37-4e65-82bc-3e91f6a37559}|
|0x00|0x01|0x01|EventLog-System|0x00|0xa000000000000000|{cbda4dbf-8d5d-4f69-9578-be14aa540d22}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{cd9c6198-bf73-4106-803b-c17d26559018}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{cdc05e28-c449-49c6-b9d2-88cf761644df}|
|0x00|0x01|0x01|EventLog-System|0x00|0x2000000000000000|{cdead503-17f5-4a3e-b7ae-df8cc2902eb9}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{ce8dee0b-d539-4000-b0f8-77bed049c590}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{cfc18ec0-96b1-4eba-961b-622caee05b0a}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{d0e22efc-ac66-4b25-a72d-382736b5e940}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4200000000000000|{d1bc9aff-2abf-4d71-9146-ecb2a986eb85}|
|0x00|0x01|0x01|EventLog-System|0x00|0x2e00000000000000|{d48ce617-33a2-4bc3-a5c7-11aa4f29619e}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{d5c25f9a-4d47-493e-9184-40dd397a004d}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{d6f68875-cdf5-43a5-a3e3-53ffd683311c}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{db66ea65-b7bb-4ca9-8748-334cb5c32400}|
|0x00|0x01|0x01|EventLog-System|0x00|0x2000000000000000|{dbe9b383-7cf3-4331-91cc-a3cb16a3b538}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{dd5ef90a-6398-47a4-ad34-4dcecdef795f}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{dd70bc80-ef44-421b-8ac3-cd31da613a4e}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{de29cf61-5ee6-43ff-9aac-959c4e13cc6c}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{de7b24ea-73c8-4a09-985d-5bdadcfa9017}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{dea07764-0790-44de-b9c4-49677b17174f}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{e104fb41-6b04-4f3a-b47d-f0df2f02b954}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{e2816346-87f4-4f85-95c3-0c79409aa89d}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{e3bac9f8-27be-4823-8d7f-1cc320c05fa7}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{e4480490-85b6-11dd-ad8b-0800200c9a66}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{e4f68870-5ae8-4e5b-9ce7-ca9ed75b0245}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{e595f735-b42a-494b-afcd-b68666945cd3}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{e5ba83f6-07d0-46b1-8bc7-7e669a1d31dc}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{e670a5a2-ce74-4ab4-9347-61b815319f4c}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{e8f9af91-afbe-5a03-dfec-5d591686326c}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{ea216962-877b-5b73-f7c5-8aef5375959e}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{ed8cc261-2123-567e-063e-75fc5f8e8a48}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{eee173ef-7ed2-45de-9877-01c70a852fbd}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{ef1cc15b-46c1-414e-bb95-e76b077bd51e}|
|0x00|0x01|0x01|EventLog-System|0x00|0x4000000000000000|{f029ac39-38f0-4a40-b7de-404d244004cb}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{f2e2ce31-0e8a-4e46-a03b-2e0fe97e93c2}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{f3c5e28e-63f6-49c7-a204-e48a1bc4b09d}|
|0x00|0x01|0x01|EventLog-System|0x00|0x800000000000000|{f5d05b38-80a6-4653-825d-c414e4ab3c68}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{f708c483-4880-11e6-9121-5cf37068b67b}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{f717d024-f5b4-4f03-9ab9-331b2dc38ffb}|
|0x00|0x01|0x01|EventLog-System|0x00|0xe000000000000000|{f9fe3908-44b8-48d9-9a32-5a763ff5ed79}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{fae10392-f0af-4ac0-b8ff-9f4d920c3cdf}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{fc4e8f51-7a04-4bab-8b91-6321416f72ab}|
|0x00|0x01|0x01|EventLog-System|0x00|0x8000000000000000|{fc65ddd8-d6ef-4962-83d5-6e5cfe9ce148}|
|0x00|0x01|0x01|EventLog-System|0x00|0xc000000000000000|{fcbb06bb-6a2a-46e3-abaa-246cb4e508b2}|
  

---
<br></br>
#### HolographicDevice

|EnableLevel|Enabled|guid|
| :---: | :---: | :---: |
|0x05|0x01|{0504EB02-3A16-54E4-A2FF-3D85FA2F13E6}|
|0x05|0x01|{05C32102-40E0-4B2B-B778-E5FD577C472B}|
|0x04|0x01|{3317C7E7-7C40-4275-9F7B-D539C10E19BA}|
|0x05|0x01|{5f9080bf-b22c-47ea-8b76-1da0cf975419}|
|0x05|0x01|{7946A50E-2DD8-475F-B677-5C44D942A386}|
|0x05|0x01|{ce491dde-a0c2-4de6-acb1-b2712cf96fda}|
|0x04|0x01|{F903DB44-149E-4B4E-AFE1-2A1096F53DFA}|
  

---
<br></br>
#### LwtNetLog

|EnableLevel|Enabled|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: |
|0x04|0x01|0x100|{01578F96-C270-4602-ADE0-578D9C29FC0C}|
|0x04|0x01|0x2000|{0BD3506A-9030-4F76-9B88-3E8FE1F7CFB6}|
|0x04|0x01|0x20|{12d25187-6c0d-4783-ad3a-84caa135acfd}|
|0x04|0x01|0x01|{15A7A4F8-0072-4EAB-ABAD-F98A4D666AED}|
|0x04|0x01|0x10000000|{1C95126E-7EEA-49A9-A3FE-A378B03DDB4D}|
|0x04|0x01|0x01|{1E39B4CE-D1E6-46CE-B65B-5AB05D6CC266}|
|0x04|0x01|0x2000|{2F07E2EE-15DB-40F1-90EF-9D7BA282188A}|
|0x04|0x01|0x20|{314DE49F-CE63-4779-BA2B-D616F6963A88}|
|0x04|0x01|0x40|{315a8872-923e-4ea2-9889-33cd4754bf64}|
|0x04|0x01|0x20|{3CB40AAA-1145-4FB8-B27B-7E30F0454316}|
|0x04|0x01|0x01|{3EB875EB-8F4A-4800-A00B-E484C97D7551}|
|0x04|0x01|0x100|{43D1A55C-76D6-4F7E-995C-64C711E5CAFE}|
|0x04|0x01|0x20|{63B530F8-29C9-4880-A5B4-B8179096E7B8}|
|0x04|0x01|0x20|{67D07935-283A-4791-8F8D-FA9117F3E6F2}|
|0x04|0x01|0x01|{6A1F2B00-6A90-4C38-95A5-5CAB3B056778}|
|0x04|0x01|0x01|{7868B0D4-1423-4681-AFDF-27913575441E}|
|0x04|0x01|0x405100|{88CD9180-4491-4640-B571-E3BEE2527943}|
|0x04|0x01|0x400|{9580D7DD-0379-4658-9870-D5BE7D52D6DE}|
|0x04|0x01|0x80|{A6BF0DEB-3659-40AD-9F81-E25AF62CE3C7}|
|0x04|0x01|0x100|{AB0D8EF9-866D-4D39-B83F-453F3B8F6325}|
|0x04|0x01|0x4000|{CDEAD503-17F5-4A3E-B7AE-DF8CC2902EB9}|
|0x04|0x01|0x10|{DF271536-4298-45E1-B0F2-E88F78619C5D}|
|0x04|0x01|0x04|{e6835967-e0d2-41fb-bcec-58387404e25a}|
|0x04|0x01|0x20|{FBCFAC3F-8459-419F-8E48-1F0B49CDB85E}|
  

---
<br></br>
#### Mellanox-Kernel

|EnableLevel|EnableProperty|Enabled|MatchAllKeyword|MatchAnyKeyword|Status|guid|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0x02|0x00|0x01|0x00|0x7fffffff|0x00|{1752F07C-7E5C-402c-9C5F-AD21E572F852}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{2a219718-1373-11dc-8314-0800200c9a66}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{3F9BC73D-EB03-453a-B27B-20F9A664211A}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{5D63D37F-E400-4455-A902-1FDABE74A9AB}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{684E068C-3FDC-4bce-89C3-CDB77A8B75A4}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{7707876a-2ff7-4808-ae74-453Ed62836f5}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{83793EC3-E8A3-4801-BECF-5E921F79F06E}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{93c5d651-de7e-449c-9801-81c18c1d3dce}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{99dc84e3-b106-431e-88a6-4dd20c9bbde3}|
|0x02|0x00|0x01|0x00|0x7fffffff|0x00|{B199CE55-F8BF-4147-B119-DACD1E5987A6}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{B94560A8-E060-48F3-B2B5-F543E534B9EF}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{BF3440A2-0830-4481-A7BB-7BFE6AA51DDE}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{bf83b73c-cc3c-4342-a2ba-bb38ead7bb52}|
|0x02|0x00|0x01|0x00|0x7fffffff|0x00|{C66F5F72-DF10-45BB-948E-5482C551CD2B}|
|0x02|0x00|0x01|0x00|0x7fffffff|0x00|{CA7A4CF7-8B0C-4C4D-96C3-505B8360EB2D}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{cb0b88ec-fb28-4b50-87cd-885c9bae58d4}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{CDE9C859-A7D6-439E-A8AC-698F92761D10}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{E51BB6E2-914A-4e21-93C0-192F4801BBFF}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{F8C96A49-AE22-41e9-8025-D7E416884D89}|
|0x03|0x00|0x01|0x00|0x7fffffff|0x00|{FB519A7D-886F-4A9D-A63F-28A34A6D469D}|
|0x02|0x00|0x01|0x00|0x7fffffff|0x00|{fec86576-9d3c-4e00-80ab-2c4abdbfbc86}|
  

---
<br></br>
#### Microsoft-Windows-AssignedAccess-Trace

|EnableLevel|Enabled|guid|
| :---: | :---: | :---: |
|0x05|0x01|{355d4f62-3d5b-5372-213f-6d9d804c75df}|
  

---
<br></br>
#### Microsoft-Windows-Rdp-Graphics-RdpIdd-Trace

|EnableLevel|Enabled|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: |
|0x04|0x01|0x40000000ffff|{7b7a87d4-6d7c-4c87-8e3d-29f31bff02b8}|
|0x04|0x01|0x4000000004f4|{D92BCB52-FA78-406F-A9A5-2037509FADEA}|
  

---
<br></br>
#### Microsoft-Windows-Setup

|EnableFlags|EnableLevel|Enabled|Status|guid|
| :---: | :---: | :---: | :---: | :---: |
|None|0x04|0x01|None|{0063715b-eeda-4007-9429-ad526f62696e}|
|None|0x04|0x01|None|{0DD4D48E-2BBF-452f-A7EC-BA3DBA8407AE}|
|None|0x04|0x01|None|{75EBC33E-0870-49e5-BDCE-9D7028279489}|
|None|0x04|0x01|None|{75EBC33E-0936-4a55-9D26-5F298F3180BF}|
|None|0x04|0x01|None|{75EBC33E-0CC6-49da-8CD9-8903A5222AA0}|
|None|0x04|0x01|None|{75EBC33E-77B8-4ba8-9474-4F4A9DB2F5C6}|
|None|0x04|0x01|None|{75EBC33E-8670-4eb6-B535-3B9D6BB222FD}|
|None|0x04|0x01|None|{75EBC33E-997F-49cf-B49F-ECC50184B75D}|
|None|0x04|0x01|None|{75EBC33E-C8AE-4f93-9CA1-683A53E20CB6}|
|None|0x04|0x01|None|{75EBC33E-D017-4D0F-93AB-0B4F86579164}|
|None|0x04|0x01|None|{A615ACB9-D5A4-4738-B561-1DF301D207F8}|
|0x10|0x04|0x01|0x00|{A68CA8B7-004F-D7B6-A698-07E2DE0F1F5D}|
|None|0x04|0x01|None|{B9DA9FE6-AE5F-4f3e-B2FA-8E623C11DC75}|
|None|0x04|0x01|None|{C553CED4-9BA3-478F-98EA-906CE99C2E4F}|
|None|0x04|0x01|None|{f5dbaa02-15d6-4644-a784-7032d508bf64}|
  

---
<br></br>
#### NBSMBLOGGER

|EnableFlags|EnableLevel|Enabled|LoggerName|_Description|guid|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0x7fffffff|0x05|0x01|lmhsvclogger|lmhsvc Trace Provider|{81f307db-f5fb-4c3e-9b9d-8b39a9cb6198}|
|0x7fffffff|0x05|0x01|netbtlogger|NetBT Trace Provider|{bca7bd7f-b0bf-4051-99f4-03cfe79664c1}|
  

---
<br></br>
#### NetCore

|(Default)|@|EnableLevel|Enabled|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: | :---: | :---: |
|None|ncsi_wpp|0x05|0x01|0x7fffffff|{014DE49F-CE63-4779-BA2B-D616F6963A87}|
|None|wcmsvc_tracelogging|0x05|0x01|0x00|{0616F7DD-722A-4DF1-B87A-414FA870D8B7}|
|None|ncsi_tracelog|0x05|0x01|0x00|{1701C7DC-045C-45C0-8CD6-4D42E3BBF387}|
|None|nla_wpp|0x05|0x01|0x7fffffff|{1AC55562-D4FF-4BC5-8EF3-A18E07C4668E}|
|None|Windows.Networking.Connectivity WinRT WPP|0x05|0x01|0x7fffffff|{2ACF2633-ED1B-41FD-A17E-9F98719CDB36}|
|None|ondemandconnroutehelper_wpp|0x05|0x01|0xffffffffffffffff|{41D92334-B49C-4938-85F1-3C22595DB157}|
|CspLte|None|0x04|0x01|0x00|{47FFA01C-6FC4-4205-BDEE-D629DFF06DB8}|
|None|cmoemutil_tracelogging|0x05|0x01|0x00|{53439AD7-895A-47F3-8372-DB39C41B641D}|
|None|triage_getconnected_tracelogging|0x05|0x01|0x00|{60523747-6516-48B7-84B1-3264FA2CB359}|
|None|wcmsvc_wpp|0x05|0x01|0xffffffffffffffff|{988ce33b-dde5-44eb-9816-ee156b443ff1}|
|None|triage_ondemand_tracelogging|0x05|0x01|0x00|{ABB1FC61-49BA-4CC3-809F-7ABE1F8BA315}|
|None|dusmsvc_tracelogging|0x05|0x01|0x00|{afa03ad9-e63c-59d0-754c-f5a51b7fe33c}|
|None|srumsvc_etw|0x03|0x01|0x00|{C8DBF506-E3D3-4822-930D-84C557EB6247}|
|None|nlm_wpp|0x05|0x01|0x7fffffff|{D9131565-E1DD-4C9E-A728-951999C2ADB5}|
|None|nlm_tracelog|0x05|0x01|0x00|{EA289C62-8C36-4904-9726-15ECD282AED5}|
|None|datausagehandlers_tracelogging|0x05|0x01|0x00|{ea893635-5ab7-562b-75a2-a22107d8058f}|
  

---
<br></br>
#### NtfsLog

|EnableFlags|EnableLevel|Enabled|LoggerName|_Description|guid|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0x8000000|0x03|0x01|ClfsLog|ClfsLog Trace Provider|{525BE239-F9A1-4080-A053-FCFE310AAE84}|
|0x07|0x03|0x01|None|ReFS WPP Trace|{740f3c34-57df-4bad-8eea-72ac69ad5df5}|
  

---
<br></br>
#### PEAuthLog

|EnableLevel|Enabled|guid|
| :---: | :---: | :---: |
|0x00|0x00|{31A91186-0A64-4466-AA59-266568B4A936}|
  

---
<br></br>
#### RadioMgr

|@|EnableLevel|Enabled|MatchAnyKeyword|Status|guid|
| :---: | :---: | :---: | :---: | :---: | :---: |
|radiomgr_wpp|0x05|0x01|0x7fffffff|0x00|{1EE4093E-D437-4847-8312-ACFC2F05E6EC}|
|wlanwwanradiomgr_wpp|0x05|0x01|0x7fffffff|0x00|{2DD11DE3-FDDE-4DA9-B57A-AF6585F74233}|
  

---
<br></br>
#### RdrLog

|EnableFlags|EnableLevel|Enabled|LoggerName|_Description|guid|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0x05|0x02|0x00|RdbssLog|RDBSS Trace Provider|{0086eae4-652e-4dc7-b58f-11fa44f927b4}|
|0x33333333|0x00|0x00|RdrLog|MupLog Trace Provider|{20c46239-d059-4214-a11e-7d6769cbe020}|
|0x21|0x02|0x00|Smb20Log|SMB20 Trace Provider|{e4ad554c-63b2-441b-9f86-fe66d8084963}|
|0x01|0x02|0x00|MrxsmbLog|MRXSMB Trace Provider|{f818ebb3-fbc4-4191-96d6-4e5c37c8a237}|
  

---
<br></br>
#### ReadyBoot

|EnableFlags|Enabled|guid|
| :---: | :---: | :---: |
|0x20|0x01|{2a274310-42d5-4019-b816-e4b8c7abe95c}|
|None|0x01|{a319d300-015c-48be-acdb-47746e154751}|
  

---
<br></br>
#### SetupPlatform

|EnableLevel|Enabled|guid|
| :---: | :---: | :---: |
|0x04|0x01|{0063715b-eeda-4007-9429-ad526f62696e}|
|0x04|0x01|{11CD958A-C507-4EF3-B3F2-5FD9DFBD2C78}|
|0x04|0x01|{30336ed4-e327-447c-9de0-51b652c86108}|
|0x04|0x01|{331c3b3a-2005-44c2-ac5e-77220c37d6b4}|
|0x04|0x01|{530FB9B9-C515-4472-9313-FB346F9255E3}|
|0x04|0x01|{75EBC33E-0CC6-49da-8CD9-8903A5222AA0}|
|0x04|0x01|{75EBC33E-77B8-4ba8-9474-4F4A9DB2F5C6}|
|0x04|0x01|{75EBC33E-8670-4eb6-B535-3B9D6BB222FD}|
|0x04|0x01|{75EBC33E-997F-49cf-B49F-ECC50184B75D}|
|0x04|0x01|{75EBC33E-C8AE-4f93-9CA1-683A53E20CB6}|
|0x04|0x01|{75EBC33E-D017-4D0F-93AB-0B4F86579164}|
|0x04|0x01|{B9DA9FE6-AE5F-4f3e-B2FA-8E623C11DC75}|
|0x04|0x01|{C553CED4-9BA3-478F-98EA-906CE99C2E4F}|
|0x04|0x01|{f0be35f8-237b-4814-86b5-ade51192e503}|
|0x04|0x01|{f5dbaa02-15d6-4644-a784-7032d508bf64}|
  

---
<br></br>
#### SetupPlatformTel

|EnableLevel|Enabled|guid|
| :---: | :---: | :---: |
|0xff|0x01|{04E7BAD5-F665-4F6E-9678-80646A3201AD}|
|0xff|0x01|{1153A52E-8D1C-4E78-B7E3-DA3DB836BC4C}|
|0xff|0x01|{393F5655-4CBA-40FD-9C19-1910B6965D01}|
|0xff|0x01|{4587E014-39E2-4150-9246-6264F9B719F2}|
|0x04|0x01|{530FB9B9-C515-4472-9313-FB346F9255E3}|
|0xff|0x01|{5FC48AED-2EB8-4CD4-9C87-54700C4B7B26}|
|0xff|0x01|{63BCA7A1-77EC-4EA7-95D0-98D3F0C0EBF7}|
|0xff|0x01|{696AC247-4E85-42E8-B0D2-FEC2475C76AD}|
|0xff|0x01|{6A5C2702-B765-49E9-AB7B-74A98431E1B3}|
|0xff|0x01|{6A5CCFD4-CF02-5640-0B5F-D2E031258F16}|
|0xff|0x01|{6C0EBBBB-C292-457D-9675-DFCC1C0D58B0}|
|0xff|0x01|{8AD0A868-0B32-47EC-B018-2FCC19D01951}|
|0xff|0x01|{8BE48F34-1F58-4180-8C12-DBE6E6E71A81}|
|0xff|0x01|{A23BD382-12AB-4F02-A0D7-273153F8B65A}|
|0xff|0x01|{AE8A2994-7D8B-4CCA-80B8-8EADAF0554C7}|
|0x04|0x01|{C553CED4-9BA3-478F-98EA-906CE99C2E4F}|
  

---
<br></br>
#### SpoolerLogger

|EnableFlags|EnableLevel|Enabled|guid|
| :---: | :---: | :---: | :---: |
|0xffff|0x05|0x01|{19E464A4-7408-49BD-B960-53446AE47820}|
|0xffff|0x05|0x01|{19E93940-A1BD-497F-BC58-CA333880BAB4}|
|0xffff|0x05|0x01|{201eb0f8-12f0-5b34-c99b-75c1541f3479}|
|0xffff|0x05|0x01|{3048407B-56AA-4D41-82B2-7d5F4b1CDD39}|
|0xffff|0x05|0x01|{402E812D-04E6-4E66-ABDB-32E5F79D36A2}|
|0xffff|0x05|0x01|{49868e3d-77fb-5083-9e09-61e3f37e0309}|
|0xffff|0x05|0x01|{62A0EB6C-3E3E-471d-960C-7C574A72534C}|
|0xffff|0x05|0x01|{6d5ca4bb-df8e-41bc-b554-8aeab241f206}|
|0xffff|0x05|0x01|{6fb61ac3-3455-4da4-8313-c1a855ee64c5}|
|0xffff|0x05|0x01|{836767A6-AF31-4938-B4C0-EF86749A9AEF}|
|0xffff|0x05|0x01|{9558985e-3bc8-45ef-a2fd-2e6ff06fb886}|
|0xffff|0x05|0x01|{99F5F45C-FD1E-439F-A910-20D0DC759D28}|
|0xffff|0x05|0x01|{acf1e4a7-9241-4fbf-9555-c27638434f8d}|
|0xffff|0x05|0x01|{B795C7DF-07BC-4362-938E-E8ABD81A9A01}|
|0xffff|0x05|0x01|{bf3eac2a-65ca-5ecc-2076-e23c6420a687}|
|0xffff|0x05|0x01|{C9BF4A01-D547-4d11-8242-E03A18B5BE01}|
|0xffff|0x05|0x01|{C9BF4A02-D547-4d11-8242-E03A18B5BE01}|
|0xffff|0x05|0x01|{C9BF4A03-D547-4d11-8242-E03A18B5BE01}|
|0xffff|0x05|0x01|{C9BF4A05-D547-4d11-8242-E03A18B5BE01}|
|0xffff|0x05|0x01|{C9BF4A9E-D547-4d11-8242-E03A18B5BE01}|
|0xffff|0x05|0x01|{C9BF4A9F-D547-4d11-8242-E03A18B5BE01}|
|0xffff|0x05|0x01|{d758d01c-7402-5923-6a27-44bdcc59a5c5}|
|0xffff|0x05|0x01|{e73d49d6-9eda-5059-74d1-b879b18cf9ae}|
  

---
<br></br>
#### SQMLogger

|EnableLevel|EnableProperty|Enabled|LoggerName|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{017BA13C-9A55-4f1f-8200-323055AAC810}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{059F0F37-910E-4FF0-A7EE-AE8D49DD319B}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{093da50c-0bb9-4d7d-b95c-3bb9fcda5ee8}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{15CA44FF-4D7A-4BAA-BBA5-0998955E531E}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{2a274310-42d5-4019-b816-e4b8c7abe95c}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{2ff3e6b7-cb90-4700-9621-443f389734ed}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{331c3b3a-2005-44c2-ac5e-77220c37d6b4}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{3e59a529-b0b3-4a11-8129-9ffe6bb46eb9}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{4214dcd2-7c33-4f74-9898-719ccceec20f}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{494e7a3d-8db9-4ec4-b43e-2844af6e38d6}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{61F044AF-9104-4CA5-81EE-CB6C51BB01AB}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{65d99466-7a8e-489c-b8e1-962bc945031e}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{7b563579-53c8-44e7-8236-0f87b9fe6594}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{9c205a39-1250-487d-abd7-e831c6290539}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{a0af438f-4431-41cb-a675-a265050ee947}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{a6ad76e3-867a-4635-91b3-4904ba6374d7}|
|0x04|0x02|0x01|None|0x8000000000000|{CD9C6198-BF73-4106-803B-C17D26559018}|
|0x04|0x02|0x01|SQMLogger|0x8000000000000|{F5344219-87A4-4399-B14A-E59CD118ABB8}|
  

---
<br></br>
#### TCPIPLOGGER

|EnableFlags|EnableLevel|Enabled|guid|
| :---: | :---: | :---: | :---: |
|0xfff|0x03|0x01|{eb004a05-9b1a-11d4-9123-0050047759bc}|
  

---
<br></br>
#### TileStore

|EnableLevel|Enabled|Status|guid|
| :---: | :---: | :---: | :---: |
|0x04|0x00|0x00|{98CCAAD9-6464-48D7-9A66-C13718226668}|
  

---
<br></br>
#### Tpm

|EnableFlags|EnableLevel|Enabled|guid|
| :---: | :---: | :---: | :---: |
|0xffff|0x06|0x01|{3A8D6942-B034-48e2-B314-F69C2B4655A3}|
  

---
<br></br>
#### UBPM

|EnableFlags|EnableLevel|Enabled|LoggerName|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0xffffff|0x00|0x01|UBPM|None|{18f4a5fd-fd3b-40a5-8fc2-e5d261c5d02e}|
|0xffffff|0x00|0x01|UBPM|None|{22b6d684-fa63-4578-87c9-effcbe6643c7}|
|0xffffff|0x00|0x01|UBPM|None|{3635d4b6-77e3-4375-8124-d545b7149337}|
|0xffffff|0x00|0x01|UBPM|None|{5b004607-1087-4f16-b10e-979685a8d131}|
|0xffffff|0x00|0x01|UBPM|None|{9b307223-4e4d-4bf5-9be8-995cd8e7420b}|
|None|0x04|0x01|UBPM|0x01|{aa1f73e8-15fd-45d2-abfd-e7f64f78eb11}|
|0xffffff|0x00|0x01|UBPM|None|{BD8FEA17-5549-4B49-AA03-1981D16396A9}|
|0xffffff|0x00|0x01|UBPM|None|{FBCFAC3F-8460-419F-8E48-1F0B49CDB85E}|
  

---
<br></br>
#### WdiContextLog
  
BufferSize : `0x10`  
FileMax : `0x03`  
FileName : `%SystemRoot%\System32\WDI\LogFiles\WdiContextLog.etl`  
GUID : `{f52ac1cc-b92d-4d8e-8cf5-699ca40a73d2}`  
LogFileMode : `0x1282`  
MaxFileSize : `0x02`  
MaximumBuffers : `0x20`  
Start : `0x01`  
Status : `0x00`
|guid|
| :---: |
|BufferSize|
|FileMax|
|FileName|
|GUID|
|LogFileMode|
|MaxFileSize|
|MaximumBuffers|
|Start|
|Status|
  

---
<br></br>
#### WFP-IPsec Trace

|EnableLevel|Enabled|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: |
|0x04|0x01|0xffffffff|{106B464A-8043-46B1-8CB8-E92A0CD7A560}|
|0x04|0x01|0xffffffff|{106B464D-8043-46B1-8CB8-E92A0CD7A560}|
|0x04|0x01|0xffffffff|{5A1600D2-68E5-4DE7-BCF4-1C2D215FE0FE}|
|0x04|0x01|0xffffffff|{AD33FA19-F2D2-46D1-8F4C-E3C3087E45AD}|
  

---
<br></br>
#### WiFiDriverIHVSession
  
BufferSize : `0x50`  
ClockType : `0x01`  
FileMax : `0x04`  
FileName : `%SystemRoot%\System32\LogFiles\WMI\WifiDriverIHVSession.etl`  
Guid : `{810F5633-19B2-4BC7-B898-5574411A7053}`  
LogFileMode : `0x02`  
MaxFileSize : `0x08`  
MaximumBuffers : `0x10`  
MinimumBuffers : `0x02`
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
  

---
<br></br>
#### WiFiDriverIHVSessionRepro
  
BufferSize : `0x50`  
ClockType : `0x01`  
FileName : `%SystemRoot%\System32\LogFiles\WMI\WifiDriverIHVSessionRepro.etl`  
Guid : `{9112C3FC-7A73-42E6-A8E1-FAECE69C7BD6}`  
LogFileMode : `0x02`  
MaxFileSize : `0x32`  
MaximumBuffers : `0x10`  
MinimumBuffers : `0x02`  
Start : `0x00`
|guid|
| :---: |
|BufferSize|
|ClockType|
|FileName|
|Guid|
|LogFileMode|
|MaxFileSize|
|MaximumBuffers|
|MinimumBuffers|
|Start|
  

---
<br></br>
#### WiFiSession

|EnableLevel|Enabled|MatchAnyKeyword|guid|
| :---: | :---: | :---: | :---: |
|0x05|0x01|0xffffffffffffffff|{047FB417-39E6-4B79-A52C-C436B60011AD}|
|0x05|0x01|0x00|{0BD3506A-9030-4f76-9B88-3E8FE1F7CFB6}|
|0x05|0x01|0xffffffffffffffff|{111ffc99-3987-4bf8-8398-61853120cb3d}|
|0xff|0x01|0xffffffffffffffff|{1193FF07-26A3-4ECA-9384-12CCF39CAE03}|
|0x04|0x01|0x00|{1fc7fc44-07d5-59f7-8a3e-fc1ee708aa8e}|
|0x04|0x01|0x7fffffff|{21ba7b61-05f8-41f1-9048-c09493dcfe38}|
|0xff|0x01|0xffffffffffffffff|{2D0CC56C-874F-422C-B25F-246F286A24BA}|
|0x04|0x01|0x00|{314DE49F-CE63-4779-BA2B-D616F6963A88}|
|0x04|0x01|0x00|{3496b396-5c43-45e7-b38e-d509b79ae721}|
|0x05|0x01|0x00|{3D42A67D-9CE8-4284-B755-2550672B0CE0}|
|0x04|0x01|0x00|{4D946A46-275B-4C9D-B835-0B2160559256}|
|0x05|0x01|0x00|{58980F4B-BD39-4a3e-B344-492ED2254A4E}|
|0x05|0x01|0x00|{5A8A94F3-249F-49F8-86D1-E6527C80622B}|
|0x05|0x01|0x7fffffff|{5B23F342-8421-42EF-87EB-3B686F5A1B2A}|
|0x04|0x01|0xff|{5CA18737-22AC-4050-85BC-B8DBB9F7D986}|
|0x05|0x01|0x00|{60523747-6516-48B7-84B1-3264FA2CB359}|
|0x03|0x01|0x800|{637A0F36-DFF5-4B2F-83DD-B106C1C725E2}|
|0x04|0x01|0x00|{681E3481-7510-4053-8C87-A6305EAFC4FA}|
|0x04|0x01|0x00|{6BE684E4-194C-43B0-B9B8-8269646DE989}|
|0x05|0x01|0x00|{6eb8db94-fe96-443f-a366-5fe0cee7fb1c}|
|0x04|0x01|0x00|{7D7180B3-A452-4FFF-8D1F-7B32B248AB70}|
|0x04|0x01|0x00|{802ec45b-1e99-4b83-9920-87c98277ba9d}|
|0x04|0x01|0x00|{814182FF-58F7-11E1-853C-78E7D1CA7337}|
|0x05|0x01|0x00|{819cf413-40ea-5e76-0bc1-b5f26ebf7075}|
|0x05|0x01|0xffffffffffffffff|{90BBBABB-255B-4FE3-A06F-685A15E93A4C}|
|0x04|0x01|0x00|{914598a6-28f0-42ac-bf3d-a29c6047a739}|
|0x04|0x01|0xffffffffffffffff|{949D7457-6151-4FA0-9E46-D82A6F9927CF}|
|0x05|0x01|0x00|{9580d7dd-0379-4658-9870-d5be7d52d6de}|
|0xff|0x01|0xffffffffffffffff|{9B322459-4AD9-4F81-8EEA-DC77CDD18CA6}|
|0x04|0x01|0x00|{9B694F87-000E-4BE6-91AC-FE2E50D61A6F}|
|0x05|0x01|0x00|{9CC0413E-5717-4af5-82EB-6103D8707B45}|
|0x04|0x01|0x00|{9CC9BEB7-9D24-47C7-8F9D-CCC9DCAC29EB}|
|0x05|0x01|0x7fffffff|{A2E2E7CD-0AEC-4CA3-B807-2E138FC29C71}|
|0x05|0x01|0x00|{AB0D8EF9-866D-4d39-B83F-453F3B8F6325}|
|0x04|0x01|0x00|{abe47285-c002-46d1-95e4-c4aec3c78f50}|
|0x04|0x01|0x00|{B8794785-F7E3-4C2D-A33D-7B0BA0D30E18}|
|0x05|0x01|0x00|{badd4729-e1ec-47b5-b5ab-898c06d32475}|
|0x04|0x01|0x00|{c02edc8d-d627-46c9-abd9-c8b78f88c223}|
|0x04|0x01|0x00|{C100BECE-D33A-4A4B-BF23-BBEF4663D017}|
|0x04|0x01|0x00|{c7491fe4-66f4-4421-9954-b55f03db3186}|
|0x05|0x01|0xffffffffffffffff|{D28262A1-8066-492D-BCE8-635DA75368B7}|
|0x04|0x01|0x00|{E5C16D49-2464-4382-BB20-97A4B5465DB9}|
|0x05|0x01|0x1f|{e6dec100-4e0f-4927-92be-e69d7c15c821}|
|0x05|0x01|0x00|{ff7d986f-df89-5ec7-3fa5-cab4600d9491}|
  

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
#### <span style="text-align: center; font-size:2em;">.NET CLR Data Service </span>

|Performance|
| :---: |
|`{'Close': 'ClosePerformanceData', 'Collect': 'CollectPerformanceData', 'Counter Names': b'S\x00q\x00l\x00C\x00l\x00i\x00e\x00n\x00t\x00:\x00 \x00C\x00u\x00r\x00r\x00e\x00n\x00t\x00 \x00#\x00 \x00p\x00o\x00o\x00l\x00e\x00d\x00 \x00a\x00n\x00d\x00 \x00n\x00o\x00n\x00p\x00o\x00o\x00l\x00e\x00d\x00 \x00c\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00S\x00q\x00l\x00C\x00l\x00i\x00e\x00n\x00t\x00:\x00 \x00C\x00u\x00r\x00r\x00e\x00n\x00t\x00 \x00#\x00 \x00p\x00o\x00o\x00l\x00e\x00d\x00 \x00c\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00S\x00q\x00l\x00C\x00l\x00i\x00e\x00n\x00t\x00:\x00 \x00C\x00u\x00r\x00r\x00e\x00n\x00t\x00 \x00#\x00 \x00c\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00 \x00p\x00o\x00o\x00l\x00s\x00\x00\x00S\x00q\x00l\x00C\x00l\x00i\x00e\x00n\x00t\x00:\x00 \x00P\x00e\x00a\x00k\x00 \x00#\x00 \x00p\x00o\x00o\x00l\x00e\x00d\x00 \x00c\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00S\x00q\x00l\x00C\x00l\x00i\x00e\x00n\x00t\x00:\x00 \x00T\x00o\x00t\x00a\x00l\x00 \x00#\x00 \x00f\x00a\x00i\x00l\x00e\x00d\x00 \x00c\x00o\x00n\x00n\x00e\x00c\x00t\x00s\x00\x00\x00S\x00q\x00l\x00C\x00l\x00i\x00e\x00n\x00t\x00:\x00 \x00T\x00o\x00t\x00a\x00l\x00 \x00#\x00 \x00f\x00a\x00i\x00l\x00e\x00d\x00 \x00c\x00o\x00m\x00m\x00a\x00n\x00d\x00s\x00\x00\x00\x00\x00', 'Counter Types': b'6\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x00\x00\x00', 'Library': '%systemroot%\\system32\\netfxperf.dll', 'Open': 'OpenPerformanceData', 'InstallType': 1, 'PerfIniFile': '_DataPerfCounters_d.ini', 'First Counter': 6840, 'Last Counter': 6852, 'First Help': 6841, 'Last Help': 6853, 'Object List': '6840'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">.NET CLR Networking Service </span>

|Performance|
| :---: |
|`{'Close': 'ClosePerformanceData', 'Collect': 'CollectPerformanceData', 'Counter Names': b'C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00 \x00E\x00s\x00t\x00a\x00b\x00l\x00i\x00s\x00h\x00e\x00d\x00\x00\x00B\x00y\x00t\x00e\x00s\x00 \x00R\x00e\x00c\x00e\x00i\x00v\x00e\x00d\x00\x00\x00B\x00y\x00t\x00e\x00s\x00 \x00S\x00e\x00n\x00t\x00\x00\x00D\x00a\x00t\x00a\x00g\x00r\x00a\x00m\x00s\x00 \x00R\x00e\x00c\x00e\x00i\x00v\x00e\x00d\x00\x00\x00D\x00a\x00t\x00a\x00g\x00r\x00a\x00m\x00s\x00 \x00S\x00e\x00n\x00t\x00\x00\x00\x00\x00', 'Counter Types': b'6\x005\x005\x003\x006\x00\x00\x006\x005\x007\x009\x002\x00\x00\x006\x005\x007\x009\x002\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x00\x00\x00', 'Library': '%systemroot%\\system32\\netfxperf.dll', 'Open': 'OpenPerformanceData', 'InstallType': 1, 'PerfIniFile': '_Networkingperfcounters_v2_d.ini', 'First Counter': 6828, 'Last Counter': 6838, 'First Help': 6829, 'Last Help': 6839, 'Object List': '6828'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">.NET CLR Networking 4.0.0.0 Service </span>

|Linkage|Performance|
| :---: | :---: |
|`{'Export': b'.\x00N\x00E\x00T\x00 \x00C\x00L\x00R\x00 \x00N\x00e\x00t\x00w\x00o\x00r\x00k\x00i\x00n\x00g\x00 \x004\x00.\x000\x00.\x000\x00.\x000\x00\x00\x00\x00\x00'}`|`{'CategoryOptions': 3, 'Close': 'ClosePerformanceData', 'Collect': 'CollectPerformanceData', 'Counter Names': b'C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00 \x00E\x00s\x00t\x00a\x00b\x00l\x00i\x00s\x00h\x00e\x00d\x00\x00\x00B\x00y\x00t\x00e\x00s\x00 \x00R\x00e\x00c\x00e\x00i\x00v\x00e\x00d\x00\x00\x00B\x00y\x00t\x00e\x00s\x00 \x00S\x00e\x00n\x00t\x00\x00\x00D\x00a\x00t\x00a\x00g\x00r\x00a\x00m\x00s\x00 \x00R\x00e\x00c\x00e\x00i\x00v\x00e\x00d\x00\x00\x00D\x00a\x00t\x00a\x00g\x00r\x00a\x00m\x00s\x00 \x00S\x00e\x00n\x00t\x00\x00\x00H\x00t\x00t\x00p\x00W\x00e\x00b\x00R\x00e\x00q\x00u\x00e\x00s\x00t\x00s\x00 \x00C\x00r\x00e\x00a\x00t\x00e\x00d\x00/\x00S\x00e\x00c\x00\x00\x00H\x00t\x00t\x00p\x00W\x00e\x00b\x00R\x00e\x00q\x00u\x00e\x00s\x00t\x00s\x00 \x00A\x00v\x00e\x00r\x00a\x00g\x00e\x00 \x00L\x00i\x00f\x00e\x00t\x00i\x00m\x00e\x00\x00\x00H\x00t\x00t\x00p\x00W\x00e\x00b\x00R\x00e\x00q\x00u\x00e\x00s\x00t\x00s\x00 \x00A\x00v\x00e\x00r\x00a\x00g\x00e\x00 \x00L\x00i\x00f\x00e\x00t\x00i\x00m\x00e\x00 \x00B\x00a\x00s\x00e\x00\x00\x00H\x00t\x00t\x00p\x00W\x00e\x00b\x00R\x00e\x00q\x00u\x00e\x00s\x00t\x00s\x00 \x00Q\x00u\x00e\x00u\x00e\x00d\x00/\x00S\x00e\x00c\x00\x00\x00H\x00t\x00t\x00p\x00W\x00e\x00b\x00R\x00e\x00q\x00u\x00e\x00s\x00t\x00s\x00 \x00A\x00v\x00e\x00r\x00a\x00g\x00e\x00 \x00Q\x00u\x00e\x00u\x00e\x00 \x00T\x00i\x00m\x00e\x00\x00\x00H\x00t\x00t\x00p\x00W\x00e\x00b\x00R\x00e\x00q\x00u\x00e\x00s\x00t\x00s\x00 \x00A\x00v\x00e\x00r\x00a\x00g\x00e\x00 \x00Q\x00u\x00e\x00u\x00e\x00 \x00T\x00i\x00m\x00e\x00 \x00B\x00a\x00s\x00e\x00\x00\x00H\x00t\x00t\x00p\x00W\x00e\x00b\x00R\x00e\x00q\x00u\x00e\x00s\x00t\x00s\x00 \x00A\x00b\x00o\x00r\x00t\x00e\x00d\x00/\x00S\x00e\x00c\x00\x00\x00H\x00t\x00t\x00p\x00W\x00e\x00b\x00R\x00e\x00q\x00u\x00e\x00s\x00t\x00s\x00 \x00F\x00a\x00i\x00l\x00e\x00d\x00/\x00S\x00e\x00c\x00\x00\x00\x00\x00', 'Counter Types': b'6\x005\x005\x003\x006\x00\x00\x006\x005\x007\x009\x002\x00\x00\x006\x005\x007\x009\x002\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x004\x001\x009\x005\x003\x002\x008\x00\x00\x001\x000\x007\x003\x008\x007\x004\x001\x007\x006\x00\x00\x001\x000\x007\x003\x009\x003\x009\x004\x005\x008\x00\x00\x004\x001\x009\x005\x003\x002\x008\x00\x00\x001\x000\x007\x003\x008\x007\x004\x001\x007\x006\x00\x00\x001\x000\x007\x003\x009\x003\x009\x004\x005\x008\x00\x00\x004\x001\x009\x005\x003\x002\x008\x00\x00\x004\x001\x009\x005\x003\x002\x008\x00\x00\x00\x00\x00', 'FileMappingSize': 131072, 'IsMultiInstance': 1, 'Library': '%systemroot%\\system32\\netfxperf.dll', 'Open': 'OpenPerformanceData', 'InstallType': 1, 'PerfIniFile': '_Networkingperfcounters_d.ini', 'First Counter': 6900, 'Last Counter': 6926, 'First Help': 6901, 'Last Help': 6927, 'Object List': '6900'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">.NET Data Provider for Oracle Service </span>

|Linkage|Performance|
| :---: | :---: |
|`{'Export': '2e,00,4e,00,45,00,54,00,20,00,44,00,61,00,74,00,61,00,20,00,50,00,72,00,6f,00,76,00,69,00,64,00,65,00,72,00,20,00,66,00,6f,00,72,00,20,00,4f,00,72,00,61,00,63,00,6c,00,65,00,00,00,00,00'}`|`{'CategoryOptions': 3, 'Close': 'ClosePerformanceData', 'Collect': 'CollectPerformanceData', 'Counter Names': b'H\x00a\x00r\x00d\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00s\x00P\x00e\x00r\x00S\x00e\x00c\x00o\x00n\x00d\x00\x00\x00H\x00a\x00r\x00d\x00D\x00i\x00s\x00c\x00o\x00n\x00n\x00e\x00c\x00t\x00s\x00P\x00e\x00r\x00S\x00e\x00c\x00o\x00n\x00d\x00\x00\x00S\x00o\x00f\x00t\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00s\x00P\x00e\x00r\x00S\x00e\x00c\x00o\x00n\x00d\x00\x00\x00S\x00o\x00f\x00t\x00D\x00i\x00s\x00c\x00o\x00n\x00n\x00e\x00c\x00t\x00s\x00P\x00e\x00r\x00S\x00e\x00c\x00o\x00n\x00d\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00N\x00o\x00n\x00P\x00o\x00o\x00l\x00e\x00d\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00P\x00o\x00o\x00l\x00e\x00d\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00A\x00c\x00t\x00i\x00v\x00e\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00P\x00o\x00o\x00l\x00G\x00r\x00o\x00u\x00p\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00I\x00n\x00a\x00c\x00t\x00i\x00v\x00e\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00P\x00o\x00o\x00l\x00G\x00r\x00o\x00u\x00p\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00A\x00c\x00t\x00i\x00v\x00e\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00P\x00o\x00o\x00l\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00I\x00n\x00a\x00c\x00t\x00i\x00v\x00e\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00P\x00o\x00o\x00l\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00A\x00c\x00t\x00i\x00v\x00e\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00F\x00r\x00e\x00e\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00S\x00t\x00a\x00s\x00i\x00s\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00R\x00e\x00c\x00l\x00a\x00i\x00m\x00e\x00d\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00\x00\x00', 'Counter Types': b'2\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x00\x00\x00', 'FileMappingSize': 131072, 'IsMultiInstance': 1, 'Library': '%systemroot%\\system32\\netfxperf.dll', 'Open': 'OpenPerformanceData', 'InstallType': 1, 'PerfIniFile': '_DataOracleClientPerfCounters_shared12_neutral_d.ini', 'First Counter': 8916, 'Last Counter': 8944, 'First Help': 8917, 'Last Help': 8945, 'Object List': '8916'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">.NET Data Provider for SqlServer Service </span>

|Linkage|Performance|
| :---: | :---: |
|`{'Export': '2e,00,4e,00,45,00,54,00,20,00,44,00,61,00,74,00,61,00,20,00,50,00,72,00,6f,00,76,00,69,00,64,00,65,00,72,00,20,00,66,00,6f,00,72,00,20,00,53,00,71,00,6c,00,53,00,65,00,72,00,76,00,65,00,72,00,00,00,00,00'}`|`{'CategoryOptions': 3, 'Close': 'ClosePerformanceData', 'Collect': 'CollectPerformanceData', 'Counter Names': b'H\x00a\x00r\x00d\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00s\x00P\x00e\x00r\x00S\x00e\x00c\x00o\x00n\x00d\x00\x00\x00H\x00a\x00r\x00d\x00D\x00i\x00s\x00c\x00o\x00n\x00n\x00e\x00c\x00t\x00s\x00P\x00e\x00r\x00S\x00e\x00c\x00o\x00n\x00d\x00\x00\x00S\x00o\x00f\x00t\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00s\x00P\x00e\x00r\x00S\x00e\x00c\x00o\x00n\x00d\x00\x00\x00S\x00o\x00f\x00t\x00D\x00i\x00s\x00c\x00o\x00n\x00n\x00e\x00c\x00t\x00s\x00P\x00e\x00r\x00S\x00e\x00c\x00o\x00n\x00d\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00N\x00o\x00n\x00P\x00o\x00o\x00l\x00e\x00d\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00P\x00o\x00o\x00l\x00e\x00d\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00A\x00c\x00t\x00i\x00v\x00e\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00P\x00o\x00o\x00l\x00G\x00r\x00o\x00u\x00p\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00I\x00n\x00a\x00c\x00t\x00i\x00v\x00e\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00P\x00o\x00o\x00l\x00G\x00r\x00o\x00u\x00p\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00A\x00c\x00t\x00i\x00v\x00e\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00P\x00o\x00o\x00l\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00I\x00n\x00a\x00c\x00t\x00i\x00v\x00e\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00P\x00o\x00o\x00l\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00A\x00c\x00t\x00i\x00v\x00e\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00F\x00r\x00e\x00e\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00S\x00t\x00a\x00s\x00i\x00s\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00N\x00u\x00m\x00b\x00e\x00r\x00O\x00f\x00R\x00e\x00c\x00l\x00a\x00i\x00m\x00e\x00d\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00\x00\x00\x00\x00', 'Counter Types': b'2\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x00\x00\x00', 'FileMappingSize': 131072, 'IsMultiInstance': 1, 'Library': '%systemroot%\\system32\\netfxperf.dll', 'Open': 'OpenPerformanceData', 'InstallType': 1, 'PerfIniFile': '_dataperfcounters_shared12_neutral_d.ini', 'First Counter': 6854, 'Last Counter': 6882, 'First Help': 6855, 'Last Help': 6883, 'Object List': '6854'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">.NET Memory Cache 4.0 Service </span>

|Linkage|Performance|
| :---: | :---: |
|`{'Export': ''}`|`{'CategoryOptions': 3, 'Close': 'ClosePerformanceData', 'Collect': 'CollectPerformanceData', 'Counter Names': b'C\x00a\x00c\x00h\x00e\x00 \x00H\x00i\x00t\x00s\x00\x00\x00C\x00a\x00c\x00h\x00e\x00 \x00M\x00i\x00s\x00s\x00e\x00s\x00\x00\x00C\x00a\x00c\x00h\x00e\x00 \x00H\x00i\x00t\x00 \x00R\x00a\x00t\x00i\x00o\x00\x00\x00C\x00a\x00c\x00h\x00e\x00 \x00H\x00i\x00t\x00 \x00R\x00a\x00t\x00i\x00o\x00 \x00B\x00a\x00s\x00e\x00\x00\x00C\x00a\x00c\x00h\x00e\x00 \x00T\x00r\x00i\x00m\x00s\x00\x00\x00C\x00a\x00c\x00h\x00e\x00 \x00E\x00n\x00t\x00r\x00i\x00e\x00s\x00\x00\x00C\x00a\x00c\x00h\x00e\x00 \x00T\x00u\x00r\x00n\x00o\x00v\x00e\x00r\x00 \x00R\x00a\x00t\x00e\x00\x00\x00\x00\x00', 'Counter Types': b'6\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x005\x003\x007\x000\x000\x003\x000\x000\x008\x00\x00\x001\x000\x007\x003\x009\x003\x009\x004\x005\x009\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x00\x00\x00', 'FileMappingSize': 131072, 'IsMultiInstance': 1, 'Library': '%systemroot%\\system32\\netfxperf.dll', 'Open': 'OpenPerformanceData', 'InstallType': 1, 'PerfIniFile': 'netmemorycache_d.ini', 'First Counter': 6884, 'Last Counter': 6898, 'First Help': 6885, 'Last Help': 6899, 'Object List': '6884'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">.NETFramework Service </span>

|Performance|
| :---: |
|`{'Close': 'CloseCtrs', 'Collect': 'CollectCtrs', 'Library': '%systemroot%\\system32\\mscoree.dll', 'Open': 'OpenCtrs', 'InstallType': 1, 'PerfIniFile': 'corperfmonsymbols_d.ini', 'First Counter': 8740, 'Last Counter': 8914, 'First Help': 8741, 'Last Help': 8915}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">1394ohci Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\1394ohci.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@1394.inf,%PCI\CC_0C0010.DeviceDesc%;1394 OHCI Compliant Host Controller`|`1394.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">3ware Service </span>



##### Service Parameters
  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AarSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\AarSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ACPI Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|Tag|Group|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\ACPI.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_CRITICAL`|`@acpi.inf,%ACPI.SvcDesc%;Microsoft ACPI Driver`|`acpi.inf`|`0x02`|`Core`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AcpiDev Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\AcpiDev.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x19`|`@acpidev.inf,%AcpiDev.SvcDesc%;ACPI Devices driver`|`acpidev.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">acpiex Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`Microsoft ACPIEx Driver`|`SERVICE_ERROR_CRITICAL`|`Boot Bus Extender`|`System32\Drivers\acpiex.sys`|`SERVICE_BOOT_START`|`0x07`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">acpipagr Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\acpipagr.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@acpipagr.inf,%SvcDesc%;ACPI Processor Aggregator Driver`|`acpipagr.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AcpiPmi Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\acpipmi.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@acpipmi.inf,%AcpiPmi.SvcDesc%;ACPI Power Meter Driver`|`acpipmi.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">acpitime Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\acpitime.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x23`|`@acpitime.inf,%AcpiTime.SvcDesc%;ACPI Wake Alarm Driver`|`acpitime.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Acx01000 Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\Acx01000.sys,-1000`|`SERVICE_ERROR_NORMAL`|`WdfLoadGroup`|`system32\drivers\Acx01000.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ADOVMPPackage Service </span>

|Final|
| :---: |
|`{'ActivationEnabled': 0}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ADP80XX Service </span>



##### Service Parameters
  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">adsi Service </span>

|Cache|Options|tracing|
| :---: | :---: | :---: |
|`{'NeverCacheDS': 0, 'PerMachine': 0}`|`Options`|`{}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AFD Service </span>



##### Service Parameters
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">afunix Service </span>



##### Service Parameters
  
Winsock : `Winsock`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ahcache Service </span>

|Description|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`@%systemroot%\system32\drivers\ahcache.sys,-101`|`@%systemroot%\system32\drivers\ahcache.sys,-102`|`SERVICE_ERROR_NORMAL`|`system32\DRIVERS\ahcache.sys`|`SERVICE_SYSTEM_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AJRouter Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\AJRouter.dll`  
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


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`31d1811f-ac3f-3745-9e0c-7e7b0c2f4b55`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`50 00 72 00 6f 00 74 00 65 00 63 00 74 00 65 00 64 00 50 00 72 00 65 00 66 00 69 00 78 00 5c 00 4c 00 6f 00 63 00 61 00 6c 00 53 00 65 00 72 00 76 00 69 00 63 00 65 00 5c 00 4d 00 53 00 41 00 4a 00 50 00 69 00 70 00 65 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ALG Service </span>

|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\Alg.exe,-113`|`@%SystemRoot%\system32\Alg.exe,-112`|`SERVICE_ERROR_NORMAL`|`84 03 00 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 e0 93 04 00 00 00 00 00 00 00 00 00`|`%SystemRoot%\System32\alg.exe`|`NT AUTHORITY\LocalService`|`['SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeImpersonatePrivilege']`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">amdgpio2 Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\amdgpio2.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x03`|`@amdgpio2.inf,%GPIO.SvcDesc%;AMD GPIO Client Driver`|`amdgpio2.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">amdi2c Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\amdi2c.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x02`|`SpbCx`|`@amdi2c.inf,%amdi2c.SVCDESC%;AMD I2C Controller Service`|`amdi2c.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AmdK8 Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|MofImagePath|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\amdk8.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x1c`|`@cpu.inf,%AmdK8.SvcDesc%;AMD K8 Processor Driver`|`cpu.inf`|`%SystemRoot%\System32\drivers\processr.sys`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AmdPPM Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|MofImagePath|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\amdppm.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x1d`|`@cpu.inf,%AmdPPM.SvcDesc%;AMD Processor Driver`|`cpu.inf`|`%SystemRoot%\System32\drivers\processr.sys`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">amdsata Service </span>



##### Service Parameters
  
Device : `{'EnableQueryAccessAlignment': 1, 'AmdSataFua': 0, 'AmdSataChannelFlags': 1, 'AmdSataWMI': 0, 'AmdSataCCC': 255, 'AmdSataCCCTV': 65535, 'AmdSataCCCCC': 32, 'AmdSataSgl': 256, 'AmdSataHints': 1, 'AmdSataDevSlp': 1000, 'AmdSataSWSP': 15}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">amdsbs Service </span>

|Settings|
| :---: |
|`Settings`|



##### Service Parameters
  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">amdxata Service </span>



##### Service Parameters
  
AmdXataOptions : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AppID Service </span>



##### Service Parameters
  
DebugFlags : `0x00`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AppIDSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\appidsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`279c2ad0-b879-d640-9b97-cf3f8b7b5d60`|`SERVICE_TRIGGER_TYPE_CUSTOM`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Appinfo Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\appinfo.dll`  
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
    Access: 0x2019d
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

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`32 00 30 00 31 00 65 00 66 00 39 00 39 00 61 00 2d 00 37 00 66 00 61 00 30 00 2d 00 34 00 34 00 34 00 63 00 2d 00 39 00 33 00 39 00 39 00 2d 00 31 00 39 00 62 00 61 00 38 00 34 00 66 00 31 00 32 00 61 00 31 00 61 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`35 00 66 00 35 00 34 00 63 00 65 00 37 00 64 00 2d 00 35 00 62 00 37 00 39 00 2d 00 34 00 31 00 37 00 35 00 2d 00 38 00 35 00 38 00 34 00 2d 00 63 00 62 00 36 00 35 00 33 00 31 00 33 00 61 00 30 00 65 00 39 00 38 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`66 00 64 00 37 00 61 00 30 00 35 00 32 00 33 00 2d 00 64 00 63 00 37 00 30 00 2d 00 34 00 33 00 64 00 64 00 2d 00 39 00 62 00 32 00 65 00 2d 00 39 00 63 00 35 00 65 00 64 00 34 00 38 00 32 00 32 00 35 00 62 00 31 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`35 00 38 00 65 00 36 00 30 00 34 00 65 00 38 00 2d 00 39 00 61 00 64 00 62 00 2d 00 34 00 64 00 32 00 65 00 2d 00 61 00 34 00 36 00 34 00 2d 00 33 00 62 00 30 00 36 00 38 00 33 00 66 00 62 00 31 00 34 00 38 00 30 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 34 00 39 00 37 00 42 00 35 00 37 00 44 00 2d 00 32 00 45 00 36 00 36 00 2d 00 34 00 32 00 34 00 46 00 2d 00 41 00 30 00 43 00 36 00 2d 00 31 00 35 00 37 00 43 00 44 00 35 00 44 00 34 00 31 00 37 00 30 00 30 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">applockerfltr Service </span>

|Instances|
| :---: |
|`Instances`|
  
Security : 
```
Owner: S-1-0-32-544
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x2008d
    SID: S-1-0-32-545
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
    Flags: 0x02
    Access: 0x201fd
    SID: S-1-0-19
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x201fd
    SID: S-1-0-80-2078495744-2416903469-4072184685-3943858305-976987417
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x2008d
    SID: S-1-0-2-1

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AppMgmt Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\appmgmts.dll`  
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
    Access: 0x2008d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x9d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x8d
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AppReadiness Service </span>



##### Service Parameters
  
ServiceDLL : `%SystemRoot%\system32\AppReadiness.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AppVClient Service </span>
  
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
    Access: 0xf01ff
    SID: S-1-0-32-544
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
#### <span style="text-align: center; font-size:2em;">AppvStrm Service </span>

|Instances|
| :---: |
|`Instances`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AppvVemgr Service </span>

|Instances|
| :---: |
|`Instances`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AppvVfs Service </span>

|Instances|
| :---: |
|`Instances`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AppXSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\appxdeploymentserver.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  
Security : 
```
Owner: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
Group: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`41 00 45 00 32 00 44 00 43 00 39 00 30 00 31 00 2d 00 33 00 31 00 32 00 44 00 2d 00 34 00 31 00 44 00 46 00 2d 00 38 00 42 00 37 00 39 00 2d 00 45 00 38 00 33 00 35 00 45 00 36 00 33 00 44 00 42 00 38 00 37 00 34 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">arcsas Service </span>



##### Service Parameters
  
Device : `{'DriverParameter': 'BLEDCheck=1'}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AssignedAccessManagerSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\assignedaccessmanagersvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 18 bc a3 2c 0f c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AsyncMac Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Description|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\asyncmac.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@%systemroot%\system32\mprmsg.dll,-32000`|`@%systemroot%\system32\mprmsg.dll,-32000`|`netrasa.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">atapi Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\atapi.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_CRITICAL`|`SCSI Miniport`|`0x1e`|`@mshdc.inf,%idechannel.DeviceDesc%;IDE Channel`|`mshdc.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AudioEndpointBuilder Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\AudioEndpointBuilder.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Audiosrv Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\Audiosrv.dll`  
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
    Access: 0x2008d
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-3-1024-1692970155-4054893335-185714091-3362601943-3526593181-1159816984-2199008581-497492991

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">autotimesvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\autotimesvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 d0 be a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">AxInstSV Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\AxInstSV.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">b06bdrv Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\bxvbda.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`System Bus Extender`|`0x02`|`@netbvbda.inf,%vbd_srv_desc%;QLogic Network Adapter VBD`|`netbvbda.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">bam Service </span>

|Description|DisplayName|ErrorControl|ImagePath|Start|Type|WOW64|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\bam.sys,-101`|`@%SystemRoot%\system32\drivers\bam.sys,-100`|`SERVICE_ERROR_NORMAL`|`system32\drivers\bam.sys`|`SERVICE_SYSTEM_START`|`SERVICE_KERNEL_DRIVER`|`0x14c`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BasicDisplay Service </span>



##### Service Parameters
  
SingleDeviceInstall : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BasicRender Service </span>



##### Service Parameters
  
SingleDeviceInstall : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BattC Service </span>

|MofImagePath|
| :---: |
|`system32\drivers\battc.sys`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BcastDVRUserService Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\BcastDVRUserService.dll`  
ServiceDllUnloadOnStop : `0x00`  
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
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">bcmfn2 Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\bcmfn2.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x04`|`@bcmfn2.inf,%bcmfn2.SVCDESC%;bcmfn2 Service`|`bcmfn2.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BDESVC Service </span>

|State|
| :---: |
|`{}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\bdesvc.dll`  
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
    Access: 0xe00ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-32-545
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-11
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf00ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 30 bc a3 2b 18 83 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Beep Service </span>

|DisplayName|ErrorControl|Group|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`Beep`|`SERVICE_ERROR_NORMAL`|`Base`|`SERVICE_SYSTEM_START`|`0x02`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BFE Service </span>



##### Service Parameters
  
Policy  
BootTime : `BootTime`  
Persistent  
Filter
|GUID|Data|
| :---: | :---: |
|{074f7f68-ee10-428a-89d1-ba78f6c327ca}|`01 10 08 00 cc cc cc cc 78 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 58 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 58 01 00 00 01 10 08 00 cc cc cc cc 48 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 68 7f 4f 07 10 ee 8a 42 89 d1 ba 78 f6 c3 27 ca 04 00 02 00 08 00 02 00 02 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 90 99 49 61 b6 3c 84 4e b9 50 53 b9 4b 69 64 f3 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0f 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`|
|{07a24961-a760-4e80-b263-6d275e1b09cb}|`01 10 08 00 cc cc cc cc a0 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 80 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 80 01 00 00 01 10 08 00 cc cc cc cc 70 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 61 49 a2 07 60 a7 80 4e b2 63 6d 27 5e 1b 09 cb 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 00 01 39 41 4c 56 32 4b bc 1d 71 80 48 35 4d 7c 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 04 00 00 00 04 00 00 00 14 00 02 00 01 00 00 00 18 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0b 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 1c 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 06 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00`|
|{0aa7fff8-919f-453c-928c-28a12122ba38}|`01 10 08 00 cc cc cc cc a0 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 80 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 80 01 00 00 01 10 08 00 cc cc cc cc 70 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 f8 ff a7 0a 9f 91 3c 45 92 8c 28 a1 21 22 ba 38 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 3b 39 72 4a 9f 31 bc 44 84 c3 ba 54 dc b3 b6 b4 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 04 00 00 00 04 00 00 00 14 00 02 00 01 00 00 00 18 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0e 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 1c 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 06 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00`|
|{0c3be01b-fe70-4cc4-89dc-c07996b67e6d}|`01 10 08 00 cc cc cc cc d0 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 b0 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 b0 01 00 00 01 10 08 00 cc cc cc cc a0 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 1b e0 3b 0c 70 fe c4 4c 89 dc c0 79 96 b6 7e 6d 04 00 02 00 08 00 02 00 02 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 04 00 00 00 04 00 00 00 14 00 02 00 02 00 00 00 18 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 06 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 20 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 02 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 06 00 00 00 03 00 00 00 03 00 00 00 00 00 80 00 fa 78 bc 71 7c f1 97 49 a6 02 6a bb 26 1f 35 1c 00 00 00 00 0d 00 00 00 0d 00 00 00 1c 00 02 00 01 00 00 00 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00`|
|{0c41d586-9c19-4e01-9d66-b5b98a97576e}|`01 10 08 00 cc cc cc cc a0 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 80 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 80 01 00 00 01 10 08 00 cc cc cc cc 70 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 86 d5 41 0c 19 9c 01 4e 9d 66 b5 b9 8a 97 57 6e 04 00 02 00 08 00 02 00 02 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 90 99 49 61 b6 3c 84 4e b9 50 53 b9 4b 69 64 f3 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 04 00 00 00 04 00 00 00 14 00 02 00 01 00 00 00 18 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 1c 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 06 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00`|
|{0ccc96a3-8c5c-45e2-b80e-7e37b16cc1ad}|`01 10 08 00 cc cc cc cc 78 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 58 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 58 01 00 00 01 10 08 00 cc cc cc cc 48 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 a3 96 cc 0c 5c 8c e2 45 b8 0e 7e 37 b1 6c c1 ad 04 00 02 00 08 00 02 00 02 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`|
|{1165065e-4996-4338-abaf-4b8556b4d431}|`01 10 08 00 cc cc cc cc d0 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 b0 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 b0 01 00 00 01 10 08 00 cc cc cc cc a0 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 5e 06 65 11 96 49 38 43 ab af 4b 85 56 b4 d4 31 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 04 00 00 00 04 00 00 00 14 00 02 00 02 00 00 00 18 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0a 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 20 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 02 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 06 00 00 00 03 00 00 00 03 00 00 00 00 00 80 00 fa 78 bc 71 7c f1 97 49 a6 02 6a bb 26 1f 35 1c 00 00 00 00 0d 00 00 00 0d 00 00 00 1c 00 02 00 01 00 00 00 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00`|
|{12c38916-82ac-4737-8f38-b6957ffebad6}|`01 10 08 00 cc cc cc cc a0 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 80 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 80 01 00 00 01 10 08 00 cc cc cc cc 70 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 16 89 c3 12 ac 82 37 47 8f 38 b6 95 7f fe ba d6 04 00 02 00 08 00 02 00 02 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 ff bd f9 65 2d 3b 5d 4e b8 c6 c7 20 65 1f e8 98 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 04 00 00 00 04 00 00 00 14 00 02 00 01 00 00 00 18 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 04 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 1c 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 06 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00`|
|{13bfd422-6f75-4408-8924-9400ec0cb19c}|`01 10 08 00 cc cc cc cc 78 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 58 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 58 01 00 00 01 10 08 00 cc cc cc cc 48 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 22 d4 bf 13 75 6f 08 44 89 24 94 00 ec 0c b1 9c 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 e7 9f cd e1 b5 f4 73 42 96 c0 59 2e 48 7b 86 50 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 15 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`|
|{17043d46-fac2-4561-bca1-0c7a05e95f5f}|`01 10 08 00 cc cc cc cc 98 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 78 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 78 01 00 00 01 10 08 00 cc cc cc cc 68 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 46 3d 04 17 c2 fa 61 45 bc a1 0c 7a 05 e9 5f 5f 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 e7 9f cd e1 b5 f4 73 42 96 c0 59 2e 48 7b 86 50 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 02 01 00 00 00 01 00 00 00 01 00 00 00 02 00 00 00 14 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 24 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 1f 00 00 00 00 00 00 00 1f 00 00 00 49 00 6e 00 74 00 65 00 72 00 66 00 61 00 63 00 65 00 20 00 55 00 6e 00 2d 00 71 00 75 00 61 00 72 00 61 00 6e 00 74 00 69 00 6e 00 65 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 00 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 02 00 00 00 6c 7c 53 97 a3 d9 67 47 a3 81 e9 42 67 5c d9 20 00 00 00 00 03 00 00 00 03 00 00 00 83 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 06 00 00 00 03 00 00 00 03 00 00 00 04 00 00 00 00 00 00 20 08 00 00 10 00 00 00 00`|
|{2db25e6c-f07a-44f4-b6c8-50a330d2790b}|`01 10 08 00 cc cc cc cc d8 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 b8 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 b8 01 00 00 01 10 08 00 cc cc cc cc a8 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 6c 5e b2 2d 7a f0 f4 44 b6 c8 50 a3 30 d2 79 0b 04 00 02 00 08 00 02 00 02 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 66 dc 69 ba 76 51 79 49 9c 89 26 a7 b4 6a 83 27 01 00 00 00 01 00 00 00 00 00 00 00 03 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 19 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 03 00 00 00 de 90 f9 89 98 e7 6d 4e ab 76 7c 95 58 29 2e 6f 00 00 00 00 03 00 00 00 03 00 00 00 83 00 00 00 dc 66 11 51 8c 7a a7 4a b5 33 95 ab 59 fb 03 40 00 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 08 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 00 00 00 0c 02 00 00 00 00 00 00 00`|
|{2dd96961-5757-434f-b617-34e732517c0e}|`01 10 08 00 cc cc cc cc d8 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 b8 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 b8 01 00 00 01 10 08 00 cc cc cc cc a8 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 61 69 d9 2d 57 57 4f 43 b6 17 34 e7 32 51 7c 0e 04 00 02 00 08 00 02 00 02 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 66 dc 69 ba 76 51 79 49 9c 89 26 a7 b4 6a 83 27 01 00 00 00 01 00 00 00 00 00 00 00 03 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 17 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 03 00 00 00 de 90 f9 89 98 e7 6d 4e ab 76 7c 95 58 29 2e 6f 00 00 00 00 03 00 00 00 03 00 00 00 83 00 00 00 dc 66 11 51 8c 7a a7 4a b5 33 95 ab 59 fb 03 40 00 00 00 00 03 00 00 00 03 00 00 00 0e 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 08 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 00 00 00 0c 02 00 00 00 00 00 00 00`|
|{3180114b-8338-4740-9a16-444134ad62f4}|`01 10 08 00 cc cc cc cc 98 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 78 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 78 01 00 00 01 10 08 00 cc cc cc cc 68 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 4b 11 80 31 38 83 40 47 9a 16 44 41 34 ad 62 f4 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 02 01 00 00 00 01 00 00 00 01 00 00 00 02 00 00 00 14 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 23 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 1f 00 00 00 00 00 00 00 1f 00 00 00 49 00 6e 00 74 00 65 00 72 00 66 00 61 00 63 00 65 00 20 00 55 00 6e 00 2d 00 71 00 75 00 61 00 72 00 61 00 6e 00 74 00 69 00 6e 00 65 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 00 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 02 00 00 00 6c 7c 53 97 a3 d9 67 47 a3 81 e9 42 67 5c d9 20 00 00 00 00 03 00 00 00 03 00 00 00 83 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 06 00 00 00 03 00 00 00 03 00 00 00 04 00 00 00 00 00 00 08 02 00 00 10 00 00 00 00`|
|{3697a558-3ed3-49be-a4c1-c1a4448653b4}|`01 10 08 00 cc cc cc cc d8 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 b8 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 b8 01 00 00 01 10 08 00 cc cc cc cc a8 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 58 a5 97 36 d3 3e be 49 a4 c1 c1 a4 44 86 53 b4 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 e7 9f cd e1 b5 f4 73 42 96 c0 59 2e 48 7b 86 50 66 dc 69 ba 76 51 79 49 9c 89 26 a7 b4 6a 83 27 01 00 00 00 01 00 00 00 00 00 00 00 03 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 1c 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 03 00 00 00 de 90 f9 89 98 e7 6d 4e ab 76 7c 95 58 29 2e 6f 00 00 00 00 03 00 00 00 03 00 00 00 83 00 00 00 dc 66 11 51 8c 7a a7 4a b5 33 95 ab 59 fb 03 40 00 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 08 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 00 00 00 30 08 00 00 00 00 00 00 00`|
|{375fb39b-08c6-40f2-bdf2-08fa63f970a2}|`01 10 08 00 cc cc cc cc d8 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 b8 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 b8 01 00 00 01 10 08 00 cc cc cc cc a8 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 9b b3 5f 37 c6 08 f2 40 bd f2 08 fa 63 f9 70 a2 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 66 dc 69 ba 76 51 79 49 9c 89 26 a7 b4 6a 83 27 01 00 00 00 01 00 00 00 00 00 00 00 03 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 18 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 03 00 00 00 de 90 f9 89 98 e7 6d 4e ab 76 7c 95 58 29 2e 6f 00 00 00 00 03 00 00 00 03 00 00 00 83 00 00 00 dc 66 11 51 8c 7a a7 4a b5 33 95 ab 59 fb 03 40 00 00 00 00 03 00 00 00 03 00 00 00 0e 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 08 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 00 00 00 0c 02 00 00 00 00 00 00 00`|
|{3a90a266-1519-4d23-911b-e84cd0f02ab8}|`01 10 08 00 cc cc cc cc d8 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 b8 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 b8 01 00 00 01 10 08 00 cc cc cc cc a8 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 66 a2 90 3a 19 15 23 4d 91 1b e8 4c d0 f0 2a b8 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 02 01 00 00 00 01 00 00 00 01 00 00 00 04 00 00 00 14 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 27 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 1f 00 00 00 00 00 00 00 1f 00 00 00 49 00 6e 00 74 00 65 00 72 00 66 00 61 00 63 00 65 00 20 00 55 00 6e 00 2d 00 71 00 75 00 61 00 72 00 61 00 6e 00 74 00 69 00 6e 00 65 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 00 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 04 00 00 00 2b ef 71 39 3e 62 9a 4f 8c b1 6e 79 b8 06 b9 a7 00 00 00 00 01 00 00 00 01 00 00 00 11 00 00 00 af a1 1b 0c 65 57 3f 45 af 22 a8 f7 91 ac 77 5b 00 00 00 00 02 00 00 00 02 00 00 00 22 02 00 00 4d 60 5a c3 2b d2 1a 4e 91 b4 68 f6 74 ee 67 4b 00 00 00 00 02 00 00 00 02 00 00 00 23 02 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 08 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 c2 e1 00 10 00 00 00 00`|
|{4137b143-2770-43d4-91a2-55bb0a069830}|`01 10 08 00 cc cc cc cc 98 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 78 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 78 01 00 00 01 10 08 00 cc cc cc cc 68 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 43 b1 37 41 70 27 d4 43 91 a2 55 bb 0a 06 98 30 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 e7 9f cd e1 b5 f4 73 42 96 c0 59 2e 48 7b 86 50 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 02 01 00 00 00 01 00 00 00 01 00 00 00 02 00 00 00 14 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 22 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 1f 00 00 00 00 00 00 00 1f 00 00 00 49 00 6e 00 74 00 65 00 72 00 66 00 61 00 63 00 65 00 20 00 55 00 6e 00 2d 00 71 00 75 00 61 00 72 00 61 00 6e 00 74 00 69 00 6e 00 65 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 00 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 02 00 00 00 de 90 f9 89 98 e7 6d 4e ab 76 7c 95 58 29 2e 6f 00 00 00 00 03 00 00 00 03 00 00 00 83 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 08 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 20 08 00 00 10 00 00 00 00`|
|{4d9581d2-aef8-4993-84cd-b986ced80d42}|`01 10 08 00 cc cc cc cc a0 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 80 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 80 01 00 00 01 10 08 00 cc cc cc cc 70 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 d2 81 95 4d f8 ae 93 49 84 cd b9 86 ce d8 0d 42 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 90 99 49 61 b6 3c 84 4e b9 50 53 b9 4b 69 64 f3 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 04 00 00 00 04 00 00 00 14 00 02 00 01 00 00 00 18 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 07 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 1c 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 06 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00`|
|{4e718c57-c397-4221-9fbb-14fd51701d6a}|`01 10 08 00 cc cc cc cc d8 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 b8 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 b8 01 00 00 01 10 08 00 cc cc cc cc a8 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 57 8c 71 4e 97 c3 21 42 9f bb 14 fd 51 70 1d 6a 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 e7 9f cd e1 b5 f4 73 42 96 c0 59 2e 48 7b 86 50 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 02 01 00 00 00 01 00 00 00 01 00 00 00 04 00 00 00 14 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 26 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 1f 00 00 00 00 00 00 00 1f 00 00 00 49 00 6e 00 74 00 65 00 72 00 66 00 61 00 63 00 65 00 20 00 55 00 6e 00 2d 00 71 00 75 00 61 00 72 00 61 00 6e 00 74 00 69 00 6e 00 65 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 00 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 04 00 00 00 2b ef 71 39 3e 62 9a 4f 8c b1 6e 79 b8 06 b9 a7 00 00 00 00 01 00 00 00 01 00 00 00 11 00 00 00 af a1 1b 0c 65 57 3f 45 af 22 a8 f7 91 ac 77 5b 00 00 00 00 02 00 00 00 02 00 00 00 44 00 00 00 4d 60 5a c3 2b d2 1a 4e 91 b4 68 f6 74 ee 67 4b 00 00 00 00 02 00 00 00 02 00 00 00 43 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 08 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 08 83 07 10 00 00 00 00`|
|{567d3836-3f5b-4067-b9c4-952f677010a2}|`01 10 08 00 cc cc cc cc 98 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 78 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 78 01 00 00 01 10 08 00 cc cc cc cc 68 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 36 38 7d 56 5b 3f 67 40 b9 c4 95 2f 67 70 10 a2 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 02 01 00 00 00 01 00 00 00 01 00 00 00 02 00 00 00 14 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 25 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 1f 00 00 00 00 00 00 00 1f 00 00 00 49 00 6e 00 74 00 65 00 72 00 66 00 61 00 63 00 65 00 20 00 55 00 6e 00 2d 00 71 00 75 00 61 00 72 00 61 00 6e 00 74 00 69 00 6e 00 65 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 00 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 02 00 00 00 2b ef 71 39 3e 62 9a 4f 8c b1 6e 79 b8 06 b9 a7 00 00 00 00 01 00 00 00 01 00 00 00 3a 00 00 00 af a1 1b 0c 65 57 3f 45 af 22 a8 f7 91 ac 77 5b 00 00 00 00 02 00 00 00 02 00 00 00 87 00 00 00 00 00 00 00 00 e0 00 10 00 00 00 00`|
|{5b0cb2e2-ab87-4974-9f1c-2f22a654eeb9}|`01 10 08 00 cc cc cc cc a0 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 80 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 80 01 00 00 01 10 08 00 cc cc cc cc 70 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 e2 b2 0c 5b 87 ab 74 49 9f 1c 2f 22 a6 54 ee b9 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 60 3b b0 7f 8d 7b fa 4d ba dd 98 01 76 fc 4e 12 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 04 00 00 00 04 00 00 00 14 00 02 00 01 00 00 00 18 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0c 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 1c 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 06 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00`|
|{64e55933-15a5-495d-a928-ccca43d44875}|`01 10 08 00 cc cc cc cc 78 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 58 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 58 01 00 00 01 10 08 00 cc cc cc cc 48 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 33 59 e5 64 a5 15 5d 49 a9 28 cc ca 43 d4 48 75 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 ff bd f9 65 2d 3b 5d 4e b8 c6 c7 20 65 1f e8 98 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 14 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`|
|{716b48eb-0a35-4a76-92ab-1d987230d288}|`01 10 08 00 cc cc cc cc d0 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 b0 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 b0 01 00 00 01 10 08 00 cc cc cc cc a0 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 eb 48 6b 71 35 0a 76 4a 92 ab 1d 98 72 30 d2 88 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 e7 9f cd e1 b5 f4 73 42 96 c0 59 2e 48 7b 86 50 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 04 00 00 00 04 00 00 00 14 00 02 00 02 00 00 00 18 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 09 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 20 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 02 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 06 00 00 00 03 00 00 00 03 00 00 00 00 00 80 00 fa 78 bc 71 7c f1 97 49 a6 02 6a bb 26 1f 35 1c 00 00 00 00 0d 00 00 00 0d 00 00 00 1c 00 02 00 01 00 00 00 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00`|
|{8b50e2ec-7cF0-4b71-b42e-5b0536f6cab8}|`01 10 08 00 cc cc cc cc 98 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 78 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 78 01 00 00 01 10 08 00 cc cc cc cc 68 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 ec e2 50 8b f0 7c 71 4b b4 2e 5b 05 36 f6 ca b8 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 02 01 00 00 00 01 00 00 00 01 00 00 00 02 00 00 00 14 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 21 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 1f 00 00 00 00 00 00 00 1f 00 00 00 49 00 6e 00 74 00 65 00 72 00 66 00 61 00 63 00 65 00 20 00 55 00 6e 00 2d 00 71 00 75 00 61 00 72 00 61 00 6e 00 74 00 69 00 6e 00 65 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 00 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 02 00 00 00 de 90 f9 89 98 e7 6d 4e ab 76 7c 95 58 29 2e 6f 00 00 00 00 03 00 00 00 03 00 00 00 83 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 08 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 08 02 00 00 10 00 00 00 00`|
|{91ffecf0-0a9e-4572-95f1-a7111af86967}|`01 10 08 00 cc cc cc cc 78 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 58 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 58 01 00 00 01 10 08 00 cc cc cc cc 48 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 f0 ec ff 91 9e 0a 72 45 95 f1 a7 11 1a f8 69 67 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 90 99 49 61 b6 3c 84 4e b9 50 53 b9 4b 69 64 f3 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 13 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`|
|{935b7f48-0ede-44dd-9bc2-e00bb635cda3}|`01 10 08 00 cc cc cc cc 98 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 78 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 78 01 00 00 01 10 08 00 cc cc cc cc 68 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 48 7f 5b 93 de 0e dd 44 9b c2 e0 0b b6 35 cd a3 04 00 02 00 08 00 02 00 02 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 24 cc 2a a8 e1 4e e1 4e b4 65 fd 1d 25 cb 10 a4 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 01 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 1d 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 08 00 00 00 03 00 00 00 03 00 00 00 00 00 0c 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00`|
|{941dad9d-7b1a-4354-997b-00cf1aa9b35c}|`01 10 08 00 cc cc cc cc 98 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 78 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 78 01 00 00 01 10 08 00 cc cc cc cc 68 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 9d ad 1d 94 1a 7b 54 43 99 7b 00 cf 1a a9 b3 5c 04 00 02 00 08 00 02 00 02 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 18 48 96 7b c7 19 3a 49 b7 1f 83 2c 36 84 d2 8c 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 01 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 1e 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 08 00 00 00 03 00 00 00 03 00 00 00 00 00 0c 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00`|
|{a47525e2-725b-4888-8af1-ba5a60c04f4d}|`01 10 08 00 cc cc cc cc 78 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 58 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 58 01 00 00 01 10 08 00 cc cc cc cc 48 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 e2 25 75 a4 5b 72 88 48 8a f1 ba 5a 60 c0 4f 4d 04 00 02 00 08 00 02 00 02 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 e7 9f cd e1 b5 f4 73 42 96 c0 59 2e 48 7b 86 50 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`|
|{b02a4013-b6b5-4859-9168-1e3299e43b24}|`01 10 08 00 cc cc cc cc 78 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 58 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 58 01 00 00 01 10 08 00 cc cc cc cc 48 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 13 40 2a b0 b5 b6 59 48 91 68 1e 32 99 e4 3b 24 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 02 01 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 1f 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 1f 00 00 00 00 00 00 00 1f 00 00 00 49 00 6e 00 74 00 65 00 72 00 66 00 61 00 63 00 65 00 20 00 55 00 6e 00 2d 00 71 00 75 00 61 00 72 00 61 00 6e 00 74 00 69 00 6e 00 65 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 00 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 08 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00`|
|{b6b2ca61-fb98-4422-adc2-e7cf56b3680c}|`01 10 08 00 cc cc cc cc a0 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 80 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 80 01 00 00 01 10 08 00 cc cc cc cc 70 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 61 ca b2 b6 98 fb 22 44 ad c2 e7 cf 56 b3 68 0c 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 d1 57 8d c3 a7 05 33 4c 90 4f 7f bc ee e6 0e 82 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 04 00 00 00 04 00 00 00 14 00 02 00 01 00 00 00 18 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0d 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 1c 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 06 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00`|
|{b6fdab6b-dcc6-43e3-99ce-7aeca65063a4}|`01 10 08 00 cc cc cc cc d8 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 b8 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 b8 01 00 00 01 10 08 00 cc cc cc cc a8 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 6b ab fd b6 c6 dc e3 43 99 ce 7a ec a6 50 63 a4 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 66 dc 69 ba 76 51 79 49 9c 89 26 a7 b4 6a 83 27 01 00 00 00 01 00 00 00 00 00 00 00 03 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 1b 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 03 00 00 00 de 90 f9 89 98 e7 6d 4e ab 76 7c 95 58 29 2e 6f 00 00 00 00 03 00 00 00 03 00 00 00 83 00 00 00 dc 66 11 51 8c 7a a7 4a b5 33 95 ab 59 fb 03 40 00 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 08 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 00 00 00 0c 02 00 00 00 00 00 00 00`|
|{be7cbdf4-b192-4aa5-94f8-1fb5c5ee07bc}|`01 10 08 00 cc cc cc cc a0 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 80 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 80 01 00 00 01 10 08 00 cc cc cc cc 70 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 f4 bd 7c be 92 b1 a5 4a 94 f8 1f b5 c5 ee 07 bc 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 ff bd f9 65 2d 3b 5d 4e b8 c6 c7 20 65 1f e8 98 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 04 00 00 00 04 00 00 00 14 00 02 00 01 00 00 00 18 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 1c 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 06 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00`|
|{c016105c-eb34-4519-a5fd-5f4e4ad4d18e}|`01 10 08 00 cc cc cc cc 78 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 58 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 58 01 00 00 01 10 08 00 cc cc cc cc 48 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 5c 10 16 c0 34 eb 19 45 a5 fd 5f 4e 4a d4 d1 8e 04 00 02 00 08 00 02 00 02 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 ff bd f9 65 2d 3b 5d 4e b8 c6 c7 20 65 1f e8 98 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`|
|{c42f1cd6-3a95-4ae2-a513-793c3ae610c7}|`01 10 08 00 cc cc cc cc d8 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 b8 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 b8 01 00 00 01 10 08 00 cc cc cc cc a8 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 d6 1c 2f c4 95 3a e2 4a a5 13 79 3c 3a e6 10 c7 04 00 02 00 08 00 02 00 02 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 e7 9f cd e1 b5 f4 73 42 96 c0 59 2e 48 7b 86 50 66 dc 69 ba 76 51 79 49 9c 89 26 a7 b4 6a 83 27 01 00 00 00 01 00 00 00 00 00 00 00 03 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 1a 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 03 00 00 00 de 90 f9 89 98 e7 6d 4e ab 76 7c 95 58 29 2e 6f 00 00 00 00 03 00 00 00 03 00 00 00 83 00 00 00 dc 66 11 51 8c 7a a7 4a b5 33 95 ab 59 fb 03 40 00 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 08 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 00 00 00 30 08 00 00 00 00 00 00 00`|
|{c970a45d-57f9-4e32-a5bd-886a9662641e}|`01 10 08 00 cc cc cc cc d0 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 b0 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 b0 01 00 00 01 10 08 00 cc cc cc cc a0 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 5d a4 70 c9 f9 57 32 4e a5 bd 88 6a 96 62 64 1e 04 00 02 00 08 00 02 00 02 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 e7 9f cd e1 b5 f4 73 42 96 c0 59 2e 48 7b 86 50 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 04 00 00 00 04 00 00 00 14 00 02 00 02 00 00 00 18 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 05 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 20 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 02 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 06 00 00 00 03 00 00 00 03 00 00 00 00 00 80 00 fa 78 bc 71 7c f1 97 49 a6 02 6a bb 26 1f 35 1c 00 00 00 00 0d 00 00 00 0d 00 00 00 1c 00 02 00 01 00 00 00 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00`|
|{cbfb56db-3c85-4543-9bc2-76ea28cdd74e}|`01 10 08 00 cc cc cc cc 78 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 58 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 58 01 00 00 01 10 08 00 cc cc cc cc 48 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 db 56 fb cb 85 3c 43 45 9b c2 76 ea 28 cd d7 4e 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 16 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`|
|{d870c96c-75ee-46a6-8a02-8e4401a73423}|`01 10 08 00 cc cc cc cc 78 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 58 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 58 01 00 00 01 10 08 00 cc cc cc cc 48 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 6c c9 70 d8 ee 75 a6 46 8a 02 8e 44 01 a7 34 23 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 e7 9f cd e1 b5 f4 73 42 96 c0 59 2e 48 7b 86 50 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 02 01 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 14 00 02 00 01 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 20 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 1f 00 00 00 00 00 00 00 1f 00 00 00 49 00 6e 00 74 00 65 00 72 00 66 00 61 00 63 00 65 00 20 00 55 00 6e 00 2d 00 71 00 75 00 61 00 72 00 61 00 6e 00 74 00 69 00 6e 00 65 00 20 00 66 00 69 00 6c 00 74 00 65 00 72 00 00 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 01 00 00 00 3b e2 2c 63 67 51 5c 43 86 d7 e9 03 68 4a a8 0c 08 00 00 00 03 00 00 00 03 00 00 00 01 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00`|
|{dc95b53e-01cf-4058-821d-350b3d0d4676}|`01 10 08 00 cc cc cc cc b8 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 98 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 98 01 00 00 01 10 08 00 cc cc cc cc 88 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 3e b5 95 dc cf 01 58 40 82 1d 35 0b 3d 0d 46 76 04 00 02 00 08 00 02 00 02 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 01 00 00 00 01 00 00 00 01 00 00 00 02 00 00 00 14 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 02 00 00 00 2b ef 71 39 3e 62 9a 4f 8c b1 6e 79 b8 06 b9 a7 00 00 00 00 01 00 00 00 01 00 00 00 3a 00 00 00 af a1 1b 0c 65 57 3f 45 af 22 a8 f7 91 ac 77 5b 00 00 00 00 02 00 00 00 02 00 00 00 87 00 00 00 00 00 00 00 00 00 00 00 00 e0 00 10 00 00 00 00`|
|{f444c576-6e60-4ea2-9faa-80d57ed12cd2}|`01 10 08 00 cc cc cc cc b8 01 00 00 00 00 00 00 00 00 02 00 05 00 00 00 98 01 00 00 04 00 02 00 00 00 00 00 00 00 00 00 98 01 00 00 01 10 08 00 cc cc cc cc 88 01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 76 c5 44 f4 60 6e a2 4e 9f aa 80 d5 7e d1 2c d2 04 00 02 00 08 00 02 00 01 00 00 00 0c 00 02 00 08 00 00 00 10 00 02 00 97 2c b4 a3 04 9f 72 46 b8 7e ce e9 c4 83 25 7f 41 d4 cd b3 90 af ba 41 a7 45 7c 60 08 ff 23 01 01 00 00 00 01 00 00 00 01 00 00 00 02 00 00 00 14 00 02 00 02 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 04 00 00 00 04 00 00 00 18 00 02 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 35 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 40 00 46 00 69 00 72 00 65 00 77 00 61 00 6c 00 6c 00 41 00 50 00 49 00 2e 00 64 00 6c 00 6c 00 2c 00 2d 00 32 00 33 00 35 00 30 00 36 00 00 00 ca 16 cc de 33 3f 46 43 be 1e 8f b4 ae 0f 3d 62 08 00 00 00 ff ff ff ff ff ff ff ff 02 00 00 00 2b ef 71 39 3e 62 9a 4f 8c b1 6e 79 b8 06 b9 a7 00 00 00 00 01 00 00 00 01 00 00 00 3a 00 00 00 af a1 1b 0c 65 57 3f 45 af 22 a8 f7 91 ac 77 5b 00 00 00 00 02 00 00 00 02 00 00 00 87 00 00 00 00 00 00 00 00 00 00 00 00 e0 00 10 00 00 00 00`|
  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x20085
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe009f
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe009d
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x85
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf00ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">bindflt Service </span>

|Instances|
| :---: |
|`Instances`|



##### Service Parameters
  
DebugOptions : `0x00`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BITS Service </span>

|Performance|
| :---: |
|`{'Close': 'PerfMon_Close', 'Collect': 'PerfMon_Collect', 'Library': 'X:\\Windows\\System32\\bitsperf.dll', 'Open': 'PerfMon_Open', 'InstallType': 1, 'PerfIniFile': 'bitsctrs.ini', 'First Counter': 8966, 'Last Counter': 8982, 'First Help': 8967, 'Last Help': 8983, 'Object List': '8966'}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\qmgr.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  
Security : 
```
Owner: S-1-0-32-544
Group: S-1-0-32-544
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0xf01ff
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
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0xc0
    Access: 0xc0000
    SID: S-1-0-32-544

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BluetoothUserService Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\Microsoft.Bluetooth.UserService.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`2a305008-44b3-da4f-9be9-90576b8d46f0`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 38 bc a3 2f 02 92 09`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 48 bc a3 2f 02 92 09`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 58 bc a3 2f 02 92 09`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 68 bc a3 2f 02 92 09`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">bowser Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%systemroot%\system32\wkssvc.dll,-2000`|`@%systemroot%\system32\wkssvc.dll,-2001`|`SERVICE_ERROR_NORMAL`|`Network`|`system32\DRIVERS\bowser.sys`|`SERVICE_DEMAND_START`|`0x05`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BrokerInfrastructure Service </span>



##### Service Parameters
  
EnergyBudgetBgTaskPercentage : `0x0f`  
EnergyBudgetImportanceDecayPeriodDays : `0x07`  
EnergyBudgetRundownTarget : `0xb40`  
ServiceDll : `%SystemRoot%\System32\psmsrv.dll`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x20085
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x95
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf00ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Browser Service </span>



##### Service Parameters
  
MaintainServerList : `Auto`  
ServiceDll : `%SystemRoot%\System32\browser.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|Data1|Data2|DataType0|DataType1|DataType2|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`079e56b7-2184-e04e-ad10-86915afdad09`|`SERVICE_TRIGGER_TYPE_FIREWALL_PORT_EVENT`|`31 00 33 00 39 00 00 00 54 00 43 00 50 00 00 00 53 00 79 00 73 00 74 00 65 00 6d 00 00 00 00 00`|`31 00 33 00 37 00 00 00 55 00 44 00 50 00 00 00 53 00 79 00 73 00 74 00 65 00 6d 00 00 00 00 00`|`31 00 33 00 38 00 00 00 55 00 44 00 50 00 00 00 53 00 79 00 73 00 74 00 65 00 6d 00 00 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_STOP`|`38ed44a1-128e-e44d-9d96-e64740b1a524`|`SERVICE_TRIGGER_TYPE_FIREWALL_PORT_EVENT`|`31 00 33 00 39 00 00 00 54 00 43 00 50 00 00 00 53 00 79 00 73 00 74 00 65 00 6d 00 00 00 00 00`|`31 00 33 00 37 00 00 00 55 00 44 00 50 00 00 00 53 00 79 00 73 00 74 00 65 00 6d 00 00 00 00 00`|`31 00 33 00 38 00 00 00 55 00 44 00 50 00 00 00 53 00 79 00 73 00 74 00 65 00 6d 00 00 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BTAGService Service </span>



##### Service Parameters
  
Settings : `{}`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`2a305008-44b3-da4f-9be9-90576b8d46f0`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BthA2dp Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\BthA2dp.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@microsoft_bluetooth_a2dp.inf,%BthA2dp.ServiceDescription%;Microsoft Bluetooth A2dp driver`|`microsoft_bluetooth_a2dp_src.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BthAvctpSvc Service </span>



##### Service Parameters
  
Profiles : `Profiles`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`2a305008-44b3-da4f-9be9-90576b8d46f0`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
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
#### <span style="text-align: center; font-size:2em;">BthHFEnum Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\bthhfenum.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x01`|`@microsoft_bluetooth_hfp.inf,%BTHHFENUM_DISPLAY_NAME%;Microsoft Bluetooth Hands-Free Profile driver`|`microsoft_bluetooth_hfp_hf.infmicrosoft_bluetooth_hfp_ag.inf`|
  

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
#### <span style="text-align: center; font-size:2em;">BthMini Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\BTHMINI.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`PNP Filter`|`0x07`|`@bth.inf,%BTHMINI.SvcDesc%;Bluetooth Radio Driver`|`bth.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BTHMODEM Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\bthmodem.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@mdmbtmdm.inf,%BthModem.DisplayName%;Bluetooth Modem Communications Driver`|`bthspp.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BTHPORT Service </span>



##### Service Parameters
  
Devices : `{}`  
ExceptionDB : `ExceptionDB`  
HciBypassServices : `{'{00001108-0000-1000-8000-00805f9b34fb}': 1, '{00001110-0000-1000-8000-00805f9b34fb}': 1, '{00001112-0000-1000-8000-00805f9b34fb}': 1, '{0000111E-0000-1000-8000-00805f9b34fb}': 1, '{0000111F-0000-1000-8000-00805f9b34fb}': 1}`  
Keys : `{}`  
LocalServices : `LocalServices`  
PerDevices : `{'(Default)': ''}`  
PnpId : `{'RFCOMM': 'MS_RFCOMM', 'BTHBRB': 'MS_BTHBRB', 'BTHPAN': 'MS_BTHPAN'}`  
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
Restrictions : `Restrictions`  
ServiceGroups : `{'MonoAudio': b'{\x000\x000\x000\x000\x001\x001\x001\x00e\x00-\x000\x000\x000\x000\x00-\x001\x000\x000\x000\x00-\x008\x000\x000\x000\x00-\x000\x000\x008\x000\x005\x00f\x009\x00b\x003\x004\x00f\x00b\x00}\x00\x00\x00{\x000\x000\x000\x000\x001\x001\x000\x008\x00-\x000\x000\x000\x000\x00-\x001\x000\x000\x000\x00-\x008\x000\x000\x000\x00-\x000\x000\x008\x000\x005\x00f\x009\x00b\x003\x004\x00f\x00b\x00}\x00\x00\x00\x00\x00'}`  
Services : `{}`  
SupportedServices : `{'{00001124-0000-1000-8000-00805f9b34fb}': 1, '{00001126-0000-1000-8000-00805f9b34fb}': 1, '{00001103-0000-1000-8000-00805f9b34fb}': 1, '{00001101-0000-1000-8000-00805f9b34fb}': 1}`  
UnsupportedServices : `{'{00001200-0000-1000-8000-00805F9B34FB}': 1, '{00001000-0000-1000-8000-00805f9b34fb}': 1, '{00001001-0000-1000-8000-00805f9b34fb}': 1, '{00001002-0000-1000-8000-00805f9b34fb}': 1, '{00001115-0000-1000-8000-00805f9b34fb}': 1, '{00001105-0000-1000-8000-00805f9b34fb}': 1, '{00001106-0000-1000-8000-00805f9b34fb}': 1, '{00001107-0000-1000-8000-00805f9b34fb}': 1, '{00001116-0000-1000-8000-00805f9b34fb}': 1, '{00001117-0000-1000-8000-00805f9b34fb}': 1, '{00001112-0000-1000-8000-00805f9b34fb}': 1, '{00001104-0000-1000-8000-00805f9b34fb}': 1, '{0000112d-0000-1000-8000-00805f9b34fb}': 1, '{0000112e-0000-1000-8000-00805f9b34fb}': 1, '{0000112f-0000-1000-8000-00805f9b34fb}': 1, '{00001111-0000-1000-8000-00805f9b34fb}': 1, '{c7f94713-891e-496a-a0e7-983a0946126e}': 1, '{00001800-0000-1000-8000-00805f9b34fb}': 1, '{00001801-0000-1000-8000-00805f9b34fb}': 1, '{0000180a-0000-1000-8000-00805f9b34fb}': 1, '{00001813-0000-1000-8000-00805f9b34fb}': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">bthserv Service </span>



##### Service Parameters
  
BluetoothControlPanelTasks : `{'State': 0}`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`2a305008-44b3-da4f-9be9-90576b8d46f0`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 46 00 43 00 43 00 41 00 45 00 39 00 36 00 32 00 2d 00 34 00 37 00 32 00 32 00 2d 00 34 00 30 00 43 00 37 00 2d 00 41 00 34 00 36 00 44 00 2d 00 46 00 45 00 35 00 31 00 35 00 33 00 32 00 38 00 30 00 37 00 32 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`32 00 41 00 43 00 42 00 39 00 44 00 36 00 38 00 2d 00 42 00 34 00 33 00 34 00 2d 00 34 00 42 00 33 00 45 00 2d 00 42 00 39 00 36 00 36 00 2d 00 45 00 30 00 36 00 42 00 34 00 42 00 33 00 41 00 38 00 34 00 43 00 42 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">BTHUSB Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\BTHUSB.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`PNP Filter`|`0x09`|`@bth.inf,%BTHUSB.SvcDesc%;Bluetooth Radio USB Driver`|`bth.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">bttflt Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|BootFlags|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\bttflt.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`PnP Filter`|`0x06`|`@virtdisk.inf,%service_desc%;Microsoft Hyper-V VHDPMEM BTT Filter`|`virtdisk.inf`|`0x02`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">buttonconverter Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\buttonconverter.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@buttonconverter.inf,%btnconv.SvcDesc%;Service for Portable Device Control devices`|`buttonconverter.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CAD Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\CAD.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@ChargeArbitration.inf,%CAD_DevDesc%;Charge Arbitration Driver`|`ChargeArbitration.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">camsvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\CapabilityAccessManager.dll`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CaptureService Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\CaptureService.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">cbdhsvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\cbdhsvc.dll`  
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
#### <span style="text-align: center; font-size:2em;">cdfs Service </span>

|DependOnGroup|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`53 00 43 00 53 00 49 00 20 00 43 00 44 00 52 00 4f 00 4d 00 20 00 43 00 6c 00 61 00 73 00 73 00 00 00 00 00`|`ISO9660/Joliet File System Reader for CD/DVDs. (Core) (All pieces)`|`CD/DVD File System Reader`|`SERVICE_ERROR_NORMAL`|`Boot File System`|`system32\DRIVERS\cdfs.sys`|`SERVICE_DISABLED`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CDPSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\CDPSvc.dll`  
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


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`1eff86a0-dcd6-f745-b3e4-6cd5c9fdd6d7`|`SERVICE_TRIGGER_TYPE_AGGREGATE`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CDPUserSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\CDPUserSvc.dll`  
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
#### <span style="text-align: center; font-size:2em;">cdrom Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|AutoRun|AutoRunAlwaysDisable|BootFlags|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\cdrom.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_SYSTEM_START`|`SERVICE_ERROR_NORMAL`|`SCSI CDROM Class`|`0x01`|`@cdrom.inf,%cdrom_ServiceDesc%;CD-ROM Driver`|`cdrom.inf`|`0x01`|`4e 00 45 00 43 00 20 00 20 00 20 00 20 00 20 00 4d 00 42 00 52 00 2d 00 37 00 20 00 20 00 20 00 00 00 4e 00 45 00 43 00 20 00 20 00 20 00 20 00 20 00 4d 00 42 00 52 00 2d 00 37 00 2e 00 34 00 20 00 00 00 50 00 49 00 4f 00 4e 00 45 00 45 00 52 00 20 00 43 00 48 00 41 00 4e 00 47 00 52 00 20 00 44 00 52 00 4d 00 2d 00 31 00 38 00 30 00 34 00 58 00 00 00 50 00 49 00 4f 00 4e 00 45 00 45 00 52 00 20 00 43 00 44 00 2d 00 52 00 4f 00 4d 00 20 00 44 00 52 00 4d 00 2d 00 36 00 33 00 32 00 34 00 58 00 00 00 50 00 49 00 4f 00 4e 00 45 00 45 00 52 00 20 00 43 00 44 00 2d 00 52 00 4f 00 4d 00 20 00 44 00 52 00 4d 00 2d 00 36 00 32 00 34 00 58 00 20 00 00 00 54 00 4f 00 52 00 69 00 53 00 41 00 4e 00 20 00 43 00 44 00 2d 00 52 00 4f 00 4d 00 20 00 43 00 44 00 52 00 5f 00 43 00 33 00 36 00 00 00 00 00`|`0x80`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CertPropSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\certprop.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `CertPropServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-32-544
Group: S-1-0-32-544
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201ff
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
    Access: 0x30
    SID: S-1-0-80-446051430-1559341753-4161941529-1950928533-810483104
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0xc0
    Access: 0xc0000
    SID: S-1-0-32-544

```


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`3052dd50-8aba-d111-bf5d-0000f805f530`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`61811d12-6d86-244a-ba58-9058940c0d47`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">cht4iscsi Service </span>



##### Service Parameters
  
BusType : `0x09`  
IoTimeoutValue : `0x1e`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">cht4vbd Service </span>



##### Service Parameters
  
BootFlags : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CimFS Service </span>

|ErrorControl|Group|Start|Type|
| :---: | :---: | :---: | :---: |
|`SERVICE_ERROR_NORMAL`|`File system`|`SERVICE_SYSTEM_START`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">circlass Service </span>

|Decoders|
| :---: |
|`Decoders`|



##### Service Parameters
  
Wdf : `{'KmdfLibraryVersion': '1.5'}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CldFlt Service </span>

|Instances|
| :---: |
|`Instances`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CLFS Service </span>



##### Service Parameters
  
EventLogLevel : `0x02`  
FlushThreshold : `0x9c40`  
MasterFilePath : `\SystemRoot\System32\config`  
<br></br>  
Security : 
```
Owner: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
Group: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0xf01ff
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x2008d
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x2008d
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x2008d
    SID: S-1-0-32-545
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x2008d
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x2008d
    SID: S-1-0-3-1024-1065365936-1281604716-3511738428-1654721687-432734479-3232135806-4053264122-3456934681

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ClipSVC Service </span>



##### Service Parameters
  
DisableSubscription : `0x00`  
InactivityShutdownDelay : `0x12c`  
RefreshRequired : `0x01`  
ServiceDll : `%SystemRoot%\System32\ClipSVC.dll`  
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
    Access: 0x201ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x94
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-11
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`36 00 34 00 44 00 31 00 44 00 30 00 34 00 35 00 2d 00 46 00 36 00 37 00 35 00 2d 00 34 00 36 00 30 00 42 00 2d 00 38 00 41 00 39 00 34 00 2d 00 35 00 37 00 30 00 32 00 34 00 36 00 42 00 33 00 36 00 44 00 41 00 42 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 21 07 85 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 21 07 85 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 18 bc a3 21 07 85 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 20 bc a3 21 07 85 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 28 bc a3 21 07 85 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|6|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 30 bc a3 21 07 85 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|7|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 68 bc a3 22 02 8f 02`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">cloudidsvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\cloudidsvc.dll`  
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
    Access: 0x2009d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-3-1024-1065365936-1281604716-3511738428-1654721687-432734479-3232135806-4053264122-3456934681

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">clr_optimization_v4.0.30319_32 Service </span>

|DelayedAutostart|FailureActions|RequiredPrivileges|
| :---: | :---: | :---: |
|`0x01`|`84 03 00 00 00 00 00 00 00 00 00 00 03 00 00 00 f9 31 0f 70 01 00 00 00 c0 d4 01 00 01 00 00 00 e0 93 04 00 00 00 00 00 00 00 00 00`|`['SeCreateGlobalPrivilege', 'SeChangeNotifyPrivilege', 'SeIncreaseBasePriorityPrivilege', 'SeIncreaseQuotaPrivilege', 'SeTcbPrivilege', 'SeAssignPrimaryTokenPrivilege', 'SeShutdownPrivilege']`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">clr_optimization_v4.0.30319_64 Service </span>

|DelayedAutostart|FailureActions|RequiredPrivileges|
| :---: | :---: | :---: |
|`0x01`|`84 03 00 00 00 00 00 00 00 00 00 00 03 00 00 00 f9 31 0f 70 01 00 00 00 c0 d4 01 00 01 00 00 00 e0 93 04 00 00 00 00 00 00 00 00 00`|`['SeCreateGlobalPrivilege', 'SeChangeNotifyPrivilege', 'SeIncreaseBasePriorityPrivilege', 'SeIncreaseQuotaPrivilege', 'SeTcbPrivilege', 'SeAssignPrimaryTokenPrivilege', 'SeShutdownPrivilege']`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CmBatt Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\CmBatt.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@cmbatt.inf,%CmBatt.SvcDesc%;Microsoft ACPI Control Method Battery Driver`|`cmbatt.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CNG Service </span>

|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`SERVICE_ERROR_CRITICAL`|`Core`|`System32\Drivers\cng.sys`|`SERVICE_BOOT_START`|`0x04`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">cnghwassist Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\cnghwassist.sys,-100`|`@%SystemRoot%\system32\drivers\cnghwassist.sys,-100`|`SERVICE_ERROR_NORMAL`|`Base`|`System32\DRIVERS\cnghwassist.sys`|`SERVICE_BOOT_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CompositeBus Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\DriverStore\FileRepository\compositebus.inf_amd64_7500cffa210c6946\CompositeBus.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x0b`|`@compositebus.inf,%CompositeBus.SVCDESC%;Composite Bus Enumerator Driver`|`compositebus.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">COMSysApp Service </span>

|DependOnService|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`RpcSsEventSystemSENS`|`@comres.dll,-948`|`@comres.dll,-947`|`SERVICE_ERROR_NORMAL`|`1e 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 e8 03 00 00 01 00 00 00 88 13 00 00 00 00 00 00 00 00 00 00`|`%SystemRoot%\system32\dllhost.exe /Processid:{02D4B3F1-FD88-11D1-960D-00805FC79235}`|`LocalSystem`|`['SeAssignPrimaryTokenPrivilege', 'SeAuditPrivilege', 'SeChangeNotifyPrivilege', 'SeCreateGlobalPrivilege', 'SeDebugPrivilege', 'SeImpersonatePrivilege', 'SeIncreaseQuotaPrivilege']`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">condrv Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`Console Driver`|`SERVICE_ERROR_NORMAL`|`Base`|`System32\drivers\condrv.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ConsentUxUserSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\ConsentUxClient.dll`  
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
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CoreMessagingRegistrar Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\coremessaging.dll`  
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
    Access: 0x201fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-2-1

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CoreUI Service </span>

|Navigation|
| :---: |
|`Navigation`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CredentialEnrollmentManagerUserSvc Service </span>
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-2-1

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CryptSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\cryptsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `CryptServiceMain`  
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
    Access: 0x201fd
    SID: S-1-0-32-549
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-3-1024-3203351429-2120443784-2872670797-1918958302-2829055647-4275794519-765664414-2751773334

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CSC Service </span>

|DependOnService|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`rdbss`|`@%systemroot%\system32\cscsvc.dll,-203`|`@%systemroot%\system32\cscsvc.dll,-202`|`SERVICE_ERROR_NORMAL`|`network`|`system32\drivers\csc.sys`|`SERVICE_SYSTEM_START`|`0x09`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">CscService Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\cscsvc.dll`  
ServiceMain : `CscServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 2e 1d 85 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">dam Service </span>

|Description|DisplayName|ErrorControl|ImagePath|Start|Type|WOW64|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\dam.sys,-101`|`@%SystemRoot%\system32\drivers\dam.sys,-100`|`SERVICE_ERROR_NORMAL`|`system32\drivers\dam.sys`|`SERVICE_SYSTEM_START`|`SERVICE_KERNEL_DRIVER`|`0x14c`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DCLocator Service </span>

|Tracing|
| :---: |
|`{}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DcomLaunch Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\rpcss.dll`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x20085
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x85
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf00ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">defragsvc Service </span>



##### Service Parameters
  
ServiceDll : `%Systemroot%\System32\defragsvc.dll`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DeviceAssociationBrokerSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\deviceaccess.dll`  
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
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-2-1

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DeviceAssociationService Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\das.dll`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`62 00 64 00 38 00 34 00 63 00 64 00 38 00 36 00 2d 00 39 00 38 00 32 00 35 00 2d 00 34 00 33 00 37 00 36 00 2d 00 38 00 31 00 33 00 64 00 2d 00 33 00 33 00 34 00 63 00 35 00 34 00 33 00 66 00 38 00 39 00 62 00 31 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`38 00 35 00 30 00 63 00 65 00 65 00 35 00 32 00 2d 00 33 00 30 00 33 00 38 00 2d 00 34 00 32 00 37 00 37 00 2d 00 62 00 39 00 62 00 34 00 2d 00 65 00 30 00 35 00 64 00 62 00 38 00 62 00 32 00 63 00 33 00 35 00 63 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`32 00 65 00 37 00 64 00 34 00 39 00 33 00 35 00 2d 00 35 00 39 00 64 00 32 00 2d 00 34 00 33 00 31 00 32 00 2d 00 61 00 32 00 63 00 38 00 2d 00 34 00 31 00 39 00 30 00 30 00 61 00 61 00 35 00 34 00 39 00 35 00 66 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`61 00 31 00 64 00 34 00 65 00 61 00 65 00 37 00 2d 00 33 00 39 00 66 00 38 00 2d 00 34 00 62 00 63 00 61 00 2d 00 38 00 65 00 37 00 32 00 2d 00 38 00 33 00 32 00 37 00 36 00 37 00 66 00 35 00 30 00 38 00 32 00 61 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DeviceInstall Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\umpnpmgr.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`35 00 63 00 39 00 61 00 34 00 63 00 64 00 37 00 2d 00 62 00 61 00 37 00 35 00 2d 00 34 00 35 00 64 00 32 00 2d 00 39 00 38 00 39 00 38 00 2d 00 31 00 37 00 37 00 33 00 62 00 33 00 64 00 31 00 65 00 35 00 66 00 31 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 3d 00 96 02`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DevicePickerUserSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\Windows.Devices.Picker.dll`  
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
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-21-2702878673-795188819-444038987-2781

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DevicesFlowUserSvc Service </span>



##### Service Parameters
  
LegacyCOMBehavior : `0x01`  
ServiceDll : `%SystemRoot%\System32\DevicesFlowBroker.dll`  
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
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-21-2702878673-795188819-444038987-2781

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DevQueryBroker Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\DevQueryBroker.dll`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 33 00 31 00 34 00 63 00 38 00 34 00 32 00 37 00 2d 00 34 00 61 00 64 00 37 00 2d 00 34 00 32 00 33 00 33 00 2d 00 39 00 39 00 35 00 61 00 2d 00 62 00 62 00 64 00 30 00 36 00 32 00 65 00 64 00 31 00 31 00 65 00 39 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Dfsc Service </span>



##### Service Parameters
  
UseDCLocatorSiteName : `0x00`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Dhcp Service </span>

|Configurations|Linkage|Parametersv6|
| :---: | :---: | :---: |
|`{}`|`Linkage`|`Parametersv6`|



##### Service Parameters
  
Options : `Options`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-32-556
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">diagnosticshub.standardcollector.service Service </span>

|Description|DisplayName|ErrorControl|ImagePath|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\DiagSvcs\DiagnosticsHub.StandardCollector.ServiceRes.dll,-1001`|`@%SystemRoot%\system32\DiagSvcs\DiagnosticsHub.StandardCollector.ServiceRes.dll,-1000`|`SERVICE_ERROR_NORMAL`|`%SystemRoot%\system32\DiagSvcs\DiagnosticsHub.StandardCollector.Service.exe`|`LocalSystem`|`['SeImpersonatePrivilege', 'SeSystemProfilePrivilege', 'SeDebugPrivilege']`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">diagsvc Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\DiagSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`46 00 44 00 44 00 34 00 35 00 39 00 32 00 34 00 2d 00 37 00 38 00 34 00 41 00 2d 00 34 00 39 00 39 00 43 00 2d 00 41 00 45 00 45 00 39 00 2d 00 30 00 38 00 31 00 33 00 38 00 35 00 30 00 43 00 45 00 31 00 38 00 32 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DiagTrack Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\diagtrack.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DialogBlockingService Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\DialogBlockingService.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">disk Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|AutoRunAlwaysDisable|TimeOutValue|IoTimeoutValue|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\disk.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`@disk.inf,%disk_ServiceDesc%;Disk Driver`|`wstorflt.infdisk.infvirtdisk.infsmrdisk.inf`|`42 00 72 00 6f 00 74 00 68 00 65 00 72 00 20 00 52 00 65 00 6d 00 6f 00 76 00 61 00 62 00 6c 00 65 00 44 00 69 00 73 00 6b 00 28 00 55 00 29 00 00 00 00 00`|`0x41`|`0x3c`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DispBrokerDesktopSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\DispBroker.Desktop.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DisplayEnhancementService Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\Microsoft.Graphics.Display.DisplayEnhancementService.dll`  
ServiceDllUnloadOnStop : `0x01`  
SvcHostSplitDisable : `0x01`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x114
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x114
    SID: S-1-0-11
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
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`41 00 36 00 39 00 38 00 31 00 36 00 46 00 35 00 2d 00 38 00 33 00 42 00 36 00 2d 00 34 00 44 00 34 00 38 00 2d 00 38 00 36 00 33 00 33 00 2d 00 30 00 36 00 37 00 46 00 39 00 39 00 46 00 35 00 46 00 32 00 44 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`42 00 35 00 34 00 45 00 39 00 41 00 41 00 33 00 2d 00 43 00 46 00 32 00 39 00 2d 00 34 00 46 00 32 00 31 00 2d 00 41 00 38 00 45 00 41 00 2d 00 39 00 38 00 43 00 35 00 38 00 35 00 30 00 43 00 45 00 32 00 39 00 36 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`c815f197-9a59-5341-8894-d2d12899918a`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`ac9a02a7-dd77-dd4d-959b-054f5574f4fb`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`864052db-90ba-1e4e-be42-894e94ecf289`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DmEnrollmentSvc Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\Windows.Internal.Management.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">dmvsc Service </span>

|ImagePath|Type|Start|ErrorControl|Owners|
| :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\dmvsc.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`wdmvsc.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">dmwappushservice Service </span>



##### Service Parameters
  
IdleTimeout(sec) : `0x78`  
ServiceDll : `%SystemRoot%\system32\dmwappushsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
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
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-11

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`37 00 39 00 35 00 42 00 36 00 42 00 46 00 39 00 2d 00 39 00 37 00 42 00 36 00 2d 00 34 00 46 00 38 00 39 00 2d 00 42 00 44 00 38 00 44 00 2d 00 32 00 46 00 34 00 32 00 42 00 42 00 42 00 45 00 39 00 39 00 36 00 45 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`39 00 34 00 35 00 36 00 39 00 33 00 63 00 34 00 2d 00 33 00 36 00 34 00 38 00 2d 00 34 00 39 00 36 00 36 00 2d 00 62 00 32 00 61 00 61 00 2d 00 33 00 37 00 64 00 36 00 36 00 65 00 32 00 34 00 34 00 39 00 35 00 66 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 61 00 30 00 64 00 62 00 36 00 31 00 34 00 2d 00 65 00 39 00 66 00 62 00 2d 00 34 00 38 00 63 00 66 00 2d 00 39 00 31 00 34 00 33 00 2d 00 37 00 61 00 65 00 37 00 31 00 38 00 66 00 66 00 32 00 63 00 38 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 90 bc a3 28 00 92 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Dnscache Service </span>

|InterfaceSpecificParameters|mDNS|
| :---: | :---: |
|`{}`|`{}`|



##### Service Parameters
  
DnsActiveIfs : `{}`  
DnsConnections : `{}`  
DnsConnectionsProxies : `{}`  
DnsPolicyConfig : `{}`  
Probe : `{}`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x2009d
    SID: S-1-0-32-545
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x200dd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x200dd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x2009d
    SID: S-1-0-20
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x2009d
    SID: S-1-0-19
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x200dd
    SID: S-1-0-32-556
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x201cd
    SID: S-1-0-80-2940520708-3855866260-481812779-327648279-1710889582
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x2009d
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x2009d
    SID: S-1-0-3-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x2009d
    SID: S-1-0-3-2
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x2009d
    SID: S-1-0-3-3
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0x200dd
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`37927c27-d851-1c5c-b089-f02c683e5ba7`|`SERVICE_TRIGGER_TYPE_CUSTOM`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DoSvc Service </span>
  
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
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x20002
    SID: S-1-0-80-3055155277-3816794035-3994065555-2874236192-2193176987
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 29 01 c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`e6ca9f65-db5b-a94d-b1ff-ca2a178d46e0`|`SERVICE_TRIGGER_TYPE_GROUP_POLICY`|||
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">dot3svc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\dot3svc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `Dot3SvcMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DPS Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\dps.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201ff
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
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">drmkaud Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\drmkaud.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@wdmaudio.inf,%drmkaud.SvcDesc%;Microsoft Trusted Audio Drivers`|`wdmaudio.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DsmSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\DeviceSetupManager.dll`  
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
    Access: 0x10
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 18 bc a3 3d 00 96 02`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DsSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\DsSvc.dll`  
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
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-0(NULL)
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-2-1

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`42 00 46 00 34 00 44 00 43 00 39 00 31 00 32 00 2d 00 45 00 35 00 32 00 46 00 2d 00 34 00 39 00 30 00 34 00 2d 00 38 00 45 00 42 00 45 00 2d 00 39 00 33 00 31 00 37 00 43 00 31 00 42 00 44 00 44 00 34 00 39 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DusmSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\dusmsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">DXGKrnl Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`Controls the underlying video driver stacks to provide fully-featured display capabilities.`|`LDDM Graphics Subsystem`|`SERVICE_ERROR_IGNORE`|`Video Init`|`\SystemRoot\System32\drivers\dxgkrnl.sys`|`SERVICE_SYSTEM_START`|`0x01`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Eaphost Service </span>
  
Methods : `Methods`


##### Service Parameters
  
EapProvPlugin : `{'(Default)': '%SystemRoot%\\System32\\eapprovp.dll', 'DllEntryPoint': 'EapProvPlugGetInfo'}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ebdrv Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\evbda.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`System Bus Extender`|`0x03`|`@netevbda.inf,%vbd_srv_desc%;QLogic 10 Gigabit Ethernet Adapter VBD`|`netevbda.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">edgeupdate Service </span>

|DelayedAutostart|DependOnService|Description|DisplayName|ErrorControl|ImagePath|ObjectName|Start|Type|WOW64|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`0x00`|`RPCSS`|`Keeps your Microsoft software up to date. If this service is disabled or stopped, your Microsoft software will not be kept up to date, meaning security vulnerabilities that may arise cannot be fixed and features may not work. This service uninstalls itself when there is no Microsoft software using it.`|`Microsoft Edge Update Service (edgeupdate)`|`SERVICE_ERROR_NORMAL`|`"X:\Program Files (x86)\Microsoft\EdgeUpdate\MicrosoftEdgeUpdate.exe" /svc`|`LocalSystem`|`SERVICE_AUTO_START`|`SERVICE_WIN32_OWN_PROCESS`|`0x14c`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">edgeupdatem Service </span>

|DelayedAutostart|DependOnService|Description|DisplayName|ErrorControl|ImagePath|ObjectName|Start|Type|WOW64|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`0x00`|`RPCSS`|`Keeps your Microsoft software up to date. If this service is disabled or stopped, your Microsoft software will not be kept up to date, meaning security vulnerabilities that may arise cannot be fixed and features may not work. This service uninstalls itself when there is no Microsoft software using it.`|`Microsoft Edge Update Service (edgeupdatem)`|`SERVICE_ERROR_NORMAL`|`"X:\Program Files (x86)\Microsoft\EdgeUpdate\MicrosoftEdgeUpdate.exe" /medsvc`|`LocalSystem`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|`0x14c`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">EFS Service </span>



##### Service Parameters
  
EdpCredLibProxy : `feclient.dll`  
ServiceDll : `%SystemRoot%\system32\efssvc.dll`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201bf
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-2-1
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0xc0
    Access: 0xd0002
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 28 08 95 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 88 bc a3 28 00 92 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`64 00 66 00 31 00 39 00 34 00 31 00 63 00 35 00 2d 00 66 00 65 00 38 00 39 00 2d 00 34 00 65 00 37 00 39 00 2d 00 62 00 66 00 31 00 30 00 2d 00 34 00 36 00 33 00 36 00 35 00 37 00 61 00 63 00 66 00 34 00 34 00 64 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 34 00 45 00 45 00 42 00 32 00 39 00 37 00 2d 00 43 00 42 00 46 00 34 00 2d 00 34 00 36 00 36 00 62 00 2d 00 38 00 41 00 32 00 41 00 2d 00 42 00 46 00 44 00 36 00 41 00 32 00 46 00 31 00 30 00 42 00 42 00 41 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">EhStorClass Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\EhStorClass.sys,-101`|`@%SystemRoot%\system32\drivers\EhStorClass.sys,-100`|`SERVICE_ERROR_NORMAL`|`SCSI Class`|`System32\drivers\EhStorClass.sys`|`SERVICE_BOOT_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">EhStorTcgDrv Service </span>



##### Service Parameters
  
KsrGuid : `{cd255889-bb93-475b-8cc3-cd3e0f609020}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">embeddedmode Service </span>



##### Service Parameters
  
Flags : `0x00`  
ServiceDll : `%SystemRoot%\System32\embeddedmodesvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  
Security : 
```
Owner: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
Group: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 24 01 92 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">EntAppSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\EnterpriseAppMgmtSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  
Security : 
```
Owner: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
Group: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ErrDev Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\errdev.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x22`|`@errdev.inf,%ERRDEV.SvcDesc%;Microsoft Hardware Error Device Driver`|`errdev.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ESENT Service </span>

|Performance|
| :---: |
|`{'Close': 'ClosePerformanceData', 'Collect': 'CollectPerformanceData', 'Library': '%systemroot%\\system32\\esentprf.dll', 'Open': 'OpenPerformanceData', 'InstallType': 1, 'PerfIniFile': 'esentprf.ini', 'First Counter': 6928, 'Last Counter': 8708, 'First Help': 6929, 'Last Help': 8709, 'Object List': '6928 7702 7934 8626'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">EventLog Service </span>

|Application|HardwareEvents|Internet Explorer|Key Management Service|System|Windows PowerShell|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`Application`|`{'DisplayNameFile': '%SystemRoot%\\system32\\wecsvc.dll', 'DisplayNameID': 256, 'File': '%systemroot%\\system32\\winevt\\logs\\HardwareEvents.evtx', 'MaxSize': 20971520, 'Retention': 0}`|`{'CustomSD': 'O:BAG:SYD:(A;;0x07;;;WD)S:(ML;;0x1;;;LW)'}`|`Key Management Service`|`System`|`Windows PowerShell`|



##### Service Parameters
  
ServiceDLL : `%SystemRoot%\System32\wevtsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">EventSystem Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\es.dll`  
ServiceDllUnLoadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">exfat Service </span>

|Description|DisplayName|ErrorControl|Group|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`exFAT File System Driver`|`exFAT File System Driver`|`SERVICE_ERROR_NORMAL`|`Boot File System`|`SERVICE_DEMAND_START`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">fastfat Service </span>

|Description|DisplayName|ErrorControl|Group|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`Note - dependance on CDROM.SYS only if required to read/write DVD-RAM media (which appears as CD class device). (Core) (All pieces)`|`FAT12/16/32 File System Driver`|`SERVICE_ERROR_NORMAL`|`Boot File System`|`SERVICE_DEMAND_START`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Fax Service </span>
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-0(NULL)
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-80-2117685068-4011115449-2646761356-2137676340-222423812
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-11

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">fdc Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\fdc.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@fdc.inf,%fdc_ServiceDesc%;Floppy Disk Controller Driver`|`fdc.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">fdPHost Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\fdPHost.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">FDResPub Service </span>

|ServiceData|
| :---: |
|`{}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\fdrespub.dll`  
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
    Access: 0x201fd
    SID: S-1-0-32-556
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`3faccffb-6084-9f41-8e48-1f0b49cdb85e`|`SERVICE_TRIGGER_TYPE_CUSTOM`|`50 00 52 00 4f 00 46 00 49 00 4c 00 45 00 5f 00 43 00 48 00 41 00 4e 00 47 00 45 00 44 00 5f 00 54 00 4f 00 5f 00 50 00 52 00 49 00 56 00 41 00 54 00 45 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">fhsvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\fhsvc.dll`  
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
    Access: 0x2019d
    SID: S-1-0-11

```


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`e6ca9f65-db5b-a94d-b1ff-ca2a178d46e0`|`SERVICE_TRIGGER_TYPE_GROUP_POLICY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`c846fb54-89f0-4c46-b1fd-59d1b62c3b50`|`SERVICE_TRIGGER_TYPE_GROUP_POLICY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">FileCrypt Service </span>

|Instances|
| :---: |
|`Instances`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">FileInfo Service </span>

|Instances|
| :---: |
|`Instances`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Filetrace Service </span>

|Instances|
| :---: |
|`Instances`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">flpydisk Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\flpydisk.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@flpydisk.inf,%floppy_ServiceDesc%;Floppy Disk Driver`|`flpydisk.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">FltMgr Service </span>

|AttachWhenLoaded|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`0x01`|`@%SystemRoot%\system32\drivers\fltmgr.sys,-10000`|`@%SystemRoot%\system32\drivers\fltmgr.sys,-10001`|`SERVICE_ERROR_CRITICAL`|`FSFilter Infrastructure`|`system32\drivers\fltmgr.sys`|`SERVICE_BOOT_START`|`0x01`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">FontCache Service </span>



##### Service Parameters
  
ClientCacheSize : `0x400000`  
FontFaceCacheSize : `0x1000000`  
ServiceDll : `%SystemRoot%\system32\FntCache.dll`  
ServiceDllUnloadOnStop : `0x01`  
UserCacheSize : `0x800000`  
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
    Access: 0x10
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x10
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-2-1
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">FrameServer Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\FrameServer.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`36 00 44 00 44 00 46 00 43 00 37 00 44 00 31 00 2d 00 37 00 46 00 43 00 41 00 2d 00 34 00 34 00 45 00 42 00 2d 00 41 00 32 00 37 00 39 00 2d 00 45 00 39 00 39 00 38 00 38 00 46 00 34 00 44 00 42 00 33 00 32 00 42 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 26 1d 90 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 21 bc a3 2e 0f 8b 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`773732e5-76f9-5b4f-9b55-b94699c46e44`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`d752e524-2365-f747-a647-d3465bf1f5ca`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">FsDepends Service </span>

|Instances|
| :---: |
|`Instances`|



##### Service Parameters
  
AccessControl : `{'ISOMountAllowNormalUser': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Fs_Rec Service </span>

|ErrorControl|Group|Start|Type|
| :---: | :---: | :---: | :---: |
|`SERVICE_ERROR_IGNORE`|`File System`|`SERVICE_BOOT_START`|`SERVICE_RECOGNIZER_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">fvevol Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\fvevol.sys,-100`|`@%SystemRoot%\system32\drivers\fvevol.sys,-100`|`SERVICE_ERROR_CRITICAL`|`PnP Filter`|`System32\DRIVERS\fvevol.sys`|`SERVICE_BOOT_START`|`0x05`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">gencounter Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\vmgencounter.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@wgencounter.inf,%GenCounter.SVCDESC%;Microsoft Hyper-V Generation Counter`|`wgencounter.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">genericusbfn Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\DriverStore\FileRepository\genericusbfn.inf_amd64_53931f0ae21d6d2c\genericusbfn.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x11`|`@genericusbfn.inf,%genericusbfn.ServiceName%;Generic USB Function Class`|`genericusbfn.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">GPIOClx0101 Service </span>

|DependOnService|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`acpiex`|`Microsoft GPIO Class Extension Driver`|`SERVICE_ERROR_CRITICAL`|`System Bus Extender`|`System32\Drivers\msgpioclx.sys`|`SERVICE_DEMAND_START`|`0x07`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">gpsvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\gpsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `GroupPolicyClientServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
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
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0xc0
    Access: 0xd0002
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`32 00 45 00 42 00 30 00 38 00 45 00 33 00 45 00 2d 00 36 00 33 00 39 00 46 00 2d 00 34 00 66 00 62 00 61 00 2d 00 39 00 37 00 42 00 31 00 2d 00 31 00 34 00 46 00 38 00 37 00 38 00 39 00 36 00 31 00 30 00 37 00 36 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">GpuEnergyDrv Service </span>

|Description|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\gpuenergydrv.sys,-101`|`@%SystemRoot%\system32\drivers\gpuenergydrv.sys,-100`|`SERVICE_ERROR_NORMAL`|`System32\drivers\gpuenergydrv.sys`|`SERVICE_SYSTEM_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">GraphicsPerfSvc Service </span>



##### Service Parameters
  
BufferSize : `0x00`  
FlushTimer : `0x00`  
IntervalSecs : `0x3c`  
MaximumBuffers : `0x00`  
MinimumBuffers : `0x00`  
ServiceDll : `%SystemRoot%\System32\GraphicsPerfSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
TimeoutSecs : `0x5a`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 78 bc a3 29 16 c6 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HdAudAddService Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\HdAudio.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@hdaudio.inf,%UAAFunctionDriverForHdAudio.SvcDesc%;Microsoft 1.1 UAA Function Driver for High Definition Audio Service`|`hdaudio.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HDAudBus Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\HDAudBus.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x0c`|`@hdaudbus.inf,%HDAudBus.SVCDESC%;Microsoft UAA Bus Driver for High Definition Audio`|`hdaudbus.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HidBatt Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\HidBatt.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@hidbatt.inf,%HidBatt.SvcDesc%;HID UPS Battery Driver`|`hidbatt.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HidBth Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\hidbth.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_IGNORE`|`extended base`|`0x02`|`@hidbth.inf,%HIDBTH.SvcDesc%;Microsoft Bluetooth HID Miniport`|`hidbth.infxinputhid.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">hidi2c Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\hidi2c.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x26`|`@hidi2c.inf,%hidi2c.SVCDESC%;Microsoft I2C HID Miniport Driver`|`hidi2c.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">hidinterrupt Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\hidinterrupt.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x27`|`@hidinterrupt.inf,%HID_Interrupt.SvcDesc%;Common Driver for HID Buttons implemented with interrupts`|`hidinterrupt.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HidIr Service </span>

|Remotes|
| :---: |
|`Remotes`|



##### Service Parameters
  
DefaultWakeProtocol : `0x01`  
DefaultWakePayload : `0x0c`  
DefaultWakeAddress : `0x00`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">hidserv Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\hidserv.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`b2551e4d-6ff1-cf11-88cb-001111000030`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 43 00 5f 00 55 00 3a 00 30 00 30 00 30 00 31 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">hidspi Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\hidspi.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x28`|`@hidspi_km.inf,%hidspi.SVCDESC%;Microsoft SPI HID Miniport Driver`|`hidspi_km.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HidUsb Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\hidusb.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_IGNORE`|`extended base`|`0x25`|`@input.inf,%HID.SvcDesc%;Microsoft HID Class Driver`|`input.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HomeGroupListener Service </span>

|ApprovedListeners|
| :---: |
|`ApprovedListeners`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\ListSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ListenerServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HomeGroupProvider Service </span>

|LocalUserMembership|ServiceData|
| :---: | :---: |
|`{}`|`{'LocalJoiningUser': '', 'Password': b'\x00'}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\provsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ProviderServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HpSAMD Service </span>



##### Service Parameters
  
Device : `{'DriverParameter': 'CSMI=None;'}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HTTP Service </span>



##### Service Parameters
  
UrlAclInfo : `{'http://*:5357/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x004\x00\x02\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00 \x01\x02\x00\x00\x00\x00\x00\x05 \x00\x00\x00!\x02\x00\x00\x00\x00\x14\x00\x00\x00\x00 \x01\x01\x00\x00\x00\x00\x00\x05\x13\x00\x00\x00', 'http://+:80/Temporary_Listen_Addresses/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x00\x1c\x00\x01\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00 \x01\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00', 'https://*:5358/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x004\x00\x02\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00 \x01\x02\x00\x00\x00\x00\x00\x05 \x00\x00\x00!\x02\x00\x00\x00\x00\x14\x00\x00\x00\x00 \x01\x01\x00\x00\x00\x00\x00\x05\x13\x00\x00\x00', 'https://+:443/sra_{BA195980-CD49-458b-9E23-C84EE0ADCD75}/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x00\\\x00\x03\x00\x00\x00\x00\x00(\x00\x00\x00\x00\x10\x01\x06\x00\x00\x00\x00\x00\x05P\x00\x00\x00~\xa6\xc8\xcc*\xae\xa7/\xc1\xeb\xfb\xe1\xba\xe3k\xc0\xda\xd0+\xaf\x00\x00\x18\x00\x00\x00\x00\x10\x01\x02\x00\x00\x00\x00\x00\x05 \x00\x00\x00 \x02\x00\x00\x00\x00\x14\x00\x00\x00\x00\x10\x01\x01\x00\x00\x00\x00\x00\x05\x12\x00\x00\x00', 'https://+:5986/wsman/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x00X\x00\x02\x00\x00\x00\x00\x00(\x00\x00\x00\x00 \x01\x06\x00\x00\x00\x00\x00\x05P\x00\x00\x00\x86*\xee!\xd7[\t\xb0\xa4[l\xad\xbb\x83\x93M\xeag\x90\x18\x00\x00(\x00\x00\x00\x00 \x01\x06\x00\x00\x00\x00\x00\x05P\x00\x00\x00C\xb4\xfa\xf1\xd3\xd4T4\xa8\xd5>JS\nl\x1f=\xee\x9b\xb2', 'http://+:47001/wsman/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x00X\x00\x02\x00\x00\x00\x00\x00(\x00\x00\x00\x00 \x01\x06\x00\x00\x00\x00\x00\x05P\x00\x00\x00\x86*\xee!\xd7[\t\xb0\xa4[l\xad\xbb\x83\x93M\xeag\x90\x18\x00\x00(\x00\x00\x00\x00 \x01\x06\x00\x00\x00\x00\x00\x05P\x00\x00\x00C\xb4\xfa\xf1\xd3\xd4T4\xa8\xd5>JS\nl\x1f=\xee\x9b\xb2', 'http://+:5985/wsman/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x00X\x00\x02\x00\x00\x00\x00\x00(\x00\x00\x00\x00 \x01\x06\x00\x00\x00\x00\x00\x05P\x00\x00\x00\x86*\xee!\xd7[\t\xb0\xa4[l\xad\xbb\x83\x93M\xeag\x90\x18\x00\x00(\x00\x00\x00\x00 \x01\x06\x00\x00\x00\x00\x00\x05P\x00\x00\x00C\xb4\xfa\xf1\xd3\xd4T4\xa8\xd5>JS\nl\x1f=\xee\x9b\xb2', 'http://*:2869/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x00\x1c\x00\x01\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00 \x01\x01\x00\x00\x00\x00\x00\x05\x13\x00\x00\x00', 'https://+:3392/rdp/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x000\x00\x01\x00\x00\x00\x00\x00(\x00\x00\x00\x00 \x01\x06\x00\x00\x00\x00\x00\x05P\x00\x00\x00f4\x96\x1a\xb9\xaa\xf1\\\x190\x12\xf8\x95\xceHt\xa0\xfdN0', 'http://+:3387/rdp/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x000\x00\x01\x00\x00\x00\x00\x00(\x00\x00\x00\x00 \x01\x06\x00\x00\x00\x00\x00\x05P\x00\x00\x00f4\x96\x1a\xb9\xaa\xf1\\\x190\x12\xf8\x95\xceHt\xa0\xfdN0', 'http://+:10247/apps/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x00\x1c\x00\x01\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00 \x01\x01\x00\x00\x00\x00\x00\x05\x0b\x00\x00\x00', 'https://+:10245/WMPNSSv4/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x000\x00\x01\x00\x00\x00\x00\x00(\x00\x00\x00\x00 \x01\x06\x00\x00\x00\x00\x00\x05P\x00\x00\x009\x0b\x9a\x8d>m\xc7-X\xa4\xad\xd2Hf\xef;\xc8\xb6J\xab', 'http://+:10243/WMPNSSv4/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x000\x00\x01\x00\x00\x00\x00\x00(\x00\x00\x00\x00 \x01\x06\x00\x00\x00\x00\x00\x05P\x00\x00\x009\x0b\x9a\x8d>m\xc7-X\xa4\xad\xd2Hf\xef;\xc8\xb6J\xab', 'http://+:10246/MDEServer/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x00\x1c\x00\x01\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00 \x01\x01\x00\x00\x00\x00\x00\x05\x0b\x00\x00\x00', 'http://+:80/0131501b-d67f-491b-9a40-c4bf27bcb4d4/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x00\x1c\x00\x01\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00 \x01\x01\x00\x00\x00\x00\x00\x05\x14\x00\x00\x00', 'https://+:443/C574AC30-5794-4AEE-B1BB-6651C5315029/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x00\x1c\x00\x01\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00 \x01\x01\x00\x00\x00\x00\x00\x05\x14\x00\x00\x00', 'http://+:80/116B50EB-ECE2-41ac-8429-9F9E963361B7/': b'\x01\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x02\x00\x1c\x00\x01\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00 \x01\x01\x00\x00\x00\x00\x00\x05\x14\x00\x00\x00'}`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
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
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-3
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">hvcrash Service </span>

|ImagePath|Type|Start|ErrorControl|Owners|
| :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\hvcrash.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DISABLED`|`SERVICE_ERROR_NORMAL`|`whvcrash.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HvHost Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\hvhostsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 25 18 8a 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">hvservice Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\hvservice.sys,-17`|`@%SystemRoot%\system32\drivers\hvservice.sys,-16`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`system32\drivers\hvservice.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HwNClx0101 Service </span>

|DisplayName|ErrorControl|Group|HwNClxSecurity|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`Microsoft Hardware Notifications Class Extension Driver`|`SERVICE_ERROR_NORMAL`|`System`|`01 00 04 80 14 00 00 00 20 00 00 00 00 00 00 00 2c 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 01 01 00 00 00 00 00 05 12 00 00 00 02 00 b4 00 05 00 00 00 00 00 14 00 00 00 00 c0 01 01 00 00 00 00 00 05 04 00 00 00 00 00 14 00 ff ff 1f 11 01 01 00 00 00 00 00 05 12 00 00 00 00 00 18 00 ff ff 1f 11 01 02 00 00 00 00 00 05 20 00 00 00 20 02 00 00 00 00 34 00 00 00 00 c0 01 09 00 00 00 00 00 05 20 00 00 00 b9 36 1b d8 f6 76 dd 9f d0 25 08 33 a5 fd f7 aa 76 10 e0 b2 d4 42 27 3c 2a f0 e7 f8 c8 60 c9 28 00 00 38 00 00 00 00 c0 01 0a 00 00 00 00 00 0f 03 00 00 00 00 04 00 00 b9 36 1b d8 f6 76 dd 9f d0 25 08 33 a5 fd f7 aa 76 10 e0 b2 d4 42 27 3c 2a f0 e7 f8 c8 60 c9 28`|`System32\Drivers\mshwnclx.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">hwpolicy Service </span>

|Description|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`@%systemroot%\system32\drivers\hwpolicy.sys,-102`|`@%systemroot%\system32\drivers\hwpolicy.sys,-101`|`SERVICE_ERROR_IGNORE`|`System32\drivers\hwpolicy.sys`|`SERVICE_BOOT_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">hyperkbd Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\hyperkbd.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_IGNORE`|`Extended Base`|`0x2d`|`whyperkbd.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">HyperVideo Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\HyperVideo.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_IGNORE`|`Video`|`0x04`|`wvmbusvideo.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">i8042prt Service </span>



##### Service Parameters
  
PollingIterations : `0x2ee0`  
PollingIterationsMaximum : `0x2ee0`  
ResendIterations : `0x03`  
LayerDriver JPN : `kbd101.dll`  
LayerDriver KOR : `kbd101a.dll`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iagpio Service </span>

|ImagePath|Type|Start|ErrorControl|DependOnService|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\iagpio.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`GPIOClx`|`@iagpio.inf,%iagpio.SVCDESC%;Intel Serial IO GPIO Controller Driver`|`iagpio.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iai2c Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|ForceDma|NoRestartCondition|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\iai2c.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x07`|`SpbCx`|`@iai2c.inf,%iai2c.SVCDESC%;Intel(R) Serial IO I2C Host Controller`|`iai2c.inf`|`000,000,000,000,000,000,000`|`0x00`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iaLPSS2i_GPIO2 Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\iaLPSS2i_GPIO2.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x08`|`@iaLPSS2i_GPIO2_SKL.inf,%iaLPSS2i_GPIO2.SVCDESC%;Intel(R) Serial IO GPIO Driver v2`|`iaLPSS2i_GPIO2_SKL.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iaLPSS2i_GPIO2_BXT_P Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\iaLPSS2i_GPIO2_BXT_P.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x05`|`@iaLPSS2i_GPIO2_BXT_P.inf,%iaLPSS2i_GPIO2_BXT_P.SVCDESC%;Intel(R) Serial IO GPIO Driver v2`|`iaLPSS2i_GPIO2_BXT_P.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iaLPSS2i_GPIO2_CNL Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\iaLPSS2i_GPIO2_CNL.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x06`|`@iaLPSS2i_GPIO2_CNL.inf,%iaLPSS2i_GPIO2_CNL.SVCDESC%;Intel(R) Serial IO GPIO Driver v2`|`iaLPSS2i_GPIO2_CNL.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iaLPSS2i_GPIO2_GLK Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\iaLPSS2i_GPIO2_GLK.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x07`|`@iaLPSS2i_GPIO2_GLK.inf,%iaLPSS2i_GPIO2_GLK.SVCDESC%;Intel(R) Serial IO GPIO Driver v2`|`iaLPSS2i_GPIO2_GLK.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iaLPSS2i_I2C Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\iaLPSS2i_I2C.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x06`|`SpbCx`|`@iaLPSS2i_I2C_SKL.inf,%iaLPSS2i_I2C.SVCDESC%;Intel(R) Serial IO I2C Driver v2`|`iaLPSS2i_I2C_SKL.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iaLPSS2i_I2C_BXT_P Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\iaLPSS2i_I2C_BXT_P.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x03`|`SpbCx`|`@iaLPSS2i_I2C_BXT_P.inf,%iaLPSS2i_I2C_BXT_P.SVCDESC%;Intel(R) Serial IO I2C Driver v2`|`iaLPSS2i_I2C_BXT_P.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iaLPSS2i_I2C_CNL Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\iaLPSS2i_I2C_CNL.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x04`|`SpbCx`|`@iaLPSS2i_I2C_CNL.inf,%iaLPSS2i_I2C_CNL.SVCDESC%;Intel(R) Serial IO I2C Driver v2`|`iaLPSS2i_I2C_CNL.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iaLPSS2i_I2C_GLK Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\iaLPSS2i_I2C_GLK.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x05`|`SpbCx`|`@iaLPSS2i_I2C_GLK.inf,%iaLPSS2i_I2C_GLK.SVCDESC%;Intel(R) Serial IO I2C Driver v2`|`iaLPSS2i_I2C_GLK.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iaLPSSi_GPIO Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\iaLPSSi_GPIO.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x15`|`@ialpssi_gpio.inf,%iaLPSSi_GPIO.SVCDESC%;Intel(R) Serial IO GPIO Controller Driver`|`ialpssi_gpio.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iaLPSSi_I2C Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\iaLPSSi_I2C.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x08`|`SpbCx`|`@ialpssi_i2c.inf,%iaLPSSi_I2C.SVCDESC%;Intel(R) Serial IO I2C Controller Driver`|`ialpssi_i2c.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iaStorAV Service </span>
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iaStorAVC Service </span>



##### Service Parameters
  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iaStorV Service </span>



##### Service Parameters
  
queuePriorityEnable : `0x00`  
BusType : `0x08`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ibbus Service </span>



##### Service Parameters
  
IPoIB : `{'DeviceId': 'IBA\\IPoIB', 'CompatibleId': b'I\x00B\x00A\x00\\\x00S\x00I\x00D\x00_\x001\x000\x000\x000\x000\x006\x006\x00a\x000\x000\x000\x002\x000\x000\x000\x000\x00\x00\x00\x00\x00', 'HardwareId': b'I\x00B\x00A\x00\\\x00I\x00P\x00o\x00I\x00B\x00\x00\x00\x00\x00', 'Description': 'Mellanox IPoIB Adapter', 'PartitionKey': '0XFFFF-IPoIB'}`  
XsigoBus : `{'DeviceId': 'IBA\\XsigoBus', 'CompatibleId': b'I\x00B\x00A\x00\\\x00S\x00I\x00D\x00_\x000\x000\x000\x000\x000\x000\x000\x000\x000\x002\x001\x003\x009\x007\x000\x002\x00\x00\x00\x00\x00', 'HardwareId': b'I\x00B\x00A\x00\\\x00X\x00s\x00i\x00g\x00o\x00B\x00u\x00s\x00\x00\x00\x00\x00', 'Description': 'Xsigo Virtual Bus', 'PartitionKey': '0XFFFF-iXsigo'}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">icssvc Service </span>

|Settings|
| :---: |
|`{}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\tetheringservice.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
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
    Access: 0x14
    SID: S-1-0-0(NULL)
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-2-155514346-2573954481-755741238-1654018636-1233331829-3075935687-2861478708
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-2-1121366727-2517420131-1100342901-1044639592-4216533239-371662368-2140263060
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-2-2543942650-389403887-2808249486-612059083-208952635-835677591-2189227231
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-2-3801529221-2855318152-1555692692-2306892612-2338533892-3542301781-2904385964

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`45 00 30 00 30 00 43 00 32 00 39 00 41 00 35 00 2d 00 30 00 46 00 36 00 32 00 2d 00 34 00 44 00 38 00 34 00 2d 00 42 00 37 00 46 00 30 00 2d 00 44 00 32 00 33 00 38 00 37 00 45 00 34 00 31 00 45 00 44 00 31 00 38 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`35 08 bc a3 3e 06 94 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">IKEEXT Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\ikeext.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `IkeServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`079e56b7-2184-e04e-ad10-86915afdad09`|`SERVICE_TRIGGER_TYPE_FIREWALL_PORT_EVENT`|`35 00 30 00 30 00 00 00 55 00 44 00 50 00 00 00 25 00 77 00 69 00 6e 00 64 00 69 00 72 00 25 00 5c 00 73 00 79 00 73 00 74 00 65 00 6d 00 33 00 32 00 5c 00 73 00 76 00 63 00 68 00 6f 00 73 00 74 00 2e 00 65 00 78 00 65 00 00 00 49 00 4b 00 45 00 45 00 58 00 54 00 00 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">IndirectKmd Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\IndirectKmd.sys,-101`|`@%SystemRoot%\system32\drivers\IndirectKmd.sys,-100`|`SERVICE_ERROR_IGNORE`|`Base`|`\SystemRoot\System32\drivers\IndirectKmd.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">inetaccs Service </span>



##### Service Parameters
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">InstallService Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\InstallService.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">intelide Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\intelide.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_CRITICAL`|`System Bus Extender`|`0x09`|`mshdc.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">intelpep Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\intelpep.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`Core Security Extensions`|`0x01`|`@intelpep.inf,%INTELPEP.SVCDESC%;Intel(R) Power Engine Plug-in Driver`|`intelpep.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">intelpmax Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\intelpmax.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x09`|`@intelpmax.inf,%SvcDesc%;Intel(R) Dynamic Device Peak Power Manager Driver`|`intelpmax.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">intelppm Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|MofImagePath|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\intelppm.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x1b`|`@cpu.inf,%IntelPPM.SvcDesc%;Intel Processor Driver`|`cpu.inf`|`%SystemRoot%\System32\drivers\processr.sys`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iorate Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\iorate.sys,-102`|`@%SystemRoot%\system32\drivers\iorate.sys,-101`|`SERVICE_ERROR_CRITICAL`|`PnP Filter`|`system32\drivers\iorate.sys`|`SERVICE_BOOT_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">IpFilterDriver Service </span>
  
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
    Access: 0x201fd
    SID: S-1-0-80-611605672-2879557022-2206624263-4029342278-3129212340
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iphlpsvc Service </span>

|config|Direct|Interfaces|Teredo|
| :---: | :---: | :---: | :---: |
|`{}`|`{}`|`{}`|`{'SP1Installed': 1}`|



##### Service Parameters
  
IPHTTPS : `{}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">IPMIDRV Service </span>

|ImagePath|Type|Start|ErrorControl|Owners|
| :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\IPMIDrv.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`ipmidrv.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">IPNAT Service </span>

|DependOnService|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`Tcpip`|`IP Network Address Translator`|`SERVICE_ERROR_NORMAL`|`System32\drivers\ipnat.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">IPT Service </span>
  
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
    Access: 0x10
    SID: S-1-0-0(NULL)
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">IpxlatCfgSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\IpxlatCfg.dll`  
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
    Access: 0x201bd
    SID: S-1-0-6
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`46 00 46 00 30 00 30 00 36 00 35 00 33 00 46 00 2d 00 30 00 36 00 34 00 41 00 2d 00 34 00 39 00 43 00 41 00 2d 00 39 00 37 00 38 00 33 00 2d 00 30 00 45 00 33 00 33 00 37 00 33 00 30 00 44 00 37 00 44 00 37 00 31 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">isapnp Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|Owners|HasBootConfig|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\isapnp.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_CRITICAL`|`Boot Bus Extender`|`0x03`|`machine.inf`|`0x00`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">iScsiPrt Service </span>



##### Service Parameters
  
BusType : `0x09`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ItSas35i Service </span>



##### Service Parameters
  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">kbdclass Service </span>



##### Service Parameters
  
ConnectMultiplePorts : `0x00`  
KeyboardDataQueueSize : `0x64`  
KeyboardDeviceBaseName : `KeyboardClass`  
MaximumPortsServiced : `0x03`  
SendOutputToAllPorts : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">kbdhid Service </span>



##### Service Parameters
  
WorkNicely : `0x00`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">kbldfltr Service </span>

|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`SERVICE_ERROR_NORMAL`|`Extended Base`|`system32\drivers\kbldfltr.sys`|`SERVICE_DEMAND_START`|`0x02`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">kdnic Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|TextModeFlags|PhysicalMedium802_3|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\kdnic.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`NDIS`|`0x03`|`@kdnic.inf,%KdNic.Service.DispName%;Microsoft Kernel Debug Network Miniport (NDIS 6.20)`|`kdnic.inf`|`0x01`|`0x00`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">KeyIso Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\keyiso.dll`  
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
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
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

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`62 00 32 00 35 00 61 00 35 00 32 00 62 00 66 00 2d 00 65 00 35 00 64 00 64 00 2d 00 34 00 66 00 34 00 61 00 2d 00 61 00 65 00 61 00 36 00 2d 00 38 00 63 00 61 00 37 00 32 00 37 00 32 00 61 00 30 00 65 00 38 00 36 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`38 00 46 00 42 00 37 00 34 00 37 00 34 00 34 00 2d 00 42 00 32 00 46 00 46 00 2d 00 34 00 43 00 30 00 30 00 2d 00 42 00 45 00 30 00 44 00 2d 00 39 00 45 00 46 00 39 00 41 00 31 00 39 00 31 00 46 00 45 00 31 00 42 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">KSecDD Service </span>

|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`SERVICE_ERROR_CRITICAL`|`Base`|`System32\Drivers\ksecdd.sys`|`SERVICE_BOOT_START`|`0x01`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">KSecPkg Service </span>

|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`SERVICE_ERROR_CRITICAL`|`Cryptography`|`System32\Drivers\ksecpkg.sys`|`SERVICE_BOOT_START`|`0x02`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ksthunk Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`Kernel Streaming Thunks`|`SERVICE_ERROR_NORMAL`|`PNP Filter`|`\SystemRoot\system32\drivers\ksthunk.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">KtmRm Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\msdtckrm.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `KtmRmServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-0(NULL)
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
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-80-2818357584-3387065753-4000393942-342927828-138088443
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
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`c3d120ce-47a2-414c-bcb8-3c7f52c8b805`|`SERVICE_TRIGGER_TYPE_CUSTOM`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">LanmanServer Service </span>

|AutotunedParameters|Linkage|Shares|
| :---: | :---: | :---: |
|`{}`|`{'Export': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00S\x00e\x00r\x00v\x00e\x00r\x00_\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00S\x00e\x00r\x00v\x00e\x00r\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00S\x00e\x00r\x00v\x00e\x00r\x00_\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00S\x00e\x00r\x00v\x00e\x00r\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00S\x00e\x00r\x00v\x00e\x00r\x00_\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00S\x00e\x00r\x00v\x00e\x00r\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00S\x00e\x00r\x00v\x00e\x00r\x00_\x00N\x00e\x00t\x00b\x00i\x00o\x00s\x00S\x00m\x00b\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00S\x00e\x00r\x00v\x00e\x00r\x00_\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00S\x00e\x00r\x00v\x00e\x00r\x00_\x00T\x00c\x00p\x00i\x00p\x00\x00\x00\x00\x00', 'Bind': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00b\x00i\x00o\x00s\x00S\x00m\x00b\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x00\x00\x00\x00\x00', 'Route': b'"\x00N\x00e\x00t\x00B\x00T\x00"\x00 \x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00"\x00\x00\x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00"\x00\x00\x00"\x00N\x00e\x00t\x00B\x00T\x00"\x00 \x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00"\x00\x00\x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00"\x00\x00\x00"\x00N\x00e\x00t\x00B\x00T\x00"\x00 \x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00"\x00\x00\x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00"\x00\x00\x00"\x00N\x00e\x00t\x00b\x00i\x00o\x00s\x00S\x00m\x00b\x00"\x00\x00\x00"\x00N\x00e\x00t\x00B\x00T\x00"\x00 \x00"\x00T\x00c\x00p\x00i\x00p\x00"\x00\x00\x00"\x00T\x00c\x00p\x00i\x00p\x00"\x00\x00\x00\x00\x00'}`|`{}`|



##### Service Parameters
  
FsctlAllowlist : `{}`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`34 00 42 00 33 00 32 00 34 00 46 00 43 00 38 00 2d 00 31 00 36 00 37 00 30 00 2d 00 30 00 31 00 44 00 33 00 2d 00 31 00 32 00 37 00 38 00 2d 00 35 00 41 00 34 00 37 00 42 00 46 00 36 00 45 00 45 00 31 00 38 00 38 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`31d1811f-ac3f-3745-9e0c-7e7b0c2f4b55`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`73 00 72 00 76 00 73 00 76 00 63 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">LanmanWorkstation Service </span>

|Linkage|NetworkProvider|
| :---: | :---: |
|`{'Export': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00W\x00o\x00r\x00k\x00s\x00t\x00a\x00t\x00i\x00o\x00n\x00_\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00W\x00o\x00r\x00k\x00s\x00t\x00a\x00t\x00i\x00o\x00n\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00W\x00o\x00r\x00k\x00s\x00t\x00a\x00t\x00i\x00o\x00n\x00_\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00W\x00o\x00r\x00k\x00s\x00t\x00a\x00t\x00i\x00o\x00n\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00W\x00o\x00r\x00k\x00s\x00t\x00a\x00t\x00i\x00o\x00n\x00_\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00W\x00o\x00r\x00k\x00s\x00t\x00a\x00t\x00i\x00o\x00n\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00W\x00o\x00r\x00k\x00s\x00t\x00a\x00t\x00i\x00o\x00n\x00_\x00N\x00e\x00t\x00b\x00i\x00o\x00s\x00S\x00m\x00b\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00W\x00o\x00r\x00k\x00s\x00t\x00a\x00t\x00i\x00o\x00n\x00_\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00L\x00a\x00n\x00m\x00a\x00n\x00W\x00o\x00r\x00k\x00s\x00t\x00a\x00t\x00i\x00o\x00n\x00_\x00T\x00c\x00p\x00i\x00p\x00\x00\x00\x00\x00', 'Bind': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00b\x00i\x00o\x00s\x00S\x00m\x00b\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x00\x00\x00\x00\x00', 'Route': b'"\x00N\x00e\x00t\x00B\x00T\x00"\x00 \x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00"\x00\x00\x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00"\x00\x00\x00"\x00N\x00e\x00t\x00B\x00T\x00"\x00 \x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00"\x00\x00\x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00"\x00\x00\x00"\x00N\x00e\x00t\x00B\x00T\x00"\x00 \x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00"\x00\x00\x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00"\x00\x00\x00"\x00N\x00e\x00t\x00b\x00i\x00o\x00s\x00S\x00m\x00b\x00"\x00\x00\x00"\x00N\x00e\x00t\x00B\x00T\x00"\x00 \x00"\x00T\x00c\x00p\x00i\x00p\x00"\x00\x00\x00"\x00T\x00c\x00p\x00i\x00p\x00"\x00\x00\x00\x00\x00'}`|`{'DeviceName': '\\Device\\LanmanRedirector', 'DisplayName': '@%systemroot%\\system32\\wkssvc.dll,-102', 'Name': 'Microsoft Windows Network', 'ProviderPath': '%SystemRoot%\\System32\\ntlanman.dll'}`|



##### Service Parameters
  
EnablePlainTextPassword : `0x00`  
EnableSecuritySignature : `0x01`  
RequireSecuritySignature : `0x00`  
ServiceDll : `%SystemRoot%\System32\wkssvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ldap Service </span>

|tracing|
| :---: |
|`{}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">lfsvc Service </span>

|Components|Service|Settings|
| :---: | :---: | :---: |
|`Components`|`{}`|`Settings`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\lfsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
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
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-3-1024-2158456844-3754929254-744589270-3611187126-2481208986-30837703-3416168463-2437063433
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-32-2158456844-3754929254-744589270-3611187126-2481208986-30837703-3416168463-2437063433
  Object ACE:
    Type:  ACCESS_ALLOWED_CALLBACK_ACE
    Flags: 0x00
    Access: 0x34
    Object Flags: 2561
    
  Object ACE:
    Type:  ACCESS_ALLOWED_CALLBACK_ACE
    Flags: 0x00
    Access: 0x34
    Object Flags: 257
    
  Object ACE:
    Type:  ACCESS_ALLOWED_CALLBACK_ACE
    Flags: 0x00
    Access: 0x34
    Object Flags: 2305
    

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 b0 bc a3 3e 0b 84 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 35 00 38 00 32 00 41 00 34 00 37 00 42 00 32 00 2d 00 42 00 43 00 44 00 38 00 2d 00 34 00 44 00 33 00 43 00 2d 00 38 00 41 00 43 00 42 00 2d 00 46 00 45 00 30 00 39 00 44 00 35 00 42 00 44 00 36 00 45 00 45 00 43 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 43 00 43 00 42 00 38 00 41 00 41 00 30 00 37 00 2d 00 37 00 32 00 32 00 35 00 2d 00 34 00 45 00 41 00 30 00 2d 00 38 00 35 00 30 00 31 00 2d 00 34 00 42 00 33 00 43 00 31 00 42 00 31 00 41 00 43 00 44 00 34 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`e4e53633-8a01-6946-84c5-bd05f3bd368b`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">LicenseManager Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\LicenseManagerSvc.dll`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`41 00 34 00 42 00 38 00 44 00 34 00 38 00 32 00 2d 00 38 00 30 00 43 00 45 00 2d 00 34 00 30 00 44 00 36 00 2d 00 39 00 33 00 34 00 44 00 2d 00 42 00 32 00 32 00 41 00 30 00 31 00 41 00 34 00 34 00 46 00 45 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 20 bc a3 21 07 85 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">lltdio Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\lltdres.dll,-6`|`@%SystemRoot%\system32\lltdres.dll,-6`|`SERVICE_ERROR_NORMAL`|`NDIS`|`system32\drivers\lltdio.sys`|`SERVICE_AUTO_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">lltdsvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\lltdsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">lmhosts Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\lmhsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`def2274f-e214-0b43-a549-7cd48cbc8245`|`SERVICE_TRIGGER_TYPE_IP_ADDRESS_AVAILABILITY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_STOP`|`2aa64bcc-2e16-4846-847a-b6bdf993e335`|`SERVICE_TRIGGER_TYPE_IP_ADDRESS_AVAILABILITY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`d804792d-905c-0942-ba6a-4c08f409934c`|`SERVICE_TRIGGER_TYPE_CUSTOM`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Lsa Service </span>

|Performance|
| :---: |
|`{'Close': 'CloseLsaPerformanceData', 'Collect': 'CollectLsaPerformanceData', 'Library': 'X:\\Windows\\System32\\Secur32.dll', 'Object List': '1570 1670', 'Open': 'OpenLsaPerformanceData'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">LSI_SAS Service </span>



##### Service Parameters
  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">LSI_SAS2i Service </span>



##### Service Parameters
  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">LSI_SAS3i Service </span>



##### Service Parameters
  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">LSI_SSS Service </span>



##### Service Parameters
  
Device : `{'DriverParameter': 'PlaceHolder=0;', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">LSM Service </span>

|Performance|
| :---: |
|`{'Close': 'CloseLagPerfData', 'Collect': 'CollectLagPerfData', 'Collect Timeout': 1000, 'Library': 'X:\\Windows\\System32\\perfts.dll', 'Open': 'OpenLagPerfData', 'Open Timeout': 1000, 'InstallType': 1, 'PerfIniFile': 'lagcounterdef.ini', 'First Counter': 9042, 'Last Counter': 9048, 'First Help': 9043, 'Last Help': 9049, 'Object List': '9042 9044 9046 9048'}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\lsm.dll`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x0d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf00ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-32-544
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf00ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">luafv Service </span>

|Instances|
| :---: |
|`Instances`|



##### Service Parameters
  
ProgramData : `X:\ProgramData`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">LxpSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\LanguageOverlayServer.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MapsBroker Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\moshost.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
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
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-2-1

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mausbhost Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\mausbhost.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x0b`|`Ucx01000`|`@mausbhost.inf,%MAUSBHost.ServiceName%;MA-USB Host Controller Driver`|`mausbhost.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mausbip Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\mausbip.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x0c`|`@mausbhost.inf,%MAUSBIP.ServiceName%;MA-USB IP Filter Driver`|`mausbhost.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MbbCx Service </span>

|DependOnService|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`NetAdapterCx`|`MBB Network Adapter Class Extension`|`SERVICE_ERROR_NORMAL`|`system32\drivers\MbbCx.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">megasas Service </span>



##### Service Parameters
  
Device : `{'DriverParameter': 'nobusywait=1', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">megasas2i Service </span>

|StorPort|
| :---: |
|`{'PowerSrbTimeout': 40}`|



##### Service Parameters
  
Device : `{'DriverParameter': 'nobusywait=1', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">megasas35i Service </span>



##### Service Parameters
  
Device : `{'DriverParameter': 'nobusywait=1', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">megasr Service </span>



##### Service Parameters
  
Device : `{'UncachedExtAlignment': 16, 'NumberOfRequests': 20}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MessagingService Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\MessagingService.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 18 bc a3 3e 03 95 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Microsoft_Bluetooth_AvrcpTransport Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\Microsoft.Bluetooth.AvrcpTransport.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@microsoft_bluetooth_avrcptransport.inf,%Microsoft_Bluetooth_AvrcpTransport.ServiceDescription%;Microsoft Bluetooth Avrcp Transport Driver`|`microsoft_bluetooth_avrcptransport.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MixedRealityOpenXRSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\MixedRealityRuntime.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mlx4_bus Service </span>



##### Service Parameters
  
DeviceManagedSteering : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MMCSS Service </span>
  
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
    Access: 0x10
    SID: S-1-0-32-545
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-2-1
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Modem Service </span>

|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`SERVICE_ERROR_IGNORE`|`Extended base`|`system32\drivers\modem.sys`|`SERVICE_DEMAND_START`|`0x04`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">monitor Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\monitor.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@monitor.inf,%Monitor.SVCDESC%;Microsoft Monitor Class Function Driver Service`|`monitor.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mouclass Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\mouclass.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@msmouse.inf,%mouclass.SvcDesc%;Mouse Class Driver`|`termmou.infmsmouse.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mouhid Service </span>



##### Service Parameters
  
UseOnlyMice : `0x00`  
TreatAbsoluteAsRelative : `0x00`  
TreatAbsolutePointerAsAbsolute : `0x00`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mountmgr Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\mountmgr.sys,-101`|`@%SystemRoot%\system32\drivers\mountmgr.sys,-100`|`SERVICE_ERROR_CRITICAL`|`System Bus Extender`|`System32\drivers\mountmgr.sys`|`SERVICE_BOOT_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mpsdrv Service </span>
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x20085
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe009f
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe009d
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x85
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf00ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mpssvc Service </span>



##### Service Parameters
  
ACService : `{}`  
AppCs : `{}`  
PortKeywords : `PortKeywords`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x20085
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe009f
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe009d
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x85
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf00ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MRxDAV Service </span>

|EncryptedDirectories|
| :---: |
|`{'EncryptedDirectories': ''}`|



##### Service Parameters
  
CloseRequestTimeoutInSec : `0x708`  
CreateRequestTimeoutInSec : `0x708`  
CreateSrvCallRequestTimeoutInSec : `0x14`  
CreateVNetRootRequestTimeoutInSec : `0x3c`  
DAVDebugFlag : `0x00`  
DevFsCtlRequestTimeoutInSec : `0x258`  
FileInformationCacheLifeTimeInSec : `0x3c`  
FileNotFoundCacheLifeTimeInSec : `0x3c`  
FinalizeFcbRequestTimeoutInSec : `0x3c`  
FinalizeFobxRequestTimeoutInSec : `0x3c`  
FinalizeSrvCallRequestTimeoutInSec : `0x258`  
FinalizeVNetRootRequestTimeoutInSec : `0x258`  
FsCtlRequestTimeoutInSec : `0x708`  
LockRefreshRequestTimeoutInSec : `0x258`  
NameCacheMaxEntries : `0x12c`  
QueryDirectoryRequestTimeoutInSec : `0x258`  
QueryFileInfoRequestTimeoutInSec : `0x258`  
QueryVolumeInfoRequestTimeoutInSec : `0x258`  
ReNameRequestTimeoutInSec : `0x258`  
SetFileInfoRequestTimeoutInSec : `0x258`  
UMRxDebugFlag : `0x00`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mrxsmb Service </span>

|DependOnService|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`rdbssmsquic`|`@%systemroot%\system32\wkssvc.dll,-1003`|`@%systemroot%\system32\wkssvc.dll,-1002`|`SERVICE_ERROR_NORMAL`|`Network`|`system32\DRIVERS\mrxsmb.sys`|`SERVICE_DEMAND_START`|`0x05`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mrxsmb10 Service </span>

|DependOnService|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`mrxsmb`|`@%systemroot%\system32\wkssvc.dll,-1005`|`@%systemroot%\system32\wkssvc.dll,-1004`|`SERVICE_ERROR_NORMAL`|`Network`|`system32\DRIVERS\mrxsmb10.sys`|`SERVICE_AUTO_START`|`0x06`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mrxsmb20 Service </span>

|DependOnService|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`mrxsmb`|`@%systemroot%\system32\wkssvc.dll,-1007`|`@%systemroot%\system32\wkssvc.dll,-1006`|`SERVICE_ERROR_NORMAL`|`Network`|`system32\DRIVERS\mrxsmb20.sys`|`SERVICE_DEMAND_START`|`0x07`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MsBridge Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|NdisImPlatformProviderClass|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\bridgeres.dll,-1`|`@%SystemRoot%\system32\bridgeres.dll,-1`|`SERVICE_ERROR_NORMAL`|`NDIS`|`System32\drivers\bridge.sys`|`0x01`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MSDTC Service </span>

|Performance|
| :---: |
|`{'Close': 'DtcPerfClose', 'Collect': 'DtcPerfCollect', 'Library': '%systemroot%\\system32\\msdtcuiu.DLL', 'Open': 'DtcPerfOpen', 'InstallType': 1, 'PerfIniFile': 'msdtcprf.ini', 'First Counter': 6776, 'Last Counter': 6802, 'First Help': 6777, 'Last Help': 6803, 'Object List': '6776'}`|
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-0(NULL)
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x200ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf00ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-80-3960419045-2460139048-4046793004-1809597027-2250574426
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MSDTC Bridge 4.0.0.0 Service </span>

|Performance|
| :---: |
|`{'CategoryOptions': 3, 'Close': 'ClosePerformanceData', 'Collect': 'CollectPerformanceData', 'Counter Names': b'M\x00e\x00s\x00s\x00a\x00g\x00e\x00 \x00s\x00e\x00n\x00d\x00 \x00f\x00a\x00i\x00l\x00u\x00r\x00e\x00s\x00/\x00s\x00e\x00c\x00\x00\x00P\x00r\x00e\x00p\x00a\x00r\x00e\x00 \x00r\x00e\x00t\x00r\x00y\x00 \x00c\x00o\x00u\x00n\x00t\x00/\x00s\x00e\x00c\x00\x00\x00C\x00o\x00m\x00m\x00i\x00t\x00 \x00r\x00e\x00t\x00r\x00y\x00 \x00c\x00o\x00u\x00n\x00t\x00/\x00s\x00e\x00c\x00\x00\x00P\x00r\x00e\x00p\x00a\x00r\x00e\x00d\x00 \x00r\x00e\x00t\x00r\x00y\x00 \x00c\x00o\x00u\x00n\x00t\x00/\x00s\x00e\x00c\x00\x00\x00R\x00e\x00p\x00l\x00a\x00y\x00 \x00r\x00e\x00t\x00r\x00y\x00 \x00c\x00o\x00u\x00n\x00t\x00/\x00s\x00e\x00c\x00\x00\x00F\x00a\x00u\x00l\x00t\x00s\x00 \x00r\x00e\x00c\x00e\x00i\x00v\x00e\x00d\x00 \x00c\x00o\x00u\x00n\x00t\x00/\x00s\x00e\x00c\x00\x00\x00F\x00a\x00u\x00l\x00t\x00s\x00 \x00s\x00e\x00n\x00t\x00 \x00c\x00o\x00u\x00n\x00t\x00/\x00s\x00e\x00c\x00\x00\x00A\x00v\x00e\x00r\x00a\x00g\x00e\x00 \x00p\x00a\x00r\x00t\x00i\x00c\x00i\x00p\x00a\x00n\x00t\x00 \x00p\x00r\x00e\x00p\x00a\x00r\x00e\x00 \x00r\x00e\x00s\x00p\x00o\x00n\x00s\x00e\x00 \x00t\x00i\x00m\x00e\x00\x00\x00A\x00v\x00e\x00r\x00a\x00g\x00e\x00 \x00p\x00a\x00r\x00t\x00i\x00c\x00i\x00p\x00a\x00n\x00t\x00 \x00p\x00r\x00e\x00p\x00a\x00r\x00e\x00 \x00r\x00e\x00s\x00p\x00o\x00n\x00s\x00e\x00 \x00t\x00i\x00m\x00e\x00 \x00B\x00a\x00s\x00e\x00\x00\x00A\x00v\x00e\x00r\x00a\x00g\x00e\x00 \x00p\x00a\x00r\x00t\x00i\x00c\x00i\x00p\x00a\x00n\x00t\x00 \x00c\x00o\x00m\x00m\x00i\x00t\x00 \x00r\x00e\x00s\x00p\x00o\x00n\x00s\x00e\x00 \x00t\x00i\x00m\x00e\x00\x00\x00A\x00v\x00e\x00r\x00a\x00g\x00e\x00 \x00p\x00a\x00r\x00t\x00i\x00c\x00i\x00p\x00a\x00n\x00t\x00 \x00c\x00o\x00m\x00m\x00i\x00t\x00 \x00r\x00e\x00s\x00p\x00o\x00n\x00s\x00e\x00 \x00t\x00i\x00m\x00e\x00 \x00B\x00a\x00s\x00e\x00\x00\x00\x00\x00', 'Counter Types': b'2\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x008\x000\x005\x004\x003\x008\x004\x006\x004\x00\x00\x001\x000\x007\x003\x009\x003\x009\x004\x005\x008\x00\x00\x008\x000\x005\x004\x003\x008\x004\x006\x004\x00\x00\x001\x000\x007\x003\x009\x003\x009\x004\x005\x008\x00\x00\x00\x00\x00', 'IsMultiInstance': 0, 'Library': '%systemroot%\\system32\\NETFXPerf.dll', 'Open': 'OpenPerformanceData', 'InstallType': 1, 'PerfIniFile': '_TransactionBridgePerfCounters_d.ini', 'First Counter': 6804, 'Last Counter': 6826, 'First Help': 6805, 'Last Help': 6827, 'Object List': '6804'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Msfs Service </span>

|ErrorControl|Group|Start|Type|
| :---: | :---: | :---: | :---: |
|`SERVICE_ERROR_NORMAL`|`File system`|`SERVICE_SYSTEM_START`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">msgpiowin32 Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\msgpiowin32.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x29`|`@msgpiowin32.inf,%GPIO.SvcDesc%;Common Driver for Buttons, DockMode and Laptop/Slate Indicator`|`msgpiowin32.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mshidkmdf Service </span>

|ImagePath|Type|Start|ErrorControl|Owners|Description|DisplayName|Group|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\mshidkmdf.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_IGNORE`|`buttonconverter.infhidvhf.inf`|`@%SystemRoot%\system32\drivers\mshidkmdf.sys,-101`|`@%SystemRoot%\system32\drivers\mshidkmdf.sys,-100`|`Base`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mshidumdf Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|Description|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\mshidumdf.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_IGNORE`|`Base`|`0x0e`|`@%SystemRoot%\system32\drivers\mshidumdf.sys,-100`|`hidbthle.infxinputhid.inf`|`@%SystemRoot%\system32\drivers\mshidumdf.sys,-101`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">msisadrv Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\msisadrv.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_CRITICAL`|`Boot Bus Extender`|`0x02`|`machine.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MSiSCSI Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\iscsiexe.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">msiserver Service </span>
  
Security : 
```
Owner: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
Group: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MsKeyboardFilter Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\KeyboardFilterSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MSKSSRV Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\MSKSSRV.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x12`|`@ksfilter.inf,%MSKSSRV.DeviceDesc%;Microsoft Streaming Service Proxy`|`ksfilter.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MsLldp Service </span>



##### Service Parameters
  
Agents : `{}`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_DENIED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-546
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01df
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-32-549
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x34
    SID: S-1-0-80-3141615172-2057878085-1754447212-2405740020-3916490453

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MSPCLOCK Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\MSPCLOCK.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x10`|`@ksfilter.inf,%MSPCLOCK.DeviceDesc%;Microsoft Streaming Clock Proxy`|`ksfilter.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MSPQM Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\MSPQM.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x11`|`@ksfilter.inf,%MSPQM.DeviceDesc%;Microsoft Streaming Quality Manager Proxy`|`ksfilter.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MsQuic Service </span>



##### Service Parameters
  
Apps : `{}`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
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
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-3
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MsRPC Service </span>

|ErrorControl|Start|Tag|Type|
| :---: | :---: | :---: | :---: |
|`SERVICE_ERROR_NORMAL`|`SERVICE_DEMAND_START`|`0x01`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MSSCNTRS Service </span>

|Performance|
| :---: |
|`{'Close': 'Close', 'Collect': 'Collect', 'Library': '%systemroot%\\system32\\msscntrs.dll', 'Open': 'Open'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MsSecFlt Service </span>

|Instances|
| :---: |
|`Instances`|
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x0b
    Access: 0x10000000
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mssmbios Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\mssmbios.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_SYSTEM_START`|`SERVICE_ERROR_NORMAL`|`@mssmbios.inf,%mssmbios_svcdesc%;Microsoft System Management BIOS Driver`|`mssmbios.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MSTEE Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\MSTEE.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x13`|`@ksfilter.inf,%MSTEE.DeviceDesc%;Microsoft Streaming Tee/Sink-to-Sink Converter`|`ksfilter.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">MTConfig Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\MTConfig.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x1e`|`@mtconfig.inf,%MTConfig.SVCDESC%;Microsoft Input Configuration Driver`|`mtconfig.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Mup Service </span>



##### Service Parameters
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">mvumis Service </span>



##### Service Parameters
  
Device : `{'NumberOfRequests': 255, 'MaximumSGList': 255}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">napagent Service </span>

|Qecs|
| :---: |
|`Qecs`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NativeWifiP Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\System32\drivers\nwifi.sys,-101`|`SERVICE_ERROR_NORMAL`|`NDIS`|`system32\DRIVERS\nwifi.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NaturalAuthentication Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\NaturalAuth.dll`  
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
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-2-1
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

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`63 00 63 00 34 00 62 00 34 00 30 00 38 00 63 00 2d 00 34 00 63 00 34 00 65 00 2d 00 34 00 32 00 32 00 66 00 2d 00 39 00 38 00 34 00 39 00 2d 00 34 00 37 00 62 00 62 00 34 00 37 00 62 00 64 00 34 00 64 00 32 00 65 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NcaSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\ncasvc.dll`  
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
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`e6ca9f65-db5b-a94d-b1ff-ca2a178d46e0`|`SERVICE_TRIGGER_TYPE_GROUP_POLICY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`ba0ae21c-5198-2144-9430-1ddeb766e809`|`SERVICE_TRIGGER_TYPE_DOMAIN_JOIN`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_STOP`|`6e51afdd-c258-6648-9574-c3b615d42ea1`|`SERVICE_TRIGGER_TYPE_DOMAIN_JOIN`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NcbService Service </span>

|NCB|
| :---: |
|`{}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\ncbservice.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`65 00 34 00 30 00 66 00 37 00 62 00 35 00 37 00 2d 00 37 00 61 00 32 00 35 00 2d 00 34 00 63 00 64 00 33 00 2d 00 61 00 31 00 33 00 35 00 2d 00 37 00 66 00 37 00 64 00 33 00 64 00 66 00 39 00 64 00 31 00 36 00 62 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`35 00 32 00 32 00 32 00 38 00 32 00 31 00 66 00 2d 00 64 00 35 00 65 00 32 00 2d 00 34 00 38 00 38 00 35 00 2d 00 38 00 34 00 66 00 31 00 2d 00 35 00 66 00 36 00 31 00 38 00 35 00 61 00 30 00 65 00 63 00 34 00 31 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`38 00 38 00 30 00 66 00 64 00 35 00 35 00 65 00 2d 00 34 00 33 00 62 00 39 00 2d 00 31 00 31 00 65 00 30 00 2d 00 62 00 31 00 61 00 38 00 2d 00 63 00 66 00 34 00 65 00 64 00 66 00 64 00 37 00 32 00 30 00 38 00 35 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 66 00 64 00 64 00 30 00 39 00 39 00 63 00 36 00 2d 00 64 00 66 00 30 00 36 00 2d 00 34 00 39 00 30 00 34 00 2d 00 38 00 33 00 62 00 34 00 2d 00 61 00 38 00 37 00 61 00 32 00 37 00 39 00 30 00 33 00 63 00 37 00 30 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 3e 06 83 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NcdAutoSetup Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\NcdAutoSetup.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `SvchostMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`3faccffb-6084-9f41-8e48-1f0b49cdb85e`|`SERVICE_TRIGGER_TYPE_CUSTOM`|`50 00 52 00 4f 00 46 00 49 00 4c 00 45 00 5f 00 43 00 48 00 41 00 4e 00 47 00 45 00 44 00 5f 00 54 00 4f 00 5f 00 50 00 52 00 49 00 56 00 41 00 54 00 45 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ndfltr Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|BootFlags|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\ndfltr.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`PNP Filter`|`0x02`|`ibbus`|`@mlx4_bus.inf,%ndfltr.ServiceDesc%;NetworkDirect Service`|`mlx4_bus.inf`|`0x01`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NDIS Service </span>

|IfTypes|
| :---: |
|`IfTypes`|



##### Service Parameters
  
MaxCachedNblContextSize : `0x200`  
PortAuthReceiveAuthorizationState : `0x02`  
PortAuthReceiveControlState : `0x02`  
PortAuthSendAuthorizationState : `0x02`  
PortAuthSendControlState : `0x02`  
ReceiveWorkerDisableAutoStart : `0x00`  
TrackNblOwner : `0x02`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NdisCap Service </span>



##### Service Parameters
  
PersistentRefCount : `0x01`  
RefCount : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NdisImPlatform Service </span>



##### Service Parameters
  
AdapterFilterAllowList : `6d 00 73 00 5f 00 6e 00 65 00 74 00 6d 00 6f 00 6e 00 00 00 4d 00 53 00 5f 00 4e 00 64 00 69 00 73 00 43 00 61 00 70 00 00 00 00 00`  
AdapterProtocolAllowList : `00 00 00 00`  
VirtualMiniportFilterBlockList : `00 00 00 00`  
VirtualMiniportProtocolBlockList : `00 00 00 00`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NdisTapi Service </span>

|AsyncEventQueueSize|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`0x300`|`@%systemroot%\system32\mprmsg.dll,-32001`|`@%systemroot%\system32\mprmsg.dll,-32001`|`SERVICE_ERROR_NORMAL`|`NDIS`|`System32\DRIVERS\ndistapi.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Ndisuio Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`NDIS Usermode I/O Protocol`|`SERVICE_ERROR_NORMAL`|`NDIS`|`system32\drivers\ndisuio.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NdisVirtualBus Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\NdisVirtualBus.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@%SystemRoot%\System32\drivers\NdisVirtualBus.sys,-200`|`ndisvirtualbus.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NdisWan Service </span>

|Linkage|
| :---: |
|`{'Export': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00d\x00i\x00s\x00W\x00a\x00n\x00\x00\x00\x00\x00', 'Bind': b'\x00\x00', 'Route': b'\x00\x00'}`|



##### Service Parameters
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ndiswanlegacy Service </span>

|Linkage|
| :---: |
|`{'Export': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00n\x00d\x00i\x00s\x00w\x00a\x00n\x00l\x00e\x00g\x00a\x00c\x00y\x00\x00\x00\x00\x00', 'Bind': b'\x00\x00', 'Route': b'\x00\x00'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NDKPing Service </span>

|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: |
|`NDKPing Driver`|`SERVICE_ERROR_NORMAL`|`system32\drivers\NDKPing.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ndproxy Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\ndproxy.sys,-6000`|`@%SystemRoot%\system32\drivers\ndproxy.sys,-6000`|`SERVICE_ERROR_NORMAL`|`PNP_TDI`|`System32\DRIVERS\NDProxy.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Ndu Service </span>

|DependOnService|Description|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`tcpip`|`@%SystemRoot%\system32\drivers\Ndu.sys,-10002`|`@%SystemRoot%\system32\drivers\Ndu.sys,-10001`|`SERVICE_ERROR_NORMAL`|`system32\drivers\Ndu.sys`|`SERVICE_AUTO_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NetAdapterCx Service </span>

|DependOnService|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`ndis`|`Network Adapter Wdf Class Extension Library`|`SERVICE_ERROR_NORMAL`|`system32\drivers\NetAdapterCx.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NetBIOS Service </span>

|Linkage|
| :---: |
|`{'Export': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00I\x00O\x00S\x00_\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00I\x00O\x00S\x00_\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00I\x00O\x00S\x00_\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00I\x00O\x00S\x00_\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x00\x00\x00\x00\x00', 'Bind': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x00\x00\x00\x00\x00', 'Route': b'"\x00N\x00e\x00t\x00B\x00T\x00"\x00 \x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00"\x00\x00\x00"\x00N\x00e\x00t\x00B\x00T\x00"\x00 \x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00"\x00\x00\x00"\x00N\x00e\x00t\x00B\x00T\x00"\x00 \x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00"\x00\x00\x00"\x00N\x00e\x00t\x00B\x00T\x00"\x00 \x00"\x00T\x00c\x00p\x00i\x00p\x00"\x00\x00\x00\x00\x00', 'LanaMap': b'\x01\x00\x01\x01\x01\x02\x01\x03'}`|



##### Service Parameters
  
MaxLana : `0x03`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NetbiosSmb Service </span>

|Linkage|
| :---: |
|`{'Export': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00b\x00i\x00o\x00s\x00S\x00m\x00b\x00\x00\x00\x00\x00', 'Bind': b'\x00\x00', 'Route': b'\x00\x00'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NetBT Service </span>

|Linkage|
| :---: |
|`{'OtherDependencies': b'T\x00c\x00p\x00i\x00p\x00\x00\x00\x00\x00', 'Export': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00N\x00e\x00t\x00B\x00T\x00_\x00T\x00c\x00p\x00i\x00p\x00\x00\x00\x00\x00', 'Bind': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x00\x00\x00\x00\x00', 'Route': b'"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00"\x00\x00\x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00"\x00\x00\x00"\x00T\x00c\x00p\x00i\x00p\x006\x00"\x00 \x00"\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00"\x00\x00\x00"\x00T\x00c\x00p\x00i\x00p\x00"\x00\x00\x00\x00\x00'}`|



##### Service Parameters
  
Interfaces : `{}`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-32-549
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x40
    SID: S-1-0-19
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x40
    SID: S-1-0-20
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-32-556

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Netlogon Service </span>



##### Service Parameters
  
DisablePasswordChange : `0x00`  
MaximumPasswordAge : `0x1e`  
RequireSignOrSeal : `0x01`  
RequireStrongKey : `0x01`  
SealSecureChannel : `0x01`  
ServiceDll : `%SystemRoot%\system32\netlogon.dll`  
SignSecureChannel : `0x01`  
Update : `no`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Netman Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\netman.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">netprofm Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\netprofmsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NetSetupSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\NetSetupSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `NetSetupServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x1d
    SID: S-1-0-20
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x1d
    SID: S-1-0-19
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x1d
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x1d
    SID: S-1-0-32-545
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x1d
    SID: S-1-0-32-556
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 23 0a 8f 12`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 23 0a 8f 12`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`61 00 31 00 31 00 31 00 66 00 31 00 63 00 35 00 2d 00 35 00 39 00 32 00 33 00 2d 00 34 00 37 00 63 00 30 00 2d 00 39 00 61 00 36 00 38 00 2d 00 64 00 30 00 62 00 61 00 66 00 62 00 35 00 37 00 37 00 39 00 30 00 31 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NetTcpPortSharing Service </span>
  
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
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-6

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">netvsc Service </span>



##### Service Parameters
  
Wdf : `{'DbgPrintOn': 0, 'DbgBreakOnError': 0}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NgcCtnrSvc Service </span>



##### Service Parameters
  
RecoveryServiceClientId : `9115dd05-fad5-4f9c-acc7-305d08b1b04e`  
RecoveryServiceDomain : `cred.microsoft.com`  
RecoveryServiceResource : `https://cred.microsoft.com/`  
ServiceDll : `%SystemRoot%\System32\NgcCtnrSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
VscHandlerPath : `X:\Windows\System32\NgcCtnrGidsHandler.dll`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x20085
    SID: S-1-0-11
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`33 00 30 00 30 00 33 00 34 00 38 00 34 00 33 00 2d 00 30 00 32 00 39 00 64 00 2d 00 34 00 36 00 65 00 63 00 2d 00 38 00 66 00 66 00 66 00 2d 00 35 00 64 00 31 00 32 00 39 00 38 00 37 00 66 00 38 00 35 00 63 00 34 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`32 00 64 00 32 00 34 00 66 00 66 00 30 00 62 00 2d 00 31 00 62 00 61 00 62 00 2d 00 34 00 30 00 34 00 63 00 2d 00 61 00 30 00 66 00 64 00 2d 00 34 00 32 00 63 00 38 00 35 00 35 00 37 00 37 00 62 00 66 00 36 00 38 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`37 00 36 00 34 00 32 00 32 00 34 00 39 00 42 00 2d 00 38 00 34 00 43 00 32 00 2d 00 34 00 34 00 30 00 34 00 2d 00 42 00 36 00 45 00 42 00 2d 00 31 00 45 00 30 00 41 00 32 00 34 00 35 00 38 00 38 00 33 00 39 00 41 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`65 00 36 00 66 00 38 00 39 00 36 00 38 00 30 00 2d 00 66 00 63 00 39 00 38 00 2d 00 31 00 31 00 65 00 33 00 2d 00 38 00 30 00 64 00 34 00 2d 00 31 00 30 00 36 00 30 00 34 00 62 00 36 00 38 00 31 00 63 00 66 00 61 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 28 00 92 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 18 bc a3 23 09 85 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|6|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 68 bc a3 23 09 85 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NgcSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\ngcsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `NgcServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x20085
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe009d
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x85
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf00ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`30 00 65 00 33 00 61 00 65 00 30 00 39 00 35 00 2d 00 38 00 61 00 32 00 33 00 2d 00 34 00 38 00 66 00 34 00 2d 00 39 00 37 00 38 00 32 00 2d 00 30 00 33 00 63 00 31 00 35 00 39 00 34 00 61 00 38 00 39 00 30 00 65 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`63 00 32 00 32 00 35 00 65 00 37 00 39 00 39 00 2d 00 32 00 39 00 64 00 65 00 2d 00 34 00 32 00 61 00 66 00 2d 00 62 00 63 00 30 00 35 00 2d 00 31 00 65 00 32 00 31 00 32 00 37 00 63 00 63 00 30 00 35 00 36 00 65 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`64 00 39 00 38 00 34 00 34 00 65 00 64 00 39 00 2d 00 66 00 37 00 32 00 61 00 2d 00 34 00 37 00 34 00 35 00 2d 00 61 00 34 00 61 00 31 00 2d 00 65 00 65 00 37 00 31 00 66 00 39 00 35 00 30 00 37 00 38 00 31 00 64 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`32 00 62 00 37 00 30 00 62 00 65 00 64 00 36 00 2d 00 31 00 37 00 35 00 37 00 2d 00 34 00 64 00 32 00 32 00 2d 00 39 00 66 00 33 00 39 00 2d 00 34 00 34 00 38 00 35 00 38 00 39 00 66 00 62 00 65 00 62 00 66 00 35 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`39 00 63 00 62 00 63 00 39 00 64 00 33 00 61 00 2d 00 37 00 35 00 38 00 36 00 2d 00 34 00 38 00 31 00 34 00 2d 00 38 00 64 00 37 00 30 00 2d 00 31 00 38 00 37 00 33 00 37 00 64 00 63 00 62 00 65 00 35 00 32 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`34 00 45 00 32 00 35 00 46 00 34 00 41 00 32 00 2d 00 32 00 31 00 45 00 38 00 2d 00 34 00 30 00 43 00 45 00 2d 00 42 00 34 00 30 00 31 00 2d 00 33 00 32 00 30 00 35 00 30 00 34 00 31 00 33 00 31 00 34 00 33 00 41 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|6|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`38 00 33 00 33 00 37 00 41 00 45 00 42 00 43 00 2d 00 35 00 35 00 36 00 34 00 2d 00 34 00 36 00 46 00 44 00 2d 00 42 00 43 00 34 00 31 00 2d 00 37 00 37 00 39 00 38 00 46 00 31 00 38 00 44 00 32 00 45 00 34 00 42 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|7|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`6509f400-9de8-8744-9890-87c3abb211f4`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NlaSvc Service </span>

|LANIds|
| :---: |
|`{'WLANDllName': 'WlanApi.dll'}`|



##### Service Parameters
  
Cache : `{}`  
Internet : `Internet`  
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
#### <span style="text-align: center; font-size:2em;">Npfs Service </span>

|Aliases|
| :---: |
|`{'lsass': b'p\x00r\x00o\x00t\x00e\x00c\x00t\x00e\x00d\x00_\x00s\x00t\x00o\x00r\x00a\x00g\x00e\x00\x00\x00n\x00e\x00t\x00l\x00o\x00g\x00o\x00n\x00\x00\x00l\x00s\x00a\x00r\x00p\x00c\x00\x00\x00s\x00a\x00m\x00r\x00\x00\x00\x00\x00', 'ntsvcs': b's\x00v\x00c\x00c\x00t\x00l\x00\x00\x00\x00\x00'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">npsvctrig Service </span>

|Instances|
| :---: |
|`Instances`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">nsi Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\nsisvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">nsiproxy Service </span>

|Description|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\nsiproxy.sys,-1`|`@%SystemRoot%\system32\drivers\nsiproxy.sys,-2`|`SERVICE_ERROR_NORMAL`|`system32\drivers\nsiproxy.sys`|`SERVICE_SYSTEM_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">NTDS Service </span>

|RID Values|
| :---: |
|`{}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Ntfs Service </span>

|EFS|
| :---: |
|`EFS`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Null Service </span>

|ErrorControl|Group|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: |
|`SERVICE_ERROR_NORMAL`|`Base`|`SERVICE_SYSTEM_START`|`0x01`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">nvdimm Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\nvdimm.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`Primary Disk`|`0x01`|`@nvdimm.inf,%nvdimm.SvcDesc%;Microsoft NVDIMM device driver`|`nvdimm.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">nvraid Service </span>



##### Service Parameters
  
Device : `{'EnableQueryAccessAlignment': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">nvstor Service </span>



##### Service Parameters
  
Device : `{'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">OneSyncSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\APHostService.dll`  
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
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-11

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">p2pimsvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\pnrpsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `IMServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_DENIED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-546
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x200fd
    SID: S-1-0-32-549
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-32-555
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-32-545

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">p2psvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\p2psvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `GroupServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_DENIED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-546
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x200fd
    SID: S-1-0-32-549
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-32-555
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-32-545

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Parport Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\parport.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_IGNORE`|`Parallel arbitrator`|`0x01`|`@msports.inf,%Parport.SVCDESC%;Parallel port driver`|`msports.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">partmgr Service </span>



##### Service Parameters
  
VolumeManagerAltitudes : `{'clusbflt': 4, 'spaceport': 16, 'volmgr': 32}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PcaSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\pcasvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
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
    Access: 0x2019d
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
#### <span style="text-align: center; font-size:2em;">pci Service </span>



##### Service Parameters
  
DmaRemappingCompatible : `0x02`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">pciide Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\pciide.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_CRITICAL`|`System Bus Extender`|`0x08`|`mshdc.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">pcmcia Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\pcmcia.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`System Bus Extender`|`0x01`|`pcmcia.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">pcw Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`Performance Counters for Windows Driver`|`SERVICE_ERROR_NORMAL`|`System Reserved`|`System32\drivers\pcw.sys`|`SERVICE_BOOT_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">pdc Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\pdc.sys,-101`|`@%SystemRoot%\system32\drivers\pdc.sys,-100`|`SERVICE_ERROR_CRITICAL`|`Boot Bus Extender`|`system32\drivers\pdc.sys`|`SERVICE_BOOT_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PEAUTH Service </span>

|Instances|
| :---: |
|`{'DefaultInstance': 'PEAUTH'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PeerDistSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\peerdistsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `SVCServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-32-549
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-32-555
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-32-545
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x94
    SID: S-1-0-2-1
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">perceptionsimulation Service </span>

|DependOnService|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`rpcss`|`@%systemroot%\system32\PerceptionSimulation\PerceptionSimulationService.exe,-102`|`@%systemroot%\system32\PerceptionSimulation\PerceptionSimulationService.exe,-101`|`SERVICE_ERROR_NORMAL`|`3c 00 00 00 00 00 00 00 00 00 00 00 04 00 00 00 14 00 00 00 01 00 00 00 64 00 00 00 01 00 00 00 e8 03 00 00 01 00 00 00 e8 03 00 00 00 00 00 00 00 00 00 00`|`%systemroot%\system32\PerceptionSimulation\PerceptionSimulationService.exe`|`LocalSystem`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">percsas2i Service </span>



##### Service Parameters
  
Device : `{'DriverParameter': 'nonuma=1', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">percsas3i Service </span>



##### Service Parameters
  
Device : `{'DriverParameter': 'placeholder=0', 'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PerfDisk Service </span>

|Performance|
| :---: |
|`{'Close': 'CloseDiskObject', 'Collect': 'CollectDiskObjectData', 'Collect Timeout': 2000, 'Library': '%SystemRoot%\\System32\\perfdisk.dll', 'Object List': '234 236', 'Open': 'OpenDiskObject', 'Open Timeout': 5000}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PerfHost Service </span>

|DependOnService|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|WOW64|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`RPCSS`|`@%systemroot%\SysWow64\perfhost.exe,-1`|`@%systemroot%\sysWow64\perfhost.exe,-2`|`SERVICE_ERROR_NORMAL`|`80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 60 ea 00 00 00 00 00 00 00 00 00 00`|`%SystemRoot%\SysWow64\perfhost.exe`|`NT AUTHORITY\LocalService`|`['SeImpersonatePrivilege']`|`SERVICE_SID_TYPE_RESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|`0x14c`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PerfNet Service </span>

|Performance|
| :---: |
|`{'Close': 'CloseNetSvcsObject', 'Collect': 'CollectNetSvcsObjectData', 'Collect Timeout': 5000, 'Library': '%SystemRoot%\\System32\\perfnet.dll', 'Object List': '52 262 330 1300', 'Open': 'OpenNetSvcsObject', 'Open Timeout': 8000}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PerfOS Service </span>

|Performance|
| :---: |
|`{'Close': 'CloseOSObject', 'Collect': 'CollectOSObjectData', 'Collect Timeout': 8000, 'Library': '%SystemRoot%\\System32\\perfos.dll', 'Object List': '2 4 86 238 260 700 1814', 'Open': 'OpenOSObject', 'Open Timeout': 5000}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PerfProc Service </span>

|Performance|
| :---: |
|`{'Close': 'CloseSysProcessObject', 'Collect': 'CollectSysProcessObjectData', 'Collect Timeout': 8000, 'Library': '%SystemRoot%\\System32\\perfproc.dll', 'Object List': '230 232 786 740 816 1408 1500 1548 1760', 'Open': 'OpenSysProcessObject', 'Open Timeout': 10000}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PhoneSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\PhoneService.dll`  
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
    Access: 0xf01ff
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
    Access: 0x14
    SID: S-1-0-0(NULL)
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-2-1

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`66 00 32 00 36 00 65 00 32 00 33 00 37 00 32 00 2d 00 64 00 36 00 30 00 31 00 2d 00 34 00 34 00 66 00 30 00 2d 00 38 00 34 00 62 00 38 00 2d 00 32 00 35 00 39 00 31 00 64 00 32 00 61 00 66 00 32 00 66 00 38 00 32 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`61 00 33 00 62 00 61 00 65 00 33 00 66 00 37 00 2d 00 62 00 66 00 39 00 37 00 2d 00 34 00 39 00 66 00 62 00 2d 00 62 00 34 00 38 00 64 00 2d 00 32 00 61 00 35 00 65 00 38 00 36 00 35 00 37 00 62 00 34 00 33 00 36 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 68 bc a3 2f 02 92 09`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PimIndexMaintenanceSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\PimIndexMaintenance.dll`  
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
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PktMon Service </span>



##### Service Parameters
  
WppRecorder_PerBufferMaxBytes : `0x10000`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">pla Service </span>

|Configuration|
| :---: |
|`{}`|



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\pla.dll`  
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
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x1fd
    SID: S-1-0-32-549
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x195
    SID: S-1-0-0(NULL)
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PlugPlay Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\umpnpmgr.dll`  
ServiceMain : `PlugPlayServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">pmem Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\pmem.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`@pmem.inf,%pmem.SvcDesc%;Microsoft persistent memory disk driver`|`pmem.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PNPMEM Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\pnpmem.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@memory.inf,%PNPMEM.SvcDesc%;Microsoft Memory Module Driver`|`memory.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PNRPAutoReg Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\pnrpauto.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `PnrpAutoSVCServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_DENIED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-546
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x200fd
    SID: S-1-0-32-549
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-32-555

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PNRPsvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\pnrpsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `SVCServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_DENIED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-546
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x200fd
    SID: S-1-0-32-549
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-32-555
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-32-545

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PolicyAgent Service </span>



##### Service Parameters
  
Cache : `{}`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`079e56b7-2184-e04e-ad10-86915afdad09`|`SERVICE_TRIGGER_TYPE_FIREWALL_PORT_EVENT`|`52 00 50 00 43 00 00 00 54 00 43 00 50 00 00 00 25 00 77 00 69 00 6e 00 64 00 69 00 72 00 25 00 5c 00 73 00 79 00 73 00 74 00 65 00 6d 00 33 00 32 00 5c 00 73 00 76 00 63 00 68 00 6f 00 73 00 74 00 2e 00 65 00 78 00 65 00 00 00 70 00 6f 00 6c 00 69 00 63 00 79 00 61 00 67 00 65 00 6e 00 74 00 00 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">portcfg Service </span>

|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: |
|`SERVICE_ERROR_NORMAL`|`PnP Filter`|`\SystemRoot\System32\drivers\portcfg.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PortProxy Service </span>
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Power Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\umpo.dll`  
ServiceMain : `UmpoMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PptpMiniport Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Description|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\raspptp.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@%systemroot%\system32\mprmsg.dll,-32006`|`@%systemroot%\system32\mprmsg.dll,-32006`|`netrasa.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PrintWorkflowUserSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\PrintWorkflowService.dll`  
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
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-3-1024-4044835139-2658482041-3127973164-329287231-3865880861-1938685643-461067658-1087000422
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-21-2702878673-795188819-444038987-2781

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Processor Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\processr.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x1a`|`@cpu.inf,%Processor.SvcDesc%;Processor Driver`|`cpu.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ProfSvc Service </span>



##### Service Parameters
  
DeleteRetryAttempts : `0x0f`  
DeleteRetryWait : `0x3e8`  
ServiceDll : `%systemroot%\system32\profsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `UserProfileServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Psched Service </span>



##### Service Parameters
  
Winsock : `Winsock`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">PushToInstall Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\PushToInstall.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 3d 1a 8f 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">QWAVE Service </span>



##### Service Parameters
  
LLTD : `0x01`  
ProbegapTrace : `0x00`  
ServiceDll : `%windir%\system32\qwave.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x9d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x9d
    SID: S-1-0-20
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x9d
    SID: S-1-0-84-0-0-0-0-0
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">QWAVEdrv Service </span>
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x9d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x9d
    SID: S-1-0-20
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x9d
    SID: S-1-0-84-0-0-0-0-0
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Ramdisk Service </span>

|Debug|
| :---: |
|`{'DebugComponents': 2147483647, 'DebugLevel': 5}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RasAcd Service </span>



##### Service Parameters
  
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
#### <span style="text-align: center; font-size:2em;">RasAgileVpn Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Description|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\AgileVpn.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@netavpna.inf,%Svc-Mp-AgileVpn-DispName%;WAN Miniport (IKEv2)`|`@netavpna.inf,%Svc-Mp-AgileVpn-DispName%;WAN Miniport (IKEv2)`|`netavpna.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RasAuto Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\rasauto.dll`  
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
    SID: S-1-0-11

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Rasl2tp Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Description|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\rasl2tp.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@%systemroot%\system32\mprmsg.dll,-32005`|`@%systemroot%\system32\mprmsg.dll,-32005`|`netrasa.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RasMan Service </span>

|IKEv2|PPP|ThirdParty|
| :---: | :---: | :---: |
|`{'DllName': 'vpnike.dll'}`|`PPP`|`{'DllName': 'rascustom.dll'}`|



##### Service Parameters
  
AllowL2TPWeakCrypto : `0x00`  
AllowPPTPWeakCrypto : `0x00`  
KeepRasConnections : `0x00`  
Medias : `72 00 61 00 73 00 74 00 61 00 70 00 69 00 00 00 00 00`  
ServiceDll : `%SystemRoot%\System32\rasmans.dll`  
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
    Access: 0x2019d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-3-1024-1068037383-729401668-2768096886-125909118-1680096985-174794564-3112554050-3241210738

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RasPppoe Service </span>

|Linkage|
| :---: |
|`{'Export': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00R\x00a\x00s\x00P\x00p\x00p\x00o\x00e\x00\x00\x00\x00\x00', 'Bind': b'\x00\x00', 'Route': b'\x00\x00'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RasSstp Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Description|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\rassstp.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@%systemroot%\system32\sstpsvc.dll,-202`|`@%systemroot%\system32\sstpsvc.dll,-202`|`netsstpa.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">rdbss Service </span>

|DependOnService|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`Mup`|`@%systemroot%\system32\wkssvc.dll,-1001`|`@%systemroot%\system32\wkssvc.dll,-1000`|`SERVICE_ERROR_NORMAL`|`Network`|`system32\DRIVERS\rdbss.sys`|`SERVICE_SYSTEM_START`|`0x04`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">rdpbus Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\rdpbus.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@rdpbus.inf,%rdpbus_svcdesc%;Remote Desktop Device Redirector Bus Driver`|`rdpbus.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RDPDR Service </span>

|DependOnService|Description|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`RDBSS`|`@%SystemRoot%\System32\DRIVERS\rdpdr.sys,-101`|`@%SystemRoot%\System32\DRIVERS\rdpdr.sys,-100`|`SERVICE_ERROR_NORMAL`|`System32\drivers\rdpdr.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RDPNP Service </span>

|NetworkProvider|
| :---: |
|`{'DeviceName': '\\Device\\RdpDr', 'DisplayName': '@%systemroot%\\system32\\drprov.dll,-100', 'Name': 'Microsoft Terminal Services', 'ProviderPath': '%SystemRoot%\\System32\\drprov.dll'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RDPUDD Service </span>

|Device0|
| :---: |
|`{'Device Description': 'RDPUDD Chained DD', 'InstalledDisplayDrivers': b'R\x00D\x00P\x00U\x00D\x00D\x00\x00\x00\x00\x00', 'VgaCompatible': 0}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RdpVideoMiniport Service </span>
  
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
    Access: 0x30
    SID: S-1-0-80-446051430-1559341753-4161941529-1950928533-810483104

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">rdyboost Service </span>

|Performance|
| :---: |
|`{'Close': 'CloseReadyBoostPerfData', 'Collect': 'CollectReadyBoostPerfData', 'Library': '%systemroot%\\system32\\sysmain.dll', 'Open': 'OpenReadyBoostPerfData', 'InstallType': 1, 'PerfIniFile': 'ReadyBoostPerfCounters.ini', 'First Counter': 8984, 'Last Counter': 9004, 'First Help': 8985, 'Last Help': 9005, 'Object List': '8984'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ReFS Service </span>

|BootFlags|ErrorControl|Group|Start|Type|
| :---: | :---: | :---: | :---: | :---: |
|`0x80`|`SERVICE_ERROR_NORMAL`|`Boot File System`|`SERVICE_DEMAND_START`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ReFSv1 Service </span>

|BootFlags|ErrorControl|Group|Start|Type|
| :---: | :---: | :---: | :---: | :---: |
|`0x80`|`SERVICE_ERROR_NORMAL`|`Boot File System`|`SERVICE_DEMAND_START`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RemoteAccess Service </span>

|Accounting|Authentication|DemandDialManager|Interfaces|Performance|Policy|RouterManagers|RoutingDomains|RoutingTableManager|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`Accounting`|`Authentication`|`{'DllPath': '%SystemRoot%\\System32\\mprddm.dll'}`|`{'Stamp': 0}`|`{'Close': 'CloseRasPerformanceData', 'Collect': 'CollectRasPerformanceData', 'Library': 'X:\\Windows\\System32\\rasctrs.dll', 'Open': 'OpenRasPerformanceData', 'InstallType': 1, 'PerfIniFile': 'rasctrs.ini', 'First Counter': 9050, 'Last Counter': 9088, 'First Help': 9051, 'Last Help': 9089}`|`Policy`|`{'Stamp': 0}`|`{}`|`RoutingTableManager`|



##### Service Parameters
  
AccountLockout : `{'MaxDenials': 0, 'ResetTime (mins)': 2880}`  
IKEV2 : `{'ConfigOptions': 0, 'idleTimeout': 300, 'networkBlackoutTime': 1800, 'saDataSize': 33553408, 'saLifeTime': 3600}`  
Ip : `{'AllowClientIpAddresses': 0, 'AllowNetworkAccess': 1, 'EnableIn': 1, 'EnableNetbtBcastFwd': 1, 'EnableRoute': 1, 'IpAddress': '0.0.0.0', 'IpMask': '0.0.0.0', 'UseDhcpAddressing': 1}`  
Ipv6 : `{'AdvertiseDefaultRoute': 1, 'AllowNetworkAccess': 1, 'EnableIn': 0, 'EnableRoute': 1, 'UseDhcpAddressing': 0}`  
L2TP : `{'idleTimeout': 300, 'saDataSize': 250000, 'saLifeTime': 3600}`  
Nbf : `{'AllowNetworkAccess': 1, 'EnableIn': 1}`  
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
    SID: S-1-0-11

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RemoteRegistry Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\regsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`31d1811f-ac3f-3745-9e0c-7e7b0c2f4b55`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`77 00 69 00 6e 00 72 00 65 00 67 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RetailDemo Service </span>



##### Service Parameters
  
ServiceDLL : `%SystemRoot%\system32\RDXService.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

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
ReservedChannels : `ReservedChannels`  
Winsock : `Winsock`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">rhproxy Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\rhproxy.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x16`|`@rhproxy.inf,%rhproxy.SVCDESC%;Resource Hub proxy driver`|`rhproxy.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RmSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\RMapi.dll`  
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
    Access: 0x201fd
    SID: S-1-0-19
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x201ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x201ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0x201fd
    SID: S-1-0-32-545

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RpcEptMapper Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\RpcEpMap.dll`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x20085
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x95
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf00ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RpcLocator Service </span>

|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|RequiredPrivileges|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%systemroot%\system32\Locator.exe,-3`|`@%systemroot%\system32\Locator.exe,-2`|`SERVICE_ERROR_NORMAL`|`84 03 00 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 e0 93 04 00 00 00 00 00 00 00 00 00`|`%SystemRoot%\system32\locator.exe`|`NT AUTHORITY\NetworkService`|`['SeChangeNotifyPrivilege']`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">RpcSs Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\rpcss.dll`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x20085
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x85
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf00ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">rspndr Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\lltdres.dll,-5`|`@%SystemRoot%\system32\lltdres.dll,-5`|`SERVICE_ERROR_NORMAL`|`NDIS`|`system32\drivers\rspndr.sys`|`SERVICE_AUTO_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">s3cap Service </span>



##### Service Parameters
  
Wdf : `{'DbgPrintOn': 0, 'DbgBreakOnError': 0}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SamSs Service </span>
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x8d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x8d
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">sbp2port Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\sbp2port.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`@sbp2.inf,%sbp2_ServiceDesc%;SBP-2 Transport/Protocol Bus Driver`|`sbp2.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SCardSvr Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\SCardSvr.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `CalaisMain`  
<br></br>  
Security : 
```
Owner: S-1-0-32-544
Group: S-1-0-32-544
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201ff
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
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0xc0
    Access: 0xc0000
    SID: S-1-0-32-544

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`3052dd50-8aba-d111-bf5d-0000f805f530`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`61811d12-6d86-244a-ba58-9058940c0d47`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`63 00 36 00 62 00 35 00 32 00 33 00 35 00 61 00 2d 00 65 00 34 00 31 00 33 00 2d 00 34 00 38 00 31 00 64 00 2d 00 39 00 61 00 63 00 38 00 2d 00 33 00 31 00 36 00 38 00 31 00 62 00 31 00 66 00 61 00 61 00 66 00 35 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 30 00 43 00 43 00 38 00 32 00 38 00 35 00 37 00 2d 00 31 00 45 00 30 00 45 00 2d 00 34 00 36 00 33 00 33 00 2d 00 41 00 36 00 37 00 33 00 2d 00 32 00 35 00 37 00 42 00 41 00 32 00 34 00 45 00 42 00 39 00 41 00 43 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ScDeviceEnum Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\ScDeviceEnum.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ScDeviceEnumServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-32-544
Group: S-1-0-32-544
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201ff
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
    Access: 0x30
    SID: S-1-0-80-3993802144-2555107232-3516638766-2735499450-3275915967
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0xc0
    Access: 0xc0000
    SID: S-1-0-32-544

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`9f90ddae-c641-1a40-9e41-dfc33006af5d`|`SERVICE_TRIGGER_TYPE_CUSTOM`|`87 66 23 5a 07 d3 e2 44 92 41 e1 c6 c2 7c eb 28`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`dfb92106-4932-5945-9889-21f76b5c80f3`|`SERVICE_TRIGGER_TYPE_CUSTOM`|`8b 9e d9 92 80 96 0b 43 9d ef 9a aa f5 79 01 3c`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`31 00 36 00 39 00 43 00 34 00 35 00 33 00 42 00 2d 00 35 00 39 00 35 00 35 00 2d 00 34 00 36 00 37 00 32 00 2d 00 42 00 45 00 34 00 34 00 2d 00 32 00 31 00 46 00 36 00 31 00 45 00 39 00 45 00 46 00 31 00 38 00 46 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">scfilter Service </span>



##### Service Parameters
  
Wdf : `{'KmdfLibraryVersion': '1.7'}`  
<br></br>  
Security : 
```
Owner: S-1-0-32-544
Group: S-1-0-32-544
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201ff
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
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0xc0
    Access: 0xc0000
    SID: S-1-0-32-544

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Schedule Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\schedsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe01dd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">scmbus Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\scmbus.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`@scmbus.inf,%scmbus.SvcDesc%;Microsoft Storage Class Memory Bus Driver`|`scmbus.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SCPolicySvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\certprop.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ScPolicyServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-32-544
Group: S-1-0-32-544
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201ff
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
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0xc0
    Access: 0xc0000
    SID: S-1-0-32-544

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">sdbus Service </span>



##### Service Parameters
  
SdCmdFlags : `05 01 06 01 08 11 09 19 0a 19 0d 11 10 01 11 01 12 01 17 01 18 05 19 05 1a 01 1b 01 1c 01 20 05 21 05 26 05 2a 01 34 02 35 02 37 01 38 01 22 01 23 05 24 01 25 01`  
SdAppCmdFlags : `06 01 0d 01 16 01 17 01 33 01 12 01 19 01 1a 01 26 01 2b 01 2c 01 2d 01 2e 01 2f 01 30 01 31 01 33 01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SDFRd Service </span>



##### Service Parameters
  
Wdf : `{'KmdfLibraryVersion': '1.15'}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SDRSVC Service </span>



##### Service Parameters
  
ServiceDll : `%Systemroot%\System32\SDRSVC.dll`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">sdstor Service </span>



##### Service Parameters
  
SdCmdFlags : `09 01 0a 01 0d 01 10 01 2a 01 20 01 21 01 26 01 22 01 23 01 24 01 25 01 32 01 39 01`  
SdAppCmdFlags : `0d 01 12 01 19 01 1a 01 26 01 2b 01 2c 01 2d 01 2e 01 2f 01 30 01 31 01 33 01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">seclogon Service </span>



##### Service Parameters
  
ServiceDll : `%windir%\system32\seclogon.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `SvcEntry_Seclogon`  
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
    Access: 0x201dd
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201cd
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201dd
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
#### <span style="text-align: center; font-size:2em;">SecurityHealthService Service </span>

|DependOnService|Description|DisplayName|ErrorControl|FailureActions|ImagePath|LaunchProtected|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`RpcSs`|`@%systemroot%\system32\SecurityHealthAgent.dll,-1001`|`@%systemroot%\system32\SecurityHealthAgent.dll,-1002`|`SERVICE_ERROR_NORMAL`|`80 51 01 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 60 ea 00 00 00 00 00 00 00 00 00 00`|`%SystemRoot%\system32\SecurityHealthService.exe`|`0x02`|`LocalSystem`|`['SeImpersonatePrivilege', 'SeBackupPrivilege', 'SeRestorePrivilege', 'SeDebugPrivilege', 'SeChangeNotifyPrivilege', 'SeSecurityPrivilege', 'SeAssignPrimaryTokenPrivilege', 'SeTcbPrivilege', 'SeSystemEnvironmentPrivilege', 'SeShutdownPrivilege']`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SEMgrSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\SEMgrSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
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
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x04
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x04
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x04
    SID: S-1-0-11
  Object ACE:
    Type:  ACCESS_ALLOWED_CALLBACK_ACE
    Flags: 0x00
    Access: 0x30
    Object Flags: 2561
    
  Object ACE:
    Type:  ACCESS_ALLOWED_CALLBACK_ACE
    Flags: 0x00
    Access: 0x30
    Object Flags: 257
    
  Object ACE:
    Type:  ACCESS_ALLOWED_CALLBACK_ACE
    Flags: 0x00
    Access: 0x30
    Object Flags: 2305
    

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 46 00 32 00 41 00 44 00 44 00 35 00 36 00 30 00 2d 00 45 00 42 00 38 00 35 00 2d 00 34 00 31 00 37 00 30 00 2d 00 38 00 32 00 41 00 32 00 2d 00 41 00 34 00 38 00 45 00 37 00 38 00 39 00 36 00 39 00 30 00 43 00 44 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 30 00 34 00 35 00 41 00 44 00 34 00 30 00 43 00 2d 00 35 00 39 00 32 00 30 00 2d 00 34 00 37 00 35 00 37 00 2d 00 39 00 30 00 41 00 35 00 2d 00 41 00 45 00 30 00 45 00 37 00 45 00 36 00 46 00 36 00 38 00 33 00 38 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SENS Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\sens.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x1fd
    SID: S-1-0-32-549
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x20084
    SID: S-1-0-2-1
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Sense Service </span>
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x0b
    Access: 0x10000000
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SensorDataService Service </span>



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`31d1811f-ac3f-3745-9e0c-7e7b0c2f4b55`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`50 00 72 00 6f 00 74 00 65 00 63 00 74 00 65 00 64 00 50 00 72 00 65 00 66 00 69 00 78 00 5c 00 41 00 64 00 6d 00 69 00 6e 00 69 00 73 00 74 00 72 00 61 00 74 00 6f 00 72 00 73 00 5c 00 53 00 65 00 6e 00 73 00 6f 00 72 00 44 00 61 00 74 00 61 00 53 00 65 00 72 00 76 00 69 00 63 00 65 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SensorService Service </span>



##### Service Parameters
  
Sensors : `Sensors`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x114
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x114
    SID: S-1-0-11
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
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`5f0ffbc2-d2e2-784c-bcd0-352a9582819d`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 30 00 39 00 42 00 44 00 45 00 42 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 41 00 33 00 34 00 2d 00 42 00 46 00 45 00 32 00 2d 00 30 00 36 00 46 00 41 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 38 00 34 00 38 00 39 00 42 00 45 00 31 00 43 00 2d 00 38 00 30 00 41 00 34 00 2d 00 34 00 38 00 42 00 43 00 2d 00 39 00 30 00 31 00 41 00 2d 00 41 00 41 00 39 00 31 00 42 00 44 00 38 00 32 00 37 00 41 00 37 00 43 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 42 00 32 00 43 00 45 00 36 00 33 00 34 00 2d 00 31 00 39 00 31 00 44 00 2d 00 34 00 32 00 41 00 46 00 2d 00 41 00 32 00 38 00 43 00 2d 00 31 00 36 00 42 00 45 00 39 00 37 00 39 00 32 00 34 00 43 00 41 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`39 00 37 00 42 00 45 00 39 00 35 00 30 00 37 00 2d 00 31 00 37 00 44 00 41 00 2d 00 34 00 39 00 39 00 39 00 2d 00 38 00 37 00 44 00 37 00 2d 00 36 00 36 00 43 00 30 00 42 00 32 00 44 00 38 00 33 00 43 00 43 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SensrSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\sensrsvc.dll`  
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
    Access: 0x114
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x114
    SID: S-1-0-11
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
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`c065a617-6390-1642-b202-5c7a255e18ce`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`0f6919ca-c7a2-7d47-a99e-99ec6e2b5648`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`f1da09cd-2e3b-3d4c-b598-b5e5ff93fd46`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`5f0ffbc2-d2e2-784c-bcd0-352a9582819d`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SerCx Service </span>

|DependOnService|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`acpiex`|`Serial UART Support Library`|`SERVICE_ERROR_NORMAL`|`system32\drivers\SerCx.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SerCx2 Service </span>

|DependOnService|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`acpiex`|`Serial UART Support Library`|`SERVICE_ERROR_NORMAL`|`system32\drivers\SerCx2.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Serenum Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\serenum.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`PNP Filter`|`0x05`|`@msports.inf,%Serenum.SVCDESC%;Serenum Filter Driver`|`msports.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Serial Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\serial.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_IGNORE`|`Extended base`|`0x20`|`@msports.inf,%Serial.SVCDESC%;Serial port driver`|`msports.infhiddigi.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">sermouse Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\sermouse.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Pointer Port`|`0x01`|`@msmouse.inf,%sermouse.SvcDesc%;Serial Mouse Driver`|`msmouse.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SessionEnv Service </span>



##### Service Parameters
  
ServiceDLL : `%SystemRoot%\system32\sessenv.dll`  
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
    Access: 0x30
    SID: S-1-0-80-446051430-1559341753-4161941529-1950928533-810483104
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x30
    SID: S-1-0-80-4130899010-3337817248-2959896732-3640118089-1866760602

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">sfloppy Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|AutoRun|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\sfloppy.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@flpydisk.inf,%sfloppy_devdesc%;High-Capacity Floppy Disk Drive`|`flpydisk.inf`|`0x00`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SgrmAgent Service </span>
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x0b
    Access: 0x10000000
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SgrmBroker Service </span>



##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`37 00 61 00 32 00 30 00 66 00 63 00 65 00 63 00 2d 00 64 00 65 00 63 00 34 00 2d 00 34 00 63 00 35 00 39 00 2d 00 62 00 65 00 35 00 37 00 2d 00 32 00 31 00 32 00 65 00 38 00 66 00 36 00 35 00 64 00 33 00 64 00 65 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SharedAccess Service </span>

|Defaults|Epoch|Epoch2|
| :---: | :---: | :---: |
|`Defaults`|`{}`|`{}`|



##### Service Parameters
  
FirewallPolicy : `FirewallPolicy`  
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
    Access: 0x201bd
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-80-3935728946-315639613-922904133-3250794525-491832002
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`45 00 36 00 34 00 42 00 39 00 41 00 45 00 45 00 2d 00 46 00 33 00 37 00 32 00 2d 00 34 00 33 00 31 00 32 00 2d 00 39 00 41 00 31 00 34 00 2d 00 38 00 46 00 31 00 35 00 30 00 32 00 42 00 35 00 43 00 38 00 45 00 33 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SharedRealitySvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\SharedRealitySvc.dll`  
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
#### <span style="text-align: center; font-size:2em;">ShellHWDetection Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\shsvcs.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `HardwareDetectionServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">shpamsvc Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\Windows.SharedPC.AccountManager.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SiSRaid2 Service </span>



##### Service Parameters
  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SiSRaid4 Service </span>



##### Service Parameters
  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SmartSAMD Service </span>



##### Service Parameters
  
Device : `{'EnableFull64Bit': b'\x00', 'EnableExtSrbs': b'\x00', 'MaxDeviceQueueDepth': 128}`  
Drive : `{'EnableQueryAccessAlignment': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">smbdirect Service </span>

|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: |
|`SERVICE_ERROR_NORMAL`|`Network`|`System32\DRIVERS\smbdirect.sys`|`SERVICE_DEMAND_START`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">smphost Service </span>



##### Service Parameters
  
ServiceDll : `%Systemroot%\System32\smphost.dll`  
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
    Access: 0x15
    SID: S-1-0-11
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
    Access: 0x2018d
    SID: S-1-0-32-582
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SmsRouter Service </span>

|State|
| :---: |
|`{}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\SmsRouterSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x20085
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x95
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf00ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`41 00 43 00 44 00 37 00 39 00 32 00 45 00 34 00 2d 00 35 00 32 00 33 00 39 00 2d 00 34 00 38 00 42 00 36 00 2d 00 38 00 42 00 41 00 46 00 2d 00 37 00 44 00 30 00 41 00 37 00 39 00 41 00 36 00 34 00 41 00 43 00 30 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`36 00 37 00 37 00 30 00 36 00 31 00 32 00 42 00 2d 00 42 00 32 00 35 00 36 00 2d 00 34 00 42 00 36 00 45 00 2d 00 38 00 39 00 31 00 42 00 2d 00 32 00 46 00 46 00 39 00 39 00 33 00 36 00 37 00 35 00 35 00 41 00 31 00 3a 00 44 00 31 00 38 00 35 00 46 00 31 00 44 00 36 00 2d 00 41 00 34 00 41 00 46 00 2d 00 34 00 34 00 63 00 32 00 2d 00 38 00 46 00 38 00 37 00 2d 00 46 00 36 00 36 00 34 00 42 00 45 00 35 00 33 00 34 00 43 00 37 00 37 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SMSvcHost 4.0.0.0 Service </span>

|Performance|
| :---: |
|`{'CategoryOptions': 3, 'Close': 'ClosePerformanceData', 'Collect': 'CollectPerformanceData', 'Counter Names': b'P\x00r\x00o\x00t\x00o\x00c\x00o\x00l\x00 \x00F\x00a\x00i\x00l\x00u\x00r\x00e\x00s\x00 \x00o\x00v\x00e\x00r\x00 \x00n\x00e\x00t\x00.\x00t\x00c\x00p\x00\x00\x00P\x00r\x00o\x00t\x00o\x00c\x00o\x00l\x00 \x00F\x00a\x00i\x00l\x00u\x00r\x00e\x00s\x00 \x00o\x00v\x00e\x00r\x00 \x00n\x00e\x00t\x00.\x00p\x00i\x00p\x00e\x00\x00\x00D\x00i\x00s\x00p\x00a\x00t\x00c\x00h\x00 \x00F\x00a\x00i\x00l\x00u\x00r\x00e\x00s\x00 \x00o\x00v\x00e\x00r\x00 \x00n\x00e\x00t\x00.\x00t\x00c\x00p\x00\x00\x00D\x00i\x00s\x00p\x00a\x00t\x00c\x00h\x00 \x00F\x00a\x00i\x00l\x00u\x00r\x00e\x00s\x00 \x00o\x00v\x00e\x00r\x00 \x00n\x00e\x00t\x00.\x00p\x00i\x00p\x00e\x00\x00\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00 \x00D\x00i\x00s\x00p\x00a\x00t\x00c\x00h\x00e\x00d\x00 \x00o\x00v\x00e\x00r\x00 \x00n\x00e\x00t\x00.\x00t\x00c\x00p\x00\x00\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00 \x00D\x00i\x00s\x00p\x00a\x00t\x00c\x00h\x00e\x00d\x00 \x00o\x00v\x00e\x00r\x00 \x00n\x00e\x00t\x00.\x00p\x00i\x00p\x00e\x00\x00\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00 \x00A\x00c\x00c\x00e\x00p\x00t\x00e\x00d\x00 \x00o\x00v\x00e\x00r\x00 \x00n\x00e\x00t\x00.\x00t\x00c\x00p\x00\x00\x00C\x00o\x00n\x00n\x00e\x00c\x00t\x00i\x00o\x00n\x00s\x00 \x00A\x00c\x00c\x00e\x00p\x00t\x00e\x00d\x00 \x00o\x00v\x00e\x00r\x00 \x00n\x00e\x00t\x00.\x00p\x00i\x00p\x00e\x00\x00\x00R\x00e\x00g\x00i\x00s\x00t\x00r\x00a\x00t\x00i\x00o\x00n\x00s\x00 \x00A\x00c\x00t\x00i\x00v\x00e\x00 \x00f\x00o\x00r\x00 \x00n\x00e\x00t\x00.\x00t\x00c\x00p\x00\x00\x00R\x00e\x00g\x00i\x00s\x00t\x00r\x00a\x00t\x00i\x00o\x00n\x00s\x00 \x00A\x00c\x00t\x00i\x00v\x00e\x00 \x00f\x00o\x00r\x00 \x00n\x00e\x00t\x00.\x00p\x00i\x00p\x00e\x00\x00\x00U\x00r\x00i\x00s\x00 \x00R\x00e\x00g\x00i\x00s\x00t\x00e\x00r\x00e\x00d\x00 \x00f\x00o\x00r\x00 \x00n\x00e\x00t\x00.\x00t\x00c\x00p\x00\x00\x00U\x00r\x00i\x00s\x00 \x00R\x00e\x00g\x00i\x00s\x00t\x00e\x00r\x00e\x00d\x00 \x00f\x00o\x00r\x00 \x00n\x00e\x00t\x00.\x00p\x00i\x00p\x00e\x00\x00\x00U\x00r\x00i\x00s\x00 \x00U\x00n\x00r\x00e\x00g\x00i\x00s\x00t\x00e\x00r\x00e\x00d\x00 \x00f\x00o\x00r\x00 \x00n\x00e\x00t\x00.\x00t\x00c\x00p\x00\x00\x00U\x00r\x00i\x00s\x00 \x00U\x00n\x00r\x00e\x00g\x00i\x00s\x00t\x00e\x00r\x00e\x00d\x00 \x00f\x00o\x00r\x00 \x00n\x00e\x00t\x00.\x00p\x00i\x00p\x00e\x00\x00\x00\x00\x00', 'Counter Types': b'6\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x00\x00\x00', 'IsMultiInstance': 0, 'Library': '%systemroot%\\system32\\NETFXPerf.dll', 'Open': 'OpenPerformanceData', 'InstallType': 1, 'PerfIniFile': '_SMSvcHostPerfCounters_d.ini', 'First Counter': 8710, 'Last Counter': 8738, 'First Help': 8711, 'Last Help': 8739, 'Object List': '8710'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SNMPTRAP Service </span>

|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@firewallapi.dll,-50324`|`@firewallapi.dll,-50323`|`SERVICE_ERROR_NORMAL`|`ff ff ff ff 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 60 ea 00 00 01 00 00 00 60 ea 00 00 00 00 00 00 00 00 00 00`|`%SystemRoot%\System32\snmptrap.exe`|`NT AUTHORITY\LocalService`|`['SeChangeNotifyPrivilege']`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">spaceparser Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%systemroot%\system32\drivers\spaceparser.sys,-1000`|`@%systemroot%\system32\drivers\spaceparser.sys,-1001`|`SERVICE_ERROR_NORMAL`|`Hyper-V Parsers`|`system32\drivers\spaceparser.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">spaceport Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\spaceport.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_CRITICAL`|`System Bus Extender`|`0x08`|`@spaceport.inf,%Spaceport_ServiceDesc%;Storage Spaces Driver`|`spaceport.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SpatialGraphFilter Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`Holographic Spatial Graph Filter`|`SERVICE_ERROR_NORMAL`|`PnP Filter`|`System32\drivers\SpatialGraphFilter.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SpbCx Service </span>

|DependOnService|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`acpiex`|`Simple Peripheral Bus Support Library`|`SERVICE_ERROR_NORMAL`|`system32\drivers\SpbCx.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">spectrum Service </span>
  
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
    Access: 0x14
    SID: S-1-0-19
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`44 00 33 00 43 00 31 00 42 00 36 00 34 00 42 00 2d 00 43 00 44 00 30 00 35 00 2d 00 34 00 46 00 42 00 32 00 2d 00 42 00 42 00 32 00 43 00 2d 00 42 00 42 00 36 00 31 00 44 00 38 00 30 00 43 00 31 00 32 00 33 00 45 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`45 00 35 00 42 00 39 00 32 00 33 00 37 00 38 00 2d 00 30 00 43 00 36 00 35 00 2d 00 34 00 34 00 32 00 43 00 2d 00 41 00 36 00 36 00 42 00 2d 00 46 00 39 00 37 00 31 00 34 00 44 00 32 00 44 00 37 00 42 00 30 00 30 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Spooler Service </span>

|Performance|
| :---: |
|`{'Close': 'PerfClose', 'Collect': 'PerfCollect', 'Collect Timeout': 2000, 'Library': 'X:\\Windows\\System32\\winspool.drv', 'Object List': '1450', 'Open': 'PerfOpen', 'Open Timeout': 4000}`|
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">sppsvc Service </span>
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x94
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-11
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`39 00 34 00 33 00 35 00 63 00 63 00 35 00 36 00 2d 00 31 00 64 00 39 00 63 00 2d 00 34 00 39 00 32 00 34 00 2d 00 61 00 63 00 37 00 64 00 2d 00 62 00 36 00 30 00 61 00 32 00 63 00 33 00 35 00 32 00 30 00 65 00 31 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`da8a52f5-5fbe-144f-8aef-a95de7281161`|`SERVICE_TRIGGER_TYPE_CUSTOM`|||
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">srv2 Service </span>

|DependOnService|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`srvnet`|`@%systemroot%\system32\srvsvc.dll,-105`|`@%systemroot%\system32\srvsvc.dll,-104`|`SERVICE_ERROR_NORMAL`|`Network`|`System32\DRIVERS\srv2.sys`|`SERVICE_DEMAND_START`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">srvnet Service </span>

|DependOnService|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`msquic`|`SERVICE_ERROR_NORMAL`|`Network`|`System32\DRIVERS\srvnet.sys`|`SERVICE_DEMAND_START`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SSDPSRV Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\ssdpsrv.dll`  
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
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x200bd
    SID: S-1-0-32-549
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-19
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-20

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ssh-agent Service </span>
  
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
    Access: 0x10
    SID: S-1-0-11

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SstpSvc Service </span>



##### Service Parameters
  
ConfigStore : `{'ListenerPort': 0, 'UseHttps': 1, 'V4CertPlumbedBySstp': 0, 'V6CertPlumbedBySstp': 0}`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-32-556
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-3-1024-1068037383-729401668-2768096886-125909118-1680096985-174794564-3112554050-3241210738
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">StateRepository Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\windows.staterepository.dll`  
ServiceDllUnloadOnStop : `0x00`  
<br></br>  
Security : 
```
Owner: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
Group: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-2-1
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">stexstor Service </span>



##### Service Parameters
  
Device : `{'RESET': 1, 'NumberOfRequests': 1024}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">stisvc Service </span>



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
#### <span style="text-align: center; font-size:2em;">storahci Service </span>



##### Service Parameters
  
Device : `{'ResetInInit': b'V\x00E\x00N\x00_\x001\x001\x000\x006\x00&\x00D\x00E\x00V\x00_\x006\x002\x008\x007\x00&\x00R\x00E\x00V\x00_\x00*\x00\x00\x00\x00\x00', 'SingleIO': b'V\x00E\x00N\x00_\x001\x001\x000\x006\x00&\x00D\x00E\x00V\x00_\x006\x002\x008\x007\x00&\x00R\x00E\x00V\x00_\x000\x000\x00\x00\x00V\x00E\x00N\x00_\x001\x001\x000\x006\x00&\x00D\x00E\x00V\x00_\x006\x002\x008\x007\x00&\x00R\x00E\x00V\x00_\x001\x000\x00\x00\x00V\x00E\x00N\x00_\x001\x001\x000\x006\x00&\x00D\x00E\x00V\x00_\x006\x002\x008\x007\x00&\x00R\x00E\x00V\x00_\x002\x000\x00\x00\x00\x00\x00', 'IgnoreHotPlug': b'V\x00E\x00N\x00_\x001\x000\x000\x002\x00&\x00D\x00E\x00V\x00_\x004\x003\x008\x000\x00&\x00R\x00E\x00V\x00_\x00*\x00\x00\x00\x00\x00', 'NeverNonQueuedErrorRecovery': b'V\x00E\x00N\x00_\x001\x000\x000\x002\x00&\x00D\x00E\x00V\x00_\x004\x003\x008\x000\x00&\x00R\x00E\x00V\x00_\x00*\x00\x00\x00\x00\x00', 'EnableCLOReset': b'V\x00E\x00N\x00_\x001\x000\x000\x002\x00&\x00D\x00E\x00V\x00_\x004\x003\x009\x001\x00&\x00R\x00E\x00V\x00_\x00*\x00\x00\x00\x00\x00', 'ExpectedMsiMessageCount': b'V\x00E\x00N\x00_\x001\x000\x002\x002\x00&\x00D\x00E\x00V\x00_\x007\x008\x000\x001\x00&\x00R\x00E\x00V\x00_\x000\x000\x00 \x008\x00\x00\x00\x00\x00', 'NoFUACommand': b'H\x00T\x00E\x00*\x00\x00\x00H\x00i\x00t\x00a\x00c\x00h\x00i\x00*\x00\x00\x00H\x00T\x00S\x00*\x00\x00\x00H\x00D\x00S\x00*\x00\x00\x00H\x00D\x00T\x00*\x00\x00\x00\x00\x00', 'NeedSetTransferModeCommand': b'M\x00C\x00B\x00Q\x00E\x006\x004\x00G\x00B\x00M\x00P\x00P\x00*\x00\x00\x00\x00\x00', 'NoLPM': b'W\x00D\x007\x004\x000\x00A\x00D\x00F\x00D\x00?\x000\x000\x00N\x00L\x00R\x001\x00*\x00\x00\x00W\x00D\x00C\x00 \x00W\x00D\x007\x004\x000\x00A\x00D\x00F\x00D\x00?\x000\x000\x00N\x00L\x00R\x001\x00*\x00\x00\x00M\x00a\x00x\x00t\x00o\x00r\x00 \x006\x00V\x00?\x00?\x00?\x00E\x000\x00*\x00\x00\x00M\x00a\x00x\x00t\x00o\x00r\x00 \x006\x00V\x00?\x00?\x00?\x00F\x000\x00*\x00\x00\x00M\x00a\x00x\x00t\x00o\x00r\x00 \x007\x00V\x00?\x00?\x00?\x00E\x000\x00*\x00\x00\x00M\x00a\x00x\x00t\x00o\x00r\x00 \x007\x00V\x00?\x00?\x00?\x00F\x000\x00*\x00\x00\x00S\x00a\x00n\x00D\x00i\x00s\x00k\x00 \x00S\x00S\x00D\x00 \x00P\x004\x00*\x00\x00\x00\x00\x00', 'NoIdleD3': b'I\x00N\x00T\x00E\x00L\x00 \x00S\x00S\x00D\x00?\x00C\x00?\x00?\x00?\x00?\x00?\x00?\x00A\x004\x00\x00\x00I\x00N\x00T\x00E\x00L\x00 \x00S\x00S\x00D\x00?\x00C\x00?\x00?\x00?\x00?\x00?\x00?\x00A\x004\x00?\x00\x00\x00I\x00N\x00T\x00E\x00L\x00 \x00S\x00S\x00D\x00?\x00C\x00?\x00?\x00?\x00?\x00?\x00?\x00A\x004\x00?\x00?\x00\x00\x00I\x00N\x00T\x00E\x00L\x00 \x00S\x00S\x00D\x00?\x00C\x00?\x00?\x00?\x00?\x00?\x00?\x00A\x005\x00\x00\x00I\x00N\x00T\x00E\x00L\x00 \x00S\x00S\x00D\x00?\x00C\x00?\x00?\x00?\x00?\x00?\x00?\x00A\x005\x00?\x00\x00\x00I\x00N\x00T\x00E\x00L\x00 \x00S\x00S\x00D\x00?\x00C\x00?\x00?\x00?\x00?\x00?\x00?\x00A\x005\x00?\x00?\x00\x00\x00\x00\x00', 'PRDTSplit': b'V\x00E\x00N\x00_\x001\x000\x002\x002\x00&\x00D\x00E\x00V\x00_\x004\x003\x00B\x005\x00&\x00R\x00E\x00V\x00_\x00*\x00\x00\x00V\x00E\x00N\x00_\x001\x000\x002\x002\x00&\x00D\x00E\x00V\x00_\x004\x003\x00B\x006\x00&\x00R\x00E\x00V\x00_\x00*\x00\x00\x00V\x00E\x00N\x00_\x001\x000\x002\x002\x00&\x00D\x00E\x00V\x00_\x004\x003\x00B\x007\x00&\x00R\x00E\x00V\x00_\x00*\x00\x00\x00V\x00E\x00N\x00_\x001\x000\x002\x002\x00&\x00D\x00E\x00V\x00_\x004\x003\x00B\x008\x00&\x00R\x00E\x00V\x00_\x00*\x00\x00\x00V\x00E\x00N\x00_\x001\x000\x002\x002\x00&\x00D\x00E\x00V\x00_\x004\x003\x00C\x008\x00&\x00R\x00E\x00V\x00_\x00*\x00\x00\x00\x00\x00'}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">storflt Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|Enabled|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\vmstorfl.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x2e`|`@wstorflt.inf,%service_desc%;Microsoft Hyper-V Storage Accelerator`|`wstorflt.inf`|`0x01`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">stornvme Service </span>



##### Service Parameters
  
Device : `{'IoStripeAlignment': b'V\x00E\x00N\x00_\x008\x000\x008\x006\x00&\x00D\x00E\x00V\x00_\x000\x009\x005\x003\x00&\x00R\x00E\x00V\x00_\x00?\x00?\x00 \x001\x002\x008\x00\x00\x00V\x00E\x00N\x00_\x008\x000\x008\x006\x00&\x00D\x00E\x00V\x00_\x000\x009\x008\x004\x00&\x00R\x00E\x00V\x00_\x00?\x00?\x00 \x001\x002\x008\x00\x00\x00V\x00E\x00N\x00_\x008\x000\x008\x006\x00&\x00D\x00E\x00V\x00_\x000\x00A\x005\x003\x00&\x00R\x00E\x00V\x00_\x00?\x00?\x00 \x001\x002\x008\x00\x00\x00V\x00E\x00N\x00_\x008\x000\x008\x006\x00&\x00D\x00E\x00V\x00_\x000\x00A\x005\x004\x00&\x00R\x00E\x00V\x00_\x00?\x00?\x00 \x001\x002\x008\x00\x00\x00V\x00E\x00N\x00_\x008\x000\x008\x006\x00&\x00D\x00E\x00V\x00_\x000\x00A\x005\x005\x00&\x00R\x00E\x00V\x00_\x00?\x00?\x00 \x001\x002\x008\x00\x00\x00\x00\x00'}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">storqosflt Service </span>

|Instances|
| :---: |
|`Instances`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">StorSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\storsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`6f00404f-33b9-5045-b532-2b58cee614d3`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`35 00 34 00 42 00 34 00 43 00 36 00 38 00 39 00 2d 00 39 00 36 00 39 00 41 00 2d 00 34 00 37 00 36 00 66 00 2d 00 38 00 44 00 43 00 32 00 2d 00 39 00 39 00 30 00 38 00 38 00 35 00 45 00 39 00 46 00 35 00 36 00 32 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`42 00 45 00 36 00 32 00 39 00 33 00 44 00 33 00 2d 00 32 00 38 00 32 00 37 00 2d 00 34 00 44 00 44 00 41 00 2d 00 38 00 30 00 35 00 37 00 2d 00 38 00 35 00 38 00 38 00 32 00 34 00 30 00 31 00 32 00 34 00 43 00 39 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">storufs Service </span>



##### Service Parameters
  
BusType : `0x13`  
IoTimeoutValue : `0x1e`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">storvsc Service </span>



##### Service Parameters
  
Device : `{'EnableQueryAccessAlignment': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">svsvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\svsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`03536a8e-cea4-8f49-afdb-e03a8a82b077`|`SERVICE_TRIGGER_TYPE_CUSTOM`|`53 00 76 00 53 00 76 00 63 00 20 00 53 00 74 00 61 00 72 00 74 00`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">swenum Service </span>

|Devices|
| :---: |
|`Devices`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">swprv Service </span>



##### Service Parameters
  
ServiceDll : `%Systemroot%\System32\swprv.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Synth3dVsc Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\Synth3dVsc.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Video Init`|`0x01`|`wsynth3dvsc.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SysMain Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\sysmain.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `SysMtServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">SystemEventsBroker Service </span>



##### Service Parameters
  
EventPolicyTable : `EventPolicyTable`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x20085
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x95
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf00ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`39 00 42 00 30 00 30 00 38 00 39 00 35 00 33 00 2d 00 46 00 31 00 39 00 35 00 2d 00 34 00 42 00 46 00 39 00 2d 00 42 00 44 00 45 00 30 00 2d 00 34 00 34 00 37 00 31 00 39 00 37 00 31 00 45 00 35 00 38 00 45 00 44 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 3e 06 83 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TabletInputService Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\TabSvc.dll`  
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
    Access: 0x10
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|Data1|Data2|Data3|DataType0|DataType1|DataType2|DataType3|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`b2551e4d-6ff1-cf11-88cb-001111000030`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 31 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 32 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 33 00 00 00`|`48 00 49 00 44 00 5f 00 44 00 45 00 56 00 49 00 43 00 45 00 5f 00 55 00 50 00 3a 00 30 00 30 00 30 00 44 00 5f 00 55 00 3a 00 30 00 30 00 30 00 34 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TapiSrv Service </span>

|Performance|
| :---: |
|`{'Close': 'CloseTapiPerformanceData', 'Collect': 'CollectTapiPerformanceData', 'Library': '%SystemRoot%\\System32\\tapiperf.dll', 'ObjectList': '1150', 'Open': 'OpenTapiPerformanceData', 'InstallType': 1, 'PerfIniFile': 'tapiperf.ini', 'First Counter': 8946, 'Last Counter': 8964, 'First Help': 8947, 'Last Help': 8965}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\tapisrv.dll`  
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
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Tcpip Service </span>

|Linkage|Performance|ServiceProvider|
| :---: | :---: | :---: |
|`{'Export': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x00\x00\x00\x00\x00', 'Bind': b'\x00\x00', 'Route': b'\x00\x00'}`|`{'Close': 'CloseTcpIpPerformanceData', 'Collect': 'CollectTcpIpPerformanceData', 'Library': '%SystemRoot%\\System32\\Perfctrs.dll', 'Object List': '502 510 546 548 582 638 658 1530 1532 1534 1820', 'Open': 'OpenTcpIpPerformanceData'}`|`{'Class': 8, 'DnsPriority': 2000, 'HostsPriority': 500, 'LocalPriority': 499, 'Name': 'TCP/IP', 'NetbtPriority': 2001, 'ProviderPath': '%SystemRoot%\\System32\\wsock32.dll'}`|



##### Service Parameters
  
Adapters : `{}`  
Interfaces : `{}`  
NsiObjectSecurity : `{}`  
PersistentRoutes : `{}`  
Winsock : `Winsock`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Tcpip6 Service </span>

|Linkage|
| :---: |
|`{'Export': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00c\x00p\x00i\x00p\x006\x00_\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\x00\x00', 'Bind': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\x00\x00', 'Route': b'"\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00"\x00\x00\x00"\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00"\x00\x00\x00"\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00"\x00\x00\x00\x00\x00'}`|



##### Service Parameters
  
Interfaces : `Interfaces`  
Winsock : `Winsock`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TCPIP6TUNNEL Service </span>

|Linkage|
| :---: |
|`{'Export': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00C\x00P\x00I\x00P\x006\x00T\x00U\x00N\x00N\x00E\x00L\x00_\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00C\x00P\x00I\x00P\x006\x00T\x00U\x00N\x00N\x00E\x00L\x00_\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00C\x00P\x00I\x00P\x006\x00T\x00U\x00N\x00N\x00E\x00L\x00_\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\x00\x00', 'Bind': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00\x00\x00\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00\x00\x00\x00\x00', 'Route': b'"\x00{\x000\x007\x003\x007\x004\x007\x005\x000\x00-\x00E\x006\x008\x00B\x00-\x004\x009\x000\x00E\x00-\x009\x003\x003\x000\x00-\x009\x00F\x00D\x007\x008\x005\x00C\x00D\x007\x001\x00B\x006\x00}\x00"\x00\x00\x00"\x00{\x002\x00E\x00E\x002\x00C\x007\x000\x00C\x00-\x00A\x000\x009\x002\x00-\x004\x00D\x008\x008\x00-\x00A\x006\x005\x004\x00-\x009\x008\x00C\x008\x00D\x007\x006\x004\x005\x00C\x00D\x005\x00}\x00"\x00\x00\x00"\x00{\x009\x003\x001\x002\x003\x002\x001\x001\x00-\x009\x006\x002\x009\x00-\x004\x00E\x000\x004\x00-\x008\x002\x00F\x000\x00-\x00E\x00A\x002\x00E\x004\x00F\x002\x002\x001\x004\x006\x008\x00}\x00"\x00\x00\x00\x00\x00'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">tcpipreg Service </span>

|DependOnService|Description|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`tcpip`|`Provides compatibility for legacy applications which interact with TCP/IP through the registry. If this service is stopped, certain applications may have impaired functionality.`|`TCP/IP Registry Compatibility`|`SERVICE_ERROR_NORMAL`|`System32\drivers\tcpipreg.sys`|`SERVICE_AUTO_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TCPIPTUNNEL Service </span>

|Linkage|
| :---: |
|`{'Export': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00T\x00C\x00P\x00I\x00P\x00T\x00U\x00N\x00N\x00E\x00L\x00\x00\x00\x00\x00', 'Bind': b'\x00\x00', 'Route': b'\x00\x00'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">tdx Service </span>

|DependOnService|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`tcpip`|`@%SystemRoot%\system32\tcpipcfg.dll,-50004`|`@%SystemRoot%\system32\tcpipcfg.dll,-50004`|`SERVICE_ERROR_NORMAL`|`PNP_TDI`|`\SystemRoot\system32\DRIVERS\tdx.sys`|`SERVICE_SYSTEM_START`|`0x04`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Telemetry Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\IntelTA.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`Core Security Extensions`|`0x02`|`@intelta.inf,%Telemetry.SVCDESC%;Intel(R) Telemetry Service`|`intelta.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">terminpt Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\terminpt.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x2b`|`@termmou.inf,%TermInpt.SVCDESC%;Microsoft Remote Desktop Input Driver`|`termmou.inftermkbd.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TermService Service </span>

|Performance|
| :---: |
|`{'Close': 'CloseTSObject', 'Collect': 'CollectTSObjectData', 'Collect Timeout': 1000, 'Library': 'X:\\Windows\\System32\\perfts.dll', 'Open': 'OpenTSObject', 'Open Timeout': 1000, 'InstallType': 1, 'PerfIniFile': 'tslabels.ini', 'First Counter': 6774, 'Last Counter': 6774, 'First Help': 6775, 'Last Help': 6775, 'Object List': '6774'}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\termsrv.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Themes Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\themeservice.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ThemeServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TieringEngineService Service </span>

|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\TieringEngineService.exe,-701`|`@%SystemRoot%\system32\TieringEngineService.exe,-702`|`SERVICE_ERROR_NORMAL`|`68 5b 00 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 e0 93 04 00 00 00 00 00 00 00 00 00`|`%SystemRoot%\system32\TieringEngineService.exe`|`localSystem`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TimeBrokerSvc Service </span>



##### Service Parameters
  
MinKeepAliveTolerance : `0x12c`  
ServiceDll : `%SystemRoot%\System32\TimeBrokerServer.dll`  
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
    Access: 0x20085
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe00fd
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x95
    SID: S-1-0-32-545
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf00ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`61 00 35 00 30 00 30 00 64 00 34 00 63 00 36 00 2d 00 30 00 64 00 64 00 31 00 2d 00 34 00 35 00 34 00 33 00 2d 00 62 00 63 00 30 00 63 00 2d 00 64 00 35 00 66 00 39 00 33 00 34 00 38 00 36 00 65 00 61 00 66 00 38 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`64 00 30 00 39 00 62 00 64 00 65 00 62 00 35 00 2d 00 36 00 31 00 37 00 31 00 2d 00 34 00 61 00 33 00 34 00 2d 00 62 00 66 00 65 00 32 00 2d 00 30 00 36 00 66 00 61 00 38 00 32 00 36 00 35 00 32 00 35 00 36 00 38 00 3a 00 62 00 35 00 63 00 63 00 64 00 35 00 65 00 66 00 2d 00 34 00 32 00 33 00 38 00 2d 00 34 00 34 00 30 00 62 00 2d 00 62 00 62 00 61 00 30 00 2d 00 39 00 39 00 39 00 66 00 38 00 32 00 38 00 66 00 31 00 63 00 66 00 65 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 3e 06 83 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TokenBroker Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\TokenBroker.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TPM Service </span>

|KeyAttestationKeys|PlatformQuoteKeys|WMI|
| :---: | :---: | :---: |
|`{}`|`{}`|`WMI`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TrkWks Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\trkwks.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TroubleshootingSvc Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\MitigationClient.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TrustedInstaller Service </span>
  
Security : 
```
Owner: S-1-0-32-544
Group: S-1-0-32-544
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x02
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201ff
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
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0xc0
    Access: 0xc0000
    SID: S-1-0-32-544

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TSDDD Service </span>

|Device0|
| :---: |
|`{'InstalledDisplayDrivers': b'T\x00S\x00D\x00D\x00D\x00\x00\x00\x00\x00', 'VgaCompatible': 0}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TsUsbFlt Service </span>

|Description|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\tsusbflt.sys,-1000`|`@%SystemRoot%\system32\drivers\tsusbflt.sys,-1000`|`SERVICE_ERROR_NORMAL`|`system32\drivers\tsusbflt.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">TsUsbGD Service </span>



##### Service Parameters
  
Wdf : `{'KmdfLibraryVersion': '1.11'}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">tsusbhub Service </span>



##### Service Parameters
  
Wdf : `{'KmdfLibraryVersion': '1.11'}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">tunnel Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\System32\drivers\tunnel.sys,-500`|`SERVICE_ERROR_NORMAL`|`NDIS`|`System32\drivers\tunnel.sys`|`SERVICE_DEMAND_START`|`0x01`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">tzautoupdate Service </span>

|Config|
| :---: |
|`{'ActiveModeThresholdKm': 10, 'GeolocatorAccuracy': 0, 'HilbertIndexPath': '%SystemRoot%\\Globalization\\Time Zone\\tzautoupdate.dat', 'MinimumMovementThresholdKm': 1, 'ServiceInactivityTimeoutMs': 20000}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\tzautoupdate.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 3e 0b 84 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 50 bc a3 21 08 95 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 30 bc a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 d0 be a3 2e 0b 8a 0d`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UASPStor Service </span>



##### Service Parameters
  
BusType : `0x07`  
IoTimeoutValue : `0x0f`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UcmCx0101 Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`USB Connector Manager KMDF Class Extension`|`SERVICE_ERROR_NORMAL`|`System Bus Extender`|`System32\Drivers\UcmCx.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UcmTcpciCx0101 Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`UCM-TCPCI KMDF Class Extension`|`SERVICE_ERROR_NORMAL`|`System Bus Extender`|`System32\Drivers\UcmTcpciCx.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UcmUcsiAcpiClient Service </span>

|ImagePath|Type|Start|ErrorControl|DependOnService|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\UcmUcsiAcpiClient.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`UcmUcsiCx`|`@UcmUcsiAcpiClient.inf,%UcmUcsiAcpiClient.ServiceName%;UCM-UCSI ACPI Client`|`UcmUcsiAcpiClient.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UcmUcsiCx0101 Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`UCM-UCSI KMDF Class Extension`|`SERVICE_ERROR_NORMAL`|`System Bus Extender`|`System32\Drivers\UcmUcsiCx.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Ucx01000 Service </span>

|BootFlags|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`0x10`|`USB Host Support Library`|`SERVICE_ERROR_NORMAL`|`Boot Bus Extender`|`system32\drivers\ucx01000.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UdeCx Service </span>

|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: |
|`USB Device Emulation Support Library`|`SERVICE_ERROR_NORMAL`|`system32\drivers\udecx.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">udfs Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`Reads/Writes UDF 1.02,1.5,2.0x,2.5 disc formats, usually found on C/DVD discs. (Core) (All pieces)`|`udfs`|`SERVICE_ERROR_NORMAL`|`Boot File System`|`system32\DRIVERS\udfs.sys`|`SERVICE_DISABLED`|`SERVICE_FILE_SYSTEM_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UdkUserSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\windowsudk.shellcommon.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
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
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UEFI Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\DriverStore\FileRepository\uefi.inf_amd64_c1628ffa62c8e54c\UEFI.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@uefi.inf,%UEFI.SvcDesc%;Microsoft UEFI Driver`|`uefi.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UevAgentDriver Service </span>

|Instances|
| :---: |
|`Instances`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UevAgentService Service </span>
  
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
    Access: 0xf01ff
    SID: S-1-0-32-544
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
#### <span style="text-align: center; font-size:2em;">Ufx01000 Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`USB Function Class Extension`|`SERVICE_ERROR_NORMAL`|`System Bus Extender`|`system32\drivers\ufx01000.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UfxChipidea Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\DriverStore\FileRepository\ufxchipidea.inf_amd64_1c78775fffab6a0a\UfxChipidea.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x12`|`ufx01000`|`@ufxchipidea.inf,%UfxChipidea.ServiceName%;USB Chipidea Controller`|`ufxchipidea.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ufxsynopsys Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\ufxsynopsys.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x13`|`ufx01000`|`@ufxsynopsys.inf,%ufxsynopsys.ServiceName%;USB Synopsys Controller`|`ufxsynopsys.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UGatherer Service </span>

|Performance|
| :---: |
|`{'Close': 'Close', 'Collect': 'Collect', 'Library': '%systemroot%\\system32\\msscntrs.dll', 'Open': 'Open', 'InstallType': 1, 'PerfIniFile': 'gsrvctr.ini', 'First Counter': 9134, 'Last Counter': 9238, 'First Help': 9135, 'Last Help': 9239}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UGTHRSVC Service </span>

|Performance|
| :---: |
|`{'Close': 'Close', 'Collect': 'Collect', 'Library': '%systemroot%\\system32\\msscntrs.dll', 'Open': 'Open', 'InstallType': 1, 'PerfIniFile': 'gthrctr.ini', 'First Counter': 9240, 'Last Counter': 9310, 'First Help': 9241, 'Last Help': 9311}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">umbus Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\DriverStore\FileRepository\umbus.inf_amd64_b78a9c5b6fd62c27\umbus.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x21`|`@umbus.inf,%umbus.SVCDESC%;UMBus Enumerator Driver`|`umbus.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UmPass Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\umpass.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x0e`|`@umpass.inf,%UmPass.SVCDESC%;Microsoft UMPass Driver`|`bthleenum.infumpass.infeaphost.infpnpxinternetgatewaydevices.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UmRdpService Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\umrdp.dll`  
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
    Access: 0x30
    SID: S-1-0-80-446051430-1559341753-4161941529-1950928533-810483104

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UnistoreSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\unistore.dll`  
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
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">upnphost Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\upnphost.dll`  
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
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x200bd
    SID: S-1-0-32-549
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-19
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-20

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UrsChipidea Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|BootFlags|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\DriverStore\FileRepository\urschipidea.inf_amd64_78ad1c14e33df968\urschipidea.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x0f`|`urscx01000`|`@urschipidea.inf,%UrsChipidea.ServiceName%;Chipidea USB Role-Switch Driver`|`urschipidea.inf`|`0x04`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UrsCx01000 Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`USB Role-Switch Support Library`|`SERVICE_ERROR_NORMAL`|`System Bus Extender`|`system32\drivers\urscx01000.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UrsSynopsys Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\DriverStore\FileRepository\urssynopsys.inf_amd64_057fa37902020500\urssynopsys.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x10`|`urscx01000`|`@urssynopsys.inf,%UrsSynopsys.ServiceName%;Synopsys USB Role-Switch Driver`|`urssynopsys.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">usbaudio Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\system32\drivers\usbaudio.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@wdma_usb.inf,%USBAudio.SvcDesc%;USB Audio Driver (WDM)`|`wdma_usb.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">usbaudio2 Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\usbaudio2.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@usbaudio2.inf,%usbaudio2.SVCDESC%;USB Audio 2.0 Service`|`usbaudio2.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">usbccgp Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|BootFlags|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\usbccgp.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x09`|`@usb.inf,%GenericParent.SvcDesc%;Microsoft USB Generic Parent Driver`|`usb.infwmbclass_wmc_union.inf`|`0x14`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">usbcir Service </span>

|PowerKey|
| :---: |
|`{'PowerKey-BB-SS-00': b"\x04\x00\x00\x00\x1f\x00\xb9\xd1\xc4\x8e\xea\x91\x0c\x90\x89\xa1\x87\xee\x1a\xaa\xde5\x9b\xec\x14\xf5\x8d\xc1\x1b\xaaBMO\xcbo\xbe\x9d\xe6\\\xfaG\xe1\xc5\xf2\x84\xa6\x1f 4\x8f\xe7q\xee\x13_U\x82\xfe\tPV*(\xefd\xf1\x97F\xab\xaa\x03\x15l\xabb\x0b#U\x9f\x03\x1f\x86\xc1\xadc\x17=n\x1f@\xfaFJw3X\x82\xe1\x1f\x81\xab\xe7\xd8j\x07>Q\x83`l\x19[\x18Og\xc1tS\x06\xf2\xb0\xd1\xc7\xc2\x99\xe1\x00\x99\xb2\xae\x1f`\xa1x\xfb\x07\xa1Z\xdb@?d+\xb1\xdb\xf5\xb4\x855\xa4dTb\xd1\x152aJ\xf4\xd21Z\xafR!\xc9\xbb\xdc\x82z\xe9\x88\x1f\x80\xdc\xfe\xadP\x1d>\x9b\x90\x03;F0\x0b\xa2\x8c\x08WU\xd8j\\\x0b\xa5\x83\xad\x87\x06\xea\xab\x86\xb4K\x19?)\x92\xd0\x85f\xd9\x1f\xa0\xd1\xd9\xfd\x08\xb7\x837B\xab3\xc3\xc5b\xdd\x97(\x94\xfaxo\xae\xefW\xe6K\xbbZ@a8\xf0\x90Q\x03\x13\xe6/\x99\xea4\x1f\xc0\xb3\x86\xef\xb0\xf7ca\xe5\xfa\xcf\xf3e\x07n\x84MJ\x92,_n\xef\x1a]\x18\xde\x88%\xeeH\x12\x10\xbe\xdb\x1b\xe2uF\xe7\xd6\x1f\xe0\x8b\x14/t\xbb'L\xcd\x85\xab#\xcfW]\xa5u\x81\r\xf4AE\x10\x9a\xaa\xdf#A\x1e\xae\xe9\x94\xea\xd6#FL\xeb\xfa,\xe9", 'PowerKey-BB-RC6-0C': b'\x06\x0c\xff\x00\x1f\x00Xr\xcd]\xc2\x98w\xf1\x19\xbc2o)~)=\xc0\x8c\xbc\xa9,\xc0\x0e\xbcs\x8aE\xbc>\x80\xef\x12\xbcf\xab\xa4\xb3\xc2\xec\x0c\x1f Q\xd9\xd1\x05\xbf\xf7\xeb`\x80\x0eR\x18\xe2\xe0\xbfMwZ\xe8\xa0\x8el\\9J\x88\x86\xfb\xc2\x15\xad\x9f\x9e\xe5\xc1ai\x97\x10]\x1f@\x95\xf411\xbe\x1b\xe4B\xa9\xfb\xfdr\x11\xea\x06\|0\xe9\xb6\x05\x17\xaf[W\xc3W\x98\x86%\xc3\xca\x02cr\xd0\xf3\xf2^\x96\xb8\x1f`\xac\x80\xd1\xfeh\x88\xd2\xf2M!VK\'\xb5\x0c\x94o\'\xec\xb3\x00b\x15}\x93g\x1bc\x90-\x85\xa1q\xb7\x99\xca\xcf\xe0d\xa7\x1f\x80\x1e"\x00\x02K\x9c\x87ac\x94\xf7\xc7\xb4A\xce\xe6\xdb\x00\x85@U\x89\x9fP\xb6e\xe5B\x18\xb8{\xce\xb8L\x9fq\x96aQ\xab\x1f\xa0\x80^\x991\xe3\xc8\x82\xf3.L\xa4\xf3:A#A`\x9e\x1c\x97\x8f\xc5,\xc3V\xbduY\xad\xc3\x80\xabvO\xa0\xd6K\xed\x8e\xc4\x1f\xc0\xa9\xbd\x92Q1\xcc\xe9\xc4\xf2\x1a\xba\xee\xe5\x0f\x98m\xe1s59\x88{\xc2\xcd\xe9\xf6G8-8\xe9fe\|@\x99\x8b\xb40\xce\x1f\xe0\xc5I\x9bv\xcf\x90\|\x06\x08[02\x86\x14\x95\x8epn=\xd2`\xccF\xacw\xc5)\xf4Y\xeeMt\x80\xa2\xab\x8b)\xa9\xcaX', 'PowerKey-BB-RC6-29': b'\x06)\xff\x00\x1f\x00l\x83\xc6\x8cQo\x98\xd3b\x82\xb7g\xf3\x9d\xac\xd2\xdd\xa7\xf0f\xb7\xbb \x89\x81\xe5\xbf\xf74\x85\xf1\x90t/\x01\x90;f\x17\x7f\x1f @\x13\xfe\x901(V\xee\xc04T\x10\x02\xd58\xf62\xd5\xd0G\xaf\x8alb\xdd\xd7\x95\x93M`\xecX\x8b\x10\x0bz\xb10\x97\|\x1f@\xb5\x19G\x1a%\xc3\xb6\xfdQ8w\xd4T\xd0\xc4R\x0e\x1cN\xaf@\xdd\xf7\xc8d\x8c[\xeb.\xddU\x15J\x9c\xbfhY\x9e\x973\x1f`\|T\xf4\xdd\x98\xcd\xa03\|D\xa5 \xa2\xe3\xab\xb1}D\xae8\xa45(\xdeh\xe6Xi\xd8\xfcf\xf6\x15\xca\xd1yc\x9f\xd7\xc9\x1f\x80"\xacY-*p\xce.\xa3.i{\x8c\xf7F\x98\x83\xc4\xc4\xe7Y<\x8e!\xa0%O\xa2\x05\x81\xf5\xd3\x9a\x96\xd1o/T\xcc\x88\x1f\xa0C\x15\x18\xc8\x1e\x9b\x84\x00\xb4\xf7r\xe4\x10\x18@\xd2i\x81N\xbe\x7f\xb7k#wZ\xafk\x8d\xba,\xf4\xaa_\r\xf4_\x1bf3\x1f\xc0\xa71\xa9\xc6\xa6\xae\xc4\xb0\xe4v\xbfX\'+\xc9\x06\r\xbf\xc1\x9b\xf5L\xe5\xd3\xdeyUU\x94=\xb4\x075<\xe0\xaf \xd9\xcd\x1c\x1f\xe0\xaf:>\xe6\x13\xc6\x07\x7fby#\xf3\xb3\xf3\xe7K&\x88\xb9\x1a\xdd\xe6u\xe7\x06\xf7\xe1&z\x99\xfb\xd0\x11\xf3\xd2*[\x12\xd1c', 'PowerKey-BB-QP-0C': b'\x08\x0c\xff\x00\x1f\x00ywx\xc0\x1b\x19\x19c\xb7L\xcc\xbf\xec\xd8\xe9w\xd7\xdf\x11\xfd\x9cBF8\x1dag\x87\xa2\xc1\xe2\xa2\x7f}\xee\xed\x0bS\xd5\n\x1f T\x0cg\xc7\xeb\x80o\x01xf\x14\xcbg\xb4bB\xf3<\x89\xfd\xaf*\x018\x9e\xc3\t\xb9\xeb\xcb\xec\xeb\x05\xb8\x11\x1e\xc4h0-\x1f@x\x8an\xde&\xd8\xe1-\xe9\x1ap\x86C%:xwH\xbar\x08\xb8\xb4\xfb)\x92>\x86\xe5\x0e2\x80\xea\xe4\xdf\xaa\xd9;B\x8b\x1f`.\xfc_\x89\xce\x1b\x91\x06\xb2\x95nKj\xc0\x8b\xe0\xc7\xa42c\xa7t\xc2c\x99a4\x151\x0f\xd2\\\x9f&\xd2\xe0\x87tNm\x1f\x80t\xe5\xed\xd0\xcfj\r\xfa\x132\xb8\xfe\xeb\x8f\xe6\x86\xe2R\xae\xc2\xadt\x0f\x02\t\x98\xe0\x1b\xa0X7\x88.K\x96\xdc\x9fV\xd5\xd3\x1f\xa0\x813\\\x81\xbc\x89b\xb4TL\x10\xac\xc5\xf0\x0b\xbf\xf20y\xd9\x10QC\xe0\xf3]\xe4\x17(\xf2\xc4\xdbw\xac\xde\xf7vTQw\x1f\xc0\x16\xbfz\xa9$\x9az5\xb0\xddjP\xb3\xb9\x8d~\xaa\x0b)\x1e\x05R\xac\x0f\t5v\xe2}>I\xa8\xdd\xa0\x8e~Y>GK\x1f\xe0\xbe\xee\xa81u\xae\xc6\x1f\xd3\x9e!\xc1T\x17]wa\xee\x00\x9b\xcc\x8b?\x8c\x80Gg\xbc\xcaz\x1dq\x83d\xd6\xd8\xe5\xace\xfb', 'PowerKey-BB-QP-29': b'\x08)\xff\x00\x1f\x00X\xa2\x1d\xd0r\xa6\xb4\n\x03s\xae\x9e;G\x03\xe5\xec\x98\x92\xd9\xad\x96_\x0cGLjLGb\xba\xde)\x13\xd4\x07X\xc7\xa1\xe1\x1f \xb5($\xd4O-7C\xb9m\r\x156R\xe2\x8eJ\r\xca\xab?\x0c\xcd&J\xdd j`\\\xde\xa1w\x1d\xb3\x1eB\x8f\xb09\x1f@E\xc7\xc2\xb42\x15\xad~\xb3Q\x1c\xa5j\x07a\xcaA\xf5\xce$g\x85>\xaeSTA\x15\xd1.\x1d\x82\xc1B6\xfa/\xe2\x17\xe9\x1f`\xd1\x96\x97\xd3\xec\x99\x8f\x9a\x8a\x03\xe6\x0322\xb1\x02\xdc\xde\x1cj\x88\xac\xccK\xfd\xe1\xd0\xedn{\xd5\xed\xfbs\xd1\xbb\xc7\x0fp\xce\x1f\x80\x94\xd0\xfa\x80\xc4\xb1\x91E"e\x8ek\x0c3\xbcR\xfc {\x93\xb1F\x15\xee\xa2\x8fm\xc0Q\xd8\xb4\xf4\xb7,\xba\xcb\xf5$O\xf6\x1f\xa0\xfa\x961\xf2`\x1f\xda\xb8\x8a\xd2\x1f\x84-\x1e6\xddU\x92P\xc4\x899<\x8dy,\xe8Z\xf2D=_vlR.\xd9\xcdix\x1f\xc0CZ\xed\'>B\x8d}\xfc\xda\xaf\xab\xaa\x14\x01\xb4\x95\xaet\x83PK!\x03&d<\xce(\xc4\x06\x8a\xfb\xc8<\\_\x08\xbfh\x1f\xe0X\xd6\xfd\xad\x15]G\xf5\xed\xd8\xc0n\x08\xa1\xfb\x0b\xbf\nq)s\xd3\xc6^\xfd\x0e\'\x8ej\x1b~\xe8\x04\x80\xe8%\x97\xe2?\x96', 'PowerKey-SF-SS-00': b'\x04\x00\x00\x00\x1d\x00\x9f@\x08*\xf4\x9c\xb65l\x16p\n\xcf\xa5\x83\r\x9d\xfcM\xf1\xe6b\x0e\x8d\xe5\xcd\x97x\xaf\xad\xf1\x05\xa0W\xe9k\xfa\xf5\xde\x1d\x1d \x93\xb8\xc0\xe7j\xa7\x9b\xd4\xd3}\xc5\xf8\xe4\xbd]l\x9d\x80\x8b\xf0\xd1 .Y\xd1\x05\xb8\x84\xda\x81\xcf\xa6\xcf6\x0fO\xfd\x9f9\x9f\x1d@\xbb\xb1Pl\xca1Z\xba*\x9eFP\xb2\xce\xd0\x7f\xb5\xdc\x1bG\xd9~\xf4\xb9\xb8\xcf\xae\x1e\x89\x8d\xb9\x1b\xf2\n\xeb\xd9/@\xe1R\x1d`\x7f+\xb3\xd9\x11\x86*\xb1X\x9f\x95\x89C\x1d\xd9N\x97z\x1a*I\xd8*I\x97\x14z\x98=\x80\xd1\xee\xbb\xf5\xff\x9c\xde\x99\t\xe2\x1d\x80\x0f\xae\x95\xdd\xd7\x14\xf3\xa8$$\xf8\x96>\x94\xe50\x06h\xf0t\xdd\xc3\xb8\xe3\x1a\xbch?9\xd0\x188W\xb3\x9flM8\xf2J\x1d\xa0j\xefy\x19\xd3\xf9\xceXnG\xf9\xdc\x99\x18\xf5\xc2\x81\xb7\x9c\x1fA\xc9M\xb3\xa2\xba\xb8\xd8\xe9\xd7Hi\xcf\xd3m\xe5\xd6\xd6\xe54\x1d\xc0\x1b\xd9\xcd\xef^\x1a\xb8\x7f\xcf\xd9V\x96\xb1O\xef9\xec\xb92/\xe9\xd7?@x#\xc5\xa0\x16\xea6o\x1a\xd4V&1\xcf_\xa3\x1d\xe0zM\xfe\x8c\x0f\xf4s\xfa\xf7TJ\xc9\xd7\x04\xd2\xe7T\x7f\x8e\x08j\x92\xbc\x15\t\xf5\xbc\x0e\xf6\xfcVQ;\xa7\xfc\xdf\x0e9\xef\xa6\x1e\x00\xed\xf6\x83\x116\x80\xfd\xb9\x15\xd3\xf3\xc5G]\xba[\xc8\xd0#\x00_0\xbck.Ll\xae\xd1\xb1\x1f\xe0\x1c\xbe\x12\x18y\xba\xf7\xde\x1e \xdc\xb5U\x08\x13\xb5\x05\xe7\xdf\x83\xa3\xa1\x1a\xd1\x84\xb8}\x02\x87\x0b)\xa5T\xe7\x90\x9ec\x87\xe1\xad\xfd\xb7\x1e\xa2\xec\xbc8\x896\xa5\x1e@\xd9h\xe8\xa4\xdcb\xd0r\xa9\x82\xcep\xee"\xd1\r\xea\x853\x84\x93\x0fZ`\xe5\xe8\xa1)\xdf=\xb3\x1c:A\x02G\xb7\x9f\xedz\x1e`<\xd0}b\xaa\xfc7;\x15\x80\xa2\x8a\xc4\x0e\x0c\xceKJ\xf14[\xbe\xed\xce6\xd7\xc7q\xe1\x0e\xdb\xf1\x15\xec\x80Mxy\x10\x0b', 'PowerKey-SF-RC6-0C': b'\x06\x0c\xff\x00\x1d\x00j1\xdb\xee\x97;\xcf\xaceWEA\xa8\x0e\xf8\xcaH!\xa6\\\xbe \xab\x86\xfde@B\x8d\xeb\x0e\x9c7\xc1\xfe\xb4*\x98\xc1\xd8\x1d "\xd8\xf4)\xceT\x1eW\xeb\xfa\x7fyiZ\xcd\xa9?\xb0UL\x8b\x98\x11\x9c\x9f\xb7[{k\x10h\xeaPP\x13c\xf1\x81\x04\x0f\x1d@\xcf\xf3\x97\x96L\x8fA\x89\x0c\xebY\xde\xf1\xac8\xa6\xb8\xddq\x16b\xde\xc0\x9d\xe2\xa9bM\xc7-\xb2\xec\xa3J\xaa\x11\xc2\xf2\x91\xb6\x1d`\x13\x88q\x0fESGLj\xe4\x06\xb7#\x88}\x0fu\xc5\xa6$\xd7\x99S(\xb0\x80\x87\x13@\x88\xf1#\xcd\x17\xb9\x1f\xd4\x0ev\x80\x1d\x8030\\\x05J\xcdE\xdbs}LP\xe9D\xe8}\xfb\xbb<*\x1fy\xae1:D4\xff\xb6\xccgFA\xebU1m\xd7\xc0\xbc\x1d\xa0YR\xd2\xf6\'\xe7\x07o[],\xc1\xcd\x95\xb9\xf2\xa4e\x13\x13\xb4\x19>LY\x15NuI\xb5\x8f\x8c4\\\to\xdb\xa4\x12\xec\x1d\xc0\x9cr\xf2\'\x1bj&`\x00\xba\xc7\x16\xa0\xcbS\x89\x93\x92h\x91\xe1\xb8\xcbQAR\xfcS\x97\xa1\xb7D\xee\xb3rk\xac\xd8>\xeb\x1d\xe0\x10"\x1cr\x90\xe1\x138\xe9r\xb4\xe9s\x14\xee\xd4\xc5q\xbeO\x9b\x98/y\xe3\xcc\xfc\xa0n\xc7\xd47\xd8\xe7\x96\x88\xad\xd9m\x02\x1e\x00\xad\x80\x08\xf9\x87D\xd6\x0c2\xe8q\'[s\x12\x9bX\xb4\xbd\x1fK#*a\xf0\xeby{\xe5\x9dy8\xc8\xdc\xce\xcf\x90\x87aX\x1e T\x0f\xd1\xf1\x9c\x8b\x13\xcc\xf6k[q\xcfh\xcb\x0b=\xdd2K\x0c\x1d\xa5\xf9\xf8\xd5\xd8\x15R*\n\xa7\xf8\x00\xc7\x04k\xefUT\x1e@\x12\xceW\xf9^\x89k\xa9\xf9\x84\xbd\xd2TBF\x02\xa7\x15\xd0\xc8\x9b\x1eC\x86X\x1b\x153F\xbf\xcd\x8c\xfa\x0c\x930D\xff\x884\x1e`\xa8.&\x97d\xcb\xbd\x06\xb8$\xe93T\xdb]\xed\x97\x8b\xe2/\x96\xd9\xcb+\xf7\xf1\xeb\xf0-\xc89\xdfgR\xe9A\x18P\xc4\x90', 'PowerKey-SF-RC6-29': b'\x06)\xff\x00\x1d\x00\xcciR\xad\x12\'\xcc4?\xa5\xc6\xb5h\x9f8TL\xe3\x86\x8d\x03\xfa.\x03\xe2\xb5\x81a\x9d@\x04\x1d\|v\x9aP\xef;\x85@\x1d C!\x95d\xc0R\x8f\x9b\xf6 H\xed.1\xfe\x13kZ-\xc0\x1a#\x1f\xff\xb8\x0251(v\xdaX*m\xea\xad\xfb\xf9\xb3\xe6\x1d@\x93\xc6d_K\xd1\xf0S\x9d\x91 \xa1\xd1eR\xed\xd2]\x18![X\xea\xea\xb8M\xfd0\xcaW=\xe1\x91\xf9>\xa3\x89\x1e\xed\|\x1d`\x98\x83\xbb\x81\xc0cv3m\x15\x0c7\x97*\xab\xa1\x8a>\x9aS\xa3\x97\t\x1a\x0c\xde\x9c\xcaF\x7f\xd5\x96\xd8\xfd\xf9\x9cD\x83\xa5Z\x1d\x80\xe6\xb7\xdd\xf6`\xde\x87J\x99\xb1\x90s%\xb9*\xbd\xd9\xfe?&7\x187`i/\xff\x82\x90\x7f.t\x15/\x8e\x06i7\xc4\x8c\x1d\xa0\xdb\xd5\xfb\xb0\|\xa3\xd4\x8b;R)\xf1\xb0!\x0c\xf7\xf6\xe5\xfe\xc1\x180ay\xe3\xbfB\xd1Qx\xf2\x88\x08}\xee\x9f"\xec$\xf0\x1d\xc0Y\x84.\xdc{n\xa4\xd1\xf5\x04v\xff\x1f\xea\xfa#i\x96k\x92\x02\xd8\xc0\xef\xc3\xec\xbd\x15\x03Xx5\x1a\x03\x7f21\xb2\xb1\xbb\x1d\xe0xfG\xea\x0c\x82\xfb/\x9d\xc6E\xee\xf7Tg\|\x1b\xf40:\x96\xd3:\xa2\xb9\x07\xdcV\xf0\|,\xe7\x99*\xda!]K9V\x1e\x00I\xa3\xca\x9f\xd4N\xf87\x15\xc6\x1a\x08\xfcma\xa9$\xb1\xf4\x01\xc5y%\xb2\xe3t\x88$,p\x16\x1c\x8bV\x86\xf7\xc5\xd23d\x1e \xb6\xf3\x08\x97Fh:\xad3\xb5e\xef\xe85\x15\xd2\xfd\xee\xa5\x87\x04ML\xc5\x9a\x93\x15Rs\xde\xa6\x11\xba\xb3\xed"c\xfb\xa0\xe7\x1e@\xc3!\xba\x10\x96\xfc=\xe9\xe8\x0f\xa3\x0c\xa8\xd9w\x89\n\xdf\x19XEN\x96\xbcI\xab2\x151\xef3\xc3\xbc6\xfc/\xcd\x97\x92\xcc\x1e`\xb9\x8d\xfcK!\x0e\x8en\xcfD*\xaf\xc9>\x1c\xd4,g\x0b1@be\x9b\xd7\xf0\x0ekraYX\x9fk\xd5=\xd1WA\x1b', 'PowerKey-SF-QP-0C': b'\x08\x0c\xff\x01\x1d\x00a\xc4oj\x86\r\xb52\xbb*\xf4r\xfe/\x05(?\xe4V{\x88\xfc\xfb\x16\x94\x1b\x81\xdeN\xcb\xfb\xea\x81\x86\xac\x8b\xab\xfc\'\x01\x1d c\xe0\xe3SK\|;\x90\xb7\x052?B\x8f\n\x08\xd2\xbfUP\'\x91\xe4\xccK\x11sx`xX\xd4i\x06s\xc1m*\xe7\x8f\x1d@\x8a\xf7\xd33\x0b\x93[(\x93\xc3\x92\x14\x0c\x1ec\xed\xfe\xa2Yc,\xa0\x8a \xa6\xd9\x9d\xc6u%.\x83\x0e\x06\xb2\xb2e\xa1\t\x93\x1d`C@\xcc\x80\x08.\xae\x00\xb7\xef\x071B\xfb\xaf\\ \x11\xd5?\xd3\xaf\xbc\xf8&\xb43\xfa\xb8\x10\xe2&\x94\xbb\xfe\x05\x03:\xa4\x9b\x1d\x80\xf5&X\xfdoKq\xfb\x8d\x95\xael\xe7z\xd7\x07\xbe\xab\x84\xc5Tj\x93\x1d2\x14\x8c\|\x0c\x82Q\x9d\x86\xff\xbe\xe4\x01,\xb2d\x1d\xa0R\x89\x83\x19\xa3\xef\x96\x94\xca\\o\tT\xa8\|\xfd\xc8<C\xd1\xd2\xde\xad\x93U\xa3\xc2>\xb7\x11\xfe\x9a\r>\x9a\x0fQ\x9bJ^\x1d\xc0\xf9\xe6\x84\xd4\x97S\xf5\x15\xdf\xa4`\x12\x81\xad6\x8e\xce\xb4\xb6jB\xbaG\|\x06\x19\xd3\x13\xd3\x11\xec1\x94\xc7\xc2\xa01\xb9G\xa0\x1d\xe0\x08\xb2v\xd5\x9a\x05\xe6\xcc5U\x82\x85f\x94J\x83\xa0\xd5E\xf8x\x9e\xa8[\x8a\xd4+c*\xbcqB\x9d\xd1a\xd2\x9e1\x11\xc2\x1e\x00\x01\x854\xe4\r\xa0J\xbe\xef\x93\x02\x95\xbdQO\xce\xa9\xa5sut}\xc6~\xe6\xad\tpJ&\xd83\xfe\x86Zm\x98\x82\xf7\x98\x1e \xcf\x96~\xe6\x101W-\x1cQ4}\xcdm\x02\xbb!\xe9>\xfdj\xc3\xd4s1u\xa0\xf3\xe9(R\xa9\xd6\x83\xf1/3\x96,\x81\x1e@\x0c\xd1\xc7\xb3\x8b\xb4\x80\xa7\x17\x9e\xcb\xfa\x8b\x9a\xec\xab\xed\x8d\xd9\xa7\xceTh\xc8\xc9)\xd4\x8b>\x94\x96\x9a\x8b\xd3\xfdG"z\xcae\x1e`\x10\xd8D\xef\xfd\x86\x16\xcc\x87\xca\xeb\xc2=\xeaY\x9c\xc6\x0bUk\xe2\xa5#\xecE\x8e\x18\x95\xfc\x8b\t\xe9\x1b\x8b7\xea\xd5\xcb\x8c,', 'PowerKey-SF-QP-29': b'\x08)\xff\x01\x1d\x00\xd8\\\xaaN\x1e\xc1KJ\x9f1\x8a$Dw5\xd7\xf1\xf0\xe9\xa4.\xa8L\x13\xbf\xa0\x03\xe7IR\x13\xd8\x01\xa7/\xc8\xc3\xe4B5\x1d \xa2\x8f\xd2`c\xaf\x02~1\xf5\xeb\x15\xf3\xffHZI\x9e\xee\x186\x9aF\x1co\xca\x9d\xcc\x02\xf9\xca*\xefeH(\xd5\xfa-Z\x1d@\xa9C=Z\xc9m\xa2\xa5\x04\xb8@b\x9a\xeb\xd8\xbc%\xd9\xa4\xf3\x07\x1cv\x05\xb0d}\x8fBn\xf3\xf3\x18\xf8xP4\xbdf\x16\x1d`\xf7sN:\xfd\xfe.Y\xf3C\x80>\xb1`90\xea\x7f?\x8e$r6p\xfc\xf0\xd2\xcdo\xcb\xaap\xb7C\xe5\xc9\xb7\xfe\x9eR\x1d\x80U\x8a\x1a\xa4\x1b\xd0 \x0e,\x85q@dG0\\\x95+PYo\xa9\x15\x84\xae\xb5\xba(\x1a\x14\xd4#;\x92A\xebb\x80\x07\x08\x1d\xa0n\x9ek\xaf\xbd\xc4\x7fI\x8b:\x7f\xa9\xf5.d\xce_\xd4\xeb\x81\xf8d\xfb\xdd:L\xfd\xc9u\xd1~\n\xbbP\xf4\xb5\x83\xeb\x96\xc7\x1d\xc0\x84\xd7N\xcd\r\x81\x9c\xbdp\x8f\xb4\x0f79\xd8\xe7\xff>\x0e\x8eV\xed\x11V\xbc\xcb\x98\xc9\x91[\x02E\xc33\xe6\x99XR\x9d\xb3\x1d\xe0^J.\x10\xa9\x92f\x01\xd2\xfe\x1d\x9c\xb1P\xdc0\|\x1d?\x95_\xc4\xcdvY\x07\xe8VW\xae\xb4C\x03\x0f\x0e\xf1w\xdfJr\x1e\x00H<S,\xc8\xceY\xae\xa5}\xa8k\x90\x96_p^Y\xe0/\xa8\xac\xef\xf2+_\xc7R\x94E\xdf\'\x8byD\x02"\x87\xb9-\x1e \x7fUB\xe6\x89\xa9V3P\x9a\x14A\x96b\xc3{\|R\xe5cD\xb2\x8d\xf7\xbe\x07\x19\xbf\x837\xe9B\xa6\x18\x82xO\xe5\x7f\x04\x1e@\xdd\xc7\x86\xe8B\x17\x9a\xe3}\xfd\xa9\xab\xb9\xcfi\xd0\xdd\xe08\xe9\xca\xd9\x7f\xd8\xe43}\xd6\xe1\x06\xe8u#\x84&O\xbd50\xf9\x1e`\x9d9\xccJ\x95\x8e\xbd\x9dR\x96`\xa9\xb9\xab\xde\xbfs\xc1\x82\x9b*bSC\x82\xe4\|`\x19\xaaKh\xf6\x04\x16\xaey\x08\xdb\x05'}`|



##### Service Parameters
  
Wdf : `{'KmdfLibraryVersion': '1.5'}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">usbehci Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|BootFlags|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\usbehci.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x17`|`@usbport.inf,%EHCIMP.SvcDesc%;Microsoft USB 2.0 Enhanced Host Controller Miniport Driver`|`usbport.inf`|`0x04`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">usbhub Service </span>

|Performance|
| :---: |
|`{'Close': 'CloseUsbPerformanceData', 'Collect': 'CollectUsbPerformanceData', 'Library': '%SystemRoot%\\system32\\usbperf.dll', 'Open': 'OpenUsbPerformanceData', 'InstallType': 1, 'PerfIniFile': 'usbperf.ini', 'First Counter': 9006, 'Last Counter': 9040, 'First Help': 9007, 'Last Help': 9041}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">USBHUB3 Service </span>



##### Service Parameters
  
Wdf : `{'LogPages': 3}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">usbohci Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\usbohci.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x16`|`@usbport.inf,%OHCIMP.SvcDesc%;Microsoft USB Open Host Controller Miniport Driver`|`usbport.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">usbprint Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\usbprint.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`extended base`|`0x14`|`@usbprint.inf,%USBPRINT.SvcDesc%;Microsoft USB PRINTER Class`|`usbprint.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">usbser Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\usbser.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@usbser.inf,%UsbSerial.DriverDesc%;Microsoft USB Serial Driver`|`usbser.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">USBSTOR Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|BootFlags|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\USBSTOR.SYS`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@usbstor.inf,%USBSTOR.SvcDesc%;USB Mass Storage Driver`|`usbstor.infv_mscdsc.inf`|`0x14`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">usbuhci Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\usbuhci.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x18`|`@usbport.inf,%UHCIMP.SvcDesc%;Microsoft USB Universal Host Controller Miniport Driver`|`usbport.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">USBXHCI Service </span>



##### Service Parameters
  
DmaRemappingCompatibleSelfhost : `0x01`  
DmaRemappingCompatible : `0x02`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UserDataSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\userdataservice.dll`  
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
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UserManager Service </span>



##### Service Parameters
  
DeviceAccessBrokerConsentRequired : `0x01`  
ServiceDll : `%SystemRoot%\System32\usermgr.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`42 00 31 00 38 00 46 00 42 00 41 00 42 00 36 00 2d 00 35 00 36 00 46 00 38 00 2d 00 34 00 37 00 30 00 32 00 2d 00 38 00 34 00 45 00 30 00 2d 00 34 00 31 00 30 00 35 00 33 00 32 00 39 00 33 00 41 00 38 00 36 00 39 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">UsoSvc Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\usosvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  
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
    Access: 0xf01ff
    SID: S-1-0-32-544
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
#### <span style="text-align: center; font-size:2em;">VacSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\vac.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">VaultSvc Service </span>



##### Service Parameters
  
ServiceDll : `X:\Windows\System32\vaultsvc.dll`  
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
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x100
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-20
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-19
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x14
    SID: S-1-0-2-1
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vdrvroot Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\vdrvroot.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_CRITICAL`|`Boot Bus Extender`|`0x04`|`@vdrvroot.inf,%vdrvroot_svcdesc%;Microsoft Virtual Drive Enumerator`|`vdrvroot.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vds Service </span>

|Alignment|SoftwareProviders|VirtualDiskProviders|
| :---: | :---: | :---: |
|`{'(Default)': 'Alignment Settings in Bytes', 'Between4_8GB': 1048576, 'Between8_32GB': 1048576, 'GreaterThan32GB': 1048576, 'LessThan4GB': 65536}`|`SoftwareProviders`|`VirtualDiskProviders`|
  
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
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x70
    SID: S-1-0-32-551
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">VerifierExt Service </span>

|BootFlags|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`0x40`|`@%SystemRoot%\System32\drivers\VerifierExt.sys,-1001`|`@%SystemRoot%\System32\drivers\VerifierExt.sys,-1000`|`SERVICE_ERROR_NORMAL`|`WdfLoadGroup`|`System32\drivers\VerifierExt.sys`|`SERVICE_DISABLED`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vhdmp Service </span>



##### Service Parameters
  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vhf Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Description|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\vhf.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x0a`|`@hidvhf.inf,%VhfService%;Virtual HID Framework (VHF) Driver`|`@hidvhf.inf,%VhfDesc%;Kernel mode driver that implements the Virtual HID Framework (VHF)`|`BthLCPen.infhidvhf.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Vid Service </span>



##### Service Parameters
  
ExoDeviceEnabledClient : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">VirtualRender Service </span>

|ImagePath|Type|Start|ErrorControl|Owners|
| :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\DriverStore\FileRepository\vrd.inf_amd64_81fbd405ff2470fc\vrd.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_IGNORE`|`vrd.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vmbus Service </span>



##### Service Parameters
  
Winsock : `Winsock`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">VMBusHID Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\VMBusHID.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_IGNORE`|`Extended Base`|`0x2c`|`wvmbushid.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vmgid Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\vmgid.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@wvmgid.inf,%VmGid.SVCDESC%;Microsoft Hyper-V Guest Infrastructure Driver`|`wvmgid.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vmicguestinterface Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\icsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `GuestInterfaceServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`e34bd134-e4de-c841-9ae7-6b174977c192`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vmicheartbeat Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\icsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `HeartbeatServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`394f1657-1591-784e-ab55-382f3bd5422d`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vmickvpexchange Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\icsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `KvpexchangeServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`e7f4a0a9-455a-964d-b827-8a841e8c03e6`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vmicrdv Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\icsvcext.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `RdvServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`f4ac6a27-15ac-6c42-98dd-7521ad3f01fe`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vmicshutdown Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\icsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ShutdownServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`31600b0e-1352-3449-818b-38d90ced39db`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vmictimesync Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\icsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `TimesyncServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`30e62795-aed0-7b49-adce-e80ab0175caf`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vmicvmsession Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\icsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `VMSessionServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`d4539e99-5c3d-3e4c-8779-bed06ec056e1`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vmicvss Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\icsvcext.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `VssServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`292efa35-23ea-3642-96ae-3a6ebacba440`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">volmgr Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\volmgr.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_CRITICAL`|`System Bus Extender`|`0x09`|`@volmgr.inf,%volmgr_svcdesc%;Volume Manager Driver`|`volmgr.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">volmgrx Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\volmgrx.sys,-101`|`@%SystemRoot%\system32\drivers\volmgrx.sys,-100`|`SERVICE_ERROR_CRITICAL`|`System Bus Extender`|`System32\drivers\volmgrx.sys`|`SERVICE_BOOT_START`|`0x0a`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">volsnap Service </span>

|Description|DisplayName|ErrorControl|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\volsnap.sys,-101`|`@%SystemRoot%\system32\drivers\volsnap.sys,-100`|`SERVICE_ERROR_CRITICAL`|`System32\drivers\volsnap.sys`|`SERVICE_BOOT_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">volume Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\volume.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_CRITICAL`|`@volume.inf,%VolumeServiceDesc%;Volume driver`|`volume.infsmrvolume.infscmvolume.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vpci Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\vpci.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`System Bus Extender`|`0x0c`|`@wvpci.inf,%vpci.SVCDESC%;Microsoft Hyper-V Virtual PCI Bus`|`wvpci.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vsmraid Service </span>



##### Service Parameters
  
Device : `{'CreateInitiatorLU': 1}`  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">VSS Service </span>

|Diag|Providers|Settings|VssAccessControl|
| :---: | :---: | :---: | :---: |
|`{}`|`Providers`|`Settings`|`{'NT Authority\\NetworkService': 1}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">VSTXRAID Service </span>



##### Service Parameters
  
PnpInterface : `{'5': 1}`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vwifibus Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Description|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\vwifibus.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@%SystemRoot%\System32\drivers\vwifibus.sys,-257`|`@%SystemRoot%\System32\drivers\vwifibus.sys,-258`|`netvwifibus.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">vwififlt Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\System32\drivers\vwififlt.sys,-260`|`@%SystemRoot%\System32\drivers\vwififlt.sys,-259`|`SERVICE_ERROR_NORMAL`|`NDIS`|`System32\drivers\vwififlt.sys`|`SERVICE_SYSTEM_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">W32Time Service </span>

|Config|SecureTimeLimits|TimeProviders|
| :---: | :---: | :---: |
|`{'AnnounceFlags': 10, 'ClockAdjustmentAuditLimit': 800, 'ClockHoldoverPeriod': 50000, 'EventLogFlags': 2, 'FrequencyCorrectRate': 4, 'HoldPeriod': 5, 'LargePhaseOffset': 50000000, 'LastKnownGoodTime': 130828608000000000, 'LocalClockDispersion': 10, 'MaxAllowedPhaseOffset': 1, 'MaxNegPhaseCorrection': 54000, 'MaxPollInterval': 15, 'MaxPosPhaseCorrection': 54000, 'MinPollInterval': 10, 'PhaseCorrectRate': 1, 'PollAdjustFactor': 5, 'SpikeWatchPeriod': 900, 'TimeJumpAuditOffset': 28800, 'UpdateInterval': 360000, 'UtilizeSslTimeData': 1}`|`{'SecureTimeEstimated': 130828608000000000, 'SecureTimeHigh': 130828608000000000, 'SecureTimeLow': 130828608000000000}`|`TimeProviders`|



##### Service Parameters
  
NtpServer : `time.windows.com,0x9`  
ServiceDll : `%systemroot%\system32\w32time.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `SvchostEntry_W32Time`  
Type : `NTP`  
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
    Access: 0x2019d
    SID: S-1-0-19
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x200a9
    SID: S-1-0-19
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-80-3169285310-278349998-1452333686-3865143136-4212226833

```


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`ba0ae21c-5198-2144-9430-1ddeb766e809`|`SERVICE_TRIGGER_TYPE_DOMAIN_JOIN`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WaaSMedicSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\WaaSMedicSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  
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
    Access: 0xf01ff
    SID: S-1-0-32-544
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
#### <span style="text-align: center; font-size:2em;">WacomPen Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\wacompen.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x1f`|`@hiddigi.inf,%WacomPen.SVCDESC%;Wacom Serial Pen HID Driver`|`hiddigi.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WalletService Service </span>



##### Service Parameters
  
ServiceDLL : `%SystemRoot%\system32\WalletService.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wanarp Service </span>

|Linkage|
| :---: |
|`{'Export': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00w\x00a\x00n\x00a\x00r\x00p\x00\x00\x00\x00\x00', 'Bind': b'\x00\x00', 'Route': b'\x00\x00'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wanarpv6 Service </span>

|Linkage|
| :---: |
|`{'Export': b'\\\x00D\x00e\x00v\x00i\x00c\x00e\x00\\\x00w\x00a\x00n\x00a\x00r\x00p\x00v\x006\x00\x00\x00\x00\x00', 'Bind': b'\x00\x00', 'Route': b'\x00\x00'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WarpJITSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\Windows.WARP.JITService.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`35 00 41 00 30 00 43 00 45 00 37 00 34 00 44 00 2d 00 46 00 39 00 43 00 46 00 2d 00 34 00 44 00 45 00 41 00 2d 00 41 00 34 00 43 00 31 00 2d 00 32 00 44 00 35 00 46 00 45 00 34 00 43 00 38 00 39 00 44 00 35 00 31 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wbengine Service </span>

|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|RequiredPrivileges|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%systemroot%\system32\wbengine.exe,-105`|`@%systemroot%\system32\wbengine.exe,-104`|`SERVICE_ERROR_NORMAL`|`84 03 00 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 e0 93 04 00 00 00 00 00 00 00 00 00`|`"%systemroot%\system32\wbengine.exe"`|`localSystem`|`['SeImpersonatePrivilege', 'SeBackupPrivilege', 'SeManageVolumePrivilege', 'SeRestorePrivilege', 'SeSystemEnvironmentPrivilege', 'SeSecurityPrivilege', 'SeTakeOwnershipPrivilege', 'SeShutdownPrivilege']`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WbioSrvc Service </span>

|Databases|Service Providers|
| :---: | :---: |
|`Databases`|`Service Providers`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wbiosrvc.dll`  
ServiceDllUnloadOnStop : `0x00`  
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
    Access: 0x2019d
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
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x15
    SID: S-1-0-2-1
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`43 00 30 00 45 00 39 00 36 00 37 00 31 00 45 00 2d 00 33 00 33 00 43 00 36 00 2d 00 34 00 34 00 33 00 38 00 2d 00 39 00 34 00 36 00 34 00 2d 00 35 00 36 00 42 00 32 00 45 00 31 00 42 00 31 00 43 00 37 00 42 00 34 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`34 00 42 00 45 00 39 00 36 00 41 00 30 00 46 00 2d 00 39 00 46 00 35 00 32 00 2d 00 34 00 37 00 32 00 39 00 2d 00 41 00 35 00 31 00 44 00 2d 00 43 00 37 00 30 00 36 00 31 00 30 00 46 00 31 00 31 00 38 00 42 00 30 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wcifs Service </span>

|Instances|
| :---: |
|`Instances`|



##### Service Parameters
  
DebugOptions : `0x0c`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Wcmsvc Service </span>

|Csps|
| :---: |
|`Csps`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wcmsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `WcmSvcMain`  
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

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`e8731faa-fd15-d245-abfd-e7f64f78eb11`|`SERVICE_TRIGGER_TYPE_CUSTOM`|`01 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wcncsvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wcncsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `WcnServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-19
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x301fd
    SID: S-1-0-32-556
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wcnfs Service </span>

|Instances|
| :---: |
|`Instances`|



##### Service Parameters
  
DebugOptions : `0x00`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WdBoot Service </span>
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x0b
    Access: 0x10000000
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Wdf01000 Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\Wdf01000.sys,-1000`|`SERVICE_ERROR_NORMAL`|`WdfLoadGroup`|`system32\drivers\Wdf01000.sys`|`SERVICE_BOOT_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WdFilter Service </span>

|Instances|
| :---: |
|`Instances`|
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x0b
    Access: 0x10000000
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WdiServiceHost Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\wdi.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201ef
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
    Access: 0x201fd
    SID: S-1-0-80-2970612574-78537857-698502321-558674196-1451644582
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WdiSystemHost Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\wdi.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201ef
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
    Access: 0x201fd
    SID: S-1-0-80-2970612574-78537857-698502321-558674196-1451644582
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wdiwifi Service </span>



##### Service Parameters
  
ForceLogsInMiniDump : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WdmCompanionFilter Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: |
|`@%SystemRoot%\system32\drivers\WdmCompanionFilter.sys,-1000`|`SERVICE_ERROR_NORMAL`|`base`|`system32\drivers\WdmCompanionFilter.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WdNisDrv Service </span>
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x0b
    Access: 0x10000000
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WdNisSvc Service </span>



##### Service Parameters
  
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
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WebClient Service </span>

|NetworkProvider|
| :---: |
|`{'DeviceName': '\\Device\\WebDavRedirector', 'Name': 'Web Client Network', 'ProviderPath': '%SystemRoot%\\System32\\davclnt.dll'}`|



##### Service Parameters
  
AcceptOfficeAndTahoeServers : `0x01`  
BasicAuthLevel : `0x01`  
ClientDebug : `0x00`  
FileAttributesLimitInBytes : `0xf4240`  
FileSizeLimitInBytes : `0x2faf080`  
InternetServerTimeoutInSec : `0x1e`  
LocalServerTimeoutInSec : `0x0f`  
SendReceiveTimeoutInSec : `0x3c`  
ServerNotFoundCacheLifeTimeInSec : `0x3c`  
ServiceDebug : `0x00`  
ServiceDll : `%SystemRoot%\System32\webclnt.dll`  
ServiceDllUnloadOnStop : `0x01`  
SupportLocking : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`84d6b622-63fa-7845-87c9-effcbe6643c7`|`SERVICE_TRIGGER_TYPE_CUSTOM`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Wecsvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\wecsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WEPHOSTSVC Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\wephostsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`35 00 36 00 32 00 34 00 34 00 32 00 34 00 33 00 2d 00 33 00 45 00 44 00 33 00 2d 00 34 00 30 00 31 00 33 00 2d 00 42 00 33 00 45 00 37 00 2d 00 30 00 46 00 43 00 38 00 30 00 39 00 45 00 33 00 35 00 46 00 42 00 41 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wercplsupport Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wercplsupport.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WerSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\WerSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|
| :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`d8ea6ee4-540c-8944-9898-8fa79d059e0e`|`SERVICE_TRIGGER_TYPE_CUSTOM`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WFDSConMgrSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wfdsconmgrsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`39 00 46 00 41 00 36 00 41 00 46 00 46 00 36 00 2d 00 45 00 30 00 41 00 44 00 2d 00 34 00 38 00 44 00 46 00 2d 00 41 00 36 00 42 00 34 00 2d 00 45 00 36 00 34 00 42 00 45 00 36 00 36 00 41 00 31 00 37 00 41 00 31 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WFPLWFS Service </span>

|BootFlags|DependOnService|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`0x01`|`ndis`|`@%SystemRoot%\System32\drivers\wfplwfs.sys,-6000`|`@%SystemRoot%\System32\drivers\wfplwfs.sys,-6000`|`SERVICE_ERROR_NORMAL`|`PNP_TDI`|`System32\drivers\wfplwfs.sys`|`SERVICE_BOOT_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WiaRpc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wiarpc.dll`  
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
    Access: 0x2019d
    SID: S-1-0-80-3182985763-1431228038-2757062859-428472846-3914011746
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
#### <span style="text-align: center; font-size:2em;">WIMMount Service </span>

|Instances|
| :---: |
|`Instances`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WinDefend Service </span>
  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x0b
    Access: 0x10000000
    SID: S-1-0-80-956008885-3418522649-1831038044-1853292631-2271478464
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xe01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2019d
    SID: S-1-0-6
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Windows Workflow Foundation 4.0.0.0 Service </span>

|Performance|
| :---: |
|`{'CategoryOptions': 1, 'Close': 'ClosePerformanceData', 'Collect': 'CollectPerformanceData', 'Counter Names': b'W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00C\x00r\x00e\x00a\x00t\x00e\x00d\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00C\x00r\x00e\x00a\x00t\x00e\x00d\x00/\x00s\x00e\x00c\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00U\x00n\x00l\x00o\x00a\x00d\x00e\x00d\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00U\x00n\x00l\x00o\x00a\x00d\x00e\x00d\x00/\x00s\x00e\x00c\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00L\x00o\x00a\x00d\x00e\x00d\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00L\x00o\x00a\x00d\x00e\x00d\x00/\x00s\x00e\x00c\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00C\x00o\x00m\x00p\x00l\x00e\x00t\x00e\x00d\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00C\x00o\x00m\x00p\x00l\x00e\x00t\x00e\x00d\x00/\x00s\x00e\x00c\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00S\x00u\x00s\x00p\x00e\x00n\x00d\x00e\x00d\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00S\x00u\x00s\x00p\x00e\x00n\x00d\x00e\x00d\x00/\x00s\x00e\x00c\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00T\x00e\x00r\x00m\x00i\x00n\x00a\x00t\x00e\x00d\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00T\x00e\x00r\x00m\x00i\x00n\x00a\x00t\x00e\x00d\x00/\x00s\x00e\x00c\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00I\x00n\x00 \x00M\x00e\x00m\x00o\x00r\x00y\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00A\x00b\x00o\x00r\x00t\x00e\x00d\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00A\x00b\x00o\x00r\x00t\x00e\x00d\x00/\x00s\x00e\x00c\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00P\x00e\x00r\x00s\x00i\x00s\x00t\x00e\x00d\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00P\x00e\x00r\x00s\x00i\x00s\x00t\x00e\x00d\x00/\x00s\x00e\x00c\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00E\x00x\x00e\x00c\x00u\x00t\x00i\x00n\x00g\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00I\x00d\x00l\x00e\x00/\x00s\x00e\x00c\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00R\x00u\x00n\x00n\x00a\x00b\x00l\x00e\x00\x00\x00W\x00o\x00r\x00k\x00f\x00l\x00o\x00w\x00s\x00 \x00P\x00e\x00n\x00d\x00i\x00n\x00g\x00\x00\x00\x00\x00', 'Counter Types': b'6\x005\x005\x003\x006\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x006\x005\x005\x003\x006\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x006\x005\x005\x003\x006\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x006\x005\x005\x003\x006\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x006\x005\x005\x003\x006\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x006\x005\x005\x003\x006\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x006\x005\x005\x003\x006\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x006\x005\x005\x003\x006\x00\x00\x002\x007\x002\x006\x009\x006\x003\x002\x000\x00\x00\x006\x005\x005\x003\x006\x00\x00\x006\x005\x005\x003\x006\x00\x00\x00\x00\x00', 'IsMultiInstance': 1, 'Library': '%systemroot%\\system32\\NETFXPerf.dll', 'Open': 'OpenPerformanceData', 'InstallType': 1, 'PerfIniFile': 'PerfCounters_d.ini', 'First Counter': 9090, 'Last Counter': 9132, 'First Help': 9091, 'Last Help': 9133, 'Object List': '9090'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WindowsTrustedRT Service </span>

|DisplayName|ErrorControl|Group|ImagePath|Start|Tag|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`Windows Trusted Execution Environment Class Extension`|`SERVICE_ERROR_CRITICAL`|`Core Security Extensions`|`system32\drivers\WindowsTrustedRT.sys`|`SERVICE_BOOT_START`|`0x01`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WindowsTrustedRTProxy Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`System32\drivers\WindowsTrustedRTProxy.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_BOOT_START`|`SERVICE_ERROR_NORMAL`|`Core Security Extensions`|`0x02`|`@WindowsTrustedRTProxy.inf,%WindowsTrustedRTProxy.SVCDESC%;Microsoft Windows Trusted Runtime Secure Service`|`WindowsTrustedRTProxy.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WinHttpAutoProxySvc Service </span>



##### Service Parameters
  
ProxyDllFile : `%SystemRoot%\system32\jsproxy.dll`  
ServiceDll : `%SystemRoot%\system32\winhttp.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `WinHttpAutoProxySvcMain`  
<br></br>  
Security : 
```
Owner: S-1-0-18
Group: S-1-0-18
DACL:
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x3009d
    SID: S-1-0-18
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x3009d
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2009d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x94
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x94
    SID: S-1-0-3-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x94
    SID: S-1-0-3-2
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x94
    SID: S-1-0-3-3
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0x3009d
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WinMad Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|BootFlags|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\winmad.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`PNP Filter`|`0x04`|`winverbs`|`@mlx4_bus.inf,%WinMad.ServiceDesc%;WinMad Service`|`mlx4_bus.inf`|`0x01`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Winmgmt Service </span>



##### Service Parameters
  
LegacyCOMBehavior : `0x01`  
ServiceDll : `%SystemRoot%\system32\wbem\WMIsvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WinNat Service </span>
  
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
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WinRM Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\WsmSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Winsock Service </span>

|Setup Migration|
| :---: |
|`Setup Migration`|



##### Service Parameters
  
Transports : `54 00 63 00 70 00 69 00 70 00 00 00 54 00 63 00 70 00 69 00 70 00 36 00 00 00 61 00 66 00 75 00 6e 00 69 00 78 00 00 00 50 00 73 00 63 00 68 00 65 00 64 00 00 00 76 00 6d 00 62 00 75 00 73 00 00 00 52 00 46 00 43 00 4f 00 4d 00 4d 00 00 00 00 00`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WinSock2 Service </span>



##### Service Parameters
  
AppId_Catalog : `AppId_Catalog`  
NameSpace_Catalog5 : `NameSpace_Catalog5`  
Protocol_Catalog9 : `Protocol_Catalog9`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WINUSB Service </span>

|ImagePath|Type|Start|ErrorControl|DisplayName|Description|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\WinUSB.SYS`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`@winusb.inf,%WINUSB_SvcName%;WinUsb Driver`|`@winusb.inf,%WINUSB_SvcDesc%;Generic driver for USB devices`|`winusb.inftransfercable.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WinVerbs Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DependOnService|DisplayName|Owners|BootFlags|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\winverbs.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`PNP Filter`|`0x03`|`ibbus`|`@mlx4_bus.inf,%WinVerbs.ServiceDesc%;WinVerbs Service`|`mlx4_bus.inf`|`0x01`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wisvc Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\flightsettings.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 2b 02 92 0f`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WlanSvc Service </span>

|VirtualizationManager|
| :---: |
|`{'WindowsPushNotificationPlatformClsid': '0C9281F9-6DA1-4006-8729-DE6E6B61581C'}`|



##### Service Parameters
  
ComInterfaceProviders : `{'IHNetIcsSettings': '{46C166AA-3108-11D4-9348-00C04F8EEB71}'}`  
EapolKeyIpAddress : `{'LocalAddress': '192.168.137.1', 'PrefixLength': 24}`  
OEM : `OEM`  
OneXAuthenticator : `{'(Default)': '%SystemRoot%\\System32\\WcnEapAuthProxy.dll'}`  
VendorSpecificIEProviders : `VendorSpecificIEProviders`  
WfdInterfaceManagement : `{'DisablePhyTypeRestriction': 0, 'DisableSetActiveWfdMgrSidCheck': 0}`  
WFDProvPlugin : `{'(Default)': '%SystemRoot%\\System32\\wfdprov.dll', 'DllEntryPoint': 'WFDProvGetInfo'}`  
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
    Access: 0x70
    SID: S-1-0-80-3906544942-1489856346-3706913989-164347954-1900376235

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wlidsvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\wlidsvc.dll`  
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
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-6

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`43 00 43 00 31 00 30 00 35 00 36 00 31 00 30 00 2d 00 44 00 41 00 30 00 33 00 2d 00 34 00 36 00 37 00 45 00 2d 00 42 00 43 00 37 00 33 00 2d 00 35 00 42 00 39 00 45 00 32 00 39 00 33 00 37 00 34 00 35 00 38 00 44 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`46 00 41 00 46 00 32 00 34 00 34 00 37 00 42 00 2d 00 42 00 33 00 34 00 38 00 2d 00 34 00 46 00 45 00 42 00 2d 00 38 00 44 00 42 00 45 00 2d 00 42 00 45 00 45 00 45 00 35 00 42 00 37 00 46 00 37 00 37 00 37 00 38 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 18 bc a3 21 07 85 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 21 07 85 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 30 bc a3 21 07 85 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 20 bc a3 20 1d 87 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wlpasvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\lpasvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `LpaSvcMain`  
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
    Access: 0x201fd
    SID: S-1-0-19
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-2-155514346-2573954481-755741238-1654018636-1233331829-3075935687-2861478708
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-2-3083765670-2301828090-3288705196-2597965991-2057664196-4044987863-2761340229
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2008d
    SID: S-1-0-2-3784866113-3187381476-3433752343-3391928953-3760210436-1684329488-1912184601

```


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 10 bc a3 3a 19 87 0f`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`34 00 66 00 34 00 66 00 61 00 37 00 38 00 36 00 2d 00 32 00 66 00 38 00 66 00 2d 00 34 00 39 00 65 00 38 00 2d 00 38 00 61 00 61 00 65 00 2d 00 36 00 36 00 36 00 39 00 66 00 65 00 62 00 64 00 35 00 64 00 31 00 64 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WManSvc Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\Windows.Management.Service.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WmiAcpi Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\wmiacpi.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Extended Base`|`0x24`|`@wmiacpi.inf,%WMIMAP.SvcDesc%;Microsoft Windows Management Interface for ACPI`|`wmiacpi.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WmiApRpl Service </span>

|Performance|
| :---: |
|`{'Close': 'WmiClosePerfData', 'Collect': 'WmiCollectPerfData', 'Library': '%systemroot%\\system32\\wbem\\wmiaprpl.dll', 'Open': 'WmiOpenPerfData', 'PerfIniFile': 'WmiApRpl.ini'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wmiApSrv Service </span>

|Description|DisplayName|ErrorControl|FailureActions|ImagePath|ObjectName|ServiceSidType|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%Systemroot%\system32\wbem\wmiapsrv.exe,-111`|`@%Systemroot%\system32\wbem\wmiapsrv.exe,-110`|`SERVICE_ERROR_NORMAL`|`84 03 00 00 00 00 00 00 00 00 00 00 03 00 00 00 14 00 00 00 01 00 00 00 c0 d4 01 00 01 00 00 00 e0 93 04 00 00 00 00 00 00 00 00 00`|`%systemroot%\system32\wbem\WmiApSrv.exe`|`localSystem`|`SERVICE_SID_TYPE_UNRESTRICTED`|`SERVICE_DEMAND_START`|`SERVICE_WIN32_OWN_PROCESS`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WMPNetworkSvc Service </span>
  
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
    Access: 0x2019d
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x2018d
    SID: S-1-0-6
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">Wof Service </span>

|Instances|
| :---: |
|`Instances`|



##### Service Parameters
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">workerdd Service </span>

|Device0|
| :---: |
|`{'InstalledDisplayDrivers': b'W\x00O\x00R\x00K\x00E\x00R\x00D\x00D\x00\x00\x00\x00\x00', 'VgaCompatible': 0}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">workfolderssvc Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\workfolderssvc.dll`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WpcMonSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\WpcDesktopMonSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `ServiceMain`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WPDBusEnum Service </span>

|BthActiveConnect|
| :---: |
|`{'ACInterval': 120, 'DCInterval': 240}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\wpdbusenum.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`0763f553-bfb6-d011-94f2-00a0c91efb8b`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|1|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`6dbce9c1-ae1d-1a42-9369-cc7ff0d6e359`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|10|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 a0 be a3 28 00 92 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|11|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 a8 be a3 28 00 92 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|2|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`7878c26a-faa6-5541-ba85-f98f491d4f33`|`SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL`|||
|3|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 18 bc a3 28 00 92 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|4|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 70 be a3 28 00 92 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|5|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`e6ca9f65-db5b-a94d-b1ff-ca2a178d46e0`|`SERVICE_TRIGGER_TYPE_GROUP_POLICY`|||
|6|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`c846fb54-89f0-4c46-b1fd-59d1b62c3b50`|`SERVICE_TRIGGER_TYPE_GROUP_POLICY`|||
|7|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`37e09f19-822b-a940-82ac-e1d46c792b99`|`SERVICE_TRIGGER_TYPE_CUSTOM`|`01 00 00 00 00 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_KEYWORD_ANY`|
|8|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 90 be a3 28 00 92 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
|9|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 98 be a3 28 00 92 13`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WpdUpFltr Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%systemroot%\System32\drivers\WpdUpFltr.sys,-100`|`@%systemroot%\System32\drivers\WpdUpFltr.sys,-100`|`SERVICE_ERROR_NORMAL`|`PnP Filter`|`System32\drivers\WpdUpFltr.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WpnService Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\WpnService.dll`  
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

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WpnUserService Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\WpnUserService.dll`  
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
    SID: S-1-0-6
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-4
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-11
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x201fd
    SID: S-1-0-2-1
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0xf01ff
    SID: S-1-0-32-544

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">ws2ifsl Service </span>



##### Service Parameters
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wscsvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wscsvc.dll`  
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
    Access: 0x2019d
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
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x15
    SID: S-1-0-80-2006800713-1441093265-249754844-3404434343-1444102779
SACL:
  ACE:
    Type:  SYSTEM_AUDIT_ACE
    Flags: 0x80
    Access: 0xf01ff
    SID: S-1-0-0(NULL)

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WSearch Service </span>
  
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
    Access: 0x2008d
    SID: S-1-0-3-1024-724741592-1210917904-489960769-637019204-3345707629-3097053430-1727148295-85063603

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WSearchIdxPi Service </span>

|Performance|
| :---: |
|`{'Close': 'PerfmonIDXClose', 'Collect': 'PerfmonIDXCollect', 'Library': '%systemroot%\\system32\\tquery.dll', 'Open': 'PerfmonIDXOpen', 'InstallType': 1, 'PerfIniFile': 'idxcntrs.ini', 'First Counter': 9312, 'Last Counter': 9438, 'First Help': 9313, 'Last Help': 9439, 'Object List': '9312'}`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">wuauserv Service </span>



##### Service Parameters
  
ServiceDll : `%systemroot%\system32\wuaueng.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `WUServiceMain`  
<br></br>  
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
    Access: 0xf01ff
    SID: S-1-0-32-544
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
#### <span style="text-align: center; font-size:2em;">WudfPf Service </span>

|Description|DisplayName|ErrorControl|Group|ImagePath|Start|Type|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`@%systemroot%\system32\drivers\Wudfpf.sys,-1001`|`@%SystemRoot%\system32\drivers\Wudfpf.sys,-1000`|`SERVICE_ERROR_NORMAL`|`base`|`system32\drivers\WudfPf.sys`|`SERVICE_DEMAND_START`|`SERVICE_KERNEL_DRIVER`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WUDFRd Service </span>

|ImagePath|Type|Start|ErrorControl|Owners|DisplayName|ObjectName|Group|Tag|Description|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\WUDFRd.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`HidTelephonyDriver.infhidbthle.infrdpidd.infehstorpwddrv.infxinputhid.infstorfwupdate.infhidcfu.infSDFLauncher.infuiccspb.inf`|`@%SystemRoot%\system32\drivers\WudfRd.sys,-1000`|`\Driver\WudfRd`|`base`|`0x0d`|`@%systemroot%\system32\drivers\WudfRd.sys,-1001`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">WwanSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\wwansvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceMain : `WwanSvcMain`  
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
    Access: 0x95
    SID: S-1-0-19
  ACE:
    Type:  ACCESS_ALLOWED_ACE
    Flags: 0x00
    Access: 0x04
    SID: S-1-0-2-1

```  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">XblAuthManager Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\XblAuthManager.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">XblGameSave Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\XblGameSave.dll`  
ServiceDllUnloadOnStop : `0x01`  
ServiceIdleTimeout : `0x258`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`67d190bc-7094-3941-a9ba-be0bbbf5b74d`|`SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT`|`46 00 36 00 43 00 39 00 38 00 37 00 30 00 38 00 2d 00 43 00 37 00 42 00 38 00 2d 00 34 00 39 00 31 00 39 00 2d 00 38 00 38 00 37 00 43 00 2d 00 32 00 43 00 45 00 36 00 36 00 45 00 37 00 38 00 42 00 39 00 41 00 30 00 00 00`|`SERVICE_TRIGGER_DATA_TYPE_STRING`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">xboxgip Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Description|Owners|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\xboxgip.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`NDIS`|`0x01`|`@xboxgip.inf,%XBOXGIP_Desc%;Xbox Game Input Protocol Driver`|`@xboxgip.inf,%XBOXGIP_Desc%;Xbox Game Input Protocol Driver`|`xboxgip.inf`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">XboxGipSvc Service </span>

|CoExAdapters|
| :---: |
|`{'PCI\\VEN_8086&DEV_24FD': 1}`|



##### Service Parameters
  
ServiceDll : `%SystemRoot%\System32\XboxGipSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>


##### Service Triggers

|ID|Action|GUID|Type|Data0|DataType0|
| :---: | :---: | :---: | :---: | :---: | :---: |
|0|`SERVICE_TRIGGER_ACTION_SERVICE_START`|`16287a2d-5e0c-fc45-9ce7-570e5ecde9c9`|`SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE`|`75 08 bc a3 2a 07 96 41`|`SERVICE_TRIGGER_DATA_TYPE_BINARY`|
  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">XboxNetApiSvc Service </span>



##### Service Parameters
  
ServiceDll : `%SystemRoot%\system32\XboxNetApiSvc.dll`  
ServiceDllUnloadOnStop : `0x01`  
<br></br>  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">xinputhid Service </span>

|ImagePath|Type|Start|ErrorControl|Group|Tag|DisplayName|Owners|DevicePropertyFlags|ConfigFlags|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|`\SystemRoot\System32\drivers\xinputhid.sys`|`SERVICE_KERNEL_DRIVER`|`SERVICE_DEMAND_START`|`SERVICE_ERROR_NORMAL`|`Base`|`0x01`|`@xinputhid.inf,%xinputhid.SvcDesc%;XINPUT HID Filter Driver`|`xinputhid.inf`|`0x0e`|`0x01`|
  

---
<br></br>
#### <span style="text-align: center; font-size:2em;">xmlprov Service </span>



##### Service Parameters
  
SchemaGroups : `SchemaGroups`  
<br></br>  

---
<br></br>  
<br></br>