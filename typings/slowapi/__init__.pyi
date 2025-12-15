from typing import Any, Callable, TypeVar
from starlette.requests import Request

F = TypeVar("F", bound=Callable[..., Any])
KeyFunc = Callable[[Request], str]

class Limiter:
    def __init__(self, key_func: KeyFunc) -> None: ...

    def limit(self, limit: str) -> Callable[[F], F]: ...
