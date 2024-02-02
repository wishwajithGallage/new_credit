# -*- coding: utf-8 -*-


import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np


# loading the saved models

credit_model = pickle.load(open('credit_model.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Credit Card Fraud Detection System',
                          
                          ['Credit_Card_Fraud_Detection'],
                          icons=['activity'],
                          default_index=0)
    
    

        
    
    

# Parkinson's Prediction Page
if (selected == "Credit_Card_Fraud_Detection"):
    
    # page title
    st.title("Credit Card Fraud Detection using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        Time = st.text_input('Time')
        
    with col2:
        V1 = st.text_input('V1')
        
    with col3:
        V2 = st.text_input('V2')
        
    with col4:
        V3 = st.text_input('V3')
        
    with col5:
        V4 = st.text_input('V4')
        
    with col1:
        V5 = st.text_input('V5')
        
    with col2:
        V6 = st.text_input('V6')
        
    with col3:
        V7 = st.text_input('V7')
        
    with col4:
        V8 = st.text_input('V8')
        
    with col5:
        V9 = st.text_input('V9')
        
    with col1:
        V10 = st.text_input('V10')
        
    with col2:
        V11 = st.text_input('V11')
        
    with col3:
        V12 = st.text_input('V12')
        
    with col4:
        V13 = st.text_input('V13')
        
    with col5:
        V14 = st.text_input('V14')
        
    with col1:
        V15 = st.text_input('V15')
        
    with col2:
        V16 = st.text_input('V16')
        
    with col3:
        V17 = st.text_input('V17')
        
    with col4:
        V18 = st.text_input('V18')
        
    with col5:
        V19 = st.text_input('V19')
        
    with col1:
        V20 = st.text_input('V20')
        
    with col2:
        V21 = st.text_input('V21')
        
    with col3:
        V22 = st.text_input('V22')
        
    with col4:
        V23 = st.text_input('V23')
        
    with col5:
        V24 = st.text_input('V24')
        
    with col1:
        V25 = st.text_input('V25')
        
    with col2:
        V26 = st.text_input('V26')
        
    with col3:
        V27 = st.text_input('V27')
        
    with col4:
        V28 = st.text_input('V28')
        
    with col5:
        Amount = st.text_input('Amount')
        

        
    
    
    # code for Prediction
    credit_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Credit_Card_Fraud_Detection_Test_Result"):
        # Assuming Time, V1 to V28, and Amount are variables with proper numeric values
        input_data = np.array([[Time,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]], dtype=float)

        # Now use this input_data for prediction
        Credit_Card_Fraud_Detection = credit_model.predict(input_data)
        #Credit_Card_Fraud_Detection = credit_model.predict([[Time,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]])                          
        
        if (Credit_Card_Fraud_Detection[0] == 0):
          credit_diagnosis = "legitimate"
        else:
         credit_diagnosis = "fraudulent"
        
    st.success(credit_diagnosis)






