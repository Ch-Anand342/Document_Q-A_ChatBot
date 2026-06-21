# test_embedding.py

from src.embeddings import embed_document

embedding = embed_document(
    "Hello World"
)

print(type(embedding))
print(len(embedding))