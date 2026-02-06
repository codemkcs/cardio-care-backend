import re
from .preprocess import normalize

def fix_decimal(num: str) -> float:
    """
    Converts '25 3' → 25.3
    Converts '0 84' → 0.84
    """
    parts = num.strip().split()
    if len(parts) == 2:
        return float(parts[0] + "." + parts[1])
    return float(parts[0])

FIELD_PATTERNS = {
    "age": r"\bage\s+(\d{1,3})",
    "bmi": r"\bbmi\s+(\d+\s*\d*)",
    "whr": r"\bwhr\s+(\d+\s*\d*)",
    "fbs": r"\bfbs\s+(\d+)",
    "hba1c": r"\bhba1c\s+(\d+\s*\d*)",
    "hdl": r"\bhdl\s+(\d+)",
    "ldl": r"\bldl\s+(\d+)",
    "vldl": r"\bvldl\s+(\d+)",
    "tgl": r"\b(tgl|triglycerides)\s+(\d+)",
    "tc": r"\b(tc|total cholesterol)\s+(\d+)",
    "creatinine": r"\bcreatinine\s+(\d+\s*\d*)",
    "systolic": r"\bsystolic\s+bp\s+(\d{2,3})",
    "diastolic": r"\bdiastolic\s+bp\s+(\d{2,3})",
}

def map_fields(texts: list) -> dict:
    joined = normalize(" ".join(texts))
    output = {}

    for field, pattern in FIELD_PATTERNS.items():
        match = re.search(pattern, joined)
        if not match:
            continue

        value = match.groups()[-1]

        try:
            if " " in value:
                output[field] = fix_decimal(value)
            else:
                output[field] = float(value)
        except Exception:
            pass

    return output
