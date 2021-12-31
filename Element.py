from types import GeneratorType
from typing import Any, Iterable

class element(object):

    __slots__ = ("_name", "_value", "_properties", "_instance")

    def __call__(self, **properties: Any) -> None:
        self._properties = properties
        return None

    def __set_name__(self, owner: Any, name: str) -> None:
        self._name = name
        self._properties = None
        self._value = None

    def __set__(self, instance: Any, value: Any) -> None:
        instance.__dict__[self._name] = self
        self._instance = instance
        self._value = value

    def __get__(self, instance: Any, owner: Any) -> str:
        instance.__dict__[self._name] = self
        return self.__repr__()

    def __delete__(self, instance: Any) -> None:
        del instance.__dict__[self._name]
        self._value = None
        self._properties = None

    def __make__(self) -> str:
        p = ''.join(f' {k}="{v}"' for k, v in self._properties.items()) if self._properties is not None else ''
        v = self._value if self._value is not None else ''
        result = f"<{self._name}{p}>{v}</{self._name}>"
        return result

    def __repr__(self) -> str:
        if not isinstance(self._value, str) and isinstance(self._value, Iterable):
            return ''.join([str(e) for e in self._value])
        else:
            return self.__make__()


class repr: 
    def __repr__(self):
        _name = self.__class__.__name__
        values = ''.join(str(e) for e in self.__dict__.values() if isinstance(e, element))
        return f"<{_name}>{values}</{_name}>"
