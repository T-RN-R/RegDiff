from reporting import *


class SystemHiveContainer(MarkdownVisitable) :
    def __init__(self, data:list[MarkdownVisitable]):
        self.data = data


class RegAutoLogger(MarkdownVisitable):
    def __init__(self, data:dict):
        self.data = data

class RegServices(MarkdownVisitable):
    def __init__(self, data:dict):
        self.data = data