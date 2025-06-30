# ⚕️ MediSense – Multi-Disease AI Diagnosis System

MediSense is an AI-powered diagnostic tool designed to assist in early detection and risk assessment of multiple diseases using Machine Learning (ML) and Deep Learning (DL). The system currently supports **Heart Disease**, **Diabetes**, **Liver Disease**, and **Pneumonia (X-ray)** detection.

---

## 🚀 Live Demo

🔗 **App Link**: [MediSense on Streamlit](https://medisense-ai.streamlit.app)

---

## 🧠 Technologies Used

| Category       | Technologies                           |
|----------------|----------------------------------------|
| **Frontend**   | Streamlit                              |
| **Backend**    | FastAPI                                |
| **ML Libraries** | scikit-learn, XGBoost                |
| **DL Libraries** | TensorFlow, Keras                    |
| **Others**     | pandas, numpy, PIL, requests           |

---

## 🩺 Disease Modules

### 💓 1. Heart Disease
- Uses classification ML model for prediction
- Input: Age, Sex, Chest pain type, Blood Pressure, Cholesterol, EKG results, Max HR, etc.
- ✅ Dataset: [UCI Heart Disease – Cleveland](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci)

---

### 🩸 2. Diabetes
- Predicts diabetes risk based on lifestyle and medical indicators
- Input: HighBP, HighChol, BMI, Smoker, Age, Physical Activity, etc.
- ✅ Dataset: [Diabetes Health Indicators BRFSS 2015](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?resource=download&select=diabetes_binary_5050split_health_indicators_BRFSS2015.csv)

---

### 🧪 3. Liver Disease
- Classifies whether a patient has liver disease or not
- Input: Age, Gender, Bilirubin levels, Enzymes, Proteins, A/G Ratio, etc.
- ✅ Dataset: [Indian Liver Patient Records (ILPD)](https://www.kaggle.com/datasets/uciml/indian-liver-patient-records)

---

### 🫁 4. Pneumonia Detection (X-ray)
- Deep Learning (CNN) model for detecting pneumonia in chest X-ray images
- Input: JPG/PNG image of chest X-ray
- ✅ Dataset: [Paul Mooney's Chest X-ray Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

---


## 🧑‍💻 How to Run Locally

```
# Step 1: Clone the repository
git clone https://github.com/ARUN-CREATOR-SVG/MediSense.git
cd MediSense

# Step 2: Create a virtual environment
python -m venv venv

# Step 3: Activate the virtual environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

# Step 4: Install dependencies
pip install -r frontend/requirements.txt
pip install -r backend/requirements.txt

# Step 5: Run the Streamlit app
streamlit run frontend/frontend.py
```

## 📬 Contact

**Arun Singh**  
📧 [arunsin2212@gmail.com](mailto:arunsin2212@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/arun-singh-7a7b9b289/)
