import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
from sklearn.preprocessing import MinMaxScaler # type: ignore

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

dataset = pd.read_csv('diabetes.csv')

dataset_X = dataset.iloc[:, [1, 2, 5, 7]].values


sc = MinMaxScaler(feature_range=(0, 1))
dataset_scaled = sc.fit_transform(dataset_X)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    For rendering results on HTML GUI
    """
    global pred
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(sc.transform(final_features))

    if prediction == 1:
        pred = "High probability of having Diabetes, please consult a Doctor."
    elif prediction == 0:
        pred = "Low Probability of having Diabetes."
    output = pred

    return render_template('index.html', prediction_text='{}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
