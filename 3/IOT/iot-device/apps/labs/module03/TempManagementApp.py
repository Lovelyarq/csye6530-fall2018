'''
Created on 2018年9月15日

@author: jrq
'''



from time import sleep
from labs.module03 import TempSensorAdaptor
#from labs.module03 import TempSensorEmulator
#from labs.module02 import SmtpClientConnector


tempSensAdaptor = TempSensorAdaptor.TempSensorAdaptor()
#tempSensEmulator = TempSensorEmulator.TempSensorEmulator()

tempSensAdaptor.daemon  = True
#tempSensEmulator.daemon = True

print('- - - - - - - - - - - - - - - - - - - - - - - - ')
print("Starting system performance app daemon thread...")

tempSensAdaptor.enableEmulator = True
#tempSensEmulator.enableEmulator   = True

#tempSensEmulator.start()
tempSensAdaptor.start()



while (True):
    sleep(10)
    pass