from flask import Flask, render_template, request
from textClassification.pipeline.prediction import PredictionPipeline  # Ensure the correct import path
import os

app = Flask(__name__)

# Initialize the PredictionPipeline
prediction_pipeline = PredictionPipeline()

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML form for text input

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']  # Get the user input text from the form
    
    try:
        # Use the PredictionPipeline to get the prediction
        prediction = prediction_pipeline.predict(text)
        return render_template('index.html', prediction=prediction, text=text)
    except Exception as e:
        return render_template('index.html', error=f"Prediction failed: {str(e)}", text=text)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
