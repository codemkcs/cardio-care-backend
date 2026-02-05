import re
from .schema import EXPECTED_FIELDS
from .preprocess import normalize

FIELD_PATTERNS = {
    "age": r"age\s*[:\-]?\s*(\d{2,3})",
    "bmi": r"bmi\s*[:\-]?\s*([\d.]+)",
    "whr": r"whr\s*[:\-]?\s*([\d.]+)",
    "fbs": r"(fbs|fasting blood sugar)\s*[:\-]?\s*([\d.]+)",
    "hba1c": r"hba1c\s*[:\-]?\s*([\d.]+)",
    "hdl": r"hdl\s*[:\-]?\s*([\d.]+)",
    "ldl": r"ldl\s*[:\-]?\s*([\d.]+)",
    "vldl": r"vldl\s*[:\-]?\s*([\d.]+)",
    "tgl": r"(triglycerides|tgl)\s*[:\-]?\s*([\d.]+)",
    "tc": r"(total cholesterol|tc)\s*[:\-]?\s*([\d.]+)",
    "creatinine": r"creatinine\s*[:\-]?\s*([\d.]+)",
    "systolic": r"(bp|blood pressure)\s*[:\-]?\s*(\d{2,3})\s*/",
    "diastolic": r"(bp|blood pressure)\s*[:\-]?\s*\d{2,3}\s*/\s*(\d{2,3})",
}

def map_fields(texts):
    joined = normalize(" ".join(texts))
    output = {}

    for field, pattern in FIELD_PATTERNS.items():
        match = re.search(pattern, joined)
        if match:
            value = match.groups()[-1]
            output[field] = float(value)

    return output
