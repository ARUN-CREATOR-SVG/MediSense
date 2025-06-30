import pandas as pd
from PIL import Image
import numpy as np
import tensorflow as tf
from fastapi import UploadFile
from io import BytesIO
from ..utils.model_loader import load_models

models=load_models()

labels = {0: "NORMAL", 1: "PNEUMONIA"}

async def predict_pneumonia_disease(file: UploadFile):
    if 'pneumonia' not in models:
        raise ValueError("Pneumonia model not loaded")

    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("RGB")
    image = image.resize((224, 224)) 
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    model = models['pneumonia']
    prob = float(model.predict(image_array)[0][0])
    pred_class = 1 if prob > 0.5 else 0
    label = labels[pred_class]

    confidence = round((prob if prob > 0.5 else 1 - prob) * 100, 2)

    return {
        "prediction": label,
        "confidence": confidence
    }


def _predict_from_model(model, data: dict):
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    return {
        'prediction': int(prediction),
        'probability': round(float(probability), 3),
        'risk_level': 'Low' if probability < 0.4 else 'Medium' if probability < 0.7 else 'High',
    }


def predict_heart_disease(data:dict):
    if 'heart' not in models:
        raise ValueError("Heart model not loaded")

    return _predict_from_model(models['heart'],data)

def predict_liver_disease(data:dict):
    if 'liver' not in models:
        raise ValueError("Liver model not loaded")

    return _predict_from_model(models['liver'],data)

def predict_diabetes_disease(data:dict):
    if 'diabetes' not in models:
        raise ValueError("Diabetes model not loaded")
    return _predict_from_model(models['diabetes'],data)