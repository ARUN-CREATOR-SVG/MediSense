import streamlit as st
import requests
import pandas as pd
from PIL import Image
from ui_utils import load_css,display_result

st.set_page_config(
    page_title="MediSense - AI Diagnosis", 
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
# Main title with custom styling
st.markdown('<h1 class="main-title">MediSense - Multi-Disease AI Diagnosis System</h1>', unsafe_allow_html=True)

# Sidebar for module selection
st.sidebar.markdown("### 🧬 Disease Detection Modules")
module = st.sidebar.selectbox("🎯 Pick a Disease to Diagnose", ["Heart Disease", "Diabetes", "Liver Disease", "Pneumonia (X-ray)"])

st.sidebar.markdown("---")
st.sidebar.markdown("💡 **Tip:** Switch between different AI models to diagnose various conditions!")

API_BASE_lab = "http://localhost:8000/lab"
API_BASE_img = "http://localhost:8000/image"

# Heart Disease Module
if module == "Heart Disease":
    
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
                else:
                    st.error("❌ Server Error")
            except Exception as e:
                st.error(f" API Error: {e}")
    
    st.markdown('</div>', unsafe_allow_html=True)


# Diabetes Module
elif module == "Diabetes":
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
            MentHlth = st.slider(
                "Mental Health (days)", 
                0, 30, 5, 
                help="Number of days in the past 30 days when you felt mentally unwell (e.g., stress, depression, anxiety)"
            )

            PhysHlth = st.slider(
                "Physical Health (days)", 
                0, 30, 7, 
                help="Number of days in the past 30 days when your physical health was not good (e.g., illness, injury, fatigue)"
            )
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
                else:
                    st.error("❌ Server Error")
            except Exception as e:
                st.error(f" API Error: {e}")
    
    st.markdown('</div>', unsafe_allow_html=True)


# Liver Disease Module
elif module == "Liver Disease":
    st.markdown('''
    <div >
        <h2>🧪 Liver Disease Prediction</h2>
        <p>Advanced ML Model for Liver Function Assessment</p>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('<div class="box">', unsafe_allow_html=True)
    
    with st.form("liver_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 👤 Patient Information")
            Age = st.number_input("Age", 1.0, 120.0, 45.0)
            Gender = st.selectbox("Gender", ["Male", "Female"])
            
            st.markdown("#### 🧪 Bilirubin Levels")
            Total_Bilirubin = st.number_input("Total Bilirubin", 0.1, 75.0, 1.0, help="Measures total bilirubin in blood, high value may indicate liver issues")
            Direct_Bilirubin = st.number_input("Direct Bilirubin", 0.1, 20.0, 0.3, help="Direct bilirubin is the conjugated form processed by the liver")
            
            st.markdown("#### 🔬 Enzyme Levels")
            Alkaline_Phosphotase = st.number_input("Alkaline Phosphotase", 1.0, 2000.0, 200.0, help="High levels may indicate liver or bone disorders")

        
        with col2:
            st.markdown("#### 📊 Liver Function Tests")
            Alamine_Aminotransferase = st.number_input("SGPT (ALT)", 1.0, 2000.0, 30.0, help="Enzyme indicating liver inflammation or damage")
            Aspartate_Aminotransferase = st.number_input("SGOT (AST)", 1.0, 2000.0, 35.0, help="Another enzyme related to liver and heart function")
            
            st.markdown("#### 🧬 Protein Levels")
            Total_Protiens = st.number_input("Total Proteins", 1.0, 10.0, 7.0, help="Measures albumin and globulin; low levels may indicate liver or kidney issues")
            Albumin = st.number_input("Albumin", 0.1, 6.0, 4.0, help="A protein made by the liver; low levels can suggest liver disease")
            Albumin_and_Globulin_Ratio = st.number_input("A/G Ratio", 0.1, 2.5, 1.2, help="Ratio of albumin to globulin; imbalance may signal liver dysfunction")
        
        submitted = st.form_submit_button("🔍 Analyze Liver Health")

        if submitted:
            input_data = {
                "Age": Age, "Gender": 1 if Gender == "Male" else 0,
                "Total_Bilirubin": Total_Bilirubin, "Direct_Bilirubin": Direct_Bilirubin,
                "Alkaline_Phosphotase": Alkaline_Phosphotase,
                "Alamine_Aminotransferase": Alamine_Aminotransferase,
                "Aspartate_Aminotransferase": Aspartate_Aminotransferase,
                "Total_Protiens": Total_Protiens, "Albumin": Albumin,
                "Albumin_and_Globulin_Ratio": Albumin_and_Globulin_Ratio
            }
            try:
                response = requests.post(f"{API_BASE_lab}/predict_liver", json=input_data)
                if response.status_code == 200:
                    result = response.json()
                    prediction_text = "🧪 Liver Disease Detected" if result['prediction'] else "💚 Liver Healthy"
                    display_result(prediction_text, result["probability"], result.get("risk_level", ""))
                    
                else:
                    st.error("❌ Server Error")
            except Exception as e:
                st.error(f" API Error: {e}")
    
    st.markdown('</div>', unsafe_allow_html=True)


# Pneumonia Module (DL)
elif module == "Pneumonia (X-ray)":
    st.markdown('''
    <div >
        <h2>🫁 Pneumonia Detection</h2>
        <p>Deep Learning CNN Model for Chest X-ray Analysis</p>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('<div class="box">', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("📁 Upload Chest X-ray Image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image, caption="📸 Uploaded X-ray", use_container_width=True)
        
        st.markdown("---")
        
        if st.button("🔍 Analyze X-ray for Pneumonia"):
            with st.spinner("🤖 AI is analyzing the X-ray..."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    response = requests.post(f"{API_BASE_img}/predict_pneumonia", files=files)

                    if response.status_code == 200:
                        result = response.json()
                        prediction_text = f"🫁 {result['prediction']}"
                        st.success(f"✅ **Prediction:** {prediction_text}")
                        st.info(f"🎯 **Confidence Score:** {result['confidence'] :.2f}%")
                        
                        if "Pneumonia" in result['prediction']:
                            st.warning("⚠️ **Important:** Please consult with a healthcare professional for proper diagnosis and treatment.")
                        else:
                            st.info("💡 **Note:** This is a screening tool. Regular check-ups are still recommended.")
                            
                    else:
                        st.error("❌ Server Error")
                except Exception as e:
                    st.error(f" API Error: {e}")
    
    else:
        st.info("📤 Please upload a chest X-ray image to begin analysis")
    
    st.markdown('</div>', unsafe_allow_html=True)