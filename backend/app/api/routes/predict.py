from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File

from app.services.recognition_service import predict_actor

router = APIRouter()

UPLOAD_DIR = Path("app/cache/predictions")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/predict")
async def predict(file: UploadFile = File(...)):

    image_path = UPLOAD_DIR / file.filename

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = predict_actor(image_path)

    if result is None:
        return {
            "success": False,
            "message": "No face detected."
        }

    return {
        "success": True,
        **result
    }