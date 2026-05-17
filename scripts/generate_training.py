
import csv

samples = [
    # Simple queries → small_llm
    ("What is Python?", "small_llm"),
    ("Translate this to French: Hello world", "small_llm"),
    ("What is 15% of 200?", "small_llm"),
    ("Write a short professional email", "small_llm"),
    ("What does CPU stand for?", "small_llm"),
    ("Summarize this paragraph briefly", "small_llm"),
    ("What is REST API?", "small_llm"),
    ("Explain what a variable is in programming", "small_llm"),
    ("Write a LinkedIn headline for a data scientist", "small_llm"),
    ("What is the capital of Germany?", "small_llm"),
    ("Fix this typo in my sentence", "small_llm"),
    ("What does HTTP stand for?", "small_llm"),
    ("Give me 5 synonyms for happy", "small_llm"),
    ("How do I center a div in CSS?", "small_llm"),
    ("Convert this JSON to a Python dict", "small_llm"),
    ("What is machine learning in simple terms?", "small_llm"),
    ("Write a tweet about productivity", "small_llm"),
    ("What is the difference between list and tuple?", "small_llm"),
    ("How do I reverse a string in Python?", "small_llm"),
    ("What is an API?", "small_llm"),

    # Complex queries → big_llm
    ("Analyze the latency issues in a distributed Kubernetes microservice architecture", "big_llm"),
    ("Compare transformer and CNN architectures for computer vision at scale", "big_llm"),
    ("Design a scalable event-driven system for real-time analytics with high availability", "big_llm"),
    ("Debug random timeout spikes in a FastAPI app under production load", "big_llm"),
    ("Evaluate GDPR compliance risks in an AI recommendation system", "big_llm"),
    ("What are the tradeoffs between monolith and microservices for a fintech startup?", "big_llm"),
    ("Optimize GPU utilization for large-scale model inference pipelines", "big_llm"),
    ("Analyze the legal implications of using customer data for model training in Europe", "big_llm"),
    ("Design a multi-region failover strategy for a high-traffic SaaS application", "big_llm"),
    ("How should I structure a financial risk model for a hedge fund portfolio?", "big_llm"),
    ("Compare RLHF and DPO for fine-tuning LLMs on preference data", "big_llm"),
    ("Debug a race condition in a multi-threaded Python service under load", "big_llm"),
    ("Evaluate the scalability of a pub-sub architecture with 10 million events per day", "big_llm"),
    ("What are the compliance requirements for medical AI systems under FDA regulations?", "big_llm"),
    ("Analyze the tradeoffs between vector databases for production RAG systems", "big_llm"),
    ("Design an observability stack for a distributed ML inference system", "big_llm"),
    ("How do I optimize a PostgreSQL query plan for a table with 500 million rows?", "big_llm"),
    ("Evaluate security risks of exposing internal APIs through a public gateway", "big_llm"),
    ("Compare investment strategies for volatile emerging markets", "big_llm"),
    ("Design a multi-tenant SaaS architecture with strict data isolation", "big_llm"),
]

with open("data/training_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["query", "label"])
    writer.writerows(samples)

print(f"Generated {len(samples)} training samples")