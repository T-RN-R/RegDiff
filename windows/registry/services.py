from windows.registry import Factory
from windows.sd import SECURITY_DESCRIPTOR_RELATIVE
from windows.ipfw import FirewallRuleString
import struct
import uuid
SERVICE_SID_TYPES = {
    0: "SERVICE_SID_TYPE_NONE",
    1: "SERVICE_SID_TYPE_UNRESTRICTED",
    3: "SERVICE_SID_TYPE_RESTRICTED",
}
SERVICE_START_TYPE = {
    0: "SERVICE_BOOT_START",
    1: "SERVICE_SYSTEM_START",
    2: "SERVICE_AUTO_START",
    3: "SERVICE_DEMAND_START",
    4: "SERVICE_DISABLED"
}
SERVICE_ERROR_CONTROL_TYPES = {
    0: "SERVICE_ERROR_IGNORE",
    1: "SERVICE_ERROR_NORMAL",
    2: "SERVICE_ERROR_SEVERE",
    3: "SERVICE_ERROR_CRITICAL"
}
SERVICE_TYPE_TYPES = {
    0x1: "SERVICE_KERNEL_DRIVER",
    0x2: "SERVICE_FILE_SYSTEM_DRIVER",
    0x4: "SERVICE_ADAPTER",
    0x8: "SERVICE_RECOGNIZER_DRIVER",
    0x10: "SERVICE_WIN32_OWN_PROCESS",
    0x20: "SERVICE_WIN32_SHARE_PROCESS",
    0x40: "SERVICE_USER_SERVICE",
    0x80: "SERVICE_USERSERVICE_INSTANCE",
    0x100: "SERVICE_INTERACTIVE_PROCESS",
    0x200: "SERVICE_PKG_SERVICE",
    0x1 | 0x2 | 0x4 | 0x8: "SERVICE_DRIVER",
    0x10 | 0x20: "SERVICE_WIN32"
}
SERVICE_TRIGGER_TYPES = {
    1: "SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL",
    2: "SERVICE_TRIGGER_TYPE_IP_ADDRESS_AVAILABILITY",
    3: "SERVICE_TRIGGER_TYPE_DOMAIN_JOIN",
    4: "SERVICE_TRIGGER_TYPE_FIREWALL_PORT_EVENT",
    5: "SERVICE_TRIGGER_TYPE_GROUP_POLICY",
    6: "SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT",
    7: "SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE",
    20: "SERVICE_TRIGGER_TYPE_CUSTOM",
    30: "SERVICE_TRIGGER_TYPE_AGGREGATE"
}

SERVICE_TRIGGER_ACTION_TYPES = {
    1: "SERVICE_TRIGGER_ACTION_SERVICE_START",
    2: "SERVICE_TRIGGER_ACTION_SERVICE_STOP"
}


SERVICE_TRIGGER_GUIDS = {
    "1ce20aba-9851-4421-9430-1ddeb766e809": "DOMAIN_JOIN_GUID",
    "ddaf516e-58c2-4866-9574-c3b615d42ea1": "DOMAIN_LEAVE_GUID",
    "b7569e07-8421-4ee0-ad10-86915afdad09": "FIREWALL_PORT_OPEN_GUID",
    "a144ed38-8e12-4de4-9d96-e64740b1a524": "FIREWALL_PORT_CLOSE_GUID",
    "659fcae6-5bdb-4da9-b1ff-ca2a178d46e0": "MACHINE_POLICY_PRESENT_GUID",
    "4f27f2de-14e2-430b-a549-7cd48cbc8245": "NETWORK_MANAGER_FIRST_IP_ADDRESS_ARRIVAL_GUID",
    "cc4ba62a-162e-4648-847a-b6bdf993e335": "NETWORK_MANAGER_LAST_IP_ADDRESS_REMOVAL_GUID",
    "54fb46c8-f089-464c-b1fd-59d1b62c3b50": "USER_POLICY_PRESENT_GUID",
    "bc90d167-9470-4139-a9ba-be0bbbf5b74d": "RPC_INTERFACE_EVENT_GUID",
    "1f81d131-3fac-4537-9e0c-7e7b0c2f4b55": "NAMED_PIPE_EVENT_GUID",

}

