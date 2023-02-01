# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:19:03 2021

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
    

sqllitelDB = Database.Database('sqllite')
# sqllitelDB = Database.Database('mysql')

where = " WHERE date LIKE '2023%' "

YRtemp = sqllitelDB.returnDictionary("select MOUNTAIN_NAME, AVG(temp) avg_temp from YR" + where + "group by MOUNTAIN_NAME ORDER BY avg_temp ASC")
MFtemp = sqllitelDB.returnDictionary("select MOUNTAIN_NAME, AVG(temp) avg_temp from MountainForcast" + where + "group by MOUNTAIN_NAME ORDER BY avg_temp ASC")

sortDict(merge(MFtemp,YRtemp))
