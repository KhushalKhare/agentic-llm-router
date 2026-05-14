import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=GROQ_API_KEY
)


def call_small_llm(query: str) -> str:

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a fast lightweight assistant "
                    "for simple low-cost tasks."
                )
            },
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content


def call_big_llm(query: str) -> str:

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an advanced reasoning assistant "
                    "for complex analytical tasks."
                )
            },
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content