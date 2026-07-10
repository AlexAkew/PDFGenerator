class PDFGeneratorError(Exception):
    """Base exception."""


class PDFOpenError(PDFGeneratorError):
    """Cannot open PDF."""


class TemplateError(PDFGeneratorError):
    """Template is invalid."""