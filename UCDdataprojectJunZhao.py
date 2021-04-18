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
