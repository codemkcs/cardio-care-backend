import re
from .preprocess import normalize

FIELD_PATTERNS = {
    "age": r"\bage\s*[:\-]?\s*(\d{1,3})",
    "bmi": r"\bbmi\s*[:\-]?\s*([\d.]+)",
    "whr": r"\bwhr\s*[:\-]?\s*([\d.]+)",
    "fbs": r"\bfbs\s*[:\-]?\s*([\d.]+)",
    "hba1c": r"\bhba1c\s*[:\-]?\s*([\d.]+)",
    "hdl": r"\bhdl\s*[:\-]?\s*([\d.]+)",
    "ldl": r"\bldl\s*[:\-]?\s*([\d.]+)",
    "vldl": r"\bvldl\s*[:\-]?\s*([\d.]+)",
    "tgl": r"\b(tgl|triglycerides)\s*[:\-]?\s*([\d.]+)",
    "tc": r"\b(tc|total cholesterol)\s*[:\-]?\s*([\d.]+)",
    "creatinine": r"\bcreatinine\s*[:\-]?\s*([\d.]+)",
    "systolic": r"\bsystolic\s*bp\s*[:\-]?\s*(\d{2,3})",
    "diastolic": r"\bdiastolic\s*bp\s*[:\-]?\s*(\d{2,3})",
}

def map_fields(texts: list) -> dict:
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
