import yfinance as yf
import streamlit as st
import pandas as pd 
import numpy as np

st.write("""
         # Simple Stock Price App
         Shown are the stock closing price and volume of Google!
         """)

#define ticker symbol
tickerSymbol = "GOOGL"


#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historcial prices for this ticker

tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)


