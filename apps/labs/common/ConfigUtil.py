'''
Created on 2018年9月15日

@author: jrq
'''

#import sys
#sys.path.append('/home/pi/workspace/iot-device/apps')

import configparser

config = configparser.ConfigParser()

class ConfigUtil():  
    def __init__(self,fileAddr):  
        #Get the address
        self.fileAddr=fileAddr  
        print ('========== Environment Setting ==========')
        print ('Already get the fileAddr:' + str(fileAddr))
        
        
    def loadConfig(self):  
        #load the file by the address above
        self.config = config.read(self.fileAddr)
        print ('Already get the config:' + str(self.config))

    def getProperty(self,section,key):  
        self.section = section
        #Get the key
        self.key = key
        return self.key  
    
    
    
    
    