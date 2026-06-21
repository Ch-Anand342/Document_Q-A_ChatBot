import os
import uuid

from document_loader import (
    load_pdf,
    load_docx,
    load_txt
)

from src.chunker import chunk_text
from src.embeddings import embed_document
from src.vectordb import collection

DATA_DIR = "data"


def process_file(path):

    if path.endswith(".pdf"):
        docs = load_pdf(path)

    elif path.endswith(".docx"):
        docs = load_docx(path)

    elif path.endswith(".txt"):
        docs = load_txt(path)

    else:
        return

    for doc in docs:

        chunks = chunk_text(doc["text"])

        for idx, chunk in enumerate(chunks):

            print(f"Processing chunk {idx + 1}/{len(chunks)}")

            try:

                embedding = embed_document(chunk)

                print("Embedding Length:", len(embedding))

                collection.add(
                    ids=[str(uuid.uuid4())],
                    embeddings=[embedding],
                    documents=[chunk],
                    metadatas=[{
                        "source": str(doc["metadata"]["source"]),
                        "page": int(doc["metadata"]["page"])
                    }]
                )

                print("Saved Successfully")

            except Exception as e:

                print("ERROR:")
                print(repr(e))
                raise


def ingest_documents():

    for file in os.listdir(DATA_DIR):

        print(f"\nProcessing file: {file}")

        process_file(
            os.path.join(DATA_DIR, file)
        )

    print("\nIngestion Completed")


if __name__ == "__main__":
    ingest_documents()