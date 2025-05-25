import streamlit as st
import joblib
import pandas as pd

def binary_encode(X):
    return X.applymap(lambda x: 1 if x == 'Yes' else 0)

model = joblib.load('models/churn_model.pkl')

st.title("Customer Churn Prediction")

gender = st.selectbox("Gender", ['Male', 'Female'])
tenure = st.slider("Tenure", 0, 72)
monthly_charges = st.number_input("Monthly Charges")

if st.button("Predict"):
    input_df = pd.DataFrame([[gender, tenure, monthly_charges]], columns=['gender', 'tenure', 'MonthlyCharges'])
    prediction = model.predict(input_df)
    st.write("Churn" if prediction[0] == 1 else "No Churn")
