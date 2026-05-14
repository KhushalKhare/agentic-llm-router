import time

from fastapi import APIRouter

from app.agents.router_agent import RouterAgent
from app.models.schemas import QueryRequest, QueryResponse
from app.services.llm_service import call_big_llm, call_small_llm
from app.utils.metrics import (
    REQUEST_COUNT,
    SMALL_LLM_CALLS,
    BIG_LLM_CALLS,
    ROUTING_STRATEGY_COUNT,
    REQUEST_LATENCY,
)

router = APIRouter()
router_agent = RouterAgent()


@router.post("/route", response_model=QueryResponse)
def route_query(request: QueryRequest):
    start_time = time.time()

    REQUEST_COUNT.inc()

    decision = router_agent.analyze_query(request.query)

    ROUTING_STRATEGY_COUNT.labels(
        strategy=decision["routing_strategy"]
    ).inc()

    if decision["selected_model"] == "small_llm":
        SMALL_LLM_CALLS.inc()
        response = call_small_llm(request.query)
    else:
        BIG_LLM_CALLS.inc()
        response = call_big_llm(request.query)

    REQUEST_LATENCY.observe(time.time() - start_time)

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