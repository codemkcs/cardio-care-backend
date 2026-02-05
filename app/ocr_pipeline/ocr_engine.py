from PIL import Image
import pytesseract

def extract_text_with_boxes(image_path: str):
    """
    SAFE OCR ENGINE
    - No OpenCV
    - No system-level crash
    - Always returns list[str]
    """

    try:
        img = Image.open(image_path)

        text = pytesseract.image_to_string(img)

        if not text or not text.strip():
            return []

        return [text.lower()]

    except Exception:
        # ❗ NEVER crash backend
        return []
