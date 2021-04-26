# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 23:02:05 2021

@author: Home
"""

#kaggle datasets download -d ajaypalsinghlo/world-happiness-report-2021
import pandas as pd
world_happiness_report_2021 = pd.read_csv("C:\\Users\\Home\\Desktop\\UCD Professional Academy\\world-happiness-report-2021.csv")
print (world_happiness_report_2021.head())
print (world_happiness_report_2021.info())
print (world_happiness_report_2021.isna().any())
print (world_happiness_report_2021[:4])

australia_rain = pd.read_csv("C:\\Users\\Home\\Desktop\\UCD Professional Academy\\datasets\\Australia rain\\weatherAUS.csv")
print (australia_rain)
print (australia_rain.head())
print (australia_rain.isna().any())
#australia_rain_index = pd.DataFrame(index = "location")

#import API request
import requests
print (requests.get('http://google.com'))


#API for open-notify.org
iss = requests.get('http://api.open-notify.org/iss-now.json')
print (iss.text)
issj = iss.json()
print (issj)
print (issj['iss_position'])

people=requests.get('http://api.open-notify.org/astros.json')
print (people.json()['people'])

#print people name in a for loop
i = 1
for name in people.json()['people']:
    print (str(i) + ' ', name['name'])
    i = i + 1
    
