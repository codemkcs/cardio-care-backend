import re

def normalize(text: str) -> str:
    """
    Normalize OCR text for regex matching.
    Keeps digits, dots, slashes.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9./\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()
