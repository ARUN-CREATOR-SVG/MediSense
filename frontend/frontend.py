import streamlit as st

st.set_page_config(
    page_title="MediSense - AI Diagnosis", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title 
st.markdown('<h1>MediSense - Multi-Disease AI Diagnosis System</h1>', unsafe_allow_html=True)

# Sidebar for module selection
st.sidebar.markdown("### 🧬 Disease Detection Modules")
module = st.sidebar.selectbox("🎯 Pick a Disease to Diagnose", ["Heart Disease", "Diabetes", "Liver Disease", "Pneumonia (X-ray)"])

st.sidebar.markdown("---")
st.sidebar.markdown("💡 **Tip:** Switch between different AI models to diagnose various conditions!")