SERVICE_TRIGGER_DATA_TYPES = {
    1:  "SERVICE_TRIGGER_DATA_TYPE_BINARY",
    2:  "SERVICE_TRIGGER_DATA_TYPE_STRING",
    3: "SERVICE_TRIGGER_DATA_TYPE_LEVEL",
    4: "SERVICE_TRIGGER_DATA_TYPE_KEYWORD_ANY",
    5: "SERVICE_TRIGGER_DATA_TYPE_KEYWORD_ALL"
}


class SystemHiveDataClass():
    def __init__(self, data):
        self._data = data


class SystemHiveSeviceSummaryEntry(SystemHiveDataClass):
    def __init__(self, name, generic_value):
        self._name = name
        self._value = generic_value
    @property
    def name(self):
        return self._name 
    @property
    def value(self):
        return self._value 
    
    @value.setter
    def value(self, val):
        self._value = val
    
class SystemHiveServiceSummaryRequiredPrivilegesEntry(SystemHiveSeviceSummaryEntry):
    def __init__(self, name, value):
        super(SystemHiveServiceSummaryRequiredPrivilegesEntry, self).__init__(name, value)
        self.value = self._convert_privilege_bytes_to_string(value)

    def _convert_privilege_bytes_to_string(self, privilege_bytes: bytes, encoding: str = "utf-16") -> str:
        return privilege_bytes.decode(encoding).strip().split("\x00")[:-2]

class SystemHiveServiceSummaryServiceSidTypeEntry(SystemHiveSeviceSummaryEntry):
    def __init__(self, name, value):
        super(SystemHiveServiceSummaryServiceSidTypeEntry, self).__init__(name, value)
        self.value = SERVICE_SID_TYPES.get(value,value)

class SystemHiveServiceSummaryTypeEntry(SystemHiveSeviceSummaryEntry):
    def __init__(self, name, value):
        super(SystemHiveServiceSummaryTypeEntry, self).__init__(name, value)
        self.value = SERVICE_TYPE_TYPES.get(value,value)


class SystemHiveServiceSummaryStartEntry(SystemHiveSeviceSummaryEntry):
    def __init__(self, name, value):
        super(SystemHiveServiceSummaryStartEntry, self).__init__(name, value)
        self.value = SERVICE_START_TYPE.get(value,value)

class SystemHiveServiceSummaryErrorControlEntry(SystemHiveSeviceSummaryEntry):
    def __init__(self, name, value):
        super(SystemHiveServiceSummaryErrorControlEntry, self).__init__(name, value)
        self.value = SERVICE_ERROR_CONTROL_TYPES.get(value,value)

class SystemHiveServiceSummaryOwnersEntry(SystemHiveSeviceSummaryEntry):
    def __init__(self, name, value:bytes):
        super(SystemHiveServiceSummaryOwnersEntry, self).__init__(name, value)
        self.value = value.decode("utf-16").strip().replace("\x00", "")

class SystemHiveServiceSummaryDependOnServiceEntry(SystemHiveSeviceSummaryEntry):
    def __init__(self, name, value:bytes):
        super(SystemHiveServiceSummaryDependOnServiceEntry, self).__init__(name, value)
        self.value = value.decode("utf-16").strip().replace("\x00", "")

class SystemHiveServiceSummaryDefaultsEntry(SystemHiveSeviceSummaryEntry):
    def __init__(self, name, value:dict):
        super(SystemHiveServiceSummaryDefaultsEntry, self).__init__(name, value)
        if "FirewallPolicy" in value:
            self.value = SystemHiveServiceFirewallPolicy(value.get("FirewallPolicy"))
        
