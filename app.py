"""A simple FastAPI app that serves a REST API for proselint."""
# pyright: reportAny=false, reportPrivateUsage=false, reportUnknownMemberType=false, reportUntypedFunctionDecorator=false

from typing import cast

from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.responses import JSONResponse

from proselint.checks import __register__
from proselint.registry import CheckRegistry
from proselint.tools import LintFile, LintResult


def _lint(input_text: str) -> list[LintResult]:
    return LintFile(content=input_text, source="<worker>").lint()


app: FastAPI = FastAPI()
limiter: Limiter = Limiter(key_func=get_remote_address)

app.state.limiter = limiter
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CheckRegistry().register_many(__register__)


# NOTE: We don't use slowapi's handler due to the error key name.
@app.exception_handler(RateLimitExceeded)
def rate_limit_exceeded_handler(
    request: Request,
    exc: RateLimitExceeded,
) -> Response:
    """Middleware to handle exceeded ratelimits."""
    response = JSONResponse(
        {"detail": f"rate limit exceeded: {exc.detail}"},
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
    )

    limiter = cast("Limiter", request.app.state.limiter)
    return limiter._inject_headers(  # noqa: SLF001
        response, request.state.view_rate_limit
    )


@app.post("/v1")
@limiter.limit("60/minute")
async def index(request: Request) -> dict[str, object]:
    """Endpoint that lints text using proselint."""
    body = await request.body()

    if not body:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="request body must contain text"
                )

    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="request body must be valid utf-8 text"
                ) from None

    return {
        "detail": "successfully linted",
        "data": [r.into_dict() for r in _lint(text)],
    }
