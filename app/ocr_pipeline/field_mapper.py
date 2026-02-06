import re
from .preprocess import normalize

# ======================================================
# ROBUST FIELD PATTERNS (TABLE + INLINE SAFE)
# ======================================================

FIELD_PATTERNS = {
    "age": r"age.*?(\d+)",
    "bmi": r"bmi.*?([\d.]+)",
    "whr": r"whr.*?([\d.]+)",
    "hba1c": r"hba1c.*?([\d.]+)",
    "fbs": r"fbs.*?(\d+)",
    "hdl": r"hdl.*?(\d+)",
    "ldl": r"ldl.*?(\d+)",
    "vldl": r"vldl.*?(\d+)",
    "tc": r"(total cholesterol|tc).*?(\d+)",
    "tgl": r"(triglycerides|tgl).*?(\d+)",
    "creatinine": r"creatinine.*?([\d.]+)",
    "systolic": r"systolic.*?(\d+)",
    "diastolic": r"diastolic.*?(\d+)",
}

# ======================================================
# FIELD MAPPER
# ======================================================

def map_fields(texts: list) -> dict:
    if not texts:
        return {}

    text = normalize(" ".join(texts))

    # remove units
    text = re.sub(r"(mg\/dl|mmhg|kg\/m2|kg m2|%)", "", text)

    output = {}

    for field, pattern in FIELD_PATTERNS.items():
        match = re.search(pattern, text)
        if match:
            value = match.groups()[-1]
            try:
                output[field] = float(value)
            except ValueError:
                pass

    return output
