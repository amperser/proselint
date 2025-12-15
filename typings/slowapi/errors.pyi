from fastapi import HTTPException


class RateLimitExceeded(HTTPException):
    detail: str
