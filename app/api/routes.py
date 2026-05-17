from fastapi import APIRouter, Depends

from app.agents.router_agent import RouterAgent
from app.models.schemas import QueryRequest, QueryResponse
from app.services.llm_service import call_big_llm, call_small_llm
from app.core.security import verify_api_key, validate_query_input

router = APIRouter()

router_agent = RouterAgent()


@router.post(
    "/route",
    response_model=QueryResponse
)
def route_query(
    request: QueryRequest,
    _: bool = Depends(verify_api_key)
):
    validate_query_input(request.query)

    decision = router_agent.analyze_query(request.query)

    if decision["selected_model"] == "small_llm":
        response = call_small_llm(request.query)
    else:
        response = call_big_llm(request.query)

    return QueryResponse(
        query=request.query,
        selected_model=decision["selected_model"],
        complexity_score=decision["complexity_score"],
        risk_score=decision["risk_score"],
        confidence=decision["confidence"],
        routing_strategy=decision["routing_strategy"],
        reason=decision["reason"],
        response=response,
    )