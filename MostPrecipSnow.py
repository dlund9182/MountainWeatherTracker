# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 22:04:44 2021

@author: backp
"""

import Database

def normalize(arr1):
    arr2 = {}
    count = 0
    divisor = 1
    for item in arr1:
        if count == 0:
            arr2[item[0]] = 1
            divisor = item[1]
        else:
            arr2[item[0]] = (item[1] / divisor)
        count = count + 1
    return(arr2)
        
def merge(d1,d2):
    d = {}
    for key in d1:
        if key in d2:
            d[key] =  (d1[key] + d2[key]) / 2
    return(d) 

def sortDict(d):
    sorted_dict = {}
    sorted_keys = sorted(d, key=d.get) 
    
    for w in sorted_keys:
        sorted_dict[w] = d[w]
    print(sorted_dict)
    
    
def addDict(d1,d2,d3):
    d = {}
    for key in d1:
        if ((key in d2) and (key in d3)):
            d[key] =  (d1[key] + d2[key] + d3[key]) / 3
    return(d)  

sqllitelDB = Database.Database('sqllite')
# sqllitelDB = Database.Database('mysql')

YRprecip = normalize(sqllitelDB.returnRecords('select MOUNTAIN_NAME, avg(PRECIPITATION) avg_PRECIPITATION from YR group by MOUNTAIN_NAME ORDER BY avg_PRECIPITATION DESC'))
MFsnow = normalize(sqllitelDB.returnRecords('select MOUNTAIN_NAME, avg(SNOW) avg_SNOW from MountainForcast group by MOUNTAIN_NAME ORDER BY avg_SNOW DESC'))
MFrain = normalize(sqllitelDB.returnRecords('select MOUNTAIN_NAME, avg(rain) avg_rain from MountainForcast group by MOUNTAIN_NAME ORDER BY avg_rain desc'))

snowPrecip = merge(MFsnow,YRprecip)

sortDict(addDict(YRprecip,MFsnow,MFrain))