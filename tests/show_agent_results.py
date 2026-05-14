import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import csv
from app.agents.router_agent import RouterAgent


test_prompts = [

    # Simple Queries
    "What is Python?",
    "Explain Docker in simple terms.",
    "Translate this sentence into German.",
    "Write a short professional email.",
    "Summarize this paragraph about AI.",
    "What does CPU stand for?",
    "Explain REST APIs briefly.",
    "Write a LinkedIn headline for a Data Scientist.",
    "How does Git work?",
    "What is Kubernetes?",

    # Medium / Ambiguous Queries
    "Explain how caching improves backend performance.",
    "Compare Redis and Memcached.",
    "How does load balancing work in cloud systems?",
    "Explain observability in distributed systems.",
    "When should a company use microservices instead of a monolith?",

    # Complex Technical Queries
    "Analyze Kubernetes latency issues in a distributed microservice architecture.",
    "Design a scalable event-driven architecture for real-time analytics.",
    "Debug random timeout spikes in a FastAPI production deployment.",
    "Compare transformer and CNN architectures for computer vision workloads.",
    "Optimize GPU utilization for large-scale AI model inference.",

    # Risk / Compliance Queries
    "Analyze the legal risks of training AI systems using customer data in Europe.",
    "Evaluate GDPR compliance risks in AI recommendation systems.",
    "Analyze financial risks of investing in volatile AI startups.",
    "Design a secure healthcare AI platform handling sensitive patient records.",

    # Multi-Step Reasoning
    "Create a migration strategy from monolith architecture to Kubernetes microservices.",
    "Evaluate tradeoffs between PostgreSQL and MongoDB for high-scale analytics.",
    "Design a monitoring strategy using Prometheus and Grafana for AI inference systems.",
    "Analyze cost optimization strategies for multi-model LLM deployments.",

    # Edge Cases
    "Hi",
    "Explain quantum computing like I am five.",
    "Should startups prioritize scalability early?",
    "Fix latency issue.",
    "Medical diagnosis for chest pain and fever symptoms."
]


def main():
    agent = RouterAgent()

    results = []

    for query in test_prompts:

        decision = agent.analyze_query(query)

        results.append({
            "query": query,
            "selected_model": decision["selected_model"],
            "complexity_score": decision["complexity_score"],
            "risk_score": decision["risk_score"],
            "confidence": decision["confidence"],
            "routing_strategy": decision["routing_strategy"],
            "reason": decision["reason"]
        })

    print("\nAGENT ROUTING RESULTS")
    print("=" * 100)

    for result in results:

        print(f"\nQuery: {result['query']}")
        print(f"Selected Model: {result['selected_model']}")
        print(f"Complexity Score: {result['complexity_score']}")
        print(f"Risk Score: {result['risk_score']}")
        print(f"Confidence: {result['confidence']}")
        print(f"Routing Strategy: {result['routing_strategy']}")
        print(f"Reason: {result['reason']}")

    with open("tests/agent_results.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "query",
                "selected_model",
                "complexity_score",
                "risk_score",
                "confidence",
                "routing_strategy",
                "reason"
            ]
        )

        writer.writeheader()
        writer.writerows(results)

    print("\nSaved results to tests/agent_results.csv")


if __name__ == "__main__":
    main()