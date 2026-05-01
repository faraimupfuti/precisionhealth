# ClaraVision Health - Deployment Guide

This guide covers deploying ClaraVision Health to various platforms for production use.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Streamlit Community Cloud (Recommended for Demo)](#streamlit-community-cloud)
3. [Heroku Deployment](#heroku-deployment)
4. [AWS Deployment](#aws-deployment)
5. [Azure Deployment](#azure-deployment)
6. [Docker Deployment](#docker-deployment)
7. [Production Considerations](#production-considerations)

---

## Prerequisites

Before deploying, ensure you have:

- ✅ Git repository with your code
- ✅ GitHub account (for Streamlit Cloud)
- ✅ Roboflow API key
- ✅ SMTP credentials (optional, for email functionality)
- ✅ Domain name (optional, for custom URL)

---

## Streamlit Community Cloud

**Best for:** Quick demos, proof of concepts, sharing with stakeholders

**Pros:**
- Free hosting
- Easy deployment
- Automatic updates from GitHub
- Built-in secrets management

**Cons:**
- Limited resources
- Public by default (can add password protection)
- Community tier limitations

### Step-by-Step Deployment

1. **Push Code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit of ClaraVision Health"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/claravision-health.git
   git push -u origin main
   ```

2. **Visit Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"

3. **Configure Deployment**
   - Repository: `YOUR_USERNAME/claravision-health`
   - Branch: `main`
   - Main file path: `app.py`
   - App URL: Choose a custom subdomain

4. **Add Secrets (Optional)**
   - Click "Advanced settings"
   - Add environment variables in TOML format:
   ```toml
   [secrets]
   SMTP_SERVER = "smtp.gmail.com"
   SMTP_PORT = "587"
   SMTP_USERNAME = "your-email@gmail.com"
   SMTP_PASSWORD = "your-app-password"
   SENDER_EMAIL = "noreply@claravision.health"
   ```

5. **Deploy**
   - Click "Deploy!"
   - Wait for deployment (usually 2-3 minutes)
   - Your app will be live at `https://YOUR_APP.streamlit.app`

6. **Enable Password Protection (Optional)**
   - In app settings, enable "Password protection"
   - Set a password for controlled access

---

## Heroku Deployment

**Best for:** Production-ready deployment with more control

### Prerequisites
- Heroku account
- Heroku CLI installed

### Deployment Steps

1. **Create Required Files**

   Create `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

   Create `setup.sh`:
   ```bash
   mkdir -p ~/.streamlit/

   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   \n\
   " > ~/.streamlit/config.toml
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   heroku create claravision-health
   ```

4. **Set Environment Variables**
   ```bash
   heroku config:set SMTP_SERVER=smtp.gmail.com
   heroku config:set SMTP_PORT=587
   heroku config:set SMTP_USERNAME=your-email@gmail.com
   heroku config:set SMTP_PASSWORD=your-app-password
   heroku config:set SENDER_EMAIL=noreply@claravision.health
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

6. **Open App**
   ```bash
   heroku open
   ```

7. **View Logs**
   ```bash
   heroku logs --tail
   ```

---

## AWS Deployment

**Best for:** Enterprise production deployment with full control

### Option A: AWS Elastic Beanstalk

1. **Install EB CLI**
   ```bash
   pip install awsebcli
   ```

2. **Initialize EB**
   ```bash
   eb init -p python-3.9 claravision-health
   ```

3. **Create Environment**
   ```bash
   eb create claravision-prod
   ```

4. **Set Environment Variables**
   ```bash
   eb setenv SMTP_SERVER=smtp.gmail.com SMTP_PORT=587 \
            SMTP_USERNAME=your-email@gmail.com \
            SMTP_PASSWORD=your-app-password \
            SENDER_EMAIL=noreply@claravision.health
   ```

5. **Deploy**
   ```bash
   eb deploy
   ```

6. **Open App**
   ```bash
   eb open
   ```

### Option B: AWS ECS (Docker)

1. **Build Docker Image**
   ```bash
   docker build -t claravision-health .
   ```

2. **Create ECR Repository**
   ```bash
   aws ecr create-repository --repository-name claravision-health
   ```

3. **Push to ECR**
   ```bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ECR_URI
   docker tag claravision-health:latest YOUR_ECR_URI/claravision-health:latest
   docker push YOUR_ECR_URI/claravision-health:latest
   ```

4. **Create ECS Cluster and Service** (via AWS Console or CLI)

---

## Azure Deployment

**Best for:** Organizations using Microsoft ecosystem

### Using Azure App Service

1. **Install Azure CLI**
   ```bash
   curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
   ```

2. **Login to Azure**
   ```bash
   az login
   ```

3. **Create Resource Group**
   ```bash
   az group create --name claravision-rg --location eastus
   ```

4. **Create App Service Plan**
   ```bash
   az appservice plan create --name claravision-plan \
                              --resource-group claravision-rg \
                              --sku B1 --is-linux
   ```

5. **Create Web App**
   ```bash
   az webapp create --resource-group claravision-rg \
                    --plan claravision-plan \
                    --name claravision-health \
                    --runtime "PYTHON|3.9"
   ```

6. **Configure Deployment**
   ```bash
   az webapp deployment source config --name claravision-health \
                                       --resource-group claravision-rg \
                                       --repo-url https://github.com/YOUR_USERNAME/claravision-health \
                                       --branch main --manual-integration
   ```

7. **Set Environment Variables**
   ```bash
   az webapp config appsettings set --resource-group claravision-rg \
                                    --name claravision-health \
                                    --settings SMTP_SERVER=smtp.gmail.com \
                                               SMTP_PORT=587 \
                                               SMTP_USERNAME=your-email@gmail.com \
                                               SMTP_PASSWORD=your-app-password
   ```

---

## Docker Deployment

**Best for:** Containerized deployment on any platform

### Dockerfile

```dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the application
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Docker Compose (docker-compose.yml)

```yaml
version: '3.8'

services:
  claravision:
    build: .
    ports:
      - "8501:8501"
    environment:
      - SMTP_SERVER=${SMTP_SERVER}
      - SMTP_PORT=${SMTP_PORT}
      - SMTP_USERNAME=${SMTP_USERNAME}
      - SMTP_PASSWORD=${SMTP_PASSWORD}
      - SENDER_EMAIL=${SENDER_EMAIL}
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped
```

### Build and Run

```bash
# Build image
docker build -t claravision-health .

# Run container
docker run -p 8501:8501 \
           -e SMTP_SERVER=smtp.gmail.com \
           -e SMTP_PORT=587 \
           -e SMTP_USERNAME=your-email@gmail.com \
           -e SMTP_PASSWORD=your-app-password \
           claravision-health

# Or use Docker Compose
docker-compose up -d
```

---

## Production Considerations

### 1. Security

#### SSL/TLS Certificate
```bash
# Using Let's Encrypt with Nginx
sudo certbot --nginx -d claravision.health -d www.claravision.health
```

#### Environment Variables
- Never commit `.env` file
- Use platform-specific secret management:
  - AWS: AWS Secrets Manager
  - Azure: Azure Key Vault
  - Heroku: Config Vars
  - Streamlit Cloud: Secrets management

#### Rate Limiting (Nginx Example)
```nginx
limit_req_zone $binary_remote_addr zone=app_limit:10m rate=10r/s;

server {
    location / {
        limit_req zone=app_limit burst=20 nodelay;
        proxy_pass http://localhost:8501;
    }
}
```

### 2. Monitoring

#### Application Monitoring with Sentry

```python
# Add to app.py
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,
    environment="production"
)
```

#### Health Checks

Add to `app.py`:
```python
@st.cache_resource
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
```

### 3. Performance Optimization

#### Caching
```python
# Already using st.cache_data and st.cache_resource
@st.cache_data(ttl=3600)
def load_disease_database():
    return DISEASE_DATABASE
```

#### Image Optimization
```python
# Resize large images before API call
max_dimension = 1024
if image.width > max_dimension or image.height > max_dimension:
    image.thumbnail((max_dimension, max_dimension), Image.LANCZOS)
```

### 4. Backup and Recovery

```bash
# Backup configuration and data
tar -czf claravision-backup-$(date +%Y%m%d).tar.gz \
    app.py disease_database.py utils.py config.py requirements.txt
```

### 5. Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('claravision.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
```

### 6. Custom Domain

#### Streamlit Cloud
- Add custom domain in app settings
- Configure DNS CNAME record pointing to your Streamlit app

#### Heroku
```bash
heroku domains:add claravision.health
heroku domains:add www.claravision.health
```

Then configure DNS:
```
CNAME www.claravision.health -> your-app-name.herokuapp.com
CNAME claravision.health -> your-app-name.herokuapp.com
```

---

## Post-Deployment Checklist

- [ ] Test all functionality (upload, analysis, PDF generation, email)
- [ ] Verify environment variables are set correctly
- [ ] Check SSL certificate is active
- [ ] Test on multiple devices (desktop, mobile, tablet)
- [ ] Verify email delivery (if enabled)
- [ ] Set up monitoring and alerts
- [ ] Configure backup strategy
- [ ] Test error handling and edge cases
- [ ] Verify medical disclaimer is prominently displayed
- [ ] Check load times and performance
- [ ] Set up analytics (if required)
- [ ] Document deployment process
- [ ] Train support team

---

## Troubleshooting

### App Won't Start
```bash
# Check logs
streamlit run app.py --logger.level=debug

# Verify dependencies
pip install -r requirements.txt --upgrade
```

### API Errors
- Verify Roboflow API key is correct
- Check API rate limits
- Ensure image format is supported

### Email Not Sending
- Verify SMTP credentials
- Check firewall/network rules
- Enable "Less secure app access" or use App Passwords for Gmail

### Memory Issues
- Reduce image size before processing
- Implement pagination for batch processing
- Use cloud storage for temporary files

---

## Support

For deployment assistance:
- Email: support@claravision.health
- Documentation: [README.md](README.md)
- Issues: GitHub Issues

---

**Good luck with your deployment! 🚀**
