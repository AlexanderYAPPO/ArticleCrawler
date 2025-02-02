class _ReadableScore:
    _val: int

    def __init__(self, val: int):
        self._val = val

    def get_readable(self) -> str:
        if self._val == -1:
            return "N/A"
        return str(self._val)

    @staticmethod
    def default() -> '_ReadableScore':
        return _ReadableScore(-1)
