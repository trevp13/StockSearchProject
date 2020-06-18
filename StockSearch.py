# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 18:51:30 2019

@author: Trevor
"""

#!Python3

import requests, pandas as pd, numpy as np
from datetime import date
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt


print("Select a Ticker")
Ticker=input()

Today=date.today()
OneYear=str(date(Today.year-1, Today.month, Today.day))
ThreeYear=str(date(Today.year-3, Today.month, Today.day))
FiveYear=str(date(Today.year-5, Today.month, Today.day))
SevenYear=str(date(Today.year-7, Today.month, Today.day))
TenYear=str(date(Today.year-10, Today.month, Today.day))

#CHOOSE FROM ONE OF THE ABOVE # OF YEARS TO GO BACK OR ENTER A SPECIFIC DATE WITH FORMAT YYYY-MM-DD
StartDate=FiveYear

#Choose from month / year / day
Frequency='month'

import requests
headers = {
    'Content-Type': 'application/json'
}

#PUT YOUR TOKEN FROM TIINGO.com HERE
token = ''
#MAKE SURE TO REGISTER TO GET YOUR TIINGO AUTHORIZATION TOKEN AND ADD IT BELOW AFTER &token=
requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/"+Ticker+"/prices?startDate="+StartDate+"&token="+token, headers=headers)
RawOutput = requestResponse.json()

MarketrequestResponse = requests.get("https://api.tiingo.com/tiingo/daily/spy/prices?startDate="+StartDate+"&token="+token, headers=headers)
MarketRawOutput = MarketrequestResponse.json()

PandaOutput = pd.DataFrame(RawOutput)
MarketPandaOutput = pd.DataFrame(MarketRawOutput)

TrimmedPanda = PandaOutput.drop(columns=['adjHigh', 'adjLow', 'adjOpen', 'adjVolume', 'close', 'divCash', 'high', 'low', 'open', 'splitFactor', 'volume', 'date'])
MarketTrimmedPanda = MarketPandaOutput.drop(columns=['adjHigh', 'adjLow', 'adjOpen', 'adjVolume', 'close', 'divCash', 'high', 'low', 'open', 'splitFactor', 'volume', 'date'])


X = TrimmedPanda.values
Y = MarketTrimmedPanda.values
BetaData = linear_model.LinearRegression()
BetaData.fit(X, Y)
Beta = BetaData.score(X, Y)
BetaString=str(Beta)
print(Ticker+' Beta: '+BetaString)
