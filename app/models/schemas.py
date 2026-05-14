from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    query: str = Field(..., min_length=3)


class QueryResponse(BaseModel):
    query: str
    selected_model: str
    complexity_score: int
    risk_score: int
    confidence: float
    routing_strategy: str
    reason: str
    response: str