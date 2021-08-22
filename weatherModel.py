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
        """
            
        Input
          tag to set the protected variable tag in class weatherModel
      
        Returns nothing(void)  
    
        """         

        self._tag = tag
        
    def _setAttr(self,attr):
        """
        
        Input
          attr to set the protected variable attr in class weatherModel
          
        Returns nothing(void)
        
        """   
        self._attr = attr         
            
    def _getArray(self,start,end,soup,option = ""):
        """
        
        Input
          start: the startTH point in the array local array results
          end: the endTH point in the local array results
          soup: The beautiful soup object
          option: optional argument that defaults to "". 
          
        Returns nothing(void)
        
        return an arrray of end-start + 1
        
        """
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
        """
        
       I will get around to documenting this later since its bit esoteric
       and not strait forward to explain
        
        """
        if (option == "temp"):
            inner = outer.find('span',{'class':'temperature__label nrk-sr'})
            if (inner):
                return(outer.text.split('Temperature')[1][:-1])      
            else:
                return(0.0)
        
        return(outer.string)
        
    def _convertToNum(self,number_string):
        """
        
        Input
          number_string which is a string which in most cases will be digits
          unless it just has "-"
          
        Returns a float represenation of number_string unless it is just "-"
        in which case it returns 0
        
        """
        if (number_string == "-"):
            return(0.0)
        else:
            return(float(number_string))
    
        
    def _convertAll(self,arr):
        """
        
        Input
           arr which is an array of strings consisting either of just digits
           or just a "-"
          
        Returns a list(array) of numbers(floats)
          
        
        """
        return(list(map(self._convertToNum, arr)))
    
    def _avg(self,arr):
        """
        
        Input
           arr which is an array of floats
          
        Returns the average of the array arr
          
        
        """
    
        Arr = self._convertAll(arr)
        return(sum(arr) / len(arr))
    
    def setSoap(self):
        self._soup = BeautifulSoup(requests.get(self._file_url).text,"lxml")

    