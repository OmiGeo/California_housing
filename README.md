
# 🏡 California House Price Prediction

This is a **Flask-based web application** that predicts **California house prices** based on various features such as location, population, and median income. The model is trained using **scikit-learn** and deployed on **Render**.

---
#The Deployment Link of the model 
https://california-housing-fqqt.onrender.com

## 🚀 Features
- 📊 **Predicts house prices** based on user inputs.
- 🌍 Uses **ocean proximity** as a categorical feature.
- 🌐 **Flask API** for handling predictions.
- 🎨 **HTML Frontend** for user interaction.
- ☁️ **Deployed on Render** for easy access.

---

## 📂 Folder Structure
```
/california-house-price-prediction
│-- /templates               # Contains the frontend HTML files
│   ├── index.html           # Main UI file
│-- app.py                   # Flask application
│-- best_model.pkl           # Trained ML model
│-- requirements.txt         # Python dependencies
│-- startup.sh               # Start script for Render deployment
│-- README.md                # Project documentation
```

---

## 🛠 Installation & Setup
### 1️⃣ **Clone the Repository**
```sh
git clone [https://github.com/OmiGeo/California_housing.git]
cd california-house-price-prediction
```

### 2️⃣ **Create a Virtual Environment**
```sh
python -m venv myenv
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate     # On Windows
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Run the Flask App Locally**
```sh
python app.py
```
✅ The app should now be running at `http://127.0.0.1:5000/`

---

## ☁️ Deploying on Render

### 1️⃣ **Push Your Code to GitHub**
Ensure all changes are committed and pushed:
```sh
git add .
git commit -m "Initial commit"
git push origin main
```

### 2️⃣ **Create a New Web Service on Render**
1. Go to [Render](https://dashboard.render.com/).
2. Click **New Web Service**.
3. Connect your **GitHub repository**.
4. Set **Build Command**: `pip install -r requirements.txt`
5. Set **Start Command**: `bash startup.sh`
6. Click **Deploy** 🚀

### 3️⃣ **Check Logs & Test**
- Once deployed, check logs for errors.
- Open the Render-provided **URL** to test the app.

---

## 🖥️ API Usage
### **Endpoint: `/predict`** (POST)
- **Input (JSON):**
```json
{
  "features": [longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income, "ocean_proximity"]
}
```
- **Output (JSON):**
```json
{
  "predicted_price": 350000.0
}
```

---

## 🤖 Tech Stack
- **Python** 🐍
- **Flask** 🌐
- **Scikit-Learn** 📊
- **Render (Deployment)** ☁️
- **HTML + JavaScript (Frontend)** 🎨

---

## 📌 Notes
- Ensure `best_model.pkl` is in the root directory before running.
- If `index.html` is missing in Render, run:
  ```sh
  git add templates/index.html
  git commit -m "Ensure index.html is inside templates/"
  git push origin main
  ```
- If the Render deployment fails, check logs for missing dependencies or port binding issues.

---

## 📝 Umashankar Kanpal
🚀 Happy Coding!

