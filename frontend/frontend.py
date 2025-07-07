import streamlit as st
from ui_utils import load_css, render_footer
from modules.heart_module import render_heart_module
from modules.diabetes_module import render_diabetes_module
from modules.liver_module import render_liver_module
from modules.pneumonia_model import render_pneumonia_module

st.set_page_config(
    page_title="MediSense - AI Diagnosis", 
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

st.markdown('<h1 class="main-title">MediSense - Multi-Disease AI Diagnosis System</h1>', unsafe_allow_html=True)

st.sidebar.info("To enable Dark Mode, go to Settings ⚙️ → Theme → Dark")

st.sidebar.markdown("### 🧬 Disease Detection Modules")
module = st.sidebar.selectbox("🎯 Pick a Disease to Diagnose", ["Heart Disease", "Diabetes", "Liver Disease", "Pneumonia (X-ray)"])

st.sidebar.markdown("---")
st.sidebar.markdown("💡 **Tip:** Switch between different AI models to diagnose various conditions!")

#Local Url
# API_BASE_lab = "http://localhost:8000/lab"
# API_BASE_img = "http://localhost:8000/image"

# Render backend url
API_BASE_lab = "https://medisense-ai.onrender.com/lab"
API_BASE_img = "https://medisense-ai.onrender.com/image"

if module == "Heart Disease":
    render_heart_module(API_BASE_lab)

elif module == "Diabetes":
    render_diabetes_module(API_BASE_lab)

elif module == "Liver Disease":
    render_liver_module(API_BASE_lab)

elif module == "Pneumonia (X-ray)":
    render_pneumonia_module(API_BASE_img)
    
#footer
render_footer()
