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
                                 "Rhode Island","New York","Pennsylvania","Connecticut",
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

##replace missing values with 0
##only for exercise purpose for this part
replace_value = USA_crime.fillna(0)
print (replace_value.isnull().sum())


##drop columns with data missing the most
##column rape_legacy, rape_revised and caveats have most missing values
USA_crime_drop = USA_crime.drop(axis=1, columns=["rape_legacy","rape_revised","caveats"])
print (USA_crime_drop.columns)

##Add a new column to USA_crime_drop as Region set as blank
##Use for loop to check state_name column against state values in dictionary
##Assign relevant key which is region name to region column

USA_crime_drop["region"] = ''
        
for key in USA_Region_State.items():
    
    for i in range(len(USA_crime_drop)):
        #print(USA_crime_drop['state_name'].values[i])
        state_name = USA_crime_drop['state_name'].values[i]
                
        if (state_name in key[1]):
            USA_crime_drop.at[i, 'region'] = key[0]
           
#USA_crime_drop.to_csv('new_USA_crime.csv', index=False)
            
print(USA_crime_drop.head())
print(USA_crime_drop.info())

##drop rows with missing value in USA_crime_drop to remove all rows with
##total number of population and crime rates
USA_crime_drop2=USA_crime_drop.dropna()
print (USA_crime_drop2.head())
print (USA_crime_drop2.info())
##No missing value left in the DataFrame

##sort under each year with region in ascending order
USA_crime_region_sorted=USA_crime_drop2.sort_values(["year","region"])
print (USA_crime_region_sorted.head())

##index was scrambled after sorting region under each year
##reset index to ascending order
USA_crime_region_sorted_index=USA_crime_region_sorted.reset_index(drop=True)
print (USA_crime_region_sorted_index.head())

##adding a column total crime with sum of each crime
##slicing all rows with year, total crime and region as a subset
USA_crime_region_sorted_index["total_crime"]=USA_crime_region_sorted_index["violent_crime"] + USA_crime_region_sorted_index["homicide"]+USA_crime_region_sorted_index["robbery"]+USA_crime_region_sorted_index["aggravated_assault"]+USA_crime_region_sorted_index["property_crime"]+USA_crime_region_sorted_index["burglary"]+USA_crime_region_sorted_index["larceny"]+USA_crime_region_sorted_index["motor_vehicle_theft"]
print (USA_crime_region_sorted_index.head())
USA_total_crime_region = USA_crime_region_sorted_index.loc[:,["year","region","total_crime"]]
print (USA_total_crime_region.head())

##groupby year and region and sum of each region's total crime
region_crime = USA_total_crime_region.groupby(["year","region"])["total_crime"].sum().reset_index()
print (region_crime)

##use line plot to show each region total crime from 1979 to 2019
lineplot1=sns.lineplot(x="year", y="total_crime",data=region_crime,hue="region")
lineplot1.set_title("Total Crime in each region USA 1979 - 2019")
lineplot1.set(xlabel="year", ylabel="Total Crime Number (x10000000)")
plt.show()


#USA_crime_region_sorted.to_csv("new_USA_crime.csv", index=False)

print (USA_crime_region_sorted_index.head())

##Def function to lineplot any state the user input to show that state's
##total crime from 1979 to 2019
def my_function(statename):
    state_file=USA_crime_region_sorted_index.loc[USA_crime_region_sorted_index["state_name"]==statename]
        
    func_lineplot=sns.lineplot(x="year",y="total_crime",data=state_file,hue="state_name")
    func_lineplot.set_title("Total Crime in " + statename + " USA 1979 - 2019")
    func_lineplot.set(xlabel="year",ylabel="Total Crime Number (x1000000")
    plt.show()
    
    
my_function("Illinois")

    
        


                
            

 





        



        
























