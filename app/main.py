from fastapi import FastAPI
from prometheus_client import make_asgi_app

from app.api.routes import router

app = FastAPI(
    title="Agentic LLM Router",
    description="Production-ready hybrid LLM routing agent with Prometheus monitoring.",
    version="1.0.0",
)

app.include_router(router, prefix="/api")

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "Agentic LLM Router",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }