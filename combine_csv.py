# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:36:10 2020

@author: lygc7
"""
import csv

stockFile=open("yfinanceData3yr - yfinanceData3yr.csv", "r")
threeYrModelFile=open("3yearmodel.csv","w", newline='')

stockRecords=csv.reader(stockFile)
threeyrModelwriter=csv.writer(threeYrModelFile)

for row in stockRecords:
    found = False
    trendFile=open("pytrend_daily_mean_median_data_version_2.csv","r")
    trendRecords=csv.reader(trendFile)    
    for row2 in trendRecords:
        if row[0]==row2[0]:
            threeyrModelwriter.writerow([row[0],row[5],row2[1],row2[3],row2[5],row2[7],row[11]])
            found = True
            break
    trendFile.close()
    if found == False:
        print(row[0])

stockFile.close()
threeYrModelFile.close()

            
