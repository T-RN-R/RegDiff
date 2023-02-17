from reporting import *
from reporting.system import *
from reporting.visitors import DiffContainer, AddedContainer, RemovedContainer
import functools


from collections.abc import Mapping

class LazyDict(Mapping):
    """
    This is an implementation of a Lazy Dictionary to support the conversion of registry paths to nested dictionaries.
    For large inputs, the conversion is prohibitively slow. With this, only the registry paths needed are computed.
    A single entry:
    {\\Control\\ControlSet\\WMI\\Data: 1}
    Becomes:
    {Control:{ControlSet:{WMI:{Data:1}}}}


    """
    def __init__(self, data:dict):
        self._raw_dict = data
        self._access_cache = {}
        

    def __getitem__(self, key):
        """
        Keeps a dictionary of LazyDicts to evaluate queries as needed.
        """
        lookahead = self._access_cache.get(key, None)
        if not lookahead:
            candidates = {k.split("\\", 1)[1]:v for k,v in self._raw_dict.items() if key in k and "\\" in k and v is not None}
            ent = LazyDict(candidates)
            self._access_cache[key] = ent
            return ent
        return lookahead 
    def __str__(self):
        return str(self._access_cache)
    def de_lazy_once(self):
        if self._access_cache == {}:
            for k in self._raw_dict.keys():
                #un-lazying the dict for iteration
                tk = k
                if "\\"  in k:
                    tk = k.split("\\",1)[0]
                    self.get(tk)
    def items(self):
        self.de_lazy_once()
        return self._access_cache.items()
    def keys(self):
        self.de_lazy_once()
        return self._access_cache.keys()
    def values(self):
        self.de_lazy_once()
        return self._access_cache.values()
    def __iter__(self):
        return iter(self._access_cache)

    def __len__(self):
        length = len({k.split("//",1)[0] for k in self._raw_dict})
        return length

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
            data = data.get(filt)    
        
        return data

        
    def deserialize_entry(self, k, v) -> dict:
        return_dict = {}
        if "\\" not in k:
            return {k:v}
        entry, rest = k.split("\\", 1)
        return_dict[entry] = self.deserialize_entry(rest, v)
        return return_dict

    def to_nested_dict(self, data:dict, filter:str=None):
        dicts = list()

        for k, v in data.items():
            if not filter or filter in k:
                dicts.append(self.deserialize_entry(k, v))
        return functools.reduce(self.merge, dicts)




    def lazy_to_dict(self,data:dict)->LazyDict:
        return LazyDict(data)


class SystemHiveSerializer(HiveSerializer):
    def __init__(self):
        pass

    def handle_wmi_autologger(self, d:dict) -> MarkdownVisitable:
        return RegAutoLogger(d)
        
    def handle_services(self, d:dict) -> MarkdownVisitable:
        return RegServices(SystemHiveServices(d))
        
    def handle_control_set(self,data:dict) -> list[MarkdownVisitable]:
        WMI_AUTOLOGGER = "Control\\WMI\\Autologger"
        SERVICES = "Services"
        results = []
        wmi_al = self.filter_on_key_string(data, WMI_AUTOLOGGER)
        results  += [self.handle_wmi_autologger(wmi_al)]
        results += [self.handle_services(self.filter_on_key_string(data,SERVICES))]

        return results
        
        

    def deserialize(self, diffs:dict, no_diffs:bool=False):
        # {added, removed, modified}
        results = []
        #Handle CurrentControlSet
        if no_diffs:
                #wmi = self.to_nested_dict(diffs,"ControlSet001\\Control\\WMI\\Autologger")
                #svcs = self.to_nested_dict(diffs,"ControlSet001\\Services")
            d = self.to_nested_dict(diffs)
            results+= [DiffContainer(self.handle_control_set(self.filter_on_key_string(d, "ControlSet001", True)))]
            return SystemHiveContainer(results)

        for diff, data in diffs.items():
            if diff == "added":
                added_data = self.to_nested_dict(data) #convert into collapsible dict form
                results += [AddedContainer(self.handle_control_set(self.filter_on_key_string(added_data, "ControlSet001", True)))]
            elif diff == "removed":
                removed_data = self.to_nested_dict(data)
                results += [RemovedContainer(self.handle_control_set(self.filter_on_key_string(removed_data, "ControlSet001", True)))]



        return SystemHiveContainer(results)
