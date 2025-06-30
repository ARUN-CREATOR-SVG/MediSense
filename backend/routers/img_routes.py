from fastapi import APIRouter, UploadFile, File, status
from fastapi.responses import JSONResponse
from schemas.img_response  import PneumoniaPredictionResponse
from utils.prediction_functions import predict_pneumonia_disease

router = APIRouter(
    prefix="/image",
    tags=["Medical Image Prediction Routes"],
)

@router.post("/predict_pneumonia", response_model=PneumoniaPredictionResponse)
async def predict_pneumonia(file: UploadFile = File(...)):
    try:
        result = await predict_pneumonia_disease(file)
        return result
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": str(e)})
