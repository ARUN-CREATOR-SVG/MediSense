import streamlit as st
import requests
from ui_utils import display_result
from llm_util import get_llm_analysis

def render_heart_module(API_BASE_lab):
    st.markdown('''
    <div>
        <h2>💓 Heart Disease Prediction</h2>
        <p>Advanced ML Model for Cardiovascular Risk Assessment</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('<div class="box">', unsafe_allow_html=True)

    with st.form("heart_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### 👤 Personal Information")
            age = st.number_input("Age", 1.0, 120.0, 50.0)
            sex = st.selectbox("Sex", ["Male", "Female"])
            chest_pain_type = st.selectbox(
                "Chest Pain Type", [0, 1, 2, 3],
                help="0: Typical Angina, 1: Atypical Angina, 2: Non-anginal Pain, 3: Asymptomatic"
            )
            bp = st.number_input("Blood Pressure", 80.0, 200.0, 120.0)
            cholesterol = st.number_input("Cholesterol", 100.0, 600.0, 200.0)
        
        with col2:
            st.markdown("#### 🩺 Medical Tests")
            ekg_results = st.selectbox(
                "EKG Results",
                [0, 1, 2],
                help="0: Normal, 1: ST-T wave abnormality, 2: Left ventricular hypertrophy"
            )
            max_hr = st.number_input(
                "Max Heart Rate Achieved", 
                60.0, 220.0, 150.0,
                help="Maximum heart rate achieved during exercise stress test (in beats per minute)"
            )
            exercise_angina = st.selectbox("Exercise Induced Angina", [0, 1])
            st_depression = st.number_input("ST Depression", 0.0, 10.0, 1.0)
        
        with col3:
            st.markdown("#### 🔬 Advanced Parameters")
            slope_of_st = st.selectbox(
                "Slope of ST", 
                [0, 1, 2],
                help="Slope of the ST segment during peak exercise: 0 = Upsloping, 1 = Flat, 2 = Downsloping"
            )
            number_of_vessels_fluro = st.selectbox("Number of Vessels Fluro", [0, 1, 2, 3, 4])
            thallium = st.selectbox(
                "Thallium", 
                [1, 2, 3],
                help="Thallium stress test result: 1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect"
            )
        
        submitted = st.form_submit_button("🔍 Analyze Heart Health")

    if submitted:
        input_data = {
            "age": age,
            "sex": 1 if sex == "Male" else 0,
            "Chest pain type": chest_pain_type,
            "BP": bp,
            "Cholesterol": cholesterol,
            "EKG results": ekg_results,
            "MAX HR": max_hr,
            "Exercise angina": exercise_angina,
            "ST depression": st_depression,
            "Slope of ST": slope_of_st,
            "Number of vessels fluro": number_of_vessels_fluro,
            "Thallium": thallium
        }

        try:
            response = requests.post(f"{API_BASE_lab}/predict_heart", json=input_data)
            if response.status_code == 200:
                result = response.json()
                prediction_text = "❤️ Heart Disease Detected" if result['prediction'] else "💚 Heart Healthy"
                display_result(prediction_text, result["probability"], result.get("risk_level", ""))
                
                # Save prediction & input for LLM call outside form
                st.session_state["heart_pred"] = {
                    "prediction_text": prediction_text,
                    "probability": result.get("probability", 0),
                    "risk_level": result.get("risk_level", ""),
                    "input_data": input_data
                }

            else:
                st.error("❌ Server Error")
        except Exception as e:
            st.error(f" API Error: {e}")

    # Button OUTSIDE form for LLM detailed analysis
    if "heart_pred" in st.session_state:
        if st.button("🔎 Click for More Analysis"):
            with st.spinner("🧠 Fetching detailed AI analysis..."):
                pred = st.session_state["heart_pred"]
                llm_response = get_llm_analysis(
                    prediction=pred["prediction_text"],
                    risk_score=pred["probability"],
                    input_data=pred["input_data"]
                )
                st.markdown("### 📝 Detailed AI Analysis")
                st.write(llm_response)

    st.markdown('</div>', unsafe_allow_html=True)
    
   