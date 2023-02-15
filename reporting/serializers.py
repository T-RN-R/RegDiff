from reporting import *
from reporting.system import *

import functools




class HiveSerializer():
    def merge(self, a, b, path=None):
        "merges b into a"
        if path is None: path = []
        for key in b:
            if key in a:
                if isinstance(a[key], dict) and isinstance(b[key], dict):
                    self.merge(a[key], b[key], path + [str(key)])
                elif a[key] == b[key]:
                    pass # same leaf value
                elif a[key] is None:
                    a[key] = b[key]
                elif b[key] is None:
                    return a
                else:
                    
                    raise Exception('Conflict at %s' % '.'.join(path + [str(key)]) + f" | {a[key]} and {b[key]} for {key}")
            else:
                a[key] = b[key]
        return a

    def filter_on_key_string(self, data:dict, filter:str, should_split:bool=False) -> dict:

        if "\\" not in filter:
            return data.get(filter)
        
        for filt in filter.split("\\"):
            data = data.get(filt, {})    
        return data

        
    def deserialize_entry(self, k, v) -> dict:
        return_dict = {}
        if "\\" not in k:
            return {k:v}
        entry, rest = k.split("\\", 1)
        return_dict[entry] = self.deserialize_entry(rest, v)
        return return_dict

    def to_nested_dict(self, data:dict):
        dicts = list()

        for k, v in data.items():
            dicts.append(self.deserialize_entry(k, v))
        return functools.reduce(self.merge, dicts)




class SystemHiveSerializer(HiveSerializer):
    def __init__(self):
        pass

    def handle_wmi_autologger(self, d:dict) -> MarkdownVisitable:
        return RegAutoLogger(d)
        
    def handle_services(self, d:dict) -> MarkdownVisitable:
        return RegServices(d)
        
    def handle_control_set(self,data:dict) -> list[MarkdownVisitable]:
        WMI_AUTOLOGGER = "Control\\WMI\\Autologger"
        SERVICES = "Services"
        results = []
        wmi_al = self.filter_on_key_string(data, WMI_AUTOLOGGER)
        results  += [self.handle_wmi_autologger(wmi_al)]
        results += [self.handle_services(self.filter_on_key_string(data,SERVICES))]
        return results
        
        

    def deserialize(self, diffs:dict):
        # {added, removed, modified}
        results = []
        #Handle CurrentControlSet
        for diff, data in diffs.items():
            if diff == "added":
                added_data = self.to_nested_dict(data) #convert into collapsible dict form
                results += [AddedContainer(self.handle_control_set(self.filter_on_key_string(added_data, "ControlSet001", True)))]
            elif diff == "removed":
                removed_data = self.to_nested_dict(data)
                results += [RemovedContainer(self.handle_control_set(self.filter_on_key_string(removed_data, "ControlSet001", True)))]


        return SystemHiveContainer(results)
