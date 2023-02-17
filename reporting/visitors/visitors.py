from reporting import *
from reporting.visitors import *
from reporting.system import *
from reporting.markdown import *
from windows.registry.services import *
import uuid


class ITextHelper():
    def __init__(self, md:MdUtils):
        self.md = md
    def get_printable_value(self, field):
        if isinstance(field, bytes):
            return field.hex(sep=" ")
        elif isinstance(field, int):
            return '0x{:02x}'.format(field)
        else:
            return str(field)

    def emphasize_text(self, text: str) -> str:
        return f"<span style=\"text-align: center; font-size:2em;\">{text} </span>"
    def convert_privilege_bytes_to_string(self, privilege_bytes: bytes, encoding: str = "utf-16") -> str:
        return privilege_bytes.decode(encoding).strip().split("\x00")[:-2]

    def utf8_bytes_to_str(self, data: bytes) -> str:
        return data.decode("utf-16").strip().replace("\x00", "")


class CoreReportMarkdownRegServicesVisitor(Visitor, ITextHelper):

    def handle_system_services(self, reg_services: RegServices):
        self.md.new_header(3, self.emphasize_text("Services"))
        self.md.new_line("\n---\n<br></br>")
        for service in reg_services.data.services:
            self.handle_single_service(service)

    def handle_single_service(self, service: SystemHiveService):
        self.md.new_header(4, self.emphasize_text(f"{service.name} Service"))
        self.handle_summary(service.summary)
        self.handle_parameters(service.parameters)
        self.handle_trigger_infos(service.trigger_info)
        self.handle_security(service.security)
        self.handle_methods(service.methods)
        self.handle_firewall_policy(service.firewall_policy)
        self.md.new_line("\n---\n<br></br>")

    def handle_summary(self, summary: SystemHiveServiceSummary):
        table_column_headers = []
        table_row = []
        for entry in summary.entries:
            if isinstance(entry, SystemHiveServiceSummaryDefaultsEntry) and isinstance(entry.value, SystemHiveServiceFirewallPolicy):
                self.md.new_line("Default Firewall Policy")
                self.handle_firewall_policy(entry.value)
            else:
                v = f"`{self.get_printable_value(entry.value)}`"
                table_column_headers.append(entry.name)
                table_row.append(v)
        if len(table_column_headers) != 0:
            self.md.new_header(5, f"Summary")
            table_helper(self.md, table_column_headers, table_row)

    def handle_parameters(self, parameters: list[SystemHiveServiceParameter]):
        self.md.new_paragraph()
        self.handle_service_parameters(parameters)
        self.md.new_line("<br></br>")

    def handle_security(self, security: SystemHiveServiceSecurity):
        if security is None:
            return

        self.md.new_line(f"Security: : \n```\n{str(security)}\n```")

    def handle_methods(self, methods: list[SystemHiveServiceMethod]):
        for method in methods:
            self.md.new_line(f"`{self.get_printable_value(method)}`")

    def handle_firewall_policy(self, fp: SystemHiveServiceFirewallPolicy):
        if fp is None:
            return
        col_hdrs = set()

        rules = {}

        fw_rules = fp.firewall_rules
        for fw_rule in fw_rules:
            rules[fw_rule.name] = fw_rule
            for c in fw_rule.rule_data:
                col_hdrs.add(c)
        real_column_headers = ["Rule Name"] + list(col_hdrs)

        data = []
        for rule_name, rule in rules.items():
            init_dict = {key: "" for key in real_column_headers}
            init_dict["Rule Name"] = rule_name
            for k, v in rule.rule_data.items():
                init_dict[k] = f"`{self.get_printable_value(v)}`"
            data.append(init_dict)

        d = []
        for e in data:
            for k, val in e.items():
                d.append(val)

        if len(d) > 0:
            self.md.new_header(5, "Firewall Rules")
            table_helper(self.md, real_column_headers, d)

        col_hdrs = set()

        rules = {}

        fw_rs = fp.restricted_services
        for rs in fw_rs:
            for fw_rule in rs.firewall_rules:
                rules[fw_rule.name] = fw_rule
                for c in fw_rule.rule_data:
                    col_hdrs.add(c)
            real_column_headers = ["Rule Name"] + list(col_hdrs)

            data = []
            for rule_name, rule in rules.items():
                init_dict = {key: "" for key in real_column_headers}
                init_dict["Rule Name"] = rule_name
                for k, v in rule.rule_data.items():
                    init_dict[k] = f"`{self.get_printable_value(v)}`"
                data.append(init_dict)

            d = []
            for e in data:
                for k, val in e.items():
                    d.append(val)

            if len(d) > 0:
                self.md.new_header(5, f"Restricted Services {rs.name} Firewall Rules")
                table_helper(self.md, real_column_headers, d)

    def handle_service_parameters(self, parameters):
        self.md.new_header(5, "Service Parameters")
        for param in parameters:
            if isinstance(param, SystemHiveServicePolicyParameter):
                self.handle_service_parameters_policy(param)
            elif isinstance(param, SystemHiveServiceFirewallPolicy):
                self.handle_firewall_policy(param)
            elif isinstance(param, SystemHiveServiceParameter):
                self.md.new_line(
                    f"{param.name} : `{self.get_printable_value(param.value)}`")
            else:
                raise Exception("Unreachable")

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

    def handle_trigger_infos(self, triggers: list[SystemHiveServiceTriggerInfo]):
        self.md.new_paragraph()

        col_headers = ["ID", "Action", "GUID", "Type"]

        for trigger_info in triggers:
            fields = trigger_info.trigger_data.entries
            for k, v in fields.items():
                if k not in col_headers:
                    col_headers.append(k)
            for idx, _ in enumerate(trigger_info.parameters.trigger_data):
                k = f"Parameter {idx}"
                if k not in col_headers:
                    col_headers.append(k)


        data = []
        for trigger_info in triggers:
            enum = trigger_info.ordinal
            fields = trigger_info.trigger_data.entries
            init_dict = {key: "" for key in col_headers}
            init_dict["ID"] = enum
            for k, v in fields.items():
                init_dict[k] = f"`{self.get_printable_value(v)}`"

            for idx, param in enumerate(trigger_info.parameters.trigger_data):
                init_dict[f"Parameter {idx}"] = f"`{self.get_printable_value(param.value)}`"
    
 
            data.append(init_dict)

        d = []
        for e in data:
            for k, val in e.items():
                d.append(val)

        if len(d) > 0:
            self.md.new_header(5, "Service Triggers")
            self.md = table_helper(self.md, col_headers, d)
            self.md.new_line("<br></br>")


