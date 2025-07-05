import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template, request
import joblib

model = joblib.load('C:\\Users\\devra\\Desktop\\Data science\\11-Logistic-Regression-Models\\Heart_Disease_Prediction\\heart_disease_pred_model.joblib')

app = Flask(__name__)

# Home route to render the input form
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:        
        data = [float(request.form[f'feature{i}']) for i in range(1, 14)]  # 13 input fields
        input_data = np.array(data).reshape(1, -1)  # Reshape for the model

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Return result as JSON or render in HTML
        return render_template('index.html', prediction_text=f'Heart Disease Prediction: {int(prediction)}')

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
