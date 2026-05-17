import os
import re

from dotenv import load_dotenv
from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

load_dotenv()

APP_API_KEY = os.getenv("APP_API_KEY")

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


def verify_api_key(api_key: str = Security(api_key_header)):
    print("EXPECTED:", APP_API_KEY)
    print("RECEIVED:", api_key)

    if not APP_API_KEY:
        raise HTTPException(status_code=500, detail="Server API key is not configured.")

    if api_key != APP_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key.")

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

load_dotenv()

APP_API_KEY = os.getenv("APP_API_KEY")
print("APP_API_KEY LOADED:", APP_API_KEY)