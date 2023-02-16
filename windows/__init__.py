import pyregf
import struct
from enum import Enum

from collections.abc import Mapping

class RegType(Enum):
    LIBREGF_VALUE_TYPE_UNDEFINED = 0
    LIBREGF_VALUE_TYPE_STRING = 1
    LIBREGF_VALUE_TYPE_EXPANDABLE_STRING = 2
    LIBREGF_VALUE_TYPE_BINARY_DATA = 3
    LIBREGF_VALUE_TYPE_INTEGER_32BIT_LITTLE_ENDIAN = 4
    LIBREGF_VALUE_TYPE_INTEGER_32BIT_BIG_ENDIAN = 5
    LIBREGF_VALUE_TYPE_SYMBOLIC_LINK = 6
    LIBREGF_VALUE_TYPE_MULTI_VALUE_STRING = 7
    LIBREGF_VALUE_TYPE_RESOURCE_LIST = 8
    LIBREGF_VALUE_TYPE_FULL_RESOURCE_DESCRIPTOR = 9
    LIBREGF_VALUE_TYPE_RESOURCE_REQUIREMENTS_LIST = 10
    LIBREGF_VALUE_TYPE_INTEGER_64BIT_LITTLE_ENDIAN = 11


class RegHiveDictView(Mapping):
    """
    Supplies dict-like APIs over libregf-python registry objects

    No function that is exposed here should pass any libregf contruct out.
    """

    def __init__(self, hive):
        self._hive = hive


    def __str__(self):
        return self._hive.get_name()
    def __getitem__(self, key: str):
        """
        Returns a RegHiveDictView at path {key}

        ie. key = CurrentControlSet\\Control\\Services
        """
        h = self._hive.get_sub_key_by_path(key)
        return RegHiveDictView(h) if h is not None else None

    def keys(self):
        return [RegHiveDictView(k) for k in self._hive.sub_keys if k is not None ]

    def values(self):
        return [self._hive_or_value_for_keyname(k)
                for k in self._hive.sub_keys ]

    
    def _hive_or_value_for_keyname(self, k):
        v = self._hive.get_sub_key_by_path(k.name) 
        if hasattr(v, "sub_keys"): 
            if len(v.sub_keys) >=1:
                return RegHiveDictView(v)        
        vals =   self._get_values_for_key(k)
        return vals
    
    def items(self):
        return [(k.name,self._hive_or_value_for_keyname(k)) for k in self._hive.sub_keys ]
    
    def __iter__(self):
        return iter(self.keys)

    def __len__(self):
        return self._hive.get_number_of_sub_keys

    def is_string_type(self, key):
        return (key == RegType.LIBREGF_VALUE_TYPE_STRING or key == RegType.LIBREGF_VALUE_TYPE_EXPANDABLE_STRING or key == RegType.LIBREGF_VALUE_TYPE_SYMBOLIC_LINK)

    def _get_values_for_key(self, key):
        coll = {}
        for cur in key.values:  # build & save printable value record paths
            curName = cur.get_name()
            data = self._value_to_python_value(cur)
            
            # data = cur.get_data()
            if curName is None:
                curName = '(Default)'
            tmpStr = '{}'.format(curName)
            coll[tmpStr] = data
        return coll

    def _value_to_python_value(self, value):
        data = None
        try:
            t = RegType(value.get_type())
            if self.is_string_type(t):
                data = value.get_data_as_string()
            elif t == RegType.LIBREGF_VALUE_TYPE_INTEGER_32BIT_BIG_ENDIAN:
                data = struct.unpack(">I", value.get_data())[0]
            elif t == RegType.LIBREGF_VALUE_TYPE_INTEGER_32BIT_LITTLE_ENDIAN:
                data = struct.unpack("<I", value.get_data())[0]
            elif t == RegType.LIBREGF_VALUE_TYPE_INTEGER_64BIT_LITTLE_ENDIAN:
                data = struct.unpack("<Q", value.get_data())[0]
            elif value.get_data() is not None:
                data = value.get_data()
            else:
                raise Exception(f"Unknown reg type {value.get_type()}")
                data = None
        except ValueError as e:
            # bug in pyregf?
            if value.get_data() is not None:
                data = value.get_data()
            else:
                data = None
        return data
