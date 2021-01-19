from __future__ import annotations


class EmptyString(ValueError):
    pass


class nonemptystr(str):
    def __new__(cls, obj: object) -> nonemptystr:
        s = str(obj)
        if not s:
            raise EmptyString
        return str.__new__(nonemptystr, s)  # type: ignore
