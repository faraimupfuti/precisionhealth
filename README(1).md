# ClaraVision Health - AI-Powered Skin Condition Analysis

![ClaraVision Health](https://img.shields.io/badge/ClaraVision-Health-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red)
![License](https://img.shields.io/badge/License-Proprietary-orange)

## 🎯 Overview

ClaraVision Health is an AI-powered skin condition analysis platform optimized for African skin tones and common dermatological conditions in the SADC region. This demonstration application provides healthcare professionals with a preliminary screening tool for skin conditions, leveraging advanced computer vision models trained on diverse African datasets.

**Key Features:**
- ✅ AI-powered skin condition classification
- ✅ Optimized for Fitzpatrick IV-VI skin tones
- ✅ Comprehensive disease information database
- ✅ Professional PDF report generation
- ✅ Email report delivery
- ✅ Treatment and prevention recommendations
- ✅ Clinical decision support interface

## 🏥 Medical Disclaimer

**IMPORTANT:** This is a demonstration tool designed to assist healthcare professionals and is NOT a substitute for professional medical diagnosis. This system is optimized for African skin tones and SADC region skin conditions. Always consult with qualified healthcare providers for proper diagnosis and treatment. This tool is intended for educational and screening purposes only.

**Regulatory Status:** Demonstration/Proof of Concept

**Planned Certifications:**
- MCAZ (Medicines Control Authority of Zimbabwe) Registration
- ISO 13485 Medical Device Quality Management
- CE Marking (via Estonia OÜ registration)
- FDA 510(k) pathway consideration

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)
- Internet connection (for API calls to Roboflow)

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/claravision-health.git
cd claravision-health
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables (Optional)

For email functionality, create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your SMTP credentials:

```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SENDER_EMAIL=noreply@claravision.health
```

**Note:** Email functionality is optional. PDF generation works without email configuration.

## 💻 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Using the Application

1. **Upload Image**: Click "Browse files" and select a clear image of the skin condition
2. **Analyze**: Click the "🔍 Analyze Image" button to run the AI analysis
3. **Review Results**: View the predictions with confidence levels and detailed information
4. **Export Report**: 
   - Click "📄 Generate PDF Report" to create a downloadable PDF
   - Enter email address and click "📧 Email Report" to send the report

### Analysis Settings (Sidebar)

- **Confidence Threshold**: Set minimum confidence level to display predictions (0-100%)
- **Show All Predictions**: Display all predictions regardless of confidence
- **Report Options**: 
  - Include/exclude treatment recommendations
  - Include/exclude prevention tips
  - Include/exclude "when to seek care" guidance

## 🗂️ Project Structure

```
claravision-health/
│
├── app.py                      # Main Streamlit application
├── disease_database.py         # Comprehensive disease information
├── utils.py                    # PDF generation and email utilities
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore file
└── README.md                  # This file
```

## 🧬 Supported Conditions

The application currently supports analysis of the following skin conditions:

1. **Acne** - Including post-inflammatory hyperpigmentation management
2. **Eczema (Atopic Dermatitis)** - Optimized for darker skin presentations
3. **Psoriasis** - Recognizing violet/grey plaques common in African skin
4. **Vitiligo** - Particularly impactful in darker skin tones
5. **Tinea (Ringworm)** - Fungal infections common in warm climates
6. **Keloid Scars** - Higher prevalence in African populations
7. **Melanoma** - Including acral and mucosal presentations
8. **Post-Inflammatory Hyperpigmentation (PIH)** - Common in darker skin
9. **Seborrheic Dermatitis** - Including scalp and facial presentations

## 🔧 Technical Details

### API Integration

The application uses Roboflow's serverless inference API:

```bash
Endpoint: https://serverless.roboflow.com/precisionhealth-skin-condition-classification/9
API Key: cmnlsaDgw7FTB0sVFZx2
```

### Model Information

- **Model Type**: Computer Vision Classification
- **Framework**: Roboflow
- **Optimization**: African skin tones (Fitzpatrick IV-VI)
- **Target Region**: SADC countries

### PDF Report Features

- Professional medical report formatting
- Patient-safe information presentation
- Comprehensive condition descriptions
- Treatment recommendations
- Prevention strategies
- "When to seek care" guidance
- Medical disclaimer and regulatory information

## 🌐 Deployment Options

### Option 1: Streamlit Community Cloud (Free)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Deploy your app by selecting the repository

### Option 2: Heroku

```bash
# Install Heroku CLI
# Create Procfile
echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Deploy
heroku create claravision-health
git push heroku main
```

### Option 3: AWS/Azure/GCP

Deploy as a containerized application using Docker:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 📊 Data Privacy & Security

- **No Data Storage**: The application does not store uploaded images or analysis results
- **Session-Based**: All data is cleared when the browser session ends
- **API Security**: Uses HTTPS for all API communications
- **GDPR Compliance**: No personal data is collected or retained
- **Local Processing**: Images are processed in-memory and not saved to disk

## 🔒 Security Considerations

1. **API Key Management**: Store API keys in environment variables, never in code
2. **HTTPS Only**: Deploy with SSL/TLS certificates in production
3. **Input Validation**: Validate file types and sizes before processing
4. **Rate Limiting**: Implement rate limiting to prevent API abuse
5. **Access Control**: Consider adding authentication for production deployments

## 📈 Future Enhancements

### Planned Features

- [ ] Multi-language support (English, Portuguese, French, Swahili)
- [ ] Batch image processing
- [ ] Integration with EHR systems
- [ ] Mobile application (iOS/Android)
- [ ] Telemedicine consultation scheduling
- [ ] Patient history tracking (with consent)
- [ ] Advanced analytics and reporting
- [ ] Integration with local SADC health information systems

### Regulatory Roadmap

- [ ] MCAZ registration application
- [ ] ISO 13485 certification process
- [ ] CE Marking documentation
- [ ] Clinical validation studies
- [ ] Real-world evidence collection
- [ ] Post-market surveillance system

## 🤝 Contributing

This is a proprietary application developed for ClaraVision Health. For collaboration inquiries, please contact the development team.

## 📞 Contact & Support

**Developer:** ClaraVision Health  
**Location:** Harare, Zimbabwe (SADC Region)  
**Entity:** Estonia OÜ (for EU grant access)

## 📄 License

This software is proprietary and confidential. Unauthorized copying, distribution, or use is strictly prohibited.

## 🙏 Acknowledgments

- African dermatology research community
- SADC healthcare professionals
- Roboflow for ML infrastructure
- Open-source Python community

## 📚 References & Resources

### Clinical Guidelines
- American Academy of Dermatology (AAD)
- British Association of Dermatologists (BAD)
- South African Dermatology Society
- WHO Essential Medicines List

### Datasets
- PASSION (Pan-African Skin Images Dataset)
- Diverse Dermatology Images (DDI)
- SCIN (Skin Condition Image Network)
- Fitzpatrick17k

### Research Papers
- "Dermatology in Skin of Color" - Journal of Clinical and Aesthetic Dermatology
- "AI in Dermatology" - JAMA Dermatology
- "Skin Disease in Africa" - International Journal of Dermatology

---

**Version:** 1.0.0  
**Last Updated:** November 2024  
**Status:** Demonstration/Proof of Concept

---

## 🎓 Recommendations for Production Deployment

### 1. Model Enhancement
- **Expand Training Dataset**: Collect more diverse African skin images across different Fitzpatrick types
- **Data Augmentation**: Implement rotation, brightness, and contrast variations
- **Class Balancing**: Address any class imbalances in training data
- **Regular Retraining**: Update model quarterly with new validated cases

### 2. Clinical Validation
- **Pilot Studies**: Conduct trials in 3-5 clinics across Zimbabwe/SADC region
- **Performance Metrics**: Track sensitivity, specificity, PPV, NPV against dermatologist diagnoses
- **Bias Assessment**: Ensure equal performance across all skin tones (Fitzpatrick IV-VI)
- **Real-World Testing**: Validate on images from actual clinical settings (variable lighting, angles)

### 3. Regulatory Compliance
- **Quality Management System**: Implement ISO 13485 compliant processes
- **Risk Management**: Conduct ISO 14971 risk analysis
- **Clinical Evidence**: Gather data for MCAZ and CE marking submissions
- **Post-Market Surveillance**: Track adverse events and performance in production

### 4. Infrastructure & Scalability
- **CDN Integration**: Use Cloudflare/AWS CloudFront for global access
- **Load Balancing**: Implement auto-scaling for high traffic
- **Database**: Add PostgreSQL for user management and analytics (with proper consent)
- **Caching**: Implement Redis for frequently accessed data
- **Monitoring**: Add Sentry for error tracking, DataDog for performance

### 5. User Experience
- **Mobile Optimization**: Ensure responsive design works on all devices
- **Progressive Web App**: Enable offline capabilities for rural areas
- **Low Bandwidth Mode**: Compress images for slow internet connections
- **Multi-language**: Add Portuguese, French, Swahili for SADC region

### 6. Business Model Integration
- **Tiered Pricing**: 
  - Free tier: 10 analyses/month for individual practitioners
  - Professional: $49/month for unlimited analyses
  - Enterprise: Custom pricing for hospital networks
- **Grant Co-PI Model**: Partner with research institutions
- **Pay-per-use**: $2-5 per analysis for casual users

### 7. Security & Privacy
- **HIPAA/GDPR**: Implement data protection measures
- **Encryption**: End-to-end encryption for all transmissions
- **Audit Logs**: Track all access and analyses
- **Data Anonymization**: De-identify data for research purposes
- **Consent Management**: Explicit opt-in for data usage

### 8. Integration Capabilities
- **FHIR API**: Enable EHR integration
- **HL7 Support**: Connect with hospital information systems
- **WhatsApp Business**: Allow report sharing via WhatsApp (popular in Africa)
- **USSD**: Consider feature-phone access for ultra-low-resource settings

### 9. Clinical Decision Support
- **Differential Diagnosis**: Show top 3-5 conditions with rationale
- **Red Flag Alerts**: Highlight urgent cases requiring immediate referral
- **Treatment Pathways**: Link to national/regional treatment guidelines
- **Medication Availability**: Check local formulary availability

### 10. Partnership Strategy
- **Academic Collaborations**: Partner with University of Zimbabwe, UCT, Makerere
- **Government Health Ministries**: Integrate with national screening programs
- **NGOs**: Work with Amref Health Africa, PEPFAR, USAID
- **Private Sector**: Partner with pharmacy chains for access points

---

**🚀 Good luck with ClaraVision Health! This has the potential to significantly impact dermatological care access across Africa.**
