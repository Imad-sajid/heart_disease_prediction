from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__,template_folder='templates')
#Staments
model = pickle.load(open('finalized_model.pkl', 'rb'))
#this slash is for home page
@app.route("/")
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():    
    """Grabs the input values and uses them to make prediction"""
    age = int(request.form["age"])
    sex = int(request.form["sex"])
    cp = int(request.form["cp"])
    trestbps = int(request.form["trestbps"])
    chol = int(request.form["chol"])
    fbs = int(request.form["fbs"])
    restecg = int(request.form["restecg"])
    thalach = int(request.form["thalach"])
    exang = int(request.form["exang"])
    oldpeak = float(request.form["oldpeak"])
    slope = int(request.form["slope"])
    ca = int(request.form["ca"])
    thal = int(request.form["thal"])

    features = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca,thal])

    features = np.reshape(features,(1, features.shape[0]))
    prediction = model.predict(features)
    value = prediction[0]
    if value == 0:
        return render_template('index.html', prediction_result = f'No heart disease. You got an healthy heart')
    else:
        return render_template('index.html', prediction_result = f'Heart failure possibility. You have to take a good care of your health.')    


if __name__ == "__main__":
    app.run(debug= True)
    