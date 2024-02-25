import streamlit as st
import joblib
import pandas as pd


model=joblib.load('crop10.joblib')
def predict_soil(features):
    # Make prediction using the loaded model
    prediction = model.predict(features)
    return prediction

st.title('CROP RECOMMENDATION SYSTEM')
st.image('th.jfif')

nitrogen=st.number_input('Enter nitrogen value')
phosporous=st.number_input('Enter phosporous value')
potassium=st.number_input('Enter potassium value')
temp=st.number_input('Enter Temperature value')
humidity=st.number_input('Enter humidity value')
ph=st.number_input('Enter ph value')
rainfall=st.number_input('Enter rain value')

data=pd.DataFrame({'N':nitrogen,
    'P':phosporous,
    'K':potassium,
    'temperature':temp,
    'humidity':humidity,
    'ph':ph,
    'rainfall':rainfall,
                }  , index=[0]
                )

if st.button("Predict"):
    # Make prediction on the input features
    prediction = predict_soil(data)
    if prediction=='rice':
        st.write('The Land is sutable for rice')
    if prediction=='maize':
        st.write('The Land is sutable for maize')
    if prediction=='chickpea':
        st.write('The Land is sutable for chickpea')
        st.image('Sa-whitegreen-chickpea.jpg')
    if prediction=='kidneybeans':
        st.write('The Land is sutable for kidneybeans')
    if prediction=='pigeonpeas':
        st.write('The Land is sutable for pigeonpeas')
    if prediction=='mothbeans':
        st.write('The Land is sutable for mothbeans')
    if prediction=='mungbean':
        st.write('The Land is sutable for mungbean')
    if prediction=='blackgram':
        st.write('The Land is sutable for blackgram')
    if prediction=='lentil':
        st.write('The Land is sutable for lentil')
    if prediction=='pomegranate':
        st.write('The Land is sutable for pomegranate')
    if prediction=='banana':
        st.write('The Land is sutable for banana')
    if prediction=='mango':
        st.write('The Land is sutable for mango')
    if prediction=='grapes':
        st.write('The Land is sutable for grapes')
    if prediction=='watermelon':
        st.write('The Land is sutable for watermelon')
    if prediction=='muskmelon':
        st.write('The Land is sutable for muskmelon')
    if prediction=='apple':
        st.write('The Land is sutable for apple')
    if prediction=='orange':
        st.write('The Land is sutable for orange')
    if prediction=='papaya':
        st.write('The Land is sutable for papaya') 
    if prediction=='coconut':
        st.write('The Land is sutable for coconut') 
    if prediction=='cotton':
        st.write('The Land is sutable for cotton') 
    if prediction=='jute':
        st.write('The Land is sutable for jute') 
    if prediction=='coffee':
        st.write('The Land is sutable for coffee')                                                                                   
       