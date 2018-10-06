'''
Created on 2018年9月15日

@author: jrq
'''
import configparser


config = configparser.ConfigParser()


class ConfigUtil():  
    def __init__(self,fileAddr):  
        #Get the address of the file
        self.fileAddr=fileAddr  
        print ('========== Environment Setting ==========')
        print ('Already get the fileAddr:' + str(fileAddr))
        #self.config={}  
        
    def loadConfig(self):  
        #Read the content of the file
        self.config = config.read(self.fileAddr)
        print ('Already get the config:' + str(self.config))

    def getProperty(self,section,key):  
        self.section = section
        #Get the key and return
        self.key = key
        return self.key  
    
    
    
    
    