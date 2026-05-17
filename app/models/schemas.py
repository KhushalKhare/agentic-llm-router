from typing import Optional
from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    query: str = Field(..., min_length=3)


class QueryResponse(BaseModel):
    query: str
    selected_model: str
    complexity_score: Optional[int] = None
    risk_score: str
    confidence: float
    routing_strategy: str
    reason: str
    response: str