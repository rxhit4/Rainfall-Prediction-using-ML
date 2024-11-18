# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 00:54:13 2024

@author: rohit
"""
import pandas as pd
import pickle
import streamlit as st

# LOADING THE SAVED PICKLE MODEL
loaded_model = pickle.load(open("C:/Users/Rohit Btech/Desktop/DEPLOYML/trained_model.sav", 'rb'))

# CREATING A FUNCTION FOR PREDICTION
def rainfall_prediction(input_data):
    input_df = pd.DataFrame([input_data], columns=['pressure', 'temparature', 'dewpoint', 'humidity', 'cloud', 'sunshine', 'winddirection', 'windspeed'])
    prediction = loaded_model.predict(input_df)
    if prediction[0] == 1:
        return 'Rainfall is Expected'
    else:
        return 'Rainfall is NOT Expected'


def main():
    # Giving a title
    st.title('Rainfall Prediction Web App')

    # Getting the input data from the user
    pressure = st.text_input('Pressure')
    temparature = st.text_input('Temperature')
    dewpoint = st.text_input('Dewpoint')
    humidity = st.text_input('Humidity')
    cloud = st.text_input('Cloud')
    sunshine = st.text_input('Sunshine')
    winddirection = st.text_input('Wind Direction')
    windspeed = st.text_input('Wind Speed')

    # Code for prediction
    if st.button('Rainfall Prediction'):
        # Make sure all inputs are filled
        if all([pressure, temparature, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]):
            input_data = [pressure, temparature, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]
            forecasting = rainfall_prediction(input_data)
            st.success(forecasting)
        else:
            st.error("Please fill in all fields")

if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
        