class SystemHiveSummaryEntryFactory(Factory):
    CONSTRUCTION_MAP = {"RequiredPrivileges":SystemHiveServiceSummaryRequiredPrivilegesEntry,
                        "ServiceSidType":SystemHiveServiceSummaryServiceSidTypeEntry,
                         "Type": SystemHiveServiceSummaryTypeEntry,
                         "ErrorControl":SystemHiveServiceSummaryErrorControlEntry,
                         "DependOnService":SystemHiveServiceSummaryDependOnServiceEntry,
                         "Owners":SystemHiveServiceSummaryOwnersEntry,
                         "Defaults":SystemHiveServiceSummaryDefaultsEntry
                         }
    def construct(self, name, value)->SystemHiveSeviceSummaryEntry:
        func =  __class__.CONSTRUCTION_MAP.get(name, SystemHiveSeviceSummaryEntry)
        return func(name,value)

        


class SystemHiveServiceSummary(SystemHiveDataClass):
    def __init__(self, summary: dict, fields_to_ignore: list):
        self._entries = [SystemHiveSummaryEntryFactory().construct(k, v) for k, v in summary.items()
                      if k not in fields_to_ignore]
        self._fields_to_ignore = fields_to_ignore

    @property
    def entries(self)->list[SystemHiveSeviceSummaryEntry]:
        return self._entries



class SystemHiveServiceParameter(SystemHiveDataClass):
    class Persistent():
        def __init__(self, data):
            self._data = data

    def __init__(self, name, value):
        self._name = name
        if self.name == "Persistent":
            self._value = __class__.Persistent(value)
        else:
            self._value = value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value


class SystemHiveServicePolicyParameter(SystemHiveDataClass):
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value

    def keys(self):
        return self.value.keys()

    def values(self):
        return self.value.values()

    def items(self):
        return self.value.items()


class SystemHiveServiceParameterFactory(Factory):
    def construct(self, name, value) -> SystemHiveDataClass:
        if name.lower() == "policy":
            return SystemHiveServicePolicyParameter(value)
        elif name.lower() == "firewallpolicy":
            return SystemHiveServiceFirewallPolicy(value)
        else:
            return SystemHiveServiceParameter(name, value)

class SystemHiveServiceTriggerDataEntry(SystemHiveDataClass):
    def __init__(self, _type, data):
        self._type = SERVICE_TRIGGER_DATA_TYPES.get(_type, _type)
        if _type == 1:
            self._data =  data
        elif _type ==2:
            self._data = data.decode("utf-16").strip().replace("\x00", "")
        elif _type ==3:
            self._data = struct.unpack("<B", data)
        elif _type == 4 or _type == 5:
            self._data = struct.unpack("<Q", data)
        else:
            raise Exception(f"Unknown data type: {_type}")

    @property
    def value(self):
        return self._data
class SystemHiveServiceTriggerData(SystemHiveDataClass):
    def __init__(self, items:dict):
        data_types = []
        data = []
        for name, item in items.items():
            if "DataType" in name:
                idx = int(name.split("DataType",1)[1])
                data_types.insert(idx, item)
            elif "Data" in name:
                idx = int(name.split("Data",1)[1])
                data.insert(idx, item)
            else:
                raise Exception("Unreachable")
        
        self._item_arr = [SystemHiveServiceTriggerDataEntry(data_types[i], data[i]) for i in range(0, len(data))]
    @property
    def trigger_data(self):
        return self._item_arr


class SystemHiveServiceTriggerFields(SystemHiveDataClass):
    def __init__(self, fields:dict):
        self._entries = {}
        for k, v in fields.items():
            if k == "Type":
                v = SERVICE_TRIGGER_TYPES.get(v, v)
            elif k == "GUID":
                g = str(uuid.UUID(bytes=v))
                # TODO GUID bytes to GUID string
                v = SERVICE_TRIGGER_GUIDS.get(g, g)
            elif k == "Action":
                v = SERVICE_TRIGGER_ACTION_TYPES.get(v, v)
            self._entries[k] = v

    @property
    def entries(self):
        return self._entries

