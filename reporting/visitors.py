from reporting import *
from reporting.system import *
class CoreReportMarkdownVisitor(MarkdownVisitor):
    def get_markdown(self, md:MdUtils, data:list) -> MdUtils:
        self.md = md
        for container in data:
            self.handle_container(container)


        return md

    def handle_container(self, container: DiffContainer):
        if isinstance(container, AddedContainer):
            self.md.new_header(3, "Added")
            self.handle_raw(container.data)

    def handle_raw(self, visitable_list):
        for entry in visitable_list:
            if isinstance(entry,RegAutoLogger):
                self.handle_system_auto_logger(entry)
            elif isinstance(entry, RegServices):
                self.handle_system_services(entry)
            else: 
                raise Exception(f"Unhandled visitable: {type(entry)}")

    def handle_system_auto_logger(self, entry:RegAutoLogger):
        self.md.new_header(4, "WMI AutoLoggers")
        al = entry.data
        for k,v in al.items():
            self.md.new_header(5, k)
            known_keys = set()
            known_keys.add("guid")
            for _, values in v.items():
                for kk in values:
                    known_keys.add(kk)
            known_keys = list(known_keys)
            known_keys.sort()
            data = list()

            for guid, values in v.items():
                init_dict = {key:None for key in known_keys}
                for key in known_keys:
                    value =  values.get(key, None)
                    if isinstance(value, bytes):
                        init_dict[key] = value.hex(sep =" ")
                    else:
                        init_dict[key] = str(value)
                init_dict["guid"] = guid
                data.append(init_dict)

            d = []
            for e in data:
                for k, val in e.items():
                    d.append(val)

            self.md.new_table(len(known_keys), (len(v.keys()) + 1), known_keys+d)
            

        
    def handle_system_services(self, entry:RegServices):
        pass