import streamlit as st
import requests
from ui_utils import display_result
from llm_util import get_llm_analysis

def render_diabetes_module(API_BASE_lab):
    st.markdown('''
    <div>
        <h2>🩸 Diabetes Prediction</h2>
        <p>Comprehensive ML Analysis for Diabetes Risk Assessment</p>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('<div class="box">', unsafe_allow_html=True)
    
    with st.form("diabetes_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### 🏥 Medical History")
            HighBP = st.selectbox("High Blood Pressure", [0, 1], format_func=lambda x: "Yes" if x else "No")
            HighChol = st.selectbox("High Cholesterol", [0, 1], format_func=lambda x: "Yes" if x else "No")
            CholCheck = st.selectbox("Cholesterol Check", [0, 1], format_func=lambda x: "Yes" if x else "No")
            BMI = st.number_input("BMI", 0.0, 100.0, 25.0)
            Smoker = st.selectbox("Smoker", [0, 1], format_func=lambda x: "Yes" if x else "No")
            Stroke = st.selectbox("Stroke History", [0, 1], format_func=lambda x: "Yes" if x else "No")
            HeartDiseaseorAttack = st.selectbox("Heart Disease/Attack", [0, 1], format_func=lambda x: "Yes" if x else "No")
        
        with col2:
            st.markdown("#### 🏃 Lifestyle Factors")
            PhysActivity = st.selectbox("Physical Activity", [0, 1], format_func=lambda x: "Yes" if x else "No")
            Fruits = st.selectbox("Fruits Consumption", [0, 1], format_func=lambda x: "Yes" if x else "No")
            Veggies = st.selectbox("Vegetables Consumption", [0, 1], format_func=lambda x: "Yes" if x else "No")
            HvyAlcoholConsump = st.selectbox("Heavy Alcohol Consumption", [0, 1], format_func=lambda x: "Yes" if x else "No")
            AnyHealthcare = st.selectbox("Healthcare Access", [0, 1], format_func=lambda x: "Yes" if x else "No")
            NoDocbcCost = st.selectbox("No Doctor Due to Cost", [0, 1], format_func=lambda x: "Yes" if x else "No")
        
        with col3:
            st.markdown("#### 📊 Health Metrics")
            GenHlth = st.slider("General Health", 1, 5, 3, help="1=Excellent, 5=Poor")
            MentHlth = st.slider("Mental Health (days)", 0, 30, 5, help="Number of days in past 30 days mentally unwell")
            PhysHlth = st.slider("Physical Health (days)", 0, 30, 7, help="Number of days in past 30 days physically unwell")
            DiffWalk = st.selectbox("Difficulty Walking", [0, 1], format_func=lambda x: "Yes" if x else "No")
            Sex = st.selectbox("Sex", ["Male", "Female"])
            Age = st.slider("Age", 0, 100, 55)
            Education = st.slider("Education Level", 1, 6, 5, help="1=Never, 6=Graduate")
            Income = st.slider("Income Level", 1, 8, 4, help="1=Lowest, 8=Highest")
        
        submitted = st.form_submit_button("🔍 Analyze Diabetes Risk")

    if submitted:
        input_data = {
            "HighBP": HighBP, "HighChol": HighChol, "CholCheck": CholCheck,
            "BMI": BMI, "Smoker": Smoker, "Stroke": Stroke,
            "HeartDiseaseorAttack": HeartDiseaseorAttack, "PhysActivity": PhysActivity,
            "Fruits": Fruits, "Veggies": Veggies, "HvyAlcoholConsump": HvyAlcoholConsump,
            "AnyHealthcare": AnyHealthcare, "NoDocbcCost": NoDocbcCost,
            "GenHlth": GenHlth, "MentHlth": MentHlth, "PhysHlth": PhysHlth,
            "DiffWalk": DiffWalk, "Sex": 1 if Sex == "Male" else 0,
            "Age": Age, "Education": Education, "Income": Income
        }
        try:
            response = requests.post(f"{API_BASE_lab}/predict_diabetes", json=input_data)
            if response.status_code == 200:
                result = response.json()
                prediction_text = "🩸 Diabetes Risk Detected" if result['prediction'] else "💚 Low Diabetes Risk"
                display_result(prediction_text, result["probability"], result.get("risk_level", ""))

                st.session_state["diabetes_pred"] = {
                    "prediction_text": prediction_text,
                    "probability": result.get("probability", 0),
                    "risk_level": result.get("risk_level", ""),
                    "input_data": input_data
                }
            else:
                st.error("❌ Server Error")
        except Exception as e:
            st.error(f" API Error: {e}")

    # More analysis button 
    if "diabetes_pred" in st.session_state:
        if st.button("🔎 Click for More Diabetes Analysis"):
            with st.spinner("🧠 Fetching detailed AI analysis..."):
                pred = st.session_state["diabetes_pred"]
                llm_response = get_llm_analysis(
                    prediction=pred["prediction_text"],
                    risk_score=pred["probability"],
                    input_data=pred["input_data"]
                )
                st.markdown("### 📝 Detailed AI Analysis")
                st.write(llm_response)

    st.markdown('</div>', unsafe_allow_html=True)
    
   