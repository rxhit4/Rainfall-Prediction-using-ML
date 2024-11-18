# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 00:54:13 2024

@author: rohit
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import resample #to manage class imbalance
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


#LOADING THE SAVED PICKLE MODEL
loaded_model = pickle.load(open("trained_model.sav", 'rb'))

#CREATING A FUNCTION FOR PREDICTION

def rainfall_prediction(input_data):
    
    
    input_df = pd.DataFrame([input_data], columns = ['pressure', 'temparature', 'dewpoint', 'humidity', 'cloud', 'sunshine', 'winddirection', 'windspeed'])
    prediction = loaded_model.predict(input_df)
    return'Prediction result:', "Rainfall is expected" if prediction == 1 else "Rainfall is NOT expected"
    
    
    def main():
        
        #giving a title
        st.title('Rainfall Prediction Web App')
        
        #Getting the input data from the user
        pressure = st.text_input('Pressure')
        temparature = st.text_input('Temperature')
        dewpoint = st.text_input('Dewpoint')
        humidity = st.text_input('Humidity')
        cloud = st.text_input('Cloud')
        sunshine = st.text_input('Sunshine')
        winddirection = st.text_input('Wind Direction')
        windspeed = st.text_input('Wind Speed')
        
        
        #CODE FOR PREDICTION
        Forecasting = ''
        
        #Creating a Button for Prediction
        if st.button('Rainfall Prediction'):
            Forecasting = rainfall_prediction([pressure, temparature, dewpoint, humidity, cloud, sunshine, winddirection, windspeed])
            
        st.success(Forecasting)
        
        
        
        
        
        
    if __name__ == "__main__":
          main()
        
        
        
        
        
        
        
        
        
