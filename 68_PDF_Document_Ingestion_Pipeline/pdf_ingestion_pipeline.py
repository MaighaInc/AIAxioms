"""
PDF Document Ingestion Pipeline
-------------------------------
This program ingests a PDF document,
extracts text, and splits it into chunks
ready for embedding and retrieval.

Author: AI Course
"""

from PyPDF2 import PdfReader


class PDFIngestionPipeline:
    def extract_text(self, pdf_path):
        reader = PdfReader(pdf_path)
        full_text = ""

        for page in reader.pages:
            full_text += page.extract_text() + "\n"

        return full_text.strip()

    def chunk_text(self, text, chunk_size=50):
        words = text.split()
        chunks = []

        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i + chunk_size])
            chunks.append(chunk)

        return chunks


def main():
    print("PDF DOCUMENT INGESTION PIPELINE")
    print("--------------------------------")

    pdf_path = "sample.pdf"  # replace with your PDF file

    pipeline = PDFIngestionPipeline()

    try:
        text = pipeline.extract_text(pdf_path)
        chunks = pipeline.chunk_text(text)

        print(f"\nExtracted {len(chunks)} chunks:\n")
        for i, chunk in enumerate(chunks[:3]):
            print(f"Chunk {i + 1}:\n{chunk}\n")

    except FileNotFoundError:
        print("\n⚠️ PDF file not found. Please place a PDF named 'sample.pdf' in this folder.")


if __name__ == "__main__":
    main()