class SystemHiveServiceTriggerInfo(SystemHiveDataClass):
    def __init__(self, ordinal, trigger):
        self._ordinal = ordinal
        d = {k:v for k, v in trigger.items() if "Data" in k} 
        self._parameters = SystemHiveServiceTriggerData(d)
        self._trigger_data = SystemHiveServiceTriggerFields({k:v for k,v in trigger.items() if "Data" not in k})

    @property
    def trigger_data(self):
        return self._trigger_data
    @property
    def parameters(self):
        return self._parameters
    @property
    def ordinal(self):
        return self._ordinal

    def keys(self):
        return self.trigger.keys()

    def values(self):
        return self.trigger.values()

    def items(self):
        return self.trigger.items()


class SystemHiveServiceMethod(SystemHiveDataClass):
    def __init__(self, method):
        self._method = method

class SystemHiveServiceFirewallRule:
    def __init__(self, name, rule_str):
        self._name = name
        self._rule = FirewallRuleString(rule_str).parse()

    @property
    def rule_data(self):
        return self._rule

    @property
    def name(self):
        return self._name
    
class SystemHiveServiceFirewallRestrictedServices:
    def __init__(self, name, data):
        """
        If any of these exceptions are trggered, this is going to need to be rewritten as a Factory.
        """
        if name != "Static":
            raise Exception(f" Found a new Restricted Firewall Rule type ('{name}')! Please implement me!")
        if data.get("System") is None:
            raise Exception(f" Found a new Static Restricted Firewall Rule type ('{data.keys()}')! Please implement me!")
        self._name = name
        self._data = data.get("System", {})
    @property
    def name(self):
        return self._name
    @property
    def firewall_rules(self):
        return [SystemHiveServiceFirewallRule(name, rule) for name, rule in self._data.items()]

class SystemHiveServiceFirewallPolicy(SystemHiveDataClass):
    def __init__(self, policy):
        self._policy = policy

    @property
    def firewall_rules(self):
        return [SystemHiveServiceFirewallRule(name, rule) for name, rule in self._policy.get("FirewallRules", {}).items()]

    @property
    def restricted_services(self):
        return [SystemHiveServiceFirewallRestrictedServices(name, rule) for name, rule in self._policy.get("RestrictedServices", {}).items()]


class SystemHiveServiceSecurity(SystemHiveDataClass):
    def __init__(self, sd: bytes):
        self._sd = SECURITY_DESCRIPTOR_RELATIVE(sd, 0, None)

    @property
    def sd(self):
        return self._sd

    def __str__(self):
        return self.sd.pretty_string()


class SystemHiveService(SystemHiveDataClass):
    SPECIAL_FIELDS = ["Parameters", "TriggerInfo",
                      "Security", "Methods", "FirewallPolicy"]

    def __init__(self, name, data: dict):
        self._name = name
        self._parameters = [SystemHiveServiceParameterFactory().construct(param_name, param_value)
                            for param_name, param_value in data.get("Parameters", {}).items()
                            ]
        self._trigger_info = [SystemHiveServiceTriggerInfo(ordinal, trigger)
                              for ordinal, trigger in data.get("TriggerInfo", {}).items()
                              ]
        sd = data.get("Security", {"Security": b''}).get("Security", None)
        self._security = SystemHiveServiceSecurity(
            sd) if sd is not None and isinstance(sd, bytes) and len(sd) > 0 else None

        self._methods = [SystemHiveServiceMethod(method)
                         for method in data.get("Methods", [])
                         ]
        fp = data.get("FirewallPolicy", None)
        self._firewall_policy = SystemHiveServiceFirewallPolicy(
            fp) if fp is not None else None

        self._summary = SystemHiveServiceSummary(
            data, SystemHiveService.SPECIAL_FIELDS)

    @property
    def name(self):
        return self._name

    @property
    def summary(self):
        return self._summary

    @property
    def parameters(self):
        return self._parameters

    @property
    def trigger_info(self):
        return self._trigger_info

    @property
    def security(self):
        return self._security

    @property
    def methods(self):
        return self._methods

    @property
    def firewall_policy(self):
        return self._firewall_policy


class SystemHiveServices(SystemHiveDataClass):
    def __init__(self, services):
        self._services = [SystemHiveService(name, service)
                          for name, service in services.items()
                          ]

    @property
    def services(self) -> SystemHiveService:
        return self._services
