'''
Created on 2018年9月15日

@author: jrq
'''

#import sys
#sys.path.append('/home/pi/workspace/iot-device/apps')

from time import sleep
from labs.semesterProject import TempSensorAdaptor

tempSensAdaptor = TempSensorAdaptor.TempSensorAdaptor()
tempSensAdaptor.daemon  = True

print('- - - - - - - - - - - - - - - - - - - - - - - - ')
print("Starting system performance app daemon thread...")

tempSensAdaptor.enableEmulator = True
tempSensAdaptor.start()

while (True):
    sleep(15)
    pass