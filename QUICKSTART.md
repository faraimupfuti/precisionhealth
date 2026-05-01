# ClaraVision Health - Quick Start Guide

Get ClaraVision Health running in under 5 minutes!

## 🚀 Super Quick Start (Local Testing)

### 1. Clone or Download the Repository

```bash
# If you haven't already
cd claravision-health
```

### 2. Install Dependencies

```bash
pip install streamlit requests Pillow reportlab python-dotenv
```

### 3. Run the Application

```bash
streamlit run app.py
```

### 4. Open in Browser

The application will automatically open at `http://localhost:8501`

### 5. Test the Application

1. Click "Browse files" and upload a test skin image
2. Click "🔍 Analyze Image"
3. View the results and detailed information
4. Click "📄 Generate PDF Report" to download a report

**That's it!** You now have ClaraVision Health running locally.

---

## 📱 Testing Workflow

### Upload Test Images

For best results, use images that are:
- Clear and well-lit
- Focused on the skin condition
- Not too close or too far
- JPEG, JPG, or PNG format
- Under 10MB in size

### Analyze Results

The app will return:
- **Predictions**: List of possible conditions
- **Confidence Levels**: High (70%+), Medium (40-70%), Low (<40%)
- **Detailed Information**: For each detected condition

### Generate Reports

1. **PDF Reports**: Click "Generate PDF Report" to download
2. **Email Reports**: Enter email address and click "Email Report" (requires SMTP setup)

### Customize Settings

Use the sidebar to:
- Adjust confidence threshold
- Show/hide all predictions
- Include/exclude treatment recommendations
- Include/exclude prevention tips
- Include/exclude "when to seek care" info

---

## 🔧 Optional: Email Configuration

To enable email functionality:

### 1. Create .env File

```bash
cp .env.example .env
```

### 2. Edit .env File

Add your SMTP credentials:

```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SENDER_EMAIL=noreply@claravision.health
```

### 3. For Gmail Users

1. Enable 2-Factor Authentication on your Google account
2. Generate an App Password:
   - Go to https://myaccount.google.com/security
   - Select "2-Step Verification"
   - Scroll down to "App passwords"
   - Generate a password for "Mail"
3. Use this app password in your `.env` file

### 4. Restart Application

```bash
streamlit run app.py
```

---

## 🌐 Deploy to Streamlit Cloud (Free!)

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/claravision-health.git
git push -u origin main
```

### 2. Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `YOUR_USERNAME/claravision-health`
5. Main file: `app.py`
6. Click "Deploy!"

### 3. Your App is Live! 🎉

Share the URL: `https://YOUR_APP.streamlit.app`

---

## 📋 Common Issues & Solutions

### Issue: "ModuleNotFoundError"
**Solution:** Install missing dependencies
```bash
pip install -r requirements.txt
```

### Issue: "Connection Error" when analyzing
**Solution:** Check your internet connection (API requires internet access)

### Issue: Email not sending
**Solution:** 
1. Verify SMTP credentials in `.env` file
2. For Gmail, use App Password (not regular password)
3. Check that `.env` file is in the same directory as `app.py`

### Issue: PDF won't generate
**Solution:** 
1. Check that reportlab is installed: `pip install reportlab`
2. Verify write permissions in the application directory

### Issue: Application is slow
**Solution:**
1. Reduce image size before uploading
2. Check your internet speed
3. Clear browser cache

---

## 🎯 Next Steps

Now that you have ClaraVision Health running:

### For Development
1. Review the code in `app.py`, `disease_database.py`, and `utils.py`
2. Customize the disease database with more conditions
3. Adjust the UI styling in the CSS section
4. Add more features (see README.md for ideas)

### For Testing
1. Test with various skin conditions
2. Validate accuracy with known conditions
3. Get feedback from healthcare professionals
4. Test on different devices (mobile, tablet, desktop)

### For Production
1. Review [DEPLOYMENT.md](DEPLOYMENT.md) for production deployment options
2. Set up monitoring and analytics
3. Configure proper security (HTTPS, authentication)
4. Implement regulatory compliance measures

---

## 📚 Documentation

- **Full Documentation**: [README.md](README.md)
- **Deployment Guide**: [DEPLOYMENT.md](DEPLOYMENT.md)
- **Configuration**: [config.py](config.py)
- **Disease Database**: [disease_database.py](disease_database.py)

---

## 💡 Pro Tips

1. **Start Simple**: Test locally before deploying to production
2. **Use Test Images**: Start with clear, well-lit images for best results
3. **Monitor API Usage**: Keep track of Roboflow API calls
4. **Backup Regularly**: Keep backups of your customizations
5. **Get Feedback**: Test with real healthcare professionals

---

## 🆘 Need Help?

- **Email**: support@claravision.health
- **GitHub Issues**: Create an issue on GitHub
- **Documentation**: Check README.md for detailed information

---

## ✅ Verification Checklist

Before sharing with stakeholders, verify:

- [ ] Application runs without errors
- [ ] Image upload works
- [ ] Analysis returns results
- [ ] PDF generation works
- [ ] Medical disclaimer is visible
- [ ] Results are accurate and helpful
- [ ] UI is responsive on mobile
- [ ] Error messages are clear
- [ ] All links work

---

**You're all set! Start analyzing skin conditions with ClaraVision Health! 🔬**
