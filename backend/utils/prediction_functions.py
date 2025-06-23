import pandas as pd
from utils.model_loader import load_models

models=load_models()

def predict_heart_disease(data:dict):
    if 'heart' not in models:
        raise ValueError("Heart model not loaded")

    input_df = pd.DataFrame([data])
    prediction = models['heart'].predict(input_df)[0]
    probability = models['heart'].predict_proba(input_df)[0][1]

    return {
        'prediction': int(prediction),
        'probability': round(float(probability), 3),
        'risk_level': 'Low' if probability < 0.4 else 'Medium' if probability < 0.7 else 'High',
    }

def predict_liver_disease(data:dict):
    if 'liver' not in models:
        raise ValueError("Liver model not loaded")

    input_df = pd.DataFrame([data])
    prediction = models['liver'].predict(input_df)[0]
    probability = models['liver'].predict_proba(input_df)[0][1]

    return {
        'prediction': int(prediction),
        'probability': round(float(probability), 3),
        'risk_level': 'Low' if probability < 0.4 else 'Medium' if probability < 0.7 else 'High',
    }