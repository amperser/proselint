from typing import Any, Callable, Protocol, TypeVar
from starlette.requests import Request
from starlette.responses import Response

class ViewRateLimit(Protocol):
    limit: str
    reset: int
    remaining: int

F = TypeVar("F", bound=Callable[..., Any])
KeyFunc = Callable[[Request], str]

class Limiter:
    def __init__(self, key_func: KeyFunc) -> None: ...

    def limit(self, limit: str) -> Callable[[F], F]: ...

    def _inject_headers(
        self,
        response: Response,
        rate_limit: ViewRateLimit,
    ) -> Response: ...
