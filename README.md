# Agentic LLM Router

Production-oriented hybrid LLM routing system built with **FastAPI**, **Groq**, and **Prometheus**.

The system dynamically routes user queries between a small and large LLM based on complexity, risk level, ambiguity, and routing confidence. The goal is to reduce unnecessary large-model usage while preserving response quality for complex or sensitive tasks.

## Features

- Hybrid LLM routing architecture
- Rule-based complexity scoring
- Risk-aware query escalation
- Ambiguity detection
- LLM judge fallback
- Dynamic model selection
- Prometheus monitoring
- Routing result evaluation
- Production-ready FastAPI backend

## Architecture

```text
User Query
    ↓
FastAPI Endpoint
    ↓
Router Agent
    ↓
Complexity + Risk + Ambiguity Analysis
    ↓
Routing Decision Engine
    ↓
Small LLM or Large LLM
    ↓
Final Response
```
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/07333e5e-d00f-4409-a594-5ae368114ebf" />


## Models

| Model Type | Model |
| ---------- | ------------------------- |
| Small LLM | `llama-3.1-8b-instant` |
| Large LLM | `llama-3.3-70b-versatile` |

## Tech Stack

- Python
- FastAPI
- Groq API
- Prometheus
- Pydantic
- Uvicorn
- Docker-ready architecture

## Example Routing

| Query Type | Selected Route |
| ----------------------------------- | ------------------ |
| Simple factual query | Small LLM |
| Basic explanation | Small LLM |
| Architecture analysis | Large LLM |
| Legal / financial / high-risk query | Large LLM |
| Ambiguous query | LLM judge fallback |

## Metrics

Prometheus metrics include:

- Request count
- Model usage
- Routing strategy distribution
- Request latency
- Fallback usage

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
python -m uvicorn app.main:app --reload
```

The API will run at:

```text
http://localhost:8000
```

## Metrics Endpoint

```text
/metrics
```

## Evaluation Output

Routing evaluation results are stored in:

```text
tests/agent_results.csv
```

This file can be used to compare expected model selection against actual routing decisions. Because apparently even routers need performance reviews now.

## Project Goal

This project demonstrates how to build a cost-aware and risk-aware LLM routing layer for AI applications. It is designed to show practical backend engineering, LLM orchestration, monitoring, and evaluation workflows.
