from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "llm_router_requests_total",
    "Total number of routing requests"
)

SMALL_LLM_CALLS = Counter(
    "llm_router_small_llm_calls_total",
    "Total number of small LLM calls"
)

BIG_LLM_CALLS = Counter(
    "llm_router_big_llm_calls_total",
    "Total number of big LLM calls"
)

ROUTING_STRATEGY_COUNT = Counter(
    "llm_router_strategy_total",
    "Routing decisions by strategy",
    ["strategy"]
)

REQUEST_LATENCY = Histogram(
    "llm_router_request_latency_seconds",
    "Request latency in seconds"
)