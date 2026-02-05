from fastapi import APIRouter, UploadFile, File
import shutil
from pathlib import Path
from app.ocr_pipeline.ocr_engine import extract_text_with_boxes
from app.ocr_pipeline.field_mapper import map_fields

router = APIRouter()

UPLOAD_DIR = Path("uploads/reports")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/ocr/upload")
async def ocr_upload(file: UploadFile = File(...)):
    path = UPLOAD_DIR / file.filename
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    texts = extract_text_with_boxes(str(path))
    mapped = map_fields(texts)

    return {
        "extracted_fields": mapped
    }
