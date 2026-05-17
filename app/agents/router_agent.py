import joblib
import numpy as np
from sentence_transformers import SentenceTransformer

from app.services.routing_judge_service import judge_query_complexity

# Load once at startup
# Do NOT load SentenceTransformer from joblib. That causes transformer version issues.
_embedder = SentenceTransformer("all-MiniLM-L6-v2")
_classifier = joblib.load("models/router_classifier.pkl")

RISK_KEYWORDS = [
    "medical", "medicine", "doctor", "diagnosis", "pregnancy", "symptoms",
    "legal", "lawyer", "sue", "court", "contract", "landlord",
    "financial", "investment", "invest", "stock", "crypto", "tax",
    "compliance", "gdpr", "privacy", "regulation",
]

CONFIDENCE_THRESHOLD = 0.75


def _check_risk(query: str) -> bool:
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in RISK_KEYWORDS)


class RouterAgent:
    def analyze_query(self, query: str) -> dict:

        if _check_risk(query):
            return {
                "selected_model": "big_llm",
                "complexity_score": None,
                "risk_score": "high",
                "confidence": 0.95,
                "routing_strategy": "rule_based_risk_override",
                "reason": "Risk-sensitive domain detected. Routed to big LLM for safety.",
            }

        embedding = _embedder.encode([query])

        probabilities = _classifier.predict_proba(embedding)[0]
        classes = _classifier.classes_

        confidence = float(np.max(probabilities))
        predicted_label = classes[np.argmax(probabilities)]

        if confidence >= CONFIDENCE_THRESHOLD:
            return {
                "selected_model": predicted_label,
                "complexity_score": None,
                "risk_score": "low",
                "confidence": round(confidence, 3),
                "routing_strategy": "embedding_classifier",
                "reason": f"Embedding classifier routed to {predicted_label} "
                          f"with {round(confidence * 100, 1)}% confidence.",
            }

        try:
            judge_decision = judge_query_complexity(query)

            return {
                "selected_model": judge_decision["selected_model"],
                "complexity_score": None,
                "risk_score": "low",
                "confidence": judge_decision["confidence"],
                "routing_strategy": "llm_judge_fallback",
                "reason": f"Classifier confidence too low ({round(confidence * 100, 1)}%). "
                          f"LLM judge decided: {judge_decision['reason']}",
            }

        except Exception as e:
            return {
                "selected_model": "big_llm",
                "complexity_score": None,
                "risk_score": "unknown",
                "confidence": 0.5,
                "routing_strategy": "safe_fallback_big_llm",
                "reason": f"LLM judge failed. Routed to big LLM for safety. Error: {str(e)}",
            }