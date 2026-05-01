"""
Configuration file for ClaraVision Health
Centralizes all application settings and constants
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ===================================
# APPLICATION METADATA
# ===================================
APP_NAME = "ClaraVision Health"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "AI-Powered Skin Condition Analysis for African Healthcare"
DEVELOPER = "ClaraVision Health"
LOCATION = "Harare, Zimbabwe (SADC Region)"
ENTITY = "Estonia OÜ"

# ===================================
# ROBOFLOW API CONFIGURATION
# ===================================
ROBOFLOW_API_URL = "https://serverless.roboflow.com/precisionhealth-skin-condition-classification/9"
ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY", "cmnlsaDgw7FTB0sVFZx2")

# ===================================
# EMAIL CONFIGURATION
# ===================================
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "noreply@claravision.health")

# ===================================
# FILE UPLOAD SETTINGS
# ===================================
ALLOWED_IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png']
MAX_FILE_SIZE_MB = 10
MAX_IMAGE_DIMENSION = 4096  # pixels

# ===================================
# ANALYSIS SETTINGS
# ===================================
DEFAULT_CONFIDENCE_THRESHOLD = 30  # percentage
MIN_CONFIDENCE_THRESHOLD = 0
MAX_CONFIDENCE_THRESHOLD = 100

# Confidence level classifications
HIGH_CONFIDENCE_THRESHOLD = 70
MEDIUM_CONFIDENCE_THRESHOLD = 40

# ===================================
# REPORT SETTINGS
# ===================================
REPORT_TIMEZONE = "Africa/Harare"
REPORT_DATE_FORMAT = "%B %d, %Y at %I:%M %p"
PDF_PAGE_SIZE = "A4"

# ===================================
# UI CONFIGURATION
# ===================================
THEME = {
    "primary_color": "#1e3a8a",
    "secondary_color": "#3b82f6",
    "accent_color": "#f59e0b",
    "background_color": "#f8f9fa",
    "text_color": "#1e293b"
}

# ===================================
# REGULATORY INFORMATION
# ===================================
REGULATORY_STATUS = "Demonstration/Proof of Concept"
TARGET_MARKETS = ["SADC Region", "Zimbabwe", "South Africa", "Botswana", "Namibia", "Zambia"]
PLANNED_CERTIFICATIONS = [
    "MCAZ (Medicines Control Authority of Zimbabwe)",
    "ISO 13485 Medical Device Quality Management",
    "CE Marking",
    "FDA 510(k) (consideration)"
]

# ===================================
# MEDICAL DISCLAIMER
# ===================================
MEDICAL_DISCLAIMER = """
This is a demonstration tool designed to assist healthcare professionals and is NOT a substitute for professional medical diagnosis. 
This system is optimized for African skin tones and SADC region skin conditions. Always consult with qualified healthcare 
providers for proper diagnosis and treatment. This tool is intended for educational and screening purposes only.
"""

# ===================================
# SUPPORTED CONDITIONS
# ===================================
SUPPORTED_CONDITIONS = [
    "Acne",
    "Eczema",
    "Psoriasis",
    "Vitiligo",
    "Tinea (Ringworm)",
    "Keloid Scars",
    "Melanoma",
    "Post-Inflammatory Hyperpigmentation (PIH)",
    "Seborrheic Dermatitis"
]

# ===================================
# SKIN TONE OPTIMIZATION
# ===================================
TARGET_FITZPATRICK_TYPES = ["IV", "V", "VI"]
SKIN_TONE_DESCRIPTION = "Optimized for African skin tones (Fitzpatrick IV-VI)"

# ===================================
# ANALYTICS & MONITORING (Future)
# ===================================
ENABLE_ANALYTICS = os.getenv("ENABLE_ANALYTICS", "False").lower() == "true"
GOOGLE_ANALYTICS_ID = os.getenv("GOOGLE_ANALYTICS_ID")
SENTRY_DSN = os.getenv("SENTRY_DSN")

# ===================================
# DATABASE (Future)
# ===================================
DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")

# ===================================
# SECURITY (Future)
# ===================================
SECRET_KEY = os.getenv("SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

# ===================================
# FEATURE FLAGS
# ===================================
ENABLE_EMAIL = bool(SMTP_SERVER and SMTP_USERNAME and SMTP_PASSWORD)
ENABLE_PDF_EXPORT = True
ENABLE_BATCH_PROCESSING = False  # Future feature
ENABLE_USER_ACCOUNTS = False  # Future feature
ENABLE_EHR_INTEGRATION = False  # Future feature

# ===================================
# PATHS
# ===================================
TEMP_DIR = "/tmp/claravision"
UPLOAD_DIR = os.path.join(TEMP_DIR, "uploads")
REPORT_DIR = os.path.join(TEMP_DIR, "reports")

# Ensure directories exist
for directory in [TEMP_DIR, UPLOAD_DIR, REPORT_DIR]:
    os.makedirs(directory, exist_ok=True)

# ===================================
# API RATE LIMITING (Future)
# ===================================
RATE_LIMIT_PER_MINUTE = 60
RATE_LIMIT_PER_HOUR = 1000
RATE_LIMIT_PER_DAY = 10000

# ===================================
# CONTACT INFORMATION
# ===================================
SUPPORT_EMAIL = "support@claravision.health"
WEBSITE_URL = "https://claravision.health"
GITHUB_URL = "https://github.com/YOUR_USERNAME/claravision-health"

# ===================================
# VALIDATION
# ===================================
def validate_config():
    """Validate critical configuration settings"""
    errors = []
    
    if not ROBOFLOW_API_KEY:
        errors.append("ROBOFLOW_API_KEY is not set")
    
    if ENABLE_EMAIL:
        if not all([SMTP_SERVER, SMTP_USERNAME, SMTP_PASSWORD]):
            errors.append("Email is enabled but SMTP settings are incomplete")
    
    if errors:
        print("Configuration Warnings:")
        for error in errors:
            print(f"  - {error}")
    
    return len(errors) == 0

# Run validation on import
validate_config()
