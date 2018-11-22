'''
Created on 2018年10月11s日

@author: jrq
'''
import sys
sys.path.append('/home/pi/workspace/iot-device/apps')

import smbus
import threading
from sense_hat import SenseHat

sense = SenseHat()

from time import sleep

from labs.common import ConfigUtil
#from labs.common import ConfigConst

i2cBus = smbus.SMBus(1) # Use I2C bus No.1 on Raspberry Pi3 +

enableControl = 0x2D
enableMeasure = 0x08

accelAddr = 0x1C # address for IMU (accelerometer)
magAddr   = 0x6A # address for IMU (magnetometer)
pressAddr = 0x5C # address for pressure sensor
humidAddr = 0x5F # address for humidity sensor

begAddr = 0x28
totBytes = 6

DEFAULT_RATE_IN_SEC = 5

class I2CSenseHatAdaptor(threading.Thread):
    data1 = 0
    data2 = 0
    data3 = 0
    data4 = 0
    rateInSec = DEFAULT_RATE_IN_SEC
    def __init__(self):
        super(I2CSenseHatAdaptor, self).__init__()
        self.config = ConfigUtil.ConfigUtil('../../../data/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))
        self.initI2CBus()
    def initI2CBus(self):
        print("Initializing I2C bus and enabling I2C addresses...")
        i2cBus.write_byte_data(accelAddr, enableControl, enableMeasure)
        i2cBus.write_byte_data(magAddr, enableControl, enableMeasure)
        i2cBus.write_byte_data(pressAddr, enableControl, enableMeasure)
        i2cBus.write_byte_data(humidAddr, enableControl, enableMeasure)
        # TODO: do the same for the magAddr, pressAddr, and humidAddr
        # NOTE: Reading data from the sensor will look like the following:
        self.data1 = i2cBus.read_i2c_block_data(accelAddr, begAddr, totBytes)
        self.data2 = i2cBus.read_i2c_block_data(magAddr, begAddr, totBytes)
        self.data3 = i2cBus.read_i2c_block_data(pressAddr, begAddr, totBytes)
        self.data4 = i2cBus.read_i2c_block_data(humidAddr, begAddr, totBytes)
        
    def displayAccelerometerData(self,Data):
        self.Data = Data
        print('AccelerometerData =' + str(self.Data))
    def displayMagnetometerData(self,Data):
        self.Data = Data
        print('MagnetometerData  =' + str(self.Data))
    def displayPressureData(self,Data):
        self.Data = Data
        print('PressureData      =' + str(self.Data))
    def displayHumidityData(self,Data):
        self.Data = Data
        print('HumidityData      =' + str(self.Data))    
        
        
    def run(self):
        while True:
            if self.enableEmulator:
                #self.initI2CBus()
                # NOTE: you must implement these methods
                self.displayAccelerometerData(self.data1)
                self.displayMagnetometerData(self.data2)
                self.displayPressureData(self.data3)
                self.displayHumidityData(self.data4)
                #a = sense.get_humidity()
                #print('mmm:' + str(a))
            sleep(self.rateInSec)
        
    
            