class CoreReportMarkdownAutoLoggerVisitor(Visitor,ITextHelper):
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



class CoreReportMarkdownVisitor(MarkdownVisitor):
    def get_markdown(self, md: MdUtils, data: list) -> MdUtils:
        self.md = md
        for container in data:
            # self.md.new_line("\n<details>\n")
            self.handle_container(container)
            # self.md.new_line("\n</details>\n")

        return md


    def handle_container(self, container: DiffContainer):
        assert isinstance(
            container, DiffContainer), "Did not pass a DiffContainer to handle_container"
        if isinstance(container, AddedContainer):
            self.md.new_line("<br></br><br></br>Added")

            # self.md.new_line("<summary> Added </summary>")
            self.handle_raw(container.data)
        elif isinstance(container, RemovedContainer):
            self.md.new_line("<br></br><br></br>Deleted")
            # self.md.new_line("<summary> Removed </summary>")
            self.handle_raw(container.data)
        elif isinstance(container, DiffContainer):
            self.handle_raw(container.data)
        else:
            raise Exception(f"Unhandled Container: {type(container)}")

    def handle_raw(self, visitable_list: list[MarkdownVisitable]):
        assert isinstance(
            visitable_list, list), "Did not pass a list to handle_raw!"
        for entry in visitable_list:
            assert isinstance(entry, MarkdownVisitable)
            if isinstance(entry, RegAutoLogger):
                CoreReportMarkdownAutoLoggerVisitor(self.md).handle_system_auto_logger(entry)
            elif isinstance(entry, RegServices):
                CoreReportMarkdownRegServicesVisitor(self.md).handle_system_services(entry)
            else:
                raise Exception(f"Unhandled visitable: {type(entry)}")
            self.md.new_line("<br></br>")


