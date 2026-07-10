from pathlib import Path

from src.pdf.document import PDFDocument


def main():
    doc = PDFDocument(Path("input/originalAccount report Contomobile-1.pdf"))

    print(f"Pages: {doc.page_count}")


if __name__ == "__main__":
    main()