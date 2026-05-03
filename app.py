import streamlit as st
import requests
import base64
import json
from datetime import datetime
import os
from PIL import Image
import io
from disease_database import DISEASE_DATABASE
try:
    from disease_database import get_disease_info
except ImportError:
    def get_disease_info(class_name):
        if class_name in DISEASE_DATABASE:
            return DISEASE_DATABASE[class_name]
        class_lower = class_name.lower()
        if class_lower in DISEASE_DATABASE:
            return DISEASE_DATABASE[class_lower]
        class_underscore = class_name.replace(' ', '_')
        if class_underscore in DISEASE_DATABASE:
            return DISEASE_DATABASE[class_underscore]
        class_no_underscore = class_name.replace('_', ' ')
        if class_no_underscore in DISEASE_DATABASE:
            return DISEASE_DATABASE[class_no_underscore]
        class_title = class_name.title()
        if class_title in DISEASE_DATABASE:
            return DISEASE_DATABASE[class_title]
        return None

from utils import generate_pdf_report, send_email_report

# Page configuration
st.set_page_config(
    page_title="ClaraVision Health - AI Skin Analysis",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern, beautiful CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0;
    }
    
    .block-container {
        padding: 2rem 3rem;
        max-width: 1400px;
    }
    
    /* Header */
    .header-card {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
    }
    
    .app-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        letter-spacing: -0.02em;
    }
    
    .app-subtitle {
        font-size: 1.1rem;
        color: #64748b;
        font-weight: 400;
        margin-top: 0.5rem;
    }
    
    /* Cards */
    .content-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
    }
    
    .card-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 1.5rem;
    }
    
    /* Top Prediction Card */
    .prediction-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border-radius: 20px;
        padding: 2.5rem;
        border-left: 6px solid #667eea;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.12);
        margin-bottom: 2rem;
    }
    
    .disease-name {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1e293b;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }
    
    .confidence-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.6rem 1.4rem;
        border-radius: 100px;
        font-weight: 600;
        font-size: 0.95rem;
    }
    
    .confidence-high {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }
    
    .confidence-medium {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);
    }
    
    .confidence-low {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
    }
    
    /* Info Blocks */
    .info-block {
        background: #f8fafc;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border-left: 4px solid #667eea;
    }
    
    .info-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 1rem;
    }
    
    .info-text {
        font-size: 1rem;
        line-height: 1.8;
        color: #475569;
    }
    
    .info-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .info-list li {
        padding: 0.6rem 0;
        padding-left: 1.5rem;
        position: relative;
        line-height: 1.6;
        color: #475569;
    }
    
    .info-list li:before {
        content: "●";
        position: absolute;
        left: 0;
        color: #667eea;
        font-weight: bold;
    }
    
    /* Alert Box */
    .alert-box {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border: 2px solid #f87171;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .alert-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #991b1b;
        margin-bottom: 0.5rem;
    }
    
    /* Disclaimer */
    .disclaimer {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border: 2px solid #fbbf24;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 2rem;
    }
    
    .disclaimer-title {
        font-weight: 700;
        color: #92400e;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    
    .disclaimer-text {
        color: #78350f;
        line-height: 1.7;
        font-size: 0.95rem;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-card">
    <h1 class="app-title">🔬 ClaraVision Health</h1>
    <p class="app-subtitle">AI-Powered Skin Analysis for African Healthcare</p>
</div>
""", unsafe_allow_html=True)

# Disclaimer
st.markdown("""
<div class="disclaimer">
    <div class="disclaimer-title">⚕️ Medical Disclaimer</div>
    <div class="disclaimer-text">
        This AI tool assists healthcare professionals and is NOT a substitute for professional medical diagnosis. 
        Optimized for African skin tones and SADC region conditions. Always consult qualified healthcare providers.
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Analysis Settings")
    
    min_confidence = st.slider(
        "Minimum Confidence (%)",
        min_value=0,
        max_value=100,
        value=20,
        help="Filter predictions below this threshold"
    )
    
    st.markdown("---")
    st.markdown("### 📄 Report Options")
    
    include_treatment = st.checkbox("Treatment Recommendations", value=True)
    include_prevention = st.checkbox("Prevention Tips", value=True)
    include_when_to_seek_care = st.checkbox("When to Seek Care", value=True)
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.info("""
    **ClaraVision Health**  
    Version 1.0  
    
    **Optimized for:**
    - African skin tones
    - SADC region  
    - Primary care
    
    **Status:** Demo/POC
    """)

# Main Content
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown('<div class="content-card"><div class="card-title">📸 Upload Image</div>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Choose a clear image",
        type=['jpg', 'jpeg', 'png'],
        help="For best results, use well-lit, focused images",
        label_visibility="collapsed"
    )
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)
        
        if st.button("🔍 Analyze Image", use_container_width=True, type="primary"):
            with st.spinner("Analyzing..."):
                try:
                    buffered = io.BytesIO()
                    image.save(buffered, format="JPEG")
                    img_base64 = base64.b64encode(buffered.getvalue()).decode()
                    
                    api_url = "https://serverless.roboflow.com/precisionhealth-skin-condition-classification/9"
                    api_key = "cmnlsaDgw7FTB0sVFZx2"
                    
                    response = requests.post(
                        f"{api_url}?api_key={api_key}",
                        data=img_base64,
                        headers={"Content-Type": "application/x-www-form-urlencoded"}
                    )
                    
                    if response.status_code == 200:
                        results = response.json()
                        st.session_state['results'] = results
                        st.session_state['image'] = image
                        st.session_state['timestamp'] = datetime.now()
                        st.success("✅ Analysis complete!")
                        st.rerun()
                    else:
                        st.error(f"❌ API Error: {response.status_code}")
                        
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if 'results' in st.session_state:
        st.markdown('<div class="content-card"><div class="card-title">📊 Analysis Results</div>', unsafe_allow_html=True)
        
        results = st.session_state['results']
        
        # Extract predictions
        predictions = None
        if 'predictions' in results:
            predictions = results['predictions']
        elif 'predicted_classes' in results:
            predictions = results['predicted_classes']
        elif isinstance(results, dict) and 'class' in results:
            predictions = [results]
        
        if predictions and len(predictions) > 0:
            if not isinstance(predictions, list):
                predictions = [predictions]
            
            # Sort by confidence
            try:
                sorted_predictions = sorted(
                    predictions,
                    key=lambda x: float(x.get('confidence', 0) if isinstance(x, dict) else 0),
                    reverse=True
                )
            except:
                sorted_predictions = predictions
            
            # Get TOP prediction only
            top_pred = sorted_predictions[0] if len(sorted_predictions) > 0 else None
            
            if top_pred and isinstance(top_pred, dict):
                # Extract info
                confidence_raw = top_pred.get('confidence', top_pred.get('score', 0))
                try:
                    confidence = float(confidence_raw) * 100
                except:
                    confidence = 0
                
                class_name = top_pred.get('class', top_pred.get('class_name', top_pred.get('label', 'Unknown')))
                
                # Get disease info
                disease_info = get_disease_info(class_name)
                display_name = disease_info.get('display_name', class_name) if disease_info else class_name
                
                # Confidence badge
                if confidence >= 70:
                    conf_class = "confidence-high"
                    conf_label = "High Confidence"
                elif confidence >= 40:
                    conf_class = "confidence-medium"
                    conf_label = "Medium Confidence"
                else:
                    conf_class = "confidence-low"
                    conf_label = "Low Confidence"
                
                # Display top prediction
                st.markdown(f"""
                <div class="prediction-card">
                    <div class="disease-name">{display_name}</div>
                    <div class="{conf_class} confidence-badge">
                        {conf_label}: {confidence:.1f}%
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Display disease information immediately
                if disease_info:
                    # Description
                    st.markdown(f"""
                    <div class="info-block">
                        <div class="info-title">📖 Description</div>
                        <div class="info-text">{disease_info['description']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Symptoms
                    symptoms_html = ''.join([f'<li>{s}</li>' for s in disease_info['symptoms']])
                    st.markdown(f"""
                    <div class="info-block">
                        <div class="info-title">🔍 Symptoms</div>
                        <ul class="info-list">{symptoms_html}</ul>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Treatment
                    if include_treatment:
                        treatment_html = ''.join([f'<li>{t}</li>' for t in disease_info['treatment']])
                        st.markdown(f"""
                        <div class="info-block">
                            <div class="info-title">💊 Treatment Plan</div>
                            <ul class="info-list">{treatment_html}</ul>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Prevention
                    if include_prevention and 'prevention' in disease_info:
                        prevention_html = ''.join([f'<li>{p}</li>' for p in disease_info['prevention']])
                        st.markdown(f"""
                        <div class="info-block">
                            <div class="info-title">🛡️ Prevention</div>
                            <ul class="info-list">{prevention_html}</ul>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # When to seek care
                    if include_when_to_seek_care and 'when_to_seek_care' in disease_info:
                        seek_care_html = ''.join([f'<li>{w}</li>' for w in disease_info['when_to_seek_care']])
                        st.markdown(f"""
                        <div class="alert-box">
                            <div class="alert-title">⚠️ When to Seek Medical Care</div>
                            <ul class="info-list">{seek_care_html}</ul>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("ℹ️ Detailed information not available for this condition.")
                
                # Export options
                st.markdown("---")
                st.markdown("### 📤 Export Report")
                
                col_pdf, col_email = st.columns(2)
                
                with col_pdf:
                    if st.button("📄 Download PDF", use_container_width=True):
                        with st.spinner("Generating PDF..."):
                            try:
                                pdf_path = generate_pdf_report(
                                    st.session_state['results'],
                                    st.session_state['image'],
                                    st.session_state['timestamp'],
                                    include_treatment,
                                    include_prevention,
                                    include_when_to_seek_care
                                )
                                
                                with open(pdf_path, "rb") as pdf_file:
                                    st.download_button(
                                        label="⬇️ Download Report",
                                        data=pdf_file,
                                        file_name=f"claravision_report_{st.session_state['timestamp'].strftime('%Y%m%d_%H%M%S')}.pdf",
                                        mime="application/pdf",
                                        use_container_width=True
                                    )
                            except Exception as e:
                                st.error(f"PDF Error: {str(e)}")
                
                with col_email:
                    email = st.text_input("Email address", placeholder="doctor@hospital.com", label_visibility="collapsed")
                    if st.button("📧 Email Report", use_container_width=True):
                        if email:
                            with st.spinner("Sending..."):
                                try:
                                    success = send_email_report(
                                        email,
                                        st.session_state['results'],
                                        st.session_state['image'],
                                        st.session_state['timestamp'],
                                        include_treatment,
                                        include_prevention,
                                        include_when_to_seek_care
                                    )
                                    if success:
                                        st.success(f"✅ Sent to {email}")
                                    else:
                                        st.warning("⚠️ Email not configured")
                                except Exception as e:
                                    st.error(f"Email Error: {str(e)}")
                        else:
                            st.warning("⚠️ Enter email address")
            else:
                st.warning("⚠️ Invalid prediction format")
        else:
            st.info("ℹ️ No predictions found. Try a clearer image or lower the confidence threshold.")
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.info("👈 Upload an image to begin analysis")
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; color: white; margin-top: 3rem;">
    <p style="font-size: 0.9rem; opacity: 0.9;">
        <strong>ClaraVision Health v1.0</strong> | Developed in Zimbabwe for African Healthcare
    </p>
    <p style="font-size: 0.8rem; opacity: 0.7; margin-top: 0.5rem;">
        Demo/POC • Not for clinical diagnosis without healthcare professional oversight
    </p>
</div>
""", unsafe_allow_html=True)
