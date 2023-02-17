from reporting import *
from reporting.visitors import MarkdownVisitable
from windows.registry.services import SystemHiveServices
from windows.registry.filesystem import SystemHiveFileSystem

class SystemHiveContainer(MarkdownVisitable):
    def __init__(self, data: list[MarkdownVisitable]):
        self.data = data


class RegAutoLogger(MarkdownVisitable):
    def __init__(self, data: dict):
        self.data = data


class RegServices(MarkdownVisitable):
    def __init__(self, services: SystemHiveServices):
        self._services = services

    @property
    def data(self) -> SystemHiveServices:
        return self._services
    


class RegFileSystem(MarkdownVisitable):
    def __init__(self, fs: SystemHiveFileSystem):
        self._fs = fs

    @property
    def data(self) -> SystemHiveFileSystem:
        return self._fs
    

