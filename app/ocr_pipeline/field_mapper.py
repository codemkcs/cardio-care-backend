import re
from .preprocess import normalize

FIELD_REGEX = {
    "age": r"\bage\b[^0-9]{0,10}(\d{2,3})",
    "bmi": r"\bbmi\b[^0-9]{0,10}([\d.]+)",
    "whr": r"\bwhr\b[^0-9]{0,10}([\d.]+)",
    "fbs": r"(fbs|fasting blood sugar)[^0-9]{0,15}([\d.]+)",
    "hba1c": r"(hba1c|hbaic|hbale)[^0-9]{0,10}([\d.]+)",
    "hdl": r"\bhdl\b[^0-9]{0,15}([\d.]+)",
    "ldl": r"\bldl\b[^0-9]{0,15}([\d.]+)",
    "vldl": r"\bvldl\b[^0-9]{0,15}([\d.]+)",
    "tgl": r"(tgl|triglycerides)[^0-9]{0,15}([\d.]+)",
    "tc": r"(tc|total cholesterol)[^0-9]{0,15}([\d.]+)",
    "creatinine": r"\bcreatinine\b[^0-9]{0,15}([\d.]+)",
    "bp": r"(\d{2,3})\s*/\s*(\d{2,3})",
}

def map_fields(texts: list) -> dict:
    text = normalize(" ".join(texts))
    output = {}

    for field, pattern in FIELD_REGEX.items():
        match = re.search(pattern, text)
        if match:
            if field == "bp":
                output["systolic"] = float(match.group(1))
                output["diastolic"] = float(match.group(2))
            else:
                value = match.groups()[-1]
                output[field] = float(value)

    return output
