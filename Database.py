# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:48:46 2021

@author: backp
"""

import sqlite3
import mysql.connector

class Database:
    def __init__(self,typeOfDatabase = "sqllite"): 
        if (typeOfDatabase == "sqllite"):
            print("sqlite")
            self.__conn = sqlite3.connect('MountainWeather.db')
            self.__c = self.__conn.cursor()
        if (typeOfDatabase == "mysql"):
            try:
                print("mysql")
                              
                self.__conn = mysql.connector.connect(
                  host="localhost",
                  # user="root",
                  user='User2',
                  password="whatever you want as your pass word",
                  database="MountainWeather"
                )  
                self.__c = self.__conn.cursor()
                # with connect(
                #     host = "localhost",
                #     user = "root",
                #     password = ""whatever you want as your pass word",
                #     database = 'MountainWeather',
                #     # user=input("Enter username: "),
                #     # password=getpass("Enter password: ")
                # ) as self.__conn:
                #     self.__c = self.__conn.cursor()
                
            except Error as e:
                print("failed",e)
                
    def deleteAll(self,table):
        """
            
        Input
          Table which is a string and name of the table to delete
      
        Returns nothing(void)  
    
        """  
        
        conn = self.__conn
        c = self.__c       
        c.execute("delete from " + table)
        conn.commit()
                
    def deleteRecord(self,table,MN,Date):
        """
            
        Input
          Table which is a string and name of the table
          MN is a string which is the name of the moutain
          Date is a date in string form
          
          All the 3 arguments are used to make the where clause to
          delete the specific record.
      
        Returns nothing(void)  
    
        """  
        
        conn = self.__conn
        c = self.__c     
        
        sql = "delete from " + table + " WHERE MOUNTAIN_NAME=" + "'" + MN + "'" + " and DATE=" + "'" + Date + "'"
        c.execute(sql)
        conn.commit()
    
    def insertRecords(self,sql1,sql2):
        """
            
        Input
          sql1 which is a string representing part of an SQL statement that will be
          executed
         
          sql2 which is a string representing the other part of an SQL statement that 
          will be executed
      
        Returns nothing(void)  
    
        """  
        
        conn = self.__conn
        c = self.__c
        c.executemany(sql1,sql2)
        conn.commit()
    
    
    def returnRecords(self,sql):
        """
            
        Input
          sql which is a string representing Select SQL statement that will be
          executed
      
        Returns an array(list) formed from the executed SQL statements resulting
        in records that are then transformed inot an array(list)
    
        """ 
        
        c = self.__c  
        c.execute(sql)
        rows = c.fetchall()  
        arr = []
        for row in rows:
            item = []
            item.append(row[0])
            item.append(row[1])
            arr.append(item)
        return(arr)
    
    def returnDictionary(self,sql):
        """
            
        Input
          sql which is a string representing Select SQL statement that will be
          executed
      
        Returns an dictionary formed from the executed SQL statements resulting
        in records that are then transformed inot a dictionary
    
        """ 
        
        c = self.__c  
        c.execute(sql)
        rows = c.fetchall()  
        arr = {}
        for row in rows:
            arr[row[0]] = row[1]
        return(arr)
    
    def selectRecords(self,sql):
        """
            
        Input
          sql which is a string representing Select SQL statement that will be
          executed
      
        Returns void(nothing)
    
        """ 
        
        c = self.__c  
        c.execute(sql)
        rows = c.fetchall()  
        for row in rows:
            print(row)
        
    def close(self):
        conn = self.__conn
        conn.close()


    
    


