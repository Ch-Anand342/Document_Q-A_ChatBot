import google.generativeai as genai

from src.config import *
from src.embeddings import embed_query
from src.vectordb import collection
from src.prompts import SYSTEM_PROMPT

genai.configure(
    api_key=GEMINI_API_KEY
)


def ask_question(question):

    query_embedding = embed_query(
        question
    )

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K,
        include=["documents", "metadatas"]
    )

    context = ""

    citations = []

    for doc, meta in zip(
            results["documents"][0],
            results["metadatas"][0]
    ):

        citation = (
            f"{meta['source']} "
            f"(Page {meta['page']})"
        )

        citations.append(citation)

        context += f"""
[{citation}]
{doc}

"""

    prompt = f"""
{SYSTEM_PROMPT}

CONTEXT:

{context}

QUESTION:

{question}

ANSWER:
"""

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    response = model.generate_content(
        prompt
    )

    return response.text