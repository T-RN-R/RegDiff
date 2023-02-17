


class SystemHiveFileSystem():
    def __init__(self, entries:dict):
        self._ents = {k:v for k, v in entries.items()}

    @property
    def entries(self):
        return self._ents