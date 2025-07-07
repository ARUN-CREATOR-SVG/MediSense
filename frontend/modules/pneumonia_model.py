import streamlit as st
import requests
from PIL import Image

def render_pneumonia_module(API_BASE_img):
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

    
   
