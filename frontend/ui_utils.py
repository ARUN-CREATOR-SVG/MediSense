import streamlit as st

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@600&display=swap');

    .main-title {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        font-family: 'Inter', sans-serif;
    }

    .box {
        background: #fff;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }

    .footer-box {
        background: #f0f0f0;
        color: #444;
        border-radius: 15px;
        margin-top: 2rem;
        padding: 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .footer-box h4, .footer-box p {
        margin: 0.3rem 0;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)


def display_result(prediction_text: str, probability: float, risk_level: str = ""):
    st.success(f"✅ **Prediction:** {prediction_text}")
    st.info(f"🎯 **Confidence Score:** {probability * 100:.2f}%")
    
    risk = risk_level.capitalize() if risk_level else ""
    if risk == "Low":
        st.success(f"🟢 **Risk Level:** {risk}")
    elif risk == "Moderate":
        st.warning(f"🟡 **Risk Level:** {risk}")
    elif risk == "High":
        st.error(f"🔴 **Risk Level:** {risk}")
    elif risk:
        st.info(f"⚠️ **Risk Level:** {risk}") 


def render_footer():
    st.markdown("""
    ---
    <div class="footer-box">
        <h4>⚕️ MediSense - AI-Powered Medical Diagnosis</h4>
        <p><em>This tool is for educational purposes only. Always consult healthcare professionals for medical decisions.</em></p>
        <p>🔬 Powered by Machine Learning & Deep Learning Models</p>
    </div>
    """, unsafe_allow_html=True)