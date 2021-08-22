# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 18:15:02 2021

@author: backp
"""

import Database

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
    
def convertWind(d):
    for key in d:
        if key in d: 
            d[key] =  d[key] * 3.6
    return(d)    

sqllitelDB = Database.Database('sqllite')

# sqllitelDB = Database.Database('mysql')
    
YRwind = sqllitelDB.returnDictionary('select MOUNTAIN_NAME, AVG(wind) avg_wind from YR group by MOUNTAIN_NAME ORDER BY avg_wind DESC')
MFwind = sqllitelDB.returnDictionary('select MOUNTAIN_NAME, AVG(wind) avg_wind from MountainForcast group by MOUNTAIN_NAME ORDER BY avg_wind DESC')


sortDict(merge(MFwind,YRwind))