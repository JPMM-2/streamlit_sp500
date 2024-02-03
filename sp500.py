# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 19:12:05 2024

@author: JPMM
"""

import yfinance as yf
import pandas as pd
import streamlit as st
import seaborn as sns



def get_data(startt, endd, list_tickers, what):
    hist = []
    msft = yf.Ticker(list_tickers[0])
    hist = msft.history(start = startt, end = endd)
    hist['Symbol'] = list_tickers[0]
    
   
    
    #for n, i in enumerate(list_tickers[1:]):
    for i in list_tickers[1:]:
        partial = []
        #print(n);print(i)
        msft = yf.Ticker(i)
        partial = msft.history(start = startt, end = endd)
        partial['Symbol'] = i
        #hist = partial.append(hist)
        hist = pd.concat([hist, partial])
    
      
    list_tickers = ['hello']
    
    return hist




def user_input(df0):
    
    for col in df0.columns:
        if df0[col].dtypes == 'object':
            categorical_fields.append(col)
            unique = df0[col].unique()
            option = st.sidebar.multiselect('Choose your ' + str(col), unique,unique)
            #st.write('# You selected:', option)
            df0 = df0[df0[col].isin(option)]
    for col in df0.columns:
        #st.write('my header isssssss ' +str(col))
        if df0[col].dtypes == 'float64' and int(df0[col].min()) != int(df0[col].max()):
            numeric_fields.append(col)
            param1 = st.sidebar.slider(col,int(df0[col].min()), int(df0[col].max()), int(df0[col].min()))
            df0 = df0[df0[col]>=param1]
        
			
    option2 = st.sidebar.selectbox('Select the field', categorical_fields)
    
    st.dataframe(df0.describe())
    #st.write(df0.columns.to_list())
    
    import matplotlib.pyplot as plt
    for col in categorical_fields:
        
        fig2 = plt.figure(figsize=(10, 4))
        sns.countplot(x=df0[col], data = df0)
        st.pyplot(fig2)

    fig = sns.pairplot(df0, hue = option2)
    st.pyplot(fig)
  
    #st.write(categorical_fields)
    #st.write(numeric_fields)
    


listt = ['AAPL','MSFT','AMZN','TSLA','GOOGL','GOOG','BRK.B','UNH','NVDA'];

df0 = get_data('2023-12-01', '2023-12-31', listt,1)
df0.reset_index(inplace = True)

df0 = df0[['Symbol', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

df0.reset_index(inplace = True)

categorical_fields = []
numeric_fields = []
option2 = ''


user_input(df0)









