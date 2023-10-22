from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load your machine learning model and any necessary preprocessing steps

# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define a route for handling the form submission
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the form data
    married = 1 if request.form['Married'].lower() == 'yes' else 0
    dependents = float(request.form['Dependents'])
    education = 1 if request.form['Education'].lower() == 'graduate' else 0
    self_employed = 1 if request.form['Self_Employed'] else 0
    applicant_income = float(request.form['ApplicantIncome'])
    coapplicant_income = float(request.form['CoapplicantIncome'])
    loan_amount = float(request.form['LoanAmount'])
    loan_amount_term = float(request.form['Loan_Amount_Term'])
    credit_history = float(request.form['Credit_History'])
    property_area = ''
    if request.form['Property_Area'].lower() == 'urban':
        property_area = 0
    elif request.form['Property_Area'].lower() == 'semi-urban':
        property_area = 1
    else:
        property_area = 2
        
        
        total_income=applicant_income+coapplicant_income
        

    # Perform any necessary preprocessing on the input data
    # Convert categorical variables to numeric representation if needed

    # Create a single prediction sample
    single_pred = np.array([married,education,self_employed,property_area,dependents, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history,total_income])

    # Make sure the input has the correct shape
    single_pred = single_pred.reshape(1, -1)
    loaded_model = pickle.load(open('./model.pkl', 'rb'))
    # Make predictions using your loaded model
    prediction = loaded_model.predict(single_pred)

    # Process the prediction and generate the result
    result = "Approved" if prediction == 1 else "Rejected"

    # Return the prediction result to the client
    return result

# Run the Flask application
if __name__ == '__main__':
    app.run()
