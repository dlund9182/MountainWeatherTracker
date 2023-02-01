# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: by D Lund.


Scraping code using beautiful soup to parse out weather forecast info
from https://www.mountain-forecast.com for various mountains. Main focus is
on remote mountains with extreme weather especially when it comes to precipitation
and especially snowfall. Forecast info is then inserted into database. Goal is
to gather a lot of date for as many years as possible to get an idea what kind
of precipitation these mountains get. It uses superclass weatherModel.weatherModel to
inherit methods and variables

       
"""

import weatherModel
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import Database
import requests
import time
import random


class MountForcast(weatherModel.weatherModel):
    def __init__(self,file_url, tag, attr):
        super().__init__(file_url, tag, attr) 
        self.__soup = BeautifulSoup(requests.get(file_url).text,"lxml")       
        results = self.__soup.find('span',{'class': 'forecast__table-value'}).text   
        if (results.strip() == "AM"):
            self.__start = 0
            self.__end = 3
        elif  (results.strip() == "PM"):  
            self.__start = 2
            self.__end = 5
        else:
            self.__start = 1
            self.__end = 4        
        
    def getDate(self):
        arr = []
        results = self.__soup.find('div',{'class':'issued__issued'}) 
        result =  results.find_all('span')[0].string.split()
        arr.append(result[2])
        arr.append(result[3])
    
        
        results = self.__soup.find('div',{'class':'copyright small-12 columns'})  
        result =  results.find_all('p')[0].string.split()
        arr.append(result[1])
        
        
        date = datetime(int(arr[2]), weatherModel.month_convert[arr[1]], int(arr[0])) 
        
        if (self.__start > 0):
            date = date + timedelta(1) 
        return(str(date).split()[0])
        
    def getRain(self):
        self._tag = 'span'
        # self._setTag('span')
        self._attr = {'class':'rain'}
        # self._setAttr({'class':'rain'})
        return(sum(self._convertAll(self._getArray(self.__start,self.__end,self.__soup))))
    
    def getSnow(self):
        self._tag = 'span'
        self._attr = {'class':'snow'}
        return(sum(self._convertAll(self._getArray(self.__start,self.__end,self.__soup))))

    def addNumbers(self,listarr):
        result = list(map(self._convertToNum, listarr))
        return ((result[0] + ((result[1] + result[2]) /2)) / 2)
    
    def getWind(self):
        self._tag = 'text'
        self._attr = {'class' :'wind-icon__val'}
        return(self.addNumbers(self._getArray(self.__start,self.__end,self.__soup)))

    
    def getTemp(self):
        self._tag = 'span'
        self._attr = {'class':'temp'}
        maxtemp = self.addNumbers(self._getArray(self.__start,self.__end,self.__soup))
        soup = self.__soup.find('tr',{'class':'forecast__table-min-temperature js-fctable-mintemp'})
        mintemp = self.addNumbers(self._getArray(self.__start,self.__end,soup))
        return((maxtemp + mintemp) / 2)
    
def sliceList(n,l):
    x = len(l) // 3
    if (n == 1):
        return(l[:x])
    elif (n == 2):
        return(l[x:(2 * x)])
    else: 
        return(l[(2 * x):])
        
        
    
def main():   
    mountains =    [ 
                               ('Cocuy','https://www.mountain-forecast.com/peaks/Cocuy-Ritak-Uwa-Blanco/forecasts/5330'),
                                  ('Nevado del Ruiz','https://www.mountain-forecast.com/peaks/Nevado-del-Ruiz/forecasts/5320'),
                                  ('Glacier Peak','https://www.mountain-forecast.com/peaks/Glacier-Peak/forecasts/3213'),
                                  ('Jannu','https://www.mountain-forecast.com/peaks/Jannu/forecasts/7710'),
                                  ('Dhaulagiri','https://www.mountain-forecast.com/peaks/Dhaulagiri/forecasts/8167'),
                                  ('Menlungtse','https://www.mountain-forecast.com/peaks/Menlungtse/forecasts/7181'),
                                  ('Nuptse','https://www.mountain-forecast.com/peaks/Nuptse/forecasts/7861'),
                                  ('makalu','https://www.mountain-forecast.com/peaks/Makalu/forecasts/8462'),
                                  ('Lhotse Shar','https://www.mountain-forecast.com/peaks/Lhotse-Shar/forecasts/8400'),
                                  ('Lhotse','https://www.mountain-forecast.com/peaks/Lhotse/forecasts/8516'),
                                  ('Meru Peak','https://www.mountain-forecast.com/peaks/Meru-Peak/forecasts/6660'),
                                  ('Thalay Sagar','https://www.mountain-forecast.com/peaks/Thalay-Sagar/forecasts/6904'),
                                  ('Changabang','https://www.mountain-forecast.com/peaks/Changabang/forecasts/6864'),
                                  ('Trango Tower','https://www.mountain-forecast.com/peaks/Trango-Towers/forecasts/6286'),
                                  ('Rakaposhi','https://www.mountain-forecast.com/peaks/Rakaposhi/forecasts/7788'),
                                  ('Masherbrum','https://www.mountain-forecast.com/peaks/Masherbrum/forecasts/7821'),
                                  ('Khiangyang Kish','https://www.mountain-forecast.com/peaks/Khiangyang-Kish/forecasts/7852'),
                                  ('Gasherbrum IV','https://www.mountain-forecast.com/peaks/Gasherbrum-IV/forecasts/7925'),
                                  ('Baintha Brakk','https://www.mountain-forecast.com/peaks/Baintha-Brakk/forecasts/7285'),
                                  ('Latok','https://www.mountain-forecast.com/peaks/Latok/forecasts/7145'),
                                  ('Mount Assiniboine','https://www.mountain-forecast.com/peaks/Mount-Assiniboine/forecasts/3618'),
                                  ('Mount Ratz', 'https://www.mountain-forecast.com/peaks/Mount-Ratz/forecasts/3090'),
                                  ('Mount Silverthrone', 'https://www.mountain-forecast.com/peaks/Mount-Silverthrone/forecasts/2865'),
                                  ('Mount Hood', 'https://www.mountain-forecast.com/peaks/Mount-Hood/forecasts/3426'),
                                ('Mount Jefferson', 'https://www.mountain-forecast.com/peaks/Mount-Jefferson/forecasts/3199'),
                                ('South Sister', 'https://www.mountain-forecast.com/peaks/South-Sister-Volcano/forecasts/3157'),
                                ('Sacajawea Peak', 'https://www.mountain-forecast.com/peaks/Sacajawea-Peak/forecasts/2999'),
                                ('Mount Robson', 'https://www.mountain-forecast.com/peaks/Mount-Robson/forecasts/3954'),
                                ('Mount Cleveland','https://www.mountain-forecast.com/peaks/Mount-Cleveland-Montana/forecasts/3190'),
                                ('Granite Peak','https://www.mountain-forecast.com/peaks/Granite-Peak/forecasts/3901'),
                                ('Cloud Peak','https://www.mountain-forecast.com/peaks/Cloud-Peak/forecasts/4013'),
                                ('Gannett Peak','https://www.mountain-forecast.com/peaks/Gannett-Peak/forecasts/4207'),
                                ('Grand Teton','https://www.mountain-forecast.com/peaks/Grand-Teton/forecasts/4197'),
                                  ('Mount Elbert','https://www.mountain-forecast.com/peaks/Mount-Elbert/forecasts/4399'),
                                  ('Kings Peak','https://www.mountain-forecast.com/peaks/Kings-Peak/forecasts/4123'),
                                  ('Borah Peak','https://www.mountain-forecast.com/peaks/Borah-Peak-Mount-Borah/forecasts/3859'),
                                  ('Mount Shasta','https://www.mountain-forecast.com/peaks/Mount-Shasta/forecasts/4317'),
                                  ('Lassen Peak','https://www.mountain-forecast.com/peaks/Lassen-Peak/forecasts/3187'),
                                  ('Thompson Peak','https://www.mountain-forecast.com/peaks/Thompson-Peak/forecasts/2744'),
                                  ('Mount Lyell','https://www.mountain-forecast.com/peaks/Mount-Lyell/forecasts/3998'),
                                  ('Mount Ritter','https://www.mountain-forecast.com/peaks/Mount-Ritter/forecasts/4006'),
                                  ('Mount Goddard','https://www.mountain-forecast.com/peaks/Mount-Goddard/forecasts/4134'),
                                  ('Mount Whitney','https://www.mountain-forecast.com/peaks/Mount-Whitney/forecasts/4418'),
                                  ('Huascarán','https://www.mountain-forecast.com/peaks/Huascaran/forecasts/6768'),
                                    ('Chimborazo','https://www.mountain-forecast.com/peaks/Chimborazo/forecasts/6267'),
                                    ('Aconcagua','https://www.mountain-forecast.com/peaks/Aconcagua/forecasts/6962'),
                                 ('Cerro Torre','https://www.mountain-forecast.com/peaks/Cerro-Torre/forecasts/3133'),
                                  ('Mount Everest','https://www.mountain-forecast.com/peaks/Mount-Everest/forecasts/8850'),
                                  ('Mont Blanc','https://www.mountain-forecast.com/peaks/Mont-Blanc/forecasts/4807'),
                                  ('Mount Elbrus','https://www.mountain-forecast.com/peaks/Mount-Elbrus/forecasts/5642'),
                                  ('Jengish Chokusu','https://www.mountain-forecast.com/peaks/Jengish-Chokusu/forecasts/7439'),
                                  ('Ismoil Somoni Peak','https://www.mountain-forecast.com/peaks/Ismoil-Somoni-Peak/forecasts/7495'),
                                ('Hvannadalshnúkur','https://www.mountain-forecast.com/peaks/Hvannadalshnukur/forecasts/2119'),
                                  ('Reclus','https://www.mountain-forecast.com/peaks/Reclus-volcano/forecasts/1000'),
                                  ('Iconoclast Mountain','https://www.mountain-forecast.com/peaks/Iconoclast-Mountain/forecasts/3251'),
                                  ('Mount Washington','https://www.mountain-forecast.com/peaks/Mount-Washington-2/forecasts/1917'),
                                  ('Namcha Barwa','https://www.mountain-forecast.com/peaks/Namcha-Barwa/forecasts/7782'),
                                  ('Nanga Parbat','https://www.mountain-forecast.com/peaks/Nanga-Parbat/forecasts/8125'), 
                                  ('Mount Crillon', 'https://www.mountain-forecast.com/peaks/Mount-Crillon/forecasts/3879'),
                                  ('Mount Fairweather', 'https://www.mountain-forecast.com/peaks/Mount-Fairweather/forecasts/4663'),
                                ('Mount Saint Elias', 'https://www.mountain-forecast.com/peaks/Mount-Saint-Elias/forecasts/5489'),
                                ('Mount Logan', 'https://www.mountain-forecast.com/peaks/Mount-Logan/forecasts/5959'),
                                ('Denali', 'https://www.mountain-forecast.com/peaks/Mount-McKinley/forecasts/6194'),
                                ('Mount Marcus Baker', 'https://www.mountain-forecast.com/peaks/Mount-Marcus-Baker/forecasts/4016'),
                                ('Mount Waddington', 'https://www.mountain-forecast.com/peaks/Mount-Waddington/forecasts/4016'),
                              ('Mount Baker', 'https://www.mountain-forecast.com/peaks/Mount-Baker/forecasts/3285'),
                              ('Mount Rainier', 'https://www.mountain-forecast.com/peaks/Mount-Rainier/forecasts/4392'),
                                ('Mount Olympus', 'https://www.mountain-forecast.com/peaks/Mount-Olympus-2/forecasts/2427'),
                                ('Saddle Mountain', 'https://www.mountain-forecast.com/peaks/Saddle-Mountain-Clatsop-County-Oregon/forecasts/1002'),
                                ('Marys Peak','https://www.mountain-forecast.com/peaks/Marys-Peak/forecasts/1249'),
                                ('Pico Cristóbal Colón','https://www.mountain-forecast.com/peaks/Pico-Cristobal-Colon/forecasts/5775'),
                              ('Farallones de Cali','https://www.mountain-forecast.com/peaks/Farallones-de-Cali/forecasts/4050'),
                              ('Nevado del Huila','https://www.mountain-forecast.com/peaks/Nevado-del-Huila/forecasts/5365'),
                              ('Lautaro','https://www.mountain-forecast.com/peaks/Lautaro/forecasts/3380'),
                                ('Aguilera','https://www.mountain-forecast.com/peaks/Aguilera-volcano/forecasts/2546'),
                              ('Cerro Arenales','https://www.mountain-forecast.com/peaks/Cerro-Arenales/forecasts/3437'),
                              ('Monte San Valentín','https://www.mountain-forecast.com/peaks/Monte-San-Valentin/forecasts/4058'),
                              ('Mount Cook','https://www.mountain-forecast.com/peaks/Aoraki-Mount-Cook/forecasts/3754'),
                              ('Mount Tutoko','https://www.mountain-forecast.com/peaks/Mount-Tutoko/forecasts/2723'),
                              ('Mawson Peak','https://www.mountain-forecast.com/peaks/Mawson-Peak/forecasts/2745'),
                              ('Mount Paget','https://www.mountain-forecast.com/peaks/Mount-Paget/forecasts/2935'),
                              ('K2','https://www.mountain-forecast.com/peaks/K2/forecasts/8612'),
                              ('Kangto','https://www.mountain-forecast.com/peaks/Kangto/forecasts/7060'),
                              ('Nanda Devi','https://www.mountain-forecast.com/peaks/Nanda-Devi/forecasts/7817'),
                              ('Kangchenjunga','https://www.mountain-forecast.com/peaks/Kangchenjunga/forecasts/8586'),
                              ('Manaslu','https://www.mountain-forecast.com/peaks/Manaslu/forecasts/8156'),
                              ('Annapurna','https://www.mountain-forecast.com/peaks/Annapurna/forecasts/8091'),
                            ('Gunnbjørn Fjeld','https://www.mountain-forecast.com/peaks/Gunnbjorn-Fjeld/forecasts/3694'),
                            ('Ridge A','https://www.mountain-forecast.com/peaks/Ridge-A/forecasts/4053'),
                           ('Dome A','https://www.mountain-forecast.com/peaks/Dome-A/forecasts/4091'),
                            ('Vinson Massif','https://www.mountain-forecast.com/peaks/Vinson-Massif/forecasts/4897'),
                            ('Puncak Jaya','https://www.mountain-forecast.com/peaks/Puncak-Jaya/forecasts/4884'),
                        ('Golden Hinde','https://www.mountain-forecast.com/peaks/Golden-Hinde/forecasts/2195')
                   ]
    
    # mountains = sliceList(1,mountains)
    # mountains = sliceList(2,mountains)
    # mountains = sliceList(3,mountains)
    
    sqlliteDB = Database.Database('sqllite')
    # mysqlDB = Database.Database('mysql')
    BuildSql = []
    

    for mountain in mountains:
        try:
            print(mountain[0])
            mf = MountForcast(mountain[1],'span',{'class': 'forecast__table-value'})
            date = mf.getDate()
            print(date)
            sqlliteDB.deleteRecord('MountainForcast',mountain[0],date) 
            
            # mysqlDB.deleteRecord('mountainforcast',mountain[0],date)  Commented out because currently not working          
            item = []
            item.append(mountain[0])   
            item.append(date) 
            item.append(mf.getRain())
            item.append(mf.getSnow()) 
            item.append(mf.getWind()) 
            item.append(mf.getTemp())
            BuildSql.append(item)
            time.sleep(20 + random.randrange(20))
                   
        except Exception as e:
            print(e)
            print("Something Went wrong for ",mountain[0])
            continue
            
        
    sqlliteDB.insertRecords('INSERT INTO MountainForcast(MOUNTAIN_NAME,DATE,RAIN,SNOW,WIND,TEMP) values (?,?,?,?,?,?)', BuildSql)
    sqlliteDB.close()
    print("after sqllite")
     #   mysqlDB.insertRecords('INSERT INTO mountainforcast(MOUNTAIN_NAME,DATE,RAIN,SNOW,WIND,TEMP) values (%s,%s,%s,%s,%s,%s)', BuildSql) 
     # mysqlDB.close()
    
      
main()
    

    



    

    


