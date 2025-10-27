# Heart Disease Prediction

##  Overview
The **Heart Disease Prediction System** is a machine learning–powered health risk classification solution designed to support early medical decision-making. It evaluates key clinical attributes such as age, blood pressure, cholesterol levels, heart rate, and other medical factors to predict whether a patient may be at high risk of heart disease.

The model is built using **Logistic Regression**, chosen for its reliability in binary medical classification tasks. The trained model is deployed using a **Flask API** and accessible via a lightweight **HTML web interface** for real-time predictions.

---

##  Core Capabilities

### ✅ Accurate Risk Classification
- Binary classification to label individuals as *high-risk* or *low-risk*
- Achieved an **accuracy of ~86%**

### ✅ End-to-End ML Workflow
Data preprocessing → Model training → API deployment → Web-based user access

### ✅ Interactive Web App
- Simple HTML UI to input patient parameters
- Predictions returned instantly via Flask backend

### ✅ Visual Health Analytics
- EDA using statistical and visualization techniques
- Insights into most influential features (e.g., chest pain, cholesterol)

---

## Architecture & Data Flow

### 🔹 Input & Data Preprocessing
- Handled missing values and encoded categorical features
- Normalization using **NumPy** and **Pandas**

### 🔹 Model Training
- **scikit-learn Logistic Regression** with train-test split
- Evaluation using key metrics such as accuracy

### 🔹 Visualization & Insights
- **Matplotlib** and **Seaborn** for charts and heatmaps

### 🔹 Deployment Layer
- Model serialized and served via **Flask API**

### 🔹 Frontend Interface
- Basic HTML form connected to Flask routes for prediction results

---

## ✅ Reliability, Validation & Observability
- ✔ Standardized data for better model convergence
- ✔ Evaluation on balanced metrics for improved reliability
- ✔ Modular architecture for scalability
- ✔ Support for additional medical features in future versions

---

##  Use Cases & Value

- Early health-screening applications  
- AI support for clinical decision-making  
- Preventive risk awareness for vulnerable groups  
- Potential integration into tele-health systems  

---

##  Future Enhancements

- Implement **ensemble models / XGBoost** for increased accuracy  
- Add **REST API documentation (Swagger)** and testing using Postman  
- Cloud deployment (Render, Azure, AWS)  
- Use **Explainable AI (SHAP/LIME)** for feature interpretability  
- Support for patient login, secure history tracking  

---

##  Tech Stack

| Component | Tools Used |
|----------|------------|
| Model | Logistic Regression (scikit-learn) |
| Deployment | Flask API |
| Frontend | HTML Form |
| Data Processing | NumPy, Pandas |
| Visualization | Matplotlib, Seaborn |

---

##  Project Status
✅ Functional Prototype with 86% model accuracy  
🔄 Continual improvements planned

---


