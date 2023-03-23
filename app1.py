import streamlit as st
import pickle
import numpy as np
import pandas as pd

pipe = pickle.load(open('Car_Price_Predictor.pkl','rb'))
df = pickle.load(open('car.pkl', 'rb'))

st.title("Car Price Predictor")

name = st.selectbox('name',df['name'].unique())

company = st.selectbox('company',df['company'].unique())

year = st.selectbox('year',df['year'].unique())

kms_driven = st.selectbox('kms_driven',df['kms_driven'].unique())

fuel_type = st.selectbox('fuel_type',df['fuel_type'].unique())

if st.button('Predict Price'):
    input_df = pd.DataFrame({'name':[name],'company':[company],'year':[year],'kms_driven':[kms_driven],'fuel_type':[fuel_type]})
    result = pipe.predict(input_df)
    st.header("The Estimated amount is")
    st.header(result)