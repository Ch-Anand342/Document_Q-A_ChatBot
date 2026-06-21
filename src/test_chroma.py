# src/test_chroma.py

from src.vectordb import collection

print("Adding...")

collection.add(
    ids=["1"],
    embeddings=[[0.1] * 3072],
    documents=["hello world"],
    metadatas=[{"source": "test", "page": 1}]
)

print("Success")