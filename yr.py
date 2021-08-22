# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:06:27 2020

@author: by D Lund.
"""

import weatherModel 
import re 
import urllib
import time
import random
import Database

class yr(weatherModel.weatherModel):
    def __init__(self,file_url):
        super().__init__(file_url, '', '')
            
    def getTemp(self):
        """
        
        Input
          none
          
        Returns
          The average temp for the first full 24 hour day forcast
          /www.yr.no/ gives 24 temperature readings for every hour.
          It returns the average of those 24 readings
        
        """    
    
        self._tag = 'span'
        self._attr = {'class':re.compile('^temperature temperature--')}
        Array = self._getArray(0,40,self._soup,"temp")
        return(self._avg(Array[-24:]))
    
    def getPrecipitation(self):
        """
        Input
          none
          
        Returns
          The average precipitation for the first full 24 hour day forcast
          /www.yr.no/ gives 24 precipitation readings for every hour.
          It returns the average of those 24 readings    
        """    
        self._tag = 'span'
        self._attr = {'class':'precipitation__value'}
        Array = self._getArray(0,40,self._soup)
        return(sum(self._convertAll(Array[-24:])))
        
    def getWind(self): 
        """
        Input
          none
          
        Returns
          The average wind speed for the first full 24 hour day forcast
          /www.yr.no/ gives 24 wind speed readings for every hour.
          It returns the average of those 24 readings    
        """    
        self._tag = 'span'
        self._attr = {'class':'wind__value'} 
        Array = (self._getArray(0,40,self._soup))
        return(self._avg(Array[-24:]))
    
    def getDate(self):
        """
        Input
          none
          
        Returns the date of forecast   
        """    
        data = urllib.request.urlopen(self._file_url)         
        for line in data: 
            search_string = 'time dateTime="' + '(20\d\d-\d\d-\d\d)' + '"'
            match = re.search(search_string, str(line))
            if match:
                return(match.group(1))
        return('2021-00-00')

def main():

    mountains = [   
                ('Mount Assiniboine','https://www.yr.no/en/forecast/hourly-table/2-6079780/Canada/British%20Columbia/Mount%20Assiniboine%20Park?i=1'),
                ('Marys Peak','https://www.yr.no/en/forecast/daily-table/2-5739271/United%20States/Oregon/Benton/Marys%20Peak'),
                ('Mount Ratz', 'https://www.yr.no/en/forecast/hourly-table/2-6082428/Canada/British%20Columbia/Mount%20Ratz?i=1'),
                ('Mount Silverthrone', 'https://www.yr.no/en/forecast/hourly-table/2-6147919/Canada/British%20Columbia/Central%20Coast%20Regional%20District/Silverthrone%20Mountain?i=1'),
                ('Mount Hood', 'https://www.yr.no/en/forecast/hourly-table/2-5731780/United%20States/Oregon/Hood%20River/Mount%20Hood?i=1'),
                ('Mount Jefferson', 'https://www.yr.no/en/forecast/hourly-table/2-5733559/United%20States/Oregon/Linn/Mount%20Jefferson?i=1'),
                ('South Sister', 'https://www.yr.no/en/forecast/hourly-table/2-5753541/United%20States/Oregon/Lane/South%20Sister?i=1'),
                ('Sacajawea Peak', 'https://www.yr.no/en/forecast/hourly-table/2-5749835/United%20States/Oregon/Wallowa/Sacajawea%20Peak?i=1'),
                ('Mount Robson', 'https://www.yr.no/en/forecast/hourly-table/2-6082495/Canada/British%20Columbia/Mount%20Robson?i=1'),
                ('Mount Cleveland','https://www.yr.no/en/forecast/hourly-table/2-5645401/United%20States/Montana/Glacier/Mount%20Cleveland?i=1'),
                ('Cloud Peak','https://www.yr.no/en/forecast/hourly-table/2-5821469/United%20States/Wyoming/Big%20Horn%20County/Cloud%20Peak?i=1'),
                ('Gannett Peak','https://www.yr.no/en/forecast/hourly-table/2-5825786/United%20States/Wyoming/Fremont/Gannett%20Peak?i=1'),
                ('Grand Teton','https://www.yr.no/en/forecast/hourly-table/2-5826325/United%20States/Wyoming/Teton/Grand%20Teton?i=1'),
                ('Mount Elbert','https://www.yr.no/en/forecast/hourly-table/2-5420942/United%20States/Colorado/Lake/Mount%20Elbert?i=1'),
                ('Kings Peak','https://www.yr.no/en/forecast/hourly-table/2-5776833/United%20States/Utah/Duchesne/Kings%20Peak?i=1'),
                ('Borah Peak','https://www.yr.no/en/forecast/hourly-table/2-5586537/United%20States/Idaho/Custer/Borah%20Peak?i=1'),
                ('Mount Shasta','https://www.yr.no/en/forecast/hourly-table/2-5571124/United%20States/California/Siskiyou/Mount%20Shasta?i=1'),
                ('Thompson Peak','https://www.yr.no/en/forecast/hourly-table/2-5572674/United%20States/California/Trinity/Thompson%20Peak?i=1'),
                ('Mount Lyell','https://www.yr.no/en/forecast/hourly-table/2-5369346/United%20States/California/Madera/Mount%20Lyell?i=1'),
                ('Mount Ritter','https://www.yr.no/en/forecast/hourly-table/2-5387778/United%20States/California/Madera/Mount%20Ritter?i=1'),
                ('Mount Goddard','https://www.yr.no/en/forecast/hourly-table/2-5352629/United%20States/California/Fresno/Mount%20Goddard?i=1'),
                ('Mount Whitney','https://www.yr.no/en/forecast/hourly-table/2-5409018/United%20States/California/Tulare/Mount%20Whitney?i=1'),
                ('Huascarán','https://www.yr.no/en/forecast/hourly-table/2-3696347/Peru/Ancash/Provincia%20de%20Yungay/Huascar%C3%A1n?i=1'),
                ('Chimborazo','https://www.yr.no/en/forecast/hourly-table/2-3659238/Ecuador/Chimborazo/Chimborazo?i=1'),
                ('Aconcagua','https://www.yr.no/en/forecast/hourly-table/2-3866949/Argentina/Mendoza/Departamento%20de%20Las%20Heras/Aconcagua?i=1'),
                ('Cerro Torre','https://www.yr.no/en/forecast/hourly-table/2-3834109/Argentina/Santa%20Cruz/Departamento%20de%20Lago%20Argentino/Cerro%20Torre?i=1'),
                ('Nanda Devi','https://www.yr.no/en/forecast/hourly-table/2-1261991/India/Uttarakhand/Chamoli/Nanda%20Devi?i=1'),
                ('Namcha Barwa','https://www.yr.no/en/forecast/hourly-table/2-1280498/China/Tibet/Namcha%20Barwa?i=1'),
                ('Mount Everest','https://www.yr.no/en/forecast/hourly-table/2-1283416/Nepal/Mount%20Everest?i=1'),
                ('Mont Blanc','https://www.yr.no/en/forecast/hourly-table/2-3181986/France/Auvergne-Rh%C3%B4ne-Alpes/Upper%20Savoy/Mont%20Blanc?i=1'),
                ('Mount Elbrus','https://www.yr.no/en/forecast/hourly-table/2-563532/Russia/Kabardino-Balkariya%20Republic/Mount%20Elbrus?i=1'),
                ('Jengish Chokusu','https://www.yr.no/en/forecast/hourly-table/2-1494813/Kyrgyzstan/Sheng-li%20Feng?i=1'),
                ('Ismoil Somoni Peak','https://www.yr.no/en/forecast/hourly-table/2-1221252/Tajikistan/Ismail%20Samani%20Peak?i=1'),
                ('Hvannadalshnúkur','https://www.yr.no/en/forecast/hourly-table/2-2629761/Iceland/East/Sveitarf%C3%A9lagi%C3%B0%20Hornafj%C3%B6r%C3%B0ur/Hvannadalshn%C3%BAkur?i=1'),
                ('Iconoclast Mountain','https://www.yr.no/en/forecast/hourly-table/2-5979265/Canada/British%20Columbia/Iconoclast%20Mountain?i=1'),
                ('Mount Washington','https://www.yr.no/en/forecast/hourly-table/2-5094284/United%20States/New%20Hampshire/Coos/Mount%20Washington?i=1'),
                ('Nevado del Ruiz','https://www.yr.no/en/forecast/hourly-table/2-9255318/Colombia/Tolima/Nevado%20Del%20Ruiz%20Volcano?i=1'),
                ('Glacier Peak','https://www.yr.no/en/forecast/hourly-table/2-5795513/United%20States/Washington/Snohomish/Glacier%20Peak?i=1'),
                ('Jannu','https://www.yr.no/en/forecast/hourly-table/2-1283175/Nepal/Province%201/Taplejung/Jannu?i=1'),
                ('Dhaulagiri','https://www.yr.no/en/forecast/hourly-table/2-1283457/Nepal/Gandaki%20Pradesh/Myagdi/Dhaulagiri?i=1'),
                ('Nuptse','https://www.yr.no/en/forecast/hourly-table/2-7302334/Nepal/Province%201/Solukhumbu/Nuptse?i=1'),
                ('makalu','https://www.yr.no/en/forecast/hourly-table/2-1283087/Nepal/Province%201/Sankhuwasabha/Makalu?i=1'),
                ('Lhotse Shar','https://www.yr.no/en/forecast/hourly-table/2-1283127/Nepal/Province%201/Solukhumbu/Lo-tzu-sha%20Feng?i=1'),
                ('Lhotse','https://www.yr.no/en/forecast/hourly-table/2-1283128/Nepal/Province%201/Solukhumbu/Lhotse?i=1'),
                ('Changabang','https://www.yr.no/en/forecast/hourly-table/2-1274665/India/Uttarakhand/Chamoli/Changabang?i=1'),
                ('Rakaposhi','https://www.yr.no/en/forecast/hourly-table/2-1167314/Pakistan/Gilgit-Baltistan/Rakaposhi%20Group?i=1'),
                ('Masherbrum','https://www.yr.no/en/forecast/hourly-table/2-1170749/Pakistan/Gilgit-Baltistan/Sk%C4%81rdu%20District/Masherbrum%20East?i=1'),
                ('Khiangyang Kish','https://www.yr.no/en/forecast/hourly-table/2-1173892/Pakistan/Gilgit-Baltistan/Hunza-Nagar%20District/Khinyang%20Chhish?i=1'),
                ('Baintha Brakk','https://www.yr.no/en/forecast/hourly-table/2-1183799/Pakistan/Gilgit-Baltistan/Sk%C4%81rdu%20District/Baintha%20Brakk?i=1'),
                ('Latok','https://www.yr.no/en/forecast/hourly-table/2-1172065/Pakistan/Gilgit-Baltistan/Latok%20Group?i=1'),
                ('Nanga Parbat','https://www.yr.no/en/forecast/hourly-table/2-1169384/Pakistan/Gilgit-Baltistan/Astor/Nanga%20Parbat?i=1'),
                ('Mount Crillon', 'https://www.yr.no/en/forecast/hourly-table/2-5846285/United%20States/Alaska/Hoonah-Angoon%20Census%20Area/Mount%20Crillon?i=1'),
                ('Mount Bertha', 'https://www.yr.no/en/forecast/hourly-table/2-5844698/United%20States/Alaska/Hoonah-Angoon%20Census%20Area/Mount%20Bertha?i=1'),
                ('Mount Fairweather', 'https://www.yr.no/en/forecast/hourly-table/2-5844913/United%20States/Alaska/Yakutat%20City%20and%20Borough/Mount%20Fairweather?i=1'),
                ('Mount Saint Elias', 'https://www.yr.no/en/forecast/hourly-table/2-5857957/United%20States/Alaska/Yakutat%20City%20and%20Borough/Mount%20Saint%20Elias?i=1'),
                ('Mount Logan', 'https://www.yr.no/en/forecast/hourly-table/2-6081596/Canada/Yukon/Mount%20Logan?i=1'),
                ('Denali', 'https://www.yr.no/en/forecast/hourly-table/2-5868589/United%20States/Alaska/Denali/Denali?i=1'),
                ('Mount Marcus Baker', 'https://www.yr.no/en/forecast/hourly-table/2-5868267/United%20States/Alaska/Valdez-Cordova/Mount%20Marcus%20Baker?i=1'),
                ('Mount Waddington', 'https://www.yr.no/en/forecast/hourly-table/2-6083114/Canada/British%20Columbia/Mount%20Waddington?i=1'),
                ('Mount Baker', 'https://www.yr.no/en/forecast/hourly-table/2-5786191/United%20States/Washington/Whatcom/Mount%20Baker?i=1'),
                ('Mount Rainier', 'https://www.yr.no/en/forecast/hourly-table/2-5807840/United%20States/Washington/Pierce/Mount%20Rainier?i=1'),
                ('Mount Olympus', 'https://www.yr.no/en/forecast/hourly-table/2-5805733/United%20States/Washington/Jefferson/Mount%20Olympus?i=1'),
                ('Saddle Mountain', 'https://www.yr.no/en/forecast/hourly-table/2-5749930/United%20States/Oregon/Clatsop/Saddle%20Mountain?i=1'),
                ('Pico Cristóbal Colón','https://www.yr.no/en/forecast/hourly-table/2-3685669/Colombia/La%20Guajira/Pico%20Crist%C3%B3bal%20Col%C3%B3n?i=1'),
                ('Farallones de Cali','https://www.yr.no/en/forecast/hourly-table/2-3687924/Colombia/Valle%20del%20Cauca/Farallones%20de%20Cali?i=1'),
                ('Lautaro','https://www.yr.no/en/forecast/hourly-table/2-11405732/Chile/Region%20of%20Magallanes/Volc%C3%A1n%20Lautaro?i=1'),
                ('Cerro Arenales','https://www.yr.no/en/forecast/hourly-table/2-3899397/Chile/Ays%C3%A9n/Provincia%20Capit%C3%A1n%20Prat/Cerro%20Arenales?i=1'),
                ('Monte San Valentín','https://www.yr.no/en/forecast/hourly-table/2-3871296/Chile/Ays%C3%A9n/Provincia%20de%20Ais%C3%A9n/Cerro%20San%20Valent%C3%ADn?i=1'),
                ('Cerro Francisco Pascasio Moreno','https://www.yr.no/en/forecast/hourly-table/2-7534285/Chile/Region%20of%20Magallanes/Provincia%20de%20%C3%9Altima%20Esperanza/Cerro%20Francisco%20Pascasio%20Moreno?i=1'),
                ('Mount Cook','https://www.yr.no/en/forecast/hourly-table/2-2192136/New%20Zealand/Canterbury/Mackenzie%20District/Aoraki/Mount%20Cook?i=1'),
                ('Mount Tutoko','https://www.yr.no/en/forecast/hourly-table/2-6202126/New%20Zealand/Southland/Southland%20District/Mount%20Tutoko?i=1'),
                ('Mawson Peak','https://www.yr.no/en/forecast/hourly-table/2-1547302/Heard%20Island%20and%20McDonald%20Islands/Mawson%20Peak?i=1'),
                ('Mount Paget','https://www.yr.no/en/forecast/hourly-table/2-3426349/South%20Georgia%20and%20South%20Sandwich%20Islands/Mount%20Paget?i=1'),
                ('K2','https://www.yr.no/en/forecast/hourly-table/2-1114951/Pakistan/Gilgit-Baltistan/Sk%C4%81rdu%20District/K2?i=1'),
                ('Kangto','https://www.yr.no/en/forecast/hourly-table/2-1268079/India/Kanggardo%20Riz%C3%AA?i=1'),
                ('Nanda Devi','https://www.yr.no/en/forecast/hourly-table/2-1261991/India/Uttarakhand/Chamoli/Nanda%20Devi?i=1'),
                ('Kangchenjunga','https://www.yr.no/en/forecast/hourly-table/2-1283259/Nepal/Province%201/Taplejung/Kanchenjunga?i=1'),
                ('Manaslu','https://www.yr.no/en/forecast/hourly-table/2-1283075/Nepal/Gandaki%20Pradesh/Manag/Manaslu?i=1'),
                ('Annapurna','https://www.yr.no/en/forecast/hourly-table/2-1283731/Nepal/Gandaki%20Pradesh/Kaski/Annapurna?i=1'),
                ('Gunnbjørn Fjeld','https://www.yr.no/en/forecast/hourly-table/2-3423611/Greenland/Sermersooq/Gunnbj%C3%B8rn%20Fjeld?i=1'),
                ('Vinson Massif','https://www.yr.no/en/forecast/hourly-table/2-6627584/Antarctica/Vinson%20Massif?i=1'),
                ('Puncak Jaya','https://www.yr.no/en/forecast/hourly-table/2-1642658/Indonesia/Papua/Puncak%20Jaya?i=1'),
                ('Golden Hinde','https://www.yr.no/en/forecast/hourly-table/2-5962619/Canada/British%20Columbia/Golden%20Hinde?i=1')
            ] 
    
    sqlliteDB = Database.Database('sqllite')
    # mysqlDB = Database.Database('mysql')
    BuildSql = []
    
    try:
        for mountain in mountains:
             print(mountain[0])
             norway = yr(mountain[1])
             item = []
             norway.setSoap()

             date = norway.getDate()
             print(date)
             # date = year + "-" + str(weatherModel.month_convert[month]) + "-" + day
             sqlliteDB.deleteRecord('YR',mountain[0],date) 
             # mysqlDB.deleteRecord('YR',mountain[0],date)  
      
             item.append(mountain[0])
             item.append(norway.getTemp())
             item.append(norway.getPrecipitation())
             item.append(norway.getWind())    
             item.append(date)
             BuildSql.append(item)
             
           # Why am I doing the following? If I don't wait for some period
            # before the next request for the next url from MountainForecast.com
            # and make the waiting period random, their system is likely to be 
            # triggered and in fact that is what happened when I didn't do the following
             time.sleep(20 + random.randrange(20))
             
    except Exception as e:
        print(e)
        print("Something Went wrong")
         
    # except:
    #     print("Exception raised")
        
    sqlliteDB.insertRecords('INSERT INTO YR(MOUNTAIN_NAME,TEMP,PRECIPITATION,WIND,DATE) values (?,?,?,?,?)', BuildSql)
    sqlliteDB.close()
    print("after sqllite")
    # mysqlDB.insertRecords('INSERT INTO YR(MOUNTAIN_NAME,TEMP,PRECIPITATION,WIND,DATE) values (%s,%s,%s,%s,%s)', BuildSql) 
    # mysqlDB.close()
         
    # Database.insertRecords('INSERT INTO YR(MOUNTAIN_NAME,TEMP,PRECIPITATION,WIND,DATE) values (?,?,?,?,?)', BuildSql) 
    # Database.conn.close()
    
    print("Inserted into Database")
         
    # print(BuildSql)
         
    # conn = sqlite3.connect('MountainWeather.db')
    # c = conn.cursor()
    
    # c.executemany('INSERT INTO YR(MOUNTAIN_NAME,TEMP,PRECIPITATION,WIND,DATE) values (?,?,?,?,?)', BuildSql)
    # conn.commit()
    
main()
     
   