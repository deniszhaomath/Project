# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 23:02:05 2021

@author: Home
"""

#kaggle datasets download -d ajaypalsinghlo/world-happiness-report-2021
#import pandas as pd
#world_happiness_report_2021 = pd.read_csv("C:\\Users\\Home\\Desktop\\UCD Professional Academy\\world-happiness-report-2021.csv")
#print (world_happiness_report_2021.head())
#print (world_happiness_report_2021.info())
#print (world_happiness_report_2021.isna().any())
#print (world_happiness_report_2021[:4])

#australia_rain = pd.read_csv("C:\\Users\\Home\\Desktop\\UCD Professional Academy\\datasets\\Australia rain\\weatherAUS.csv")
#print (australia_rain)
#print (australia_rain.head())
#print (australia_rain.isna().any())
#australia_rain_index = pd.DataFrame(index = "location")

#import API request
import requests
#print (requests.get('http://google.com'))


#API for open-notify.org
#iss = requests.get('http://api.open-notify.org/iss-now.json')
#print (iss.text)
#issj = iss.json()
#print (issj)
#print (issj['iss_position'])

#people=requests.get('http://api.open-notify.org/astros.json')
#print (people.json()['people'])

#print people name in a for loop
#i = 1
#for name in people.json()['people']:
#    print (str(i) + ' ', name['name'])
#    i = i + 1

#import api file to datafram
#peopletable=pd.DataFrame(people.json())
#print (peopletable)

#API in alphavantage
from alpha_vantage.timeseries import TimeSeries
key = 'NNV2OBWS7SL55JOQ'
ts = TimeSeries(key,output_format='pandas')
#data,meta = ts.get_intraday('TSLA',interval='1min',outputsize='full')
#print (data.info())
#print (data.head())
#data.columns=['open','high','low','close','volume']
#data['close'].plot()
#data['date']=data.index.date
#data['time']=data.index.time
#data.index.names=['datetime']
#print(data.head())
#market = data.between_time('09:00:00', '16:00:00').copy()
#market.sort_index(inplace=True)
#print(market.head())
#market_mean=market.groupby('date').mean()
#print(market_mean.head())
#high_low=market.groupby('date').agg({'low':min, 'high':max})
#print (high_low.head())

#myapi trial

#from alpha_vantage.fundamentaldata import FundamentalData
#fd=FundamentalData(key,output_format='pandas')
#data=fd.get_cash_flow_annual('TSLA')
#print (data)

import pandas as pd
from alpha_vantage.foreignexchange import ForeignExchange
fx=ForeignExchange(key,output_format='pandas')
fxdata=fx.get_currency_exchange_daily('EUR','USD',outputsize='compact')
EUR_USD_Daily= pd.DataFrame(fxdata[0])
print (EUR_USD_Daily)
EUR_USD_Daily.plot(title='EUR to USD Daily Rate')








    
