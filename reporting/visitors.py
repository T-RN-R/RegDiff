from reporting import *
from reporting.system import *
from windows.sd import get_sid_string
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


class CoreReportMarkdownVisitor(MarkdownVisitor):
    def get_markdown(self, md: MdUtils, data: list) -> MdUtils:
        self.md = md
        for container in data:
            #self.md.new_line("\n<details>\n")
            self.handle_container(container)
            #self.md.new_line("\n</details>\n")

        return md

    def get_printable_value(self, field):
        if isinstance(field, bytes):
            return field.hex(sep=" ")
        elif isinstance(field, int):
            return '0x{:02x}'.format(field)
        else:
            return str(field)
    def emphasize_text(self, text:str) -> str:
        return f"<span style=\"text-align: center; font-size:2em;\">{text} </span>"
    def handle_container(self, container: DiffContainer):
        assert isinstance(container, DiffContainer), "Did not pass a DiffContainer to handle_container"
        if isinstance(container, AddedContainer):
            self.md.new_line("<br></br><br></br>Added")

            #self.md.new_line("<summary> Added </summary>")
            self.handle_raw(container.data)
        elif isinstance(container, RemovedContainer):
            self.md.new_line("<br></br><br></br>Deleted")
            #self.md.new_line("<summary> Removed </summary>")
            self.handle_raw(container.data)
        elif isinstance(container, DiffContainer):
            self.handle_raw(container.data)
        else:
            raise Exception(f"Unhandled Container: {type(container)}")

    def handle_raw(self, visitable_list:list[MarkdownVisitable]):
        assert isinstance(visitable_list, list), "Did not pass a list to handle_raw!"
        for entry in visitable_list:
            assert isinstance(entry, MarkdownVisitable)
            if isinstance(entry, RegAutoLogger):
                self.handle_system_auto_logger(entry)
            elif isinstance(entry, RegServices):
                self.handle_system_services(entry)
            else:
                raise Exception(f"Unhandled visitable: {type(entry)}")
            self.md.new_line("<br></br>")

    def convert_privilege_bytes_to_string(self, privilege_bytes: bytes, encoding: str = "utf-16") -> str:
        return privilege_bytes.decode(encoding).strip().split("\x00")[:-2]

    def utf8_bytes_to_str(self, data: bytes) -> str:
        return data.decode("utf-16").strip().replace("\x00", "")

    def handle_system_auto_logger(self, entry: RegAutoLogger):
        self.md.new_header(3, "WMI AutoLoggers")
        self.md.new_line("\n---\n<br></br>")

        al = entry.data
        for k, v in al.items():
            self.md.new_header(4, k)
            known_keys = set()
            known_keys.add("guid")
            for _, values in v.items():
                if isinstance(values, dict):
                    for kk in values:
                        known_keys.add(kk)
                else:
                    self.md.new_line(
                        f"{_} : `{self.get_printable_value(values)}`")

            known_keys = list(known_keys)
            known_keys.sort()
            data = list()

            for guid, values in v.items():
                init_dict = {key: None for key in known_keys}
                for key in known_keys:
                    if not isinstance(values, dict):
                        break
                    value = values.get(key, None)
                    init_dict[key] = self.get_printable_value(value)
                init_dict["guid"] = self.get_printable_value(guid)
                data.append(init_dict)
            d = []
            for e in data:
                for k, val in e.items():
                    d.append(val)

            self.md.new_table(
                len(known_keys), (len(v.keys()) + 1), known_keys+d)
            self.md.new_line("\n---\n<br></br>")

    def handle_system_services(self, entry: RegServices):
        self.md.new_header(3, self.emphasize_text("Services"))
        self.md.new_line("\n---\n<br></br>")
        services = entry.data
        for service_name, service_data in services.items():
            self.handle_single_service(service_name, service_data)

    def handle_single_service(self, service_name: str, service_data: dict):
        self.md.new_header(4, self.emphasize_text(f"{service_name} Service"))
        table_column_headers = []
        table_row = []
        custom_view_headings = ["parameters", "triggerinfo", "security", "methods"]

        # loop to generate summary table
        for k, v in service_data.items():
            if k.lower() in custom_view_headings or v is None:
                continue

            table_column_headers.append(k)
            if k == "RequiredPrivileges":
                v = f"`{self.get_printable_value(self.convert_privilege_bytes_to_string(v))}`"
            elif k == "ServiceSidType":
                v = f"`{SERVICE_SID_TYPES.get(v,v)}`"
            elif k == "Type":
                v = f"`{SERVICE_TYPE_TYPES.get(v,v)}`"
            elif k == "Start":
                v = f"`{SERVICE_START_TYPE.get(v,v)}`"
            elif k == "ErrorControl":
                v = f"`{SERVICE_ERROR_CONTROL_TYPES.get(v,v)}`"
            elif k == "DependOnService":
                v = f"`{self.utf8_bytes_to_str(v)}`"
            elif k == "Owners":
                v = f"`{self.utf8_bytes_to_str(v)}`"
            elif v != None:
                v = f"`{self.get_printable_value(v)}`"
            table_row.append(v)
        if len(table_column_headers) != 0:
            # sometimes we don't have a table to show!
            self.md.new_table(len(table_column_headers), 2, table_column_headers+table_row)
        # non-table information
        for k, v, in service_data.items():
            if k.lower() == "Parameters".lower():
                self.md.new_paragraph()
                self.handle_service_parameters(v)
                self.md.new_line("<br></br>")
            elif k == "TriggerInfo":
                self.md.new_paragraph()
                self.handle_trigger_infos(v)
                self.md.new_line("<br></br>")

            elif k == "Security":
                sec = v.get("Security", b'')
                if sec is None:
                    continue
                if not isinstance(sec, bytes):
                    continue
                if len(sec)==0:
                    continue
                self.md.new_line(f"{k} : \n```\n{self.get_printable_value(get_sid_string(sec))}\n```")
            elif k =="Methods":
                self.md.new_line(f"{k} : `{self.get_printable_value(v)}`")
            # elif k == "Defaults"

        self.md.new_line("\n---\n<br></br>")

    def handle_service_parameters(self, parameters):
        self.md.new_header(5, "Service Parameters")
        for param_name, value in parameters.items():
            if param_name == "Policy":
                self.handle_service_parameters_policy(value)
            else:
                self.md.new_line(
                    f"{param_name} : `{self.get_printable_value(value)}`")

    def handle_service_parameters_policy(self, policy: dict):
        self.md.new_line("Policy")
        for k, v in policy.items():
            if k == "Persistent":
                self.md.new_line("Persistent")
                for kk, vv in v.items():
                    if isinstance(vv, dict):
                        l = []
                        self.md.new_line(f"{kk}")
                        for kkk, vvv in vv.items():
                            l.append(kkk)
                            l.append(f"`{self.get_printable_value(vvv)}`")
                        self.md.new_table(2, len(vv)+1, ["GUID", "Data"] + l)

                    else:
                        self.md.new_line(
                            f"{kk} : `{self.get_printable_value(vv)}`")
            else:
                self.md.new_line(f"{k} : `{self.get_printable_value(v)}`")

    def handle_trigger_infos(self, triggers):

        self.md.new_header(5, "Service Triggers")
        self
        col_headers = ["ID", "Action", "GUID", "Type"]
        data = []
        for enum, fields in triggers.items():
            for k, v in fields.items():
                if k.startswith("Data"):
                    if k not in col_headers:
                        col_headers.append(k)
                    # indicates string_type
                    if v == 2 and k.startswith("DataType"):
                        # Update the Data fields to be more readable if they are strings
                        data_index = k.split("DataType", 1)[1]
                        tmp_k = f"Data{data_index}"
                        tmp_ent = fields.get(tmp_k, None)
                        if tmp_ent:
                            fields[tmp_k] = self.utf8_bytes_to_str(tmp_ent)

        for enum, fields in triggers.items():
            init_dict = {key: "" for key in col_headers}
            init_dict["ID"] = enum
            for k, v in fields.items():
                if k not in fields:
                    raise Exception(f"Unhandled service triggerInfo field {k}")
                if k == "Type":
                    v = SERVICE_TRIGGER_TYPES.get(v, v)
                elif k == "GUID":
                    g = str(uuid.UUID(bytes=v))
                    # TODO GUID bytes to GUID string
                    v = SERVICE_TRIGGER_GUIDS.get(g, g)
                elif k == "Action":
                    v = SERVICE_TRIGGER_ACTION_TYPES.get(v, v)
                elif k.startswith("DataType"):
                    v = SERVICE_TRIGGER_DATA_TYPES.get(v, v)

                init_dict[k] = f"`{self.get_printable_value(v)}`"
            data.append(init_dict)

        d = []
        for e in data:
            for k, val in e.items():
                d.append(val)

        self.md.new_table(len(col_headers), (len(
            triggers.keys()) + 1), list(col_headers)+list(d))
