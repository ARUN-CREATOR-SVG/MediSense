from fastapi import  APIRouter,status
from fastapi.responses import JSONResponse
from schemas.lab_response import HeartDiseaseResponse,LiverDiseaseResponse
from schemas.lab_forms import HeartDiseaseForm,LiverDiseaseForm
from utils.model_loader import load_models
from utils.prediction_functions import predict_heart_disease,predict_liver_disease

router=APIRouter(
    prefix='/lab',
    tags=["Lab Disease Prediction Routes"],
)


@router.post('/predict_heart',response_model=HeartDiseaseResponse)
def predict_heart(data: HeartDiseaseForm):
    input_data = {
        'age': data.age,
        'sex': data.sex,
        'Chest pain type': data.chest_pain_type,
        'BP': data.bp,
        'Cholesterol': data.cholesterol,
        'EKG results': data.ekg_results,
        'MAX HR': data.max_hr,
        'Exercise angina': data.exercise_angina,
        'ST depression': data.st_depression,
        'Slope of ST': data.slope_of_st,
        'Number of vessels fluro': data.number_of_vessels_fluro,
        'Thallium': data.thallium
    }

    try:      
        prediction = predict_heart_disease(input_data)
        return JSONResponse(status_code=status.HTTP_200_OK, content={'predicted_category': prediction})

    except Exception as e:
        return  JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,content=str(e))

@router.post('/predict_liver',response_model=LiverDiseaseResponse)
def predict_liver(data:LiverDiseaseForm):
    input_data={
        'Age': data.Age,
        'Gender':data.Gender,
        'Total_Bilirubin':data.Total_Bilirubin,
        'Direct_Bilirubin':data.Direct_Bilirubin,
        'Alkaline_Phosphotase':data.Alkaline_Phosphotase,
        'Alamine_Aminotransferase':data.Alamine_Aminotransferase,
        'Aspartate_Aminotransferase': data.Aspartate_Aminotransferase,
        'Total_Protiens':data.Total_Protiens,
        'Albumin':data.Albumin,
        'Albumin_and_Globulin_Ratio':data.Albumin_and_Globulin_Ratio
        }
    try:
        prediction = predict_liver_disease(input_data)
        return JSONResponse(status_code=status.HTTP_200_OK, content={'predicted_category': prediction})

    except Exception as e:
        return  JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,content=str(e))
