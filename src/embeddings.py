import google.generativeai as genai

from src.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


def embed_document(text):
    response = genai.embed_content(
        model="models/gemini-embedding-001",
        content=text,
        task_type="retrieval_document"
    )

    return response["embedding"]


def embed_query(text):
    response = genai.embed_content(
        model="models/gemini-embedding-001",
        content=text,
        task_type="retrieval_query"
    )

    return response["embedding"]