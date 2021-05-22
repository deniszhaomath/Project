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

##Use iterrows function to loop through datafram to 
##access violence rate information
#for ind,row in USA_crime_region_sorted_index.iterrows():
 #   print (" In ", str(row["year"]), " ",row["state_name"]," has ", str(row["violent_crime"])," violent crime.")
    
##merge datafram
##first subset 2 dataframs, then merge them together
print (USA_crime_region_sorted_index.info())
USA_violent_crime = USA_crime_region_sorted_index[["year","state_name","violent_crime","aggravated_assault"]]
print (USA_violent_crime.head())
USA_light_crime = USA_crime_region_sorted_index[["year","state_name","robbery","burglary","motor_vehicle_theft"]]
print (USA_light_crime.head())
USA_mixed_crime = USA_violent_crime.merge(USA_light_crime,left_index=True,right_index=True)
print (USA_mixed_crime.info())

##numpy function
##use numpy function to calculate max, min, mean and median total crime in each region
print (USA_crime_region_sorted_index.info())
crime_stats = USA_crime_region_sorted_index.groupby(["year","region"])["total_crime"].agg([np.max,np.min,np.mean,np.median])
print (crime_stats)
bar=sns.lineplot(x="year",y="median",hue="region",data=crime_stats)
bar.set_title("Median Crime Rate in USA Regions 1979 - 2019")
bar.set(xlabel="year", ylabel="Median Crime Rate")
plt.show()

##Visualisation insight

##Insight 1
##Correlation between population and total crime rate
print (USA_crime_region_sorted_index.info())
sns.lmplot(x="population",y="total_crime",ci=95,data=USA_crime_region_sorted_index)
plt.xlabel("Population (x 10000000")
plt.ylabel("Total Crime Number (x 1000000")
plt.title("Correlation Between Population And Total Crime Rate", y =1.05)
plt.show()

##Insight 3
##From the Median Crime Rate in USA Regions 1979 - 2019
##we see crime rate peaked around 1990 in South, Midwest and Northeast
##First we want to see the top 5 states in each of these 3 regions with highest crime in 1990
south_midwest_northeast = USA_crime_region_sorted_index[(USA_crime_region_sorted_index["year"] == 1990)
                                      &(USA_crime_region_sorted_index["region"].isin(["South","Midwest","Northeast"]))].sort_values(["region","total_crime"],ascending = [True,False])
print (south_midwest_northeast.head())

smnbar=sns.catplot(x="total_crime",y="state_name",
                   data=south_midwest_northeast.groupby("region").apply(lambda x: x.nlargest(5,["total_crime"])),
                   kind="bar", hue = "region")
smnbar.fig.suptitle("Top 5 states with highest total crime in South, Midwest and Northeast Regions USA 1990", y=1.02)
smnbar.set(xlabel = "Total Crime (x1000000)", ylabel = "Top 5 states in South, Midwest and Northeast Regions")
plt.show()                

##now we have top 5 total crime states in south, midwest and northeast regions
##we want to show the comparison of serious crime and light crime in 1990
##we will use total of violent_crime, homicide and aggravated_assault as serious crime
##we will use total of robbery, property_crime, burglary, larceny and motor_vehicle_theft as light crime
south_midwest_northeast["total_serious_crime"]=south_midwest_northeast["violent_crime"]+south_midwest_northeast["homicide"]+south_midwest_northeast["aggravated_assault"]
south_midwest_northeast["total_light_crime"]=south_midwest_northeast["robbery"]+south_midwest_northeast["property_crime"]+south_midwest_northeast["burglary"]+south_midwest_northeast["larceny"]+south_midwest_northeast["motor_vehicle_theft"]
print (south_midwest_northeast.head())
print (south_midwest_northeast.info())

serious=sns.lmplot(data=south_midwest_northeast,x="population",y="total_serious_crime",hue="region",ci=95)
serious.fig.suptitle("Correlation between population and total serious crime rate in USA regions 1990",y=1.02)
serious.set(xlabel="Population (x10000000)",ylabel="Total Serious Crime Rate")
plt.show()

light=sns.lmplot(data=south_midwest_northeast,x="population",y="total_light_crime",hue="region",ci=95)
light.fig.suptitle("Correlation between population and total light crime rate in USA regions 1990",y=1.02)
light.set(xlabel="Population (x10000000)",ylabel="Total Light Crime Rate")
plt.show()

##compare total crime rate of each region in 1979, 1990 and 2019
year=(1979,1990,2019)
compare=USA_crime_region_sorted_index[USA_crime_region_sorted_index["year"].isin(year)
                                      ].sort_values(["year","region","total_crime"],ascending = [True,True,False])
print (compare)
compare_year=sns.catplot(x="region",y="total_crime",kind="bar",data=compare,hue="year",ci=None)
compare_year.fig.suptitle("Comparison of total crime rate in each region USA in 1979,1990 and 2019",y=1.02)
compare_year.set(xlabel="region", ylabel="Total Crime Rate")
plt.show()
        
##insight 5
##top 5 states in each region in 2019 are they still the same?
smn_2019 = USA_crime_region_sorted_index[(USA_crime_region_sorted_index["year"] == 2019)
                                      &(USA_crime_region_sorted_index["region"].isin(["South","Midwest","Northeast"]))].sort_values(["region","total_crime"],ascending = [True,False])
print (smn_2019.head())

smnbar_2019=sns.catplot(x="total_crime",y="state_name",
                   data=smn_2019.groupby("region").apply(lambda x: x.nlargest(5,["total_crime"])),
                   kind="bar", hue = "region")
smnbar_2019.fig.suptitle("Top 5 states with highest total crime in South, Midwest and Northeast Regions USA 2019", y=1.02)
smnbar_2019.set(xlabel = "Total Crime (x1000000)", ylabel = "Top 5 states in South, Midwest and Northeast Regions")
plt.show()            























