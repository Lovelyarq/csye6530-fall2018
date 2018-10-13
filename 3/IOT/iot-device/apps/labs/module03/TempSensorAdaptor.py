'''
Created on 2018年9月22日

@author: jrq
'''

import random
from time import sleep
import threading
from labs.common import SensorData
from labs.common import ActuatorData
from labs.common import ConfigUtil
from labs.common import ConfigConst
from labs.module03 import SmtpClientConnector 
#from labs.module03 import TempSensorEmulator
from labs.module03 import TempActuatorEmulator



DEFAULT_RATE_IN_SEC = 10


TempAcEmu = TempActuatorEmulator.TempActuatorEmulator()
config = ConfigUtil.ConfigUtil
Sens = SensorData.SensorData()
ActD = ActuatorData.ActuatorData()
SmtpConnector = SmtpClientConnector.SmtpClientConnector()
#tempEmu = TempSensorEmulator.TempSensorEmulator()


class TempSensorAdaptor (threading.Thread):
    enableEmulator = False
    isPrevTempSet  = False
    rateInSec      = DEFAULT_RATE_IN_SEC
    Sens.setName('Temperature')
    
    lowVal = 0
    highVal = 30
    alertDiff = 2
    
    
    Data = ActD
    Data.setCommand(0)
    Data.setValue(0)
    Data.setErrorCode(0)
    Data.setStateData(0)
    Data.setStatusCode(0)
   
    def __init__(self, rateInSec = DEFAULT_RATE_IN_SEC):
        self.config = ConfigUtil.ConfigUtil('../../../data/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        self.nomalTemp = self.config.getProperty(ConfigConst.DEVICE_SECTION, ConfigConst.nominalTemp)
        self.botton = self.config.getProperty(ConfigConst.DEVICE_SECTION, ConfigConst.enableEmulator)
        print("The nomalTemp is = " + str(self.nomalTemp))
        super(TempSensorAdaptor, self).__init__()
        
        if rateInSec > 0:
            self.rateInSec = rateInSec

    def run(self):
        while True:
            if self.enableEmulator:
                self.curTemp = random.uniform(float(self.lowVal), float(self.highVal))      
                #self.curTemp = tempEmu.getCurTemp()       
                Sens.addValue(self.curTemp)
                ActD.setValue(self.curTemp)
                #self.SensorData.addValue(self.curTemp)
                print('\n--------------------')
                print('New sensor readings:')
                print(' ' + str(self.curTemp))
                

                if self.isPrevTempSet == False:
                    self.prevTemp = self.curTemp
                    self.isPrevTempSet = True
                    
                else:
                    ################
                    if (self.curTemp > self.nomalTemp):
                        self.dif = self.curTemp - self.nomalTemp
                        print('Current temperature exceeds nomalTemp by > ' + str(self.dif))
                        #self.sensorData = AcData.__str__()
                        print('BBBBBBBBBBBBBBBBBig')
                        self.Data.setCommand(1)
                        self.Data.setStateData(1)
                        self.Data.setErrorCode(0)
                        self.Data.setStatusCode(1)
                        self.Data.setValue(self.dif)
                        TempAcEmu.processMessage(self.Data)
                        
                    elif(self.curTemp < self.nomalTemp):
                        self.dif = self.curTemp - self.nomalTemp
                        print('\nCurrent temperature falls below nomalTemp by > ' + str(self.dif))
                        print('SSSSSSSSSSSSSSSSmall')
                        self.Data.setCommand(1)
                        self.Data.setStateData(1)
                        self.Data.setErrorCode(0)
                        self.Data.setStatusCode(1)
                        self.Data.setValue(self.dif)
                        TempAcEmu.processMessage(self.dif)
                            
                    else:{
                        print('Nothing need to do.')                       
                    }
                    #############
                    print (Sens.__str__())
                    print ('\nCurTemp - AvgValue = ' + str(abs(self.curTemp - Sens.getAvgValue())))
                    print ('Threshold          = ' + str(self.alertDiff))

                    if (abs(self.curTemp - Sens.getAvgValue()) >= self.alertDiff):
                        print('\nCurrent temp exceeds average by > ' + str(self.alertDiff) + '. Triggeringalert...')
                        self.sensorData = Sens.__str__()
                        #SmtpConnector.publishMessage('Exceptional sensor data [test]', self.sensorData)
                        
                sleep(self.rateInSec)
                
                
                
                
            