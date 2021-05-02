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

#import australia rain csv file and set "Date" column as index
import pandas as pd
import numpy as np
australia_rain = pd.read_csv("C:\\Users\\Home\\Desktop\\UCD Professional Academy\\datasets\\Australia rain\\weatherAUS.csv",index_col="Date")
print (australia_rain)
#sort value of "Location" acending and "MinTemp" decending and save as australia_rain_min
australia_rain_loc_min = australia_rain.sort_values(["Location","MinTemp"], ascending = [True,False])
print (australia_rain_loc_min.head())
#creat a new table for major cities sorted in alphabetic order
aus_bigcity=["Adelaide", "Brisbane", "Darwin", "Melbourne", "Perth", "Sydney"]
aus_bigcity_rain = australia_rain[australia_rain["Location"].isin(aus_bigcity)]
aus_bigcity_rain_locsorted = aus_bigcity_rain.sort_values("Location",ascending = True)
print (aus_bigcity_rain_locsorted)
#create new column of temperature difference 
aus_bigcity_rain_locsorted["TempDifferance"] = aus_bigcity_rain_locsorted["MaxTemp"] - aus_bigcity_rain_locsorted["MinTemp"]
print (aus_bigcity_rain_locsorted)
#for each location, use numpy to get min, max, mean and median of Temp3pm
aus_loc_temp3pm = aus_bigcity_rain_locsorted.groupby("Location")["Temp3pm"].agg([np.min, np.max, np.mean, np.median])
print (aus_loc_temp3pm)
#pivot table and numpy to get min, max, mean and median of Temp3pm
aus_loc_temp3pm_piv = aus_bigcity_rain_locsorted.pivot_table(values = "Temp3pm", index = "Location", aggfunc = [np.min, np.max, np.mean, np.median])
print (aus_loc_temp3pm_piv)


print (aus_bigcity_rain_locsorted.isna().any())
#index as location and remove rows with missing value
aus_loc_index = aus_bigcity_rain_locsorted.set_index (["Location"]).dropna()
print (aus_loc_index.loc["Brisbane":"Melbourne"])
aus_loc_index.to_csv ("aus_loc_index.csv")
#scatter plot for rainfall vs pressure 9am
import matplotlib.pyplot as plt
aus_loc_index.plot (x = "Humidity3pm", y = "Rainfall", kind = "scatter", title = "Rainfall (mm) vs. Humidity at 3pm")
plt.show()

#create two small dataframes and merge
for city in australia_rain:
    city = australia_rain [australia_rain["Location"]=="Brisbane"]
print (city)




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

#Import API data from alpha_vantage website 
import pandas as pd
from alpha_vantage.foreignexchange import ForeignExchange
fx=ForeignExchange(key,output_format='pandas')
fxdata=fx.get_currency_exchange_daily('EUR','USD',outputsize='compact')
EUR_USD_Daily= pd.DataFrame(fxdata[0])
print (EUR_USD_Daily)
EUR_USD_Daily.plot(title='EUR to USD Daily Rate')








    
