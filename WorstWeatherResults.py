# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:09:13 2021

@author: D Lund
"""

import Database


def normalize(arrlist):
    """
    
    Input
      arrlist = an array(list)
      
    outputs
     a Normalized version of the array or in other words where every item
     in the list is updated to be basically a % of the largest of item in
     list.
    
    """  
    
    normalized_array = {}
    count = 0
    divisor = 1
    for item in arrlist:
        if count == 0:
            normalized_array[item[0]] = 1
            divisor = item[1]
        else:
            normalized_array[item[0]] = (item[1] / divisor)
        count = count + 1
    return(normalized_array)

def normalizeTemp(arrlist):
    """
    
    Input
      arrlist = an array(list)
      
    outputs
     a Normalized version of the array or in other words where every item
     in the list is updated to be basically a % of the largest of item in
     list. So basically like the previous version except this is specifically
     with Temperature which has negative values which makes a little different
     to deal with.
    
    """  
    normalized_array = {}
    coldest = arrlist[0]
    warmest = arrlist[len(arrlist) - 1]
    difference = warmest[1] - coldest[1]
    for item in arrlist:
        normalized_array[item[0]] = ((warmest[1] - item[1]) / difference)
    return(normalized_array)
        
def average_2_dictionaries(dictionary1,dictionary2):
    """
    
    Input
      Two dictionaries dictionary1 and dictionary2
      
    outputs
       returns a new dictionary consisting of keys that are in both dictionary1 
       and dictionary2 and whose value for each key is the average of the
       value for that key for dictionary1 and dictionary2 
    
    """  
    new_dictionary = {}
    for key in dictionary1:
        if key in dictionary2:
            new_dictionary[key] =  (dictionary1[key] + dictionary2[key]) / 2
    return(new_dictionary)

def average_3_dictionaries(dictionary1,dictionary2,dictionary3):
    new_dictionary  = {}
    for key in dictionary1:
        if ((key in dictionary2) and (key in dictionary3)):
            new_dictionary[key] =  (dictionary1[key] + dictionary2[key] + dictionary3[key]) / 3
    return(new_dictionary)   

def sortDict(d):
    sorted_dict = {}
    sorted_keys = sorted(d, key=d.get) 
    
    for w in sorted_keys:
        sorted_dict[w] = d[w]
    print(sorted_dict)
        
       
    
            
def main():
    sqllitelDB = Database.Database('sqllite')
    # sqllitelDB = Database.Database('mysql')
    
    YRprecip = normalize(sqllitelDB.returnRecords('select MOUNTAIN_NAME, avg(PRECIPITATION) avg_PRECIPITATION from YR group by MOUNTAIN_NAME ORDER BY avg_PRECIPITATION DESC'))
    YRwind = normalize(sqllitelDB.returnRecords('select MOUNTAIN_NAME, AVG(wind) avg_wind from YR group by MOUNTAIN_NAME ORDER BY avg_wind DESC'))
    YRtemp = normalizeTemp(sqllitelDB.returnRecords('select MOUNTAIN_NAME, AVG(temp) avg_temp from YR group by MOUNTAIN_NAME ORDER BY avg_temp ASC'))
    MFsnow = normalize(sqllitelDB.returnRecords('select MOUNTAIN_NAME, avg(SNOW) avg_SNOW from MountainForcast group by MOUNTAIN_NAME ORDER BY avg_SNOW DESC'))
    MFwind = normalize(sqllitelDB.returnRecords('select MOUNTAIN_NAME, AVG(wind) avg_wind from MountainForcast group by MOUNTAIN_NAME ORDER BY avg_wind DESC'))
    MFtemp = normalizeTemp(sqllitelDB.returnRecords('select MOUNTAIN_NAME, AVG(temp) avg_temp from MountainForcast group by MOUNTAIN_NAME ORDER BY avg_temp ASC'))
    
    snowPrecip = average_2_dictionaries(MFsnow,YRprecip)
    temp = average_2_dictionaries(MFtemp,YRtemp)
    Wind = average_2_dictionaries(MFwind,YRwind)
    
    sortDict(average_3_dictionaries(snowPrecip,temp,Wind))



    # mysqlDB.deleteAll('YR')
    # mysqlDB.deleteAll('MountainForcast')
    # mysqlDB.selectRecords("select MOUNTAIN_NAME, count(PRECIPITATION) count_PRECIPITATION from YR group by MOUNTAIN_NAME")
    
    # sqlliteDB = DatabaseTemp.Database('sqllite')
    # sqlliteDB.selectRecords("select MOUNTAIN_NAME, count(PRECIPITATION) count_PRECIPITATION from YR group by MOUNTAIN_NAME")
    
    print("-------------") 
    
    # sqlliteDB.selectRecords("select wind from MountainForcast")
    
    
    # sqlliteDB.selectRecords("select MOUNTAIN_NAME, sum(SNOW) sum_SNOW from MountainForcast group by MOUNTAIN_NAME ORDER BY sum_SNOW DESC")
    
    # "select MOUNTAIN_NAME, AVG(wind) avg_wind from MountainForcast group by MOUNTAIN_NAME ORDER BY avg_wind DESC"
    
    # "select MOUNTAIN_NAME, AVG(temp) avg_temp from MountainForcast group by MOUNTAIN_NAME ORDER BY avg_temp ASC"
    
    # "select MOUNTAIN_NAME, sum(rain) sum_rain from MountainForcast group by MOUNTAIN_NAME ORDER BY sum_rain desc"
    
    # select MOUNTAIN_NAME, SUM(PRECIPITATION) SUM_PRECIPITATION from YR group by MOUNTAIN_NAME ORDER BY SUM_PRECIPITATION DESC
    
    # select MOUNTAIN_NAME, AVG(wind) avg_wind from YR group by MOUNTAIN_NAME ORDER BY avg_wind DES
    
    # select MOUNTAIN_NAME, AVG(temp) avg_temp from YR group by MOUNTAIN_NAME ORDER BY avg_temp ASC
    
    # select MOUNTAIN_NAME, avg(PRECIPITATION) avg_PRECIPITATION from YR group by MOUNTAIN_NAME ORDER BY avg_PRECIPITATION DESC
    
    # select MOUNTAIN_NAME, avg(SNOW) avg_SNOW from MountainForcast group by MOUNTAIN_NAME ORDER BY avg_SNOW DESC
    
    
main()