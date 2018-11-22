'''
Created on 2018年9月13日

@author: jrq
'''

import sys
sys.path.append('/home/pi/workspace/iot-device/apps')

from time import sleep
from labs.module04 import I2CSenseHatAdaptor
I2CAdap = I2CSenseHatAdaptor.I2CSenseHatAdaptor()
I2CAdap.daemon  = True

print('- - - - - - - - - - - - - - - - - - - - - - - - ')
print("Starting system performance app daemon thread...")

I2CAdap.enableEmulator = True
I2CAdap.start()

while (True):
    sleep(15)
    pass



