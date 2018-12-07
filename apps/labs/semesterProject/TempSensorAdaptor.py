'''
Created on 2018年9月22日

@author: jrq
'''

#import sys
#sys.path.append('/home/pi/workspace/iot-device/apps')

import random
from time import sleep
import threading
from labs.common import SensorData
from labs.common import ActuatorData

from sense_hat import SenseHat

from labs.semesterProject import SmtpClientConnector 
from labs.semesterProject import TempActuatorEmulator
from labs.semesterProject import CoapClientConnector

DEFAULT_RATE_IN_SEC = 15

TempAcEmu = TempActuatorEmulator.TempActuatorEmulator()
Sens = SensorData.SensorData()
ActD = ActuatorData.ActuatorData()
CoAP = CoapClientConnector.CoapClientConnector()
SmtpConnector = SmtpClientConnector.SmtpClientConnector()
sense = SenseHat()


class TempSensorAdaptor (threading.Thread):
    enableEmulator = False
    isPrevTempSet  = False
    rateInSec      = DEFAULT_RATE_IN_SEC
    Sens.setName('Temperature')
    
    lowVal = 0
    highVal = 30
    alertDiff = 1
    
    Data = ActD
    Data.setCommand(0)
    Data.setValue(0)
    Data.setErrorCode(0)
    Data.setStateData(0)
    Data.setStatusCode(0)
   
    def __init__(self, rateInSec = DEFAULT_RATE_IN_SEC):
        super(TempSensorAdaptor, self).__init__()
        if rateInSec > 0:
            self.rateInSec = rateInSec

    def run(self):
        while True:
            if self.enableEmulator:
                self.curTemp = random.uniform(float(self.lowVal), float(self.highVal))      
                #self.curTemp = tempEmu.getCurTemp()  
                #self.curTemp = sense.get_temperature()     
                Sens.addValue(self.curTemp)
                #self.SensorData.addValue(self.curTemp)
                print('\n--------------------')
                print('New sensor readings:')
                print(' ' + str(self.curTemp))
                
                if self.isPrevTempSet == False:
                    self.prevTemp = self.curTemp
                    self.isPrevTempSet = True
                else:
                    ########-- COAP Part --########
                    print('Transport data by protocol:COAP | Sending..... ')    
                    CoAP.handlePostTest("temp", str(self.curTemp))
                    
                    ########-- Actuator Part --########
                    #Check the curTemp is higher or lower than nominalTemp
                    self.dif = TempAcEmu.Check(self.curTemp)
                    
                    if (self.dif > 0):
                        print("Current temperature exceeds nomalTemp by --> " + str(self.dif) )
                        #If higher then set Command = 1, others is no needed for this module
                        TempAcEmu.setMessage(self.Data, 1, 0, None, 1)
                        self.Data.setValue(self.dif)
                        #Send the instance of ActuatorData to TempActuatorEmulator by processMessage
                        TempAcEmu.processMessage(self.Data)
                            
                    if (self.dif < 0):
                        print("\nCurrent temperature falls below nomalTemp by -->" + str(abs(self.dif)) )
                        #If lower then set Command = 0
                        TempAcEmu.setMessage(self.Data, 0, 0, None, 1)
                        self.Data.setValue(abs(self.dif))
                        #Send the instance of ActuatorData to TempActuatorEmulator by processMessage
                        TempAcEmu.processMessage(self.Data) 
                    
                    if (self.dif == 0):
                        print("Current temperature equal to nomalTemp.")
                        print('Nothing need to do.') 
                            
                    ########-- Adaptor Part --########
                    print (Sens.__str__())
                    print ('\nCurTemp - AvgValue = ' + str(abs(self.curTemp - Sens.getAvgValue())))
                    print ('Threshold          = ' + str(self.alertDiff))
                    #Check if higher than threshold
                    if (abs(self.curTemp - Sens.getAvgValue()) >= self.alertDiff):
                        print('\nCurrent temp exceeds average by > ' + str(self.alertDiff) + '. Triggeringalert...')
                        self.sensorData = Sens.__str__()
                        #Used SMTP to send message to remote device.
                        SmtpConnector.publishMessage('Exceptional sensor data [test]', self.sensorData)

                    
                sleep(self.rateInSec)
                

                
                
                
                
            