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

"""EDIT TICKER BELOW!!"""
Ticker='NKE'

Today=date.today()
OneYear=str(date(Today.year-1, Today.month, Today.day))
ThreeYear=str(date(Today.year-3, Today.month, Today.day))
FiveYear=str(date(Today.year-5, Today.month, Today.day))
SevenYear=str(date(Today.year-7, Today.month, Today.day))
TenYear=str(date(Today.year-10, Today.month, Today.day))

#EDIT THE NUMBER OF DATES TO GO BACK!
SpecificDate='2008-1-1'
StartDate=FiveYear

#Choose from month / year / day
Frequency='month'

import requests
headers = {
    'Content-Type': 'application/json'
}
requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/"+Ticker+"/prices?startDate="+StartDate+"&token=1bd9aa149ea0c64cc64e4abd8e22f0a5f2757d11", headers=headers)
RawOutput = requestResponse.json()

MarketrequestResponse = requests.get("https://api.tiingo.com/tiingo/daily/spy/prices?startDate="+StartDate+"&token=1bd9aa149ea0c64cc64e4abd8e22f0a5f2757d11", headers=headers)
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
print(Ticker+'Beta: '+BetaString)