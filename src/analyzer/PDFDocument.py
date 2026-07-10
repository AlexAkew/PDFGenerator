class PDFDocument:
    def __init__(self, path: Path):
        ...

    @property
    def page_count(self) -> int:
        ...

    def page(self, number: int) -> PDFPage:
        ...