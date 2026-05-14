from app.services.routing_judge_service import judge_query_complexity


class RouterAgent:
    def analyze_query(self, query: str) -> dict:
        query_lower = query.lower()
        word_count = len(query.split())

        complexity_score = 0
        risk_score = 0

        complex_keywords = [
            "analyze",
            "compare",
            "debug",
            "architecture",
            "optimize",
            "strategy",
            "research",
            "evaluate",
            "multi-step",
            "scalability",
            "latency",
            "observability",
            "kubernetes",
            "production",
            "distributed",
            "tradeoff",
            "design",
        ]

        risk_keywords = [
            "medical",
            "legal",
            "financial",
            "investment",
            "diagnosis",
            "contract",
            "tax",
            "compliance",
            "gdpr",
        ]

        for keyword in complex_keywords:
            if keyword in query_lower:
                complexity_score += 2

        for keyword in risk_keywords:
            if keyword in query_lower:
                risk_score += 3

        if word_count > 100:
            complexity_score += 5
        elif word_count > 60:
            complexity_score += 3
        elif word_count > 30:
            complexity_score += 1

        if risk_score >= 3:
            return {
                "selected_model": "big_llm",
                "complexity_score": complexity_score,
                "risk_score": risk_score,
                "confidence": 0.95,
                "routing_strategy": "rule_based_risk_override",
                "reason": "Selected big LLM because risk-sensitive keywords were detected.",
            }

        if complexity_score >= 6:
            return {
                "selected_model": "big_llm",
                "complexity_score": complexity_score,
                "risk_score": risk_score,
                "confidence": 0.90,
                "routing_strategy": "rule_based_complexity",
                "reason": "Selected big LLM because complexity score is high.",
            }

        if complexity_score <= 1 and word_count <= 25:
            return {
                "selected_model": "small_llm",
                "complexity_score": complexity_score,
                "risk_score": risk_score,
                "confidence": 0.90,
                "routing_strategy": "rule_based_simple",
                "reason": "Selected small LLM because query is short and low complexity.",
            }

        judge_decision = judge_query_complexity(query)

        return {
            "selected_model": judge_decision["selected_model"],
            "complexity_score": complexity_score,
            "risk_score": risk_score,
            "confidence": judge_decision["confidence"],
            "routing_strategy": "llm_judge_fallback",
            "reason": judge_decision["reason"],
        }