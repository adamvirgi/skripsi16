
import streamlit as st
import pickle
import pandas as pd

# Load the pickle model
model = pickle.load(open('stunting.pkl', 'rb'))

# Define the application layout
st.title('Stunting Prediction App')

# Get user input
age = st.number_input('Age (Month)', min_value=0, max_value=72)
gender = st.selectbox('Gender', ['Female', 'Male'])
body_height = st.number_input('Body Height (cm)', min_value=0.0, max_value=1.0)

# Preprocess the user input
input_data = {
    'Age (Month)': [age],
    'Gender': [gender],
    'Body height': [body_height]
}
input_df = pd.DataFrame(input_data)

# Make predictions
if st.button('Predict'):
    prediction = model.predict(input_df)[0]
    status = 'Stunted' if prediction == 0 else 'Tall' if prediction == 1 else 'Normal' if prediction == 2 else 'Severely Stunted'
    st.write(f'Predicted Status: {status}')

