# Agentic LLM Router

Production-oriented hybrid LLM routing system built with FastAPI and Groq.

## Features

- Hybrid routing architecture
- Rule-based complexity scoring
- Risk-aware query escalation
- LLM fallback judgment
- Dynamic model selection
- Prometheus monitoring
- Production-ready FastAPI backend

## Architecture

User Query → Router Agent → Complexity/Risk Analysis → LLM Selection → Response
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/192f6ce1-c787-43ff-91d1-bfe8c2e2eb4b" />


## Models

- Small Model:
  - llama-3.1-8b-instant

- Large Model:
  - llama-3.3-70b-versatile

## Tech Stack

- Python
- FastAPI
- Groq API
- Prometheus
- Docker-ready architecture

## Example Routing

| Query Type | Selected Model |
|---|---|
| Simple factual query | small_llm |
| Architecture analysis | big_llm |
| Legal/financial risk | big_llm |
| Ambiguous query | LLM judge fallback |

## Metrics

Prometheus metrics:
- Request count
- Model usage
- Routing strategy distribution
- Request latency

## Run Locally

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

## Metrics Endpoint

```text
/metrics
```
