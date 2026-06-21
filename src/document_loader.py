import os

from pypdf import PdfReader
from docx import Document


def load_pdf(path):
    docs = []

    reader = PdfReader(path)

    for page_num, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        if text:

            docs.append({
                "text": text,
                "metadata": {
                    "source": os.path.basename(path),
                    "page": page_num
                }
            })

    return docs


def load_docx(path):

    doc = Document(path)

    text = "\n".join(
        para.text for para in doc.paragraphs
    )

    return [{
        "text": text,
        "metadata": {
            "source": os.path.basename(path),
            "page": 1
        }
    }]


def load_txt(path):

    with open(path, encoding="utf-8") as f:

        text = f.read()

    return [{
        "text": text,
        "metadata": {
            "source": os.path.basename(path),
            "page": 1
        }
    }]