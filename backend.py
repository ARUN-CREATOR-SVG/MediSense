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

# Load heart disease model
with open(r"C:\Users\Ankit\Desktop\MediSense\Models\Heart_Disease_model.pkl", 'rb') as f:
    model = pickle.load(f)

# Load pneumonia CNN model
pneumonia_model = load_model(r"C:\Users\Ankit\Desktop\MediSense\Models\pneumonia_cnn_model.keras")

# --- MAPPINGS ---
chest_pain_mapping = {'Type 1': 0, 'Type 2': 1, 'Type 3': 2, 'Type 4': 3, '0': 0, '1': 1, '2': 2, '3': 3}
ekg_result_mapping = {'Normal': 0, 'ST-T Wave Abnormality': 1, 'Left Ventricular Hypertrophy': 2, '0': 0, '1': 1, '2': 2}
exercise_angina_mapping = {'No': 0, 'Yes': 1, '0': 0, '1': 1}
slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2, '0': 0, '1': 1, '2': 2}
vessels_mapping = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}
thallium_mapping = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2, '0': 0, '1': 1, '2': 2}
sex_mapping = {'Male': 1, 'Female': 0, '0': 0, '1': 1}

# --- ROUTES ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/heart_disease')
def heart_disease():
    return render_template('heart_disease.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        def safe_get_categorical(data_dict, key, mapping_dict, default_key):
            raw_value = data_dict.get(key, default_key)
            mapped_value = mapping_dict.get(raw_value, None)
            if mapped_value is not None:
                return mapped_value
            try:
                numeric_value = int(raw_value)
                if numeric_value in set(mapping_dict.values()):
                    return numeric_value
            except (ValueError, TypeError):
                pass
            return mapping_dict.get(default_key)

        def safe_get_float(data_dict, key, default_value=0.0):
            try:
                return float(data_dict.get(key, default_value))
            except (ValueError, TypeError):
                return default_value

        # Extract inputs
        sex = safe_get_categorical(data, 'sex', sex_mapping, 'Male')
        chest_pain = safe_get_categorical(data, 'chestPainType', chest_pain_mapping, 'Type 1')
        ekg_results = safe_get_categorical(data, 'ekgResults', ekg_result_mapping, 'Normal')
        exercise_angina = safe_get_categorical(data, 'exerciseAngina', exercise_angina_mapping, 'No')
        slope = safe_get_categorical(data, 'slopeOfST', slope_mapping, 'Upsloping')
        vessels = safe_get_categorical(data, 'numberOfVesselsFluro', vessels_mapping, '0')
        thallium = safe_get_categorical(data, 'thallium', thallium_mapping, 'Normal')
        age = safe_get_float(data, 'age')
        bp = safe_get_float(data, 'bp')
        cholesterol = safe_get_float(data, 'cholesterol')
        max_hr = safe_get_float(data, 'maxHR')
        st_depression = safe_get_float(data, 'stDepression')

        input_df = pd.DataFrame({
            'age': [age],
            'sex': [sex],
            'Chest pain type': [chest_pain],
            'BP': [bp],
            'Cholesterol': [cholesterol],
            'EKG results': [ekg_results],
            'MAX HR': [max_hr],
            'Exercise angina': [exercise_angina],
            'ST depression': [st_depression],
            'Slope of ST': [slope],
            'Number of vessels fluro': [vessels],
            'Thallium': [thallium]
        })

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

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
        img = Image.open(file).convert("L")              # Convert to grayscale
        img = img.resize((256, 256))                    # Resize to 256x256
        img_array = np.array(img) / 255.0               # Normalize to [0, 1]
        img_array = np.expand_dims(img_array, axis=-1)  # Add channel dim: (256, 256, 1)
        img_array = np.expand_dims(img_array, axis=0)   # Add batch dim: (1, 256, 256, 1)

        prediction = float(pneumonia_model.predict(img_array)[0][0])  # Sigmoid output
        diagnosis = "Pneumonia" if prediction >= 0.5 else "Normal"
        confidence = prediction if diagnosis == "Pneumonia" else 1 - prediction
        confidence_percent = round(confidence * 100, 2)

        return jsonify({
            "prediction": diagnosis,
            "confidence": f"{confidence_percent}%",
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
