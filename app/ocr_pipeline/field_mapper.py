import re
from .schema import EXPECTED_FIELDS
from .preprocess import normalize

FIELD_PATTERNS = {
    "age": r"\bage\b\s*[:\-]?\s*(\d{2,3})",
    "bmi": r"\bbmi\b\s*[:\-]?\s*([\d.]+)",
    "whr": r"\bwhr\b\s*[:\-]?\s*([\d.]+)",
    "fbs": r"(fbs|fasting blood sugar)\s*[:\-]?\s*([\d.]+)",
    "hba1c": r"\bhba1c\b\s*[:\-]?\s*([\d.]+)",
    "hdl": r"\bhdl\b\s*[:\-]?\s*([\d.]+)",
    "ldl": r"\bldl\b\s*[:\-]?\s*([\d.]+)",
    "vldl": r"\bvldl\b\s*[:\-]?\s*([\d.]+)",
    "tgl": r"(triglycerides|tgl)\s*[:\-]?\s*([\d.]+)",
    "tc": r"(total cholesterol|tc)\s*[:\-]?\s*([\d.]+)",
    "creatinine": r"\bcreatinine\b\s*[:\-]?\s*([\d.]+)",
    "systolic": r"(bp|blood pressure)\s*[:\-]?\s*(\d{2,3})\s*/",
    "diastolic": r"(bp|blood pressure)\s*[:\-]?\s*\d{2,3}\s*/\s*(\d{2,3})",
}

def map_fields(texts: list) -> dict:
    """
    HARD FIELD MAPPER:
    BMI → BMI only
    HDL → HDL only
    """
    joined = normalize(" ".join(texts))
    output = {}

    for field, pattern in FIELD_PATTERNS.items():
        match = re.search(pattern, joined)
        if match:
            value = match.groups()[-1]
            try:
                output[field] = float(value)
            except ValueError:
                pass

    return output
