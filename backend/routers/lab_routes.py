from fastapi import  APIRouter,status
from fastapi.responses import JSONResponse
from schemas.lab_response import HeartDiseaseResponse
from schemas.lab_forms import HeartDiseaseForm
from utils.model_loader import load_models
from utils.prediction_functions import predict_heart_disease

router=APIRouter(
    prefix='/lab',
    tags=["Lab Disease Prediction Routes"],
)


@router.post('/predict_heart',response_model=HeartDiseaseResponse)
def predict_heart(data: HeartDiseaseForm):
    input_data = {
        'age': [data.age],
        'sex': [data.sex],
        'Chest pain type': [data.chest_pain_type],
        'BP': [data.bp],
        'Cholesterol': [data.cholesterol],
        'EKG results': [data.ekg_results],
        'MAX HR': [data.max_hr],
        'Exercise angina': [data.exercise_angina],
        'ST depression': [data.st_depression],
        'Slope of ST': [data.slope_of_st],
        'Number of vessels fluro': [data.number_of_vessels_fluro],
        'Thallium': [data.thallium]
    }

    try:      
        prediction = predict_heart_disease(input_data)
        return JSONResponse(status_code=status.HTTP_200_OK, content={'predicted_category': prediction})

    except Exception as e:
        return  JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,content=str(e))
