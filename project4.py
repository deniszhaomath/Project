# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:57:02 2021

@author: Home
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##Creat dictionary 
USA_Region_State = {"Northeast":["Maine","Vermont","New Hampshire","Massachusetts",
                                 "Rhode Island","New York","Pennsylvania","Conneticut",
                                 "New Jersey"],
                    "South":["Delaware","North Carolina","South Carolina","Georgia",
                             "Florida","Tennessee","Alabama","Mississippi",
                             "Louisiana","Maryland","Virginia","West Virginia",
                             "District of Columbia","Kentucky","Arkansas","Oklahoma",
                             "Texas"],
                    "Midwest":["Ohio","Michigan","Indiana","Wisconsin","Illinois",
                               "Minnesota","Iowa","Missouri","North Dakota",
                               "South Dakota","Nebraska","Kansas"],
                    "West":["Arizona","Colorado","Idaho","Montana","Nevada",
                            "New Mexico","Utah","Wyoming","Alaska","California",
                            "Hawaii","Oregon","Washington"]}

##import csv file american crime estimation 1979 to 2019
USA_crime = pd.read_csv("C:\\Users\\Home\\Desktop\\estimated_crimes_1979_2019.csv")
##checking dataframe
print (USA_crime.head())
print (USA_crime.shape)
print (USA_crime.info())

##count number of missing value in each column
missing_value = USA_crime.isnull().sum()
print (missing_value)

##drop columns data is missing the most
##column rape_revised and caveats have most missing values
USA_crime_drop = USA_crime.drop(axis=1, columns=["rape_revised","caveats"])
print (USA_crime_drop.columns)

##Using For loop to check state_name from USA_crime_drop against dictionary values
##create a new column region write key value from dictionary to cells
##result is to check state name and assign region name for later analysis

USA_crime_drop["region"] = ''
        
for key in USA_Region_State.items():
    
    for i in range(len(USA_crime_drop)):
        #print(USA_crime_drop['state_name'].values[i])
        state_name = USA_crime_drop['state_name'].values[i]
                
        if (state_name in key[1]):
            USA_crime_drop.at[i, 'region'] = key[0]
           
USA_crime_drop.to_csv('new.csv', index=False)
            
print(USA_crime_drop)





        



        
























