from reporting import *
from reporting.visitors import MarkdownVisitable
from windows.registry.services import SystemHiveServices


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
