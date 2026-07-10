from pathlib import Path
import fitz


class PDFDocument:
    def __init__(self, path: Path):
        self._doc = fitz.open(path)

    @property
    def page_count(self) -> int:
        return self._doc.page_count

    @property
    def pages(self):
        return self._doc