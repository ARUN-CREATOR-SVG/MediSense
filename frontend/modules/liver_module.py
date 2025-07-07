import streamlit as st
import requests
from ui_utils import display_result
from llm_util import get_llm_analysis

def render_liver_module(API_BASE_lab):
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
                
                st.session_state["liver_pred"] = {
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
    if "liver_pred" in st.session_state:
        if st.button("🔎 Click for More Liver Analysis"):
            with st.spinner("🧠 Fetching detailed AI analysis..."):
                pred = st.session_state["liver_pred"]
                llm_response = get_llm_analysis(
                    prediction=pred["prediction_text"],
                    risk_score=pred["probability"],
                    input_data=pred["input_data"]
                )
                st.markdown("### 📝 Detailed AI Analysis")
                st.write(llm_response)

    st.markdown('</div>', unsafe_allow_html=True)
    
   