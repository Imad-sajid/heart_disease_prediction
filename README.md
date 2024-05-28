# Heart Disease Prediction

This repository contains code and resources for predicting heart disease using machine learning models.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project aims to predict the presence of heart disease in patients based on various medical attributes. It utilizes machine learning algorithms to build predictive models.

## Dataset
The dataset used for this project includes medical records with features such as age, gender, blood pressure, cholesterol levels, etc. It is sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Heart+Disease).

## Installation
To run this project locally, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/Imad-sajid/heart_disease_prediction.git
2. Navigate to the project directory:
   ```bash
   cd heart_disease_prediction
3. Install the required dependencies
   ```bash
   pip install -r requirements.txt
## Usage
### 1. Training the model
   - Open and run the heart_diseas_model_trained.ipynb notebook to train the model.
   - The trained model will be saved as 'finalized_model.pkl'.
### 2. Prediction
   - Use the 'app.py' script to run a Flask web application for predicting heart disease.
   - Start the application:
     ```bash
     python app.py
   - Access the web application at http://localhost:5000.


## Files
- **'heartdisease.ipynb':** Data exploration and preprocessing.
- **'heart_diseas_model_trained.ipynb':** Model training and evaluation.
- **'app.py':** Flask web application for making predictions.
- **'finalized_model.pkl':** Trained machine learning model.
- **'templates/':** HTML templates for the web application.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code follows best practices and includes necessary tests.

### License
This project is licensed under the owner of the repository. Feel free to use it as you please and make sure to attribute the developers.
