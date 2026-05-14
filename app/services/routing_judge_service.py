import json
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def judge_query_complexity(query: str) -> dict:
    prompt = f"""
You are an LLM routing judge.

Decide whether the query should be handled by:
- small_llm: simple, low-risk, short, factual, rewriting, translation, basic explanation
- big_llm: complex reasoning, debugging, architecture, legal/financial/medical risk, multi-step analysis

Return ONLY valid JSON in this format:
{{
  "selected_model": "small_llm" or "big_llm",
  "confidence": 0.0 to 1.0,
  "reason": "short reason"
}}

Query:
{query}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0,
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "selected_model": "big_llm",
            "confidence": 0.5,
            "reason": "LLM judge returned invalid JSON, defaulting to safer big model.",
        }