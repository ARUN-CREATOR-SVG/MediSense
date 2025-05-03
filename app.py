from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np
import pandas as pd
import os
from flask_cors import CORS
from PIL import Image
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)

# Load models
MODEL_DIR = r"C:\Users\Ankit\Desktop\MediSense\Models"
with open(os.path.join(MODEL_DIR, "Heart_Disease_model.pkl"), 'rb') as f:
    heart_model = pickle.load(f)

pneumonia_model = load_model(os.path.join(MODEL_DIR, "pneumonia_cnn_model.keras"))

# --- MAPPINGS ---
MAPPINGS = {
    'sex': {'Male': 1, 'Female': 0, '0': 0, '1': 1},
    'chestPainType': {'Type 1': 0, 'Type 2': 1, 'Type 3': 2, 'Type 4': 3, '0': 0, '1': 1, '2': 2, '3': 3},
    'ekgResults': {'Normal': 0, 'ST-T Wave Abnormality': 1, 'Left Ventricular Hypertrophy': 2, '0': 0, '1': 1, '2': 2},
    'exerciseAngina': {'No': 0, 'Yes': 1, '0': 0, '1': 1},
    'slopeOfST': {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2, '0': 0, '1': 1, '2': 2},
    'numberOfVesselsFluro': {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4},
    'thallium': {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2, '0': 0, '1': 1, '2': 2}
}

# --- HELPERS ---
def safe_get_categorical(data, key, default_key):
    raw_value = data.get(key, default_key)
    mapping = MAPPINGS.get(key, {})
    return mapping.get(str(raw_value), mapping.get(str(default_key), 0))

def safe_get_float(data, key, default=0.0):
    try:
        return float(data.get(key, default))
    except (ValueError, TypeError):
        return default

# --- ROUTES ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/heart_disease')
def heart_disease():
    return render_template('heart_disease.html')

@app.route('/predict', methods=['POST'])
def predict_heart():
    try:
        data = request.get_json() if request.is_json else request.form

        input_data = {
            'age': safe_get_float(data, 'age'),
            'sex': safe_get_categorical(data, 'sex', 'Male'),
            'Chest pain type': safe_get_categorical(data, 'chestPainType', 'Type 1'),
            'BP': safe_get_float(data, 'bp'),
            'Cholesterol': safe_get_float(data, 'cholesterol'),
            'EKG results': safe_get_categorical(data, 'ekgResults', 'Normal'),
            'MAX HR': safe_get_float(data, 'maxHR'),
            'Exercise angina': safe_get_categorical(data, 'exerciseAngina', 'No'),
            'ST depression': safe_get_float(data, 'stDepression'),
            'Slope of ST': safe_get_categorical(data, 'slopeOfST', 'Upsloping'),
            'Number of vessels fluro': safe_get_categorical(data, 'numberOfVesselsFluro', '0'),
            'Thallium': safe_get_categorical(data, 'thallium', 'Normal')
        }

        input_df = pd.DataFrame([input_data])
        prediction = heart_model.predict(input_df)[0]
        probability = heart_model.predict_proba(input_df)[0][1]

        return jsonify({
            'prediction': int(prediction),
            'probability': round(probability, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/predict_pneumonia", methods=["POST"])
def predict_pneumonia():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    try:
        file = request.files['image']
        img = Image.open(file).convert("L").resize((256, 256))
        img_array = np.expand_dims(np.expand_dims(np.array(img) / 255.0, axis=-1), axis=0)

        pred = float(pneumonia_model.predict(img_array)[0][0])
        diagnosis = "Pneumonia" if pred >= 0.5 else "Normal"
        confidence = round((pred if diagnosis == "Pneumonia" else 1 - pred) * 100, 2)

        return jsonify({
            "prediction": diagnosis,
            "confidence": f"{confidence}%"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- MAIN ---
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
