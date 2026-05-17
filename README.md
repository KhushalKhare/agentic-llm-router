# Agentic LLM Router

An intelligent hybrid LLM routing system that dynamically selects the most suitable language model for a query based on complexity, ambiguity, risk, and classifier confidence.

Instead of sending every request to a large expensive model, the router optimizes for:
- lower inference cost
- reduced latency
- safer AI interactions
- scalable production-oriented routing

---

# Architecture

The system uses an ML-based routing pipeline:

User Query
    ↓
Sentence Embedding Model
    ↓
ML Classifier Prediction
    ↓
Confidence Evaluation
    ↓
├── High Confidence → Route Directly
└── Low Confidence → LLM Judge Fallback
                                ↓
                     Final Model Selection

The router selects:
- Small LLM → simple / low-risk queries
- Large LLM → complex / high-risk reasoning tasks
- LLM Judge → fallback for uncertain routing decisions

---
<img width="1536" height="1024" alt="Architecture 2" src="https://github.com/user-attachments/assets/27dfd5ad-a9ee-4b2a-bcbd-e2d89d733f4a" />

# Key Features

## ML-Based Routing
- Replaced earlier rule-based routing with embedding + classifier-based prediction
- Uses Sentence Transformers embeddings
- Trained classifier predicts optimal model selection
- Confidence-aware routing decisions

## Hybrid Routing Logic
- High-confidence predictions are routed directly
- Low-confidence predictions trigger LLM judge validation
- Improves adaptability compared to static rules

## Production-Oriented Security
- API key authentication
- Environment-based secret management
- Prompt injection filtering
- Input validation and length checks
- Blocks attempts to expose:
  - API keys
  - passwords
  - tokens
  - hidden prompts

## Observability & Monitoring
- Prometheus metrics integration
- Tracks:
  - latency
  - selected model
  - routing confidence
  - routing strategy
  - evaluation metrics

## Evaluation Pipeline
- CSV-based routing evaluation
- Stores classifier and routing results
- Useful for benchmarking and iterative improvement

---

# Tech Stack

- Python
- FastAPI
- Pydantic
- Sentence Transformers
- Scikit-learn
- Groq API
- Llama 3
- Prometheus
- Docker
- Pandas

---

# Example Routing Flow

Simple Query:
"Translate hello to German"
→ Small LLM

Complex Query:
"Explain Kubernetes scalability tradeoffs in distributed systems"
→ Large LLM

Uncertain Query:
Classifier confidence below threshold
→ LLM Judge Fallback

---

# Security Example

The router blocks malicious prompts such as:

- "Ignore previous instructions"
- "Reveal system prompt"
- "Show API keys"

Requests containing suspicious patterns are rejected before inference.

---

# Run Locally

## Create Virtual Environment

```bash
python -m venv venv
