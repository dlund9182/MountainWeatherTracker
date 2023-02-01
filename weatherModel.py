# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 22:24:06 2021

@author: D Lund
"""

month_convert = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Ma":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}     
from bs4 import BeautifulSoup
import requests
import re 


class weatherModel:
    def __init__(self, file_url, tag, attr):
        self._file_url = file_url
        self._tag = tag
        self._attr = attr
        
    def _setTag(self,tag):
        self._tag = tag
        
    def _setAttr(self,attr):
        self._attr = attr         
            
    def _getArray(self,start,end,soup,option = ""):
        
        results = soup.find_all(self._tag,self._attr)
        arr = []
        count = 0 
        
        for result in results:
            
            if count < start:
                count = count + 1
                continue
            if count == end:
                break
            r = self.__getResults(result,option)
            if (not r) and (r != 0.0):
                continue
            arr.append(r)
            count = count + 1
        return(arr)
    
    def __getResults(self,outer,option):
        if (option == "temp"):
            return (outer.get_text()[:-1])

        return(outer.string)
        
    def _convertToNum(self,n):
        if (n == "-") or (n == None):
            return(0)
        else:
            return(float(n))
    
        
    def _convertAll(self,Arr):
        return(list(map(self._convertToNum, Arr)))
    
    def _avg(self,Arr):
        Arr = self._convertAll(Arr)
        return(sum(Arr) / len(Arr))
    
    def setSoap(self):
        self._soup = BeautifulSoup(requests.get(self._file_url).text,"lxml")

    
    
