'''
Created on 2018年9月15日

@author: xingli
'''
import os,sys
sys.path.append('/home/pi/Desktop/xing/iot-device/apps')
from time           import sleep
from labs.module03 import TempSensorAdaptor
from labs.module03 import mqttSimpleClient
sysPerfAdaptor = TempSensorAdaptor.TempSensorAdaptor()

print("Starting system performance app daemon thread...")
sysPerfAdaptor.setEnableAdaptorFlag(True)#set enableAdaptor to true
sysPerfAdaptor.start()#start the run function in TempSensorAdaptor

#keep running
while (True):
    sleep(5)
    pass