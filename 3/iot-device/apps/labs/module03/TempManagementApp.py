'''
Created on 2018年9月15日

@author: jrq
'''



from time import sleep
from labs.module03 import TempSensorAdaptor

tempSensAdaptor = TempSensorAdaptor.TempSensorAdaptor()
tempSensAdaptor.daemon  = True

print('- - - - - - - - - - - - - - - - - - - - - - - - ')
print("Starting system performance app daemon thread...")

tempSensAdaptor.enableEmulator = True

tempSensAdaptor.start()

while (True):
    sleep(10)
    pass