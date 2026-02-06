import re
from .preprocess import normalize

# All aliases OCR may produce
FIELD_ALIASES = {
    "age": ["age"],
    "bmi": ["bmi"],
    "whr": ["whr"],
    "fbs": ["fbs", "fasting blood sugar"],
    "hba1c": ["hba1c", "hbale", "hbaic"],
    "hdl": ["hdl"],
    "ldl": ["ldl"],
    "vldl": ["vldl"],
    "tgl": ["tgl", "triglycerides"],
    "tc": ["tc", "total cholesterol"],
    "creatinine": ["creatinine"],
    "systolic": ["systolic"],
    "diastolic": ["diastolic"],
}

NUMBER_PATTERN = re.compile(r"\d+(\.\d+)?")

def map_fields(texts: list) -> dict:
    text = normalize(" ".join(texts))

    # remove units
    for unit in ["mg/dl", "mmhg", "%"]:
        text = text.replace(unit, "")

    tokens = text.split()
    output = {}

    for field, aliases in FIELD_ALIASES.items():
        for alias in aliases:
            if alias in tokens:
                idx = tokens.index(alias)

                # search forward for nearest number
                for j in range(idx + 1, min(idx + 6, len(tokens))):
                    if NUMBER_PATTERN.fullmatch(tokens[j]):
                        output[field] = float(tokens[j])
                        break

    return output
