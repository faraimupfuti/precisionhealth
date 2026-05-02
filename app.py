import streamlit as st
import requests
import base64
import json
from datetime import datetime
import os
from PIL import Image
import io
from disease_database import DISEASE_DATABASE, get_disease_info
from utils import generate_pdf_report, send_email_report

# Page configuration
st.set_page_config(
    page_title="ClaraVision Health - Skin Condition Analysis",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional medical interface
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@400;600;700&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');
    
    /* Global styles */
    .main {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .header-title {
        font-family: 'Crimson Pro', serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: white;
        margin: 0;
        text-align: center;
    }
    
    .header-subtitle {
        font-family: 'IBM Plex Sans', sans-serif;
        font-size: 1.1rem;
        color: #e0e7ff;
        text-align: center;
        margin-top: 0.5rem;
    }
    
    /* Card styling */
    .info-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #3b82f6;
    }
    
    .disease-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        border: 2px solid #e2e8f0;
    }
    
    .disease-title {
        font-family: 'Crimson Pro', serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .confidence-badge {
        display: inline-block;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-family: 'IBM Plex Sans', sans-serif;
        font-weight: 600;
        font-size: 0.9rem;
        margin: 0.5rem 0;
    }
    
    .high-confidence {
        background: #dcfce7;
        color: #166534;
    }
    
    .medium-confidence {
        background: #fef3c7;
        color: #92400e;
    }
    
    .low-confidence {
        background: #fee2e2;
        color: #991b1b;
    }
    
    /* Section headers */
    .section-header {
        font-family: 'Crimson Pro', serif;
        font-size: 1.4rem;
        font-weight: 600;
        color: #1e3a8a;
        margin: 1.5rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #3b82f6;
    }
    
    /* Warning/Disclaimer box */
    .disclaimer-box {
        background: #fef3c7;
        border: 2px solid #f59e0b;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .disclaimer-title {
        font-family: 'IBM Plex Sans', sans-serif;
        font-size: 1.1rem;
        font-weight: 600;
        color: #92400e;
        margin-bottom: 0.5rem;
    }
    
    .disclaimer-text {
        font-family: 'IBM Plex Sans', sans-serif;
        font-size: 0.95rem;
        color: #78350f;
        line-height: 1.6;
    }
    
    /* Button styling */
    .stButton>button {
        font-family: 'IBM Plex Sans', sans-serif;
        font-weight: 500;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        transition: all 0.3s ease;
    }
    
    /* Info sections */
    .info-section {
        background: #f8fafc;
        border-radius: 8px;
        padding: 1.2rem;
        margin: 1rem 0;
        border-left: 3px solid #3b82f6;
    }
    
    .info-section-title {
        font-family: 'IBM Plex Sans', sans-serif;
        font-size: 1.1rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.8rem;
    }
    
    .info-section-text {
        font-family: 'IBM Plex Sans', sans-serif;
        font-size: 0.95rem;
        color: #475569;
        line-height: 1.7;
    }
    
    /* List styling */
    .custom-list {
        font-family: 'IBM Plex Sans', sans-serif;
        font-size: 0.95rem;
        color: #475569;
        line-height: 1.8;
        padding-left: 1.2rem;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        font-family: 'IBM Plex Sans', sans-serif;
        font-size: 0.9rem;
        color: #64748b;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container">
    <h1 class="header-title">🔬 ClaraVision Health</h1>
    <p class="header-subtitle">AI-Powered Skin Condition Analysis for African Healthcare</p>
</div>
""", unsafe_allow_html=True)

# Disclaimer
st.markdown("""
<div class="disclaimer-box">
    <div class="disclaimer-title">⚕️ Medical Disclaimer</div>
    <div class="disclaimer-text">
        This is a demonstration tool designed to assist healthcare professionals and is NOT a substitute for professional medical diagnosis. 
        This system is optimized for African skin tones and SADC region skin conditions. Always consult with qualified healthcare 
        providers for proper diagnosis and treatment. This tool is intended for educational and screening purposes only.
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 📋 Analysis Settings")
    
    confidence_threshold = st.slider(
        "Minimum Confidence (%)",
        min_value=0,
        max_value=100,
        value=20,
        help="Filter out predictions below this confidence level"
    )
    
    show_all_predictions = st.checkbox(
        "Show More Than Top 3",
        value=False,
        help="By default, only the top 3 predictions are shown. Enable to see all predictions above the confidence threshold."
    )
    
    st.markdown("---")
    st.markdown("### 📊 Report Options")
    
    include_treatment = st.checkbox("Include Treatment Recommendations", value=True)
    include_prevention = st.checkbox("Include Prevention Tips", value=True)
    include_when_to_seek_care = st.checkbox("Include When to Seek Care", value=True)
    
    st.markdown("---")
    st.markdown("### 🌍 About ClaraVision")
    st.info("""
    **ClaraVision Health** leverages advanced AI to provide skin condition analysis 
    optimized for African skin tones and common conditions in the SADC region.
    
    **Version:** 1.0 (Demo)
    
    **Target Markets:** SADC Region
    
    **Regulatory Status:** Demo/POC
    """)

# Main content
tab1, tab2, tab3 = st.tabs(["📸 Analysis", "📚 Disease Information", "ℹ️ About"])

with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="section-header">Upload Image</div>', unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Choose a skin condition image",
            type=['jpg', 'jpeg', 'png'],
            help="Upload a clear image of the affected area"
        )
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
            
            # Analysis button
            if st.button("🔍 Analyze Image", type="primary", use_container_width=True):
                with st.spinner("Analyzing image..."):
                    try:
                        # Convert image to base64
                        buffered = io.BytesIO()
                        image.save(buffered, format="JPEG")
                        img_base64 = base64.b64encode(buffered.getvalue()).decode()
                        
                        # Make API request to Roboflow
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
                        else:
                            st.error(f"❌ Error: {response.status_code} - {response.text}")
                            
                    except Exception as e:
                        st.error(f"❌ Error during analysis: {str(e)}")
    
    with col2:
        if 'results' in st.session_state:
            st.markdown('<div class="section-header">Analysis Results</div>', unsafe_allow_html=True)
            
            results = st.session_state['results']
            
            # Debug: Show raw response structure (optional - can be removed after testing)
            with st.expander("🔍 Debug: View Raw API Response", expanded=False):
                st.json(results)
            
            # Handle different API response formats
            predictions = None
            
            # Try to extract predictions from different possible formats
            if 'predictions' in results:
                predictions = results['predictions']
            elif 'predicted_classes' in results:
                predictions = results['predicted_classes']
            elif isinstance(results, dict):
                # Check if results itself contains prediction data
                if 'class' in results and 'confidence' in results:
                    predictions = [results]  # Single prediction
            
            # Display predictions
            if predictions and len(predictions) > 0:
                # Ensure predictions is a list
                if not isinstance(predictions, list):
                    predictions = [predictions]
                
                # Sort by confidence with better error handling
                try:
                    sorted_predictions = sorted(
                        predictions, 
                        key=lambda x: float(x.get('confidence', 0) if isinstance(x, dict) else 0), 
                        reverse=True
                    )
                except (AttributeError, TypeError, ValueError) as e:
                    st.error(f"⚠️ Error sorting predictions: {str(e)}")
                    sorted_predictions = predictions  # Use unsorted if sorting fails
                
                # Limit to top 3 predictions unless show_all is enabled
                if not show_all_predictions:
                    display_predictions = sorted_predictions[:3]
                else:
                    display_predictions = sorted_predictions
                
                # Show summary
                st.info(f"📊 Showing top {len(display_predictions)} prediction(s) from {len(sorted_predictions)} total")
                
                for idx, pred in enumerate(display_predictions):
                    # Handle different prediction formats
                    if not isinstance(pred, dict):
                        st.warning(f"⚠️ Unexpected prediction format at index {idx}: {type(pred)}")
                        continue
                    
                    # Extract confidence and class name with fallbacks
                    confidence_raw = pred.get('confidence', pred.get('score', 0))
                    try:
                        confidence = float(confidence_raw) * 100
                    except (TypeError, ValueError):
                        confidence = 0
                        st.warning(f"⚠️ Invalid confidence value: {confidence_raw}")
                    
                    class_name = pred.get('class', pred.get('class_name', pred.get('label', 'Unknown')))
                    
                    # Apply confidence filter
                    if confidence < confidence_threshold:
                        continue
                    
                    # Get disease information using helper function
                    disease_info = get_disease_info(class_name)
                    
                    # Use display name if available
                    display_name = disease_info.get('display_name', class_name) if disease_info else class_name
                    
                    # Determine confidence level
                    if confidence >= 70:
                        conf_class = "high-confidence"
                        conf_label = "High Confidence"
                    elif confidence >= 40:
                        conf_class = "medium-confidence"
                        conf_label = "Medium Confidence"
                    else:
                        conf_class = "low-confidence"
                        conf_label = "Low Confidence"
                    
                    st.markdown(f"""
                    <div class="disease-card">
                        <div class="disease-title">{display_name}</div>
                        <span class="confidence-badge {conf_class}">
                            {conf_label}: {confidence:.1f}%
                        </span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Display disease information if available
                    if disease_info:
                        with st.expander("📖 View Detailed Information", expanded=(idx == 0)):
                            # Description
                            st.markdown(f"""
                            <div class="info-section">
                                <div class="info-section-title">Description</div>
                                <div class="info-section-text">{disease_info['description']}</div>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Symptoms
                            st.markdown(f"""
                            <div class="info-section">
                                <div class="info-section-title">Common Symptoms</div>
                                <div class="custom-list">
                                    {''.join([f'• {symptom}<br>' for symptom in disease_info['symptoms']])}
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Treatment recommendations
                            if include_treatment:
                                st.markdown(f"""
                                <div class="info-section">
                                    <div class="info-section-title">Treatment Recommendations</div>
                                    <div class="custom-list">
                                        {''.join([f'• {treatment}<br>' for treatment in disease_info['treatment']])}
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                            
                            # Prevention
                            if include_prevention and 'prevention' in disease_info:
                                st.markdown(f"""
                                <div class="info-section">
                                    <div class="info-section-title">Prevention Tips</div>
                                    <div class="custom-list">
                                        {''.join([f'• {tip}<br>' for tip in disease_info['prevention']])}
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                            
                            # When to seek care
                            if include_when_to_seek_care and 'when_to_seek_care' in disease_info:
                                st.markdown(f"""
                                <div class="info-section" style="border-left-color: #ef4444;">
                                    <div class="info-section-title" style="color: #dc2626;">⚠️ When to Seek Medical Care</div>
                                    <div class="custom-list">
                                        {''.join([f'• {item}<br>' for item in disease_info['when_to_seek_care']])}
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                    else:
                        st.info("ℹ️ Detailed information not available for this condition. Please consult a healthcare professional.")
            else:
                st.warning("⚠️ No predictions found in the response.")
                st.info("""
                **Possible reasons:**
                - The model couldn't detect any skin conditions in the image
                - The image quality is too low
                - The API response format is unexpected
                
                **Try:**
                - Upload a clearer, well-lit image
                - Ensure the image shows a skin condition clearly
                - Check the Debug section above to see the raw API response
                """)
            
            # Export options
            st.markdown('<div class="section-header">Export Report</div>', unsafe_allow_html=True)
            
            col_pdf, col_email = st.columns(2)
            
            with col_pdf:
                if st.button("📄 Generate PDF Report", use_container_width=True):
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
                                    label="⬇️ Download PDF Report",
                                    data=pdf_file,
                                    file_name=f"claravision_report_{st.session_state['timestamp'].strftime('%Y%m%d_%H%M%S')}.pdf",
                                    mime="application/pdf",
                                    use_container_width=True
                                )
                        except Exception as e:
                            st.error(f"❌ Error generating PDF: {str(e)}")
            
            with col_email:
                email_address = st.text_input("Email address", placeholder="doctor@hospital.com")
                if st.button("📧 Email Report", use_container_width=True):
                    if email_address:
                        with st.spinner("Sending email..."):
                            try:
                                success = send_email_report(
                                    email_address,
                                    st.session_state['results'],
                                    st.session_state['image'],
                                    st.session_state['timestamp'],
                                    include_treatment,
                                    include_prevention,
                                    include_when_to_seek_care
                                )
                                if success:
                                    st.success(f"✅ Report sent to {email_address}")
                                else:
                                    st.error("❌ Email configuration required. Please set up SMTP settings in environment variables.")
                            except Exception as e:
                                st.error(f"❌ Error sending email: {str(e)}")
                    else:
                        st.warning("⚠️ Please enter an email address.")

with tab2:
    st.markdown('<div class="section-header">Disease Information Database</div>', unsafe_allow_html=True)
    
    # Create list of display names
    disease_options = {disease_info.get('display_name', key): key for key, disease_info in DISEASE_DATABASE.items()}
    display_names = sorted(disease_options.keys())
    
    selected_display_name = st.selectbox("Select a condition to learn more:", display_names)
    
    if selected_display_name:
        selected_disease = disease_options[selected_display_name]
        disease_info = DISEASE_DATABASE[selected_disease]
        
        st.markdown(f"""
        <div class="disease-card">
            <div class="disease-title">{disease_info.get('display_name', selected_disease)}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="info-section">
            <div class="info-section-title">Description</div>
            <div class="info-section-text">{disease_info['description']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="info-section">
                <div class="info-section-title">Common Symptoms</div>
                <div class="custom-list">
                    {''.join([f'• {symptom}<br>' for symptom in disease_info['symptoms']])}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if 'prevention' in disease_info:
                st.markdown(f"""
                <div class="info-section">
                    <div class="info-section-title">Prevention Tips</div>
                    <div class="custom-list">
                        {''.join([f'• {tip}<br>' for tip in disease_info['prevention']])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="info-section">
                <div class="info-section-title">Treatment Recommendations</div>
                <div class="custom-list">
                    {''.join([f'• {treatment}<br>' for treatment in disease_info['treatment']])}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if 'when_to_seek_care' in disease_info:
                st.markdown(f"""
                <div class="info-section" style="border-left-color: #ef4444;">
                    <div class="info-section-title" style="color: #dc2626;">⚠️ When to Seek Medical Care</div>
                    <div class="custom-list">
                        {''.join([f'• {item}<br>' for item in disease_info['when_to_seek_care']])}
                    </div>
                </div>
                """, unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="section-header">About ClaraVision Health</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <h3>🎯 Mission</h3>
        <p>ClaraVision Health is dedicated to democratizing dermatological care across Africa by providing 
        AI-powered skin condition analysis optimized for African skin tones and common conditions in the SADC region.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>🔬 Technology</h3>
            <ul class="custom-list">
                <li>Advanced computer vision models</li>
                <li>Optimized for Fitzpatrick IV-VI skin tones</li>
                <li>Trained on diverse African datasets</li>
                <li>Real-time inference via Roboflow</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>🌍 Target Markets</h3>
            <ul class="custom-list">
                <li>SADC Region (Primary)</li>
                <li>Sub-Saharan Africa</li>
                <li>Resource-limited settings</li>
                <li>Primary care facilities</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <h3>⚖️ Regulatory & Compliance</h3>
        <p><strong>Current Status:</strong> Demonstration/Proof of Concept</p>
        <p><strong>Planned Certifications:</strong></p>
        <ul class="custom-list">
            <li>MCAZ (Medicines Control Authority of Zimbabwe) Registration</li>
            <li>ISO 13485 Medical Device Quality Management</li>
            <li>CE Marking (via Estonia OÜ registration)</li>
            <li>FDA 510(k) pathway consideration</li>
        </ul>
        <p><strong>Clinical Decision Support Classification:</strong> This tool is positioned as a Clinical Decision Support 
        System (CDSS) to enable early revenue generation while full regulatory clearance is pursued.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <h3>📞 Contact Information</h3>
        <p><strong>Developer:</strong> ClaraVision Health</p>
        <p><strong>Location:</strong> Harare, Zimbabwe (SADC Region)</p>
        <p><strong>Entity:</strong> Estonia OÜ (for EU grant access)</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>ClaraVision Health v1.0 | Developed in Zimbabwe for African Healthcare</p>
    <p style="font-size: 0.8rem; margin-top: 0.5rem;">
        This is a demonstration system. Not for clinical diagnosis without healthcare professional oversight.
    </p>
</div>
""", unsafe_allow_html=True)
