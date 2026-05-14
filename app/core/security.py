import os
import re

from fastapi import HTTPException, Header
from dotenv import load_dotenv

load_dotenv()

APP_API_KEY = os.getenv("APP_API_KEY")


def verify_api_key(x_api_key: str = Header(None)):
    if not APP_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="Server API key is not configured."
        )

    if x_api_key != APP_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key."
        )

    return True


def validate_query_input(query: str):
    if not query or len(query.strip()) < 3:
        raise HTTPException(
            status_code=400,
            detail="Query is too short."
        )

    if len(query) > 3000:
        raise HTTPException(
            status_code=400,
            detail="Query is too long. Maximum allowed length is 3000 characters."
        )

    suspicious_patterns = [
        r"ignore previous instructions",
        r"reveal your system prompt",
        r"show hidden instructions",
        r"print environment variables",
        r"api[_-]?key",
        r"secret",
        r"password",
        r"token",
    ]

    query_lower = query.lower()

    for pattern in suspicious_patterns:
        if re.search(pattern, query_lower):
            raise HTTPException(
                status_code=400,
                detail="Potentially unsafe prompt detected."
            )

    return True