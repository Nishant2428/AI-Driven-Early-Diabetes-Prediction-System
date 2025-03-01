# AI-driven Early Diabetes Prediction Using Machine Learning

## Overview
This project implements an AI-driven approach to predict early-stage diabetes using machine learning. It utilizes various ML models to analyze health parameters and provide a risk assessment for diabetes. The study achieved a 75% accuracy using the K-Nearest Neighbors (KNN) model and was deployed using Flask for real-time prediction.

## Features
- Machine Learning models for diabetes prediction
- Data preprocessing and feature selection
- Flask-based web application for real-time predictions
- Visualization of model performance
- Trained using publicly available datasets

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-diabetes-prediction.git
   cd ai-diabetes-prediction
   ```
2. Create and activate a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## Usage
1. Open your web browser and go to `http://127.0.0.1:5000`
2. Upload health-related data (e.g., glucose levels, BMI, age, etc.)
3. Click "Predict" to get the diabetes risk assessment

## Screenshots
Here are some screenshots of the interface and results:

### Web Interface
![Web_Interface](https://github.com/user-attachments/assets/9cdb00f2-bdb4-41f6-bbaa-f7e989c430c0)

### Prediction Results
![Prediction_Results](https://github.com/user-attachments/assets/117221ab-592e-4998-a5c1-45f29e03b09a)

## Dataset
The project uses a diabetes dataset that contains various health attributes. The dataset is preprocessed to handle missing values and normalize data.

## Methodology
- Data preprocessing (handling missing values, normalization)
- Feature selection for improved model performance
- Training different ML models (KNN, SVM, Decision Tree, Random Forest, etc.)
- Model evaluation using accuracy, precision, recall, and F1-score
- Deployment using Flask for real-time predictions

## Contributors  
- **Nishant Kumar**  
  Supervised by **Inderdeep Kaur**

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
