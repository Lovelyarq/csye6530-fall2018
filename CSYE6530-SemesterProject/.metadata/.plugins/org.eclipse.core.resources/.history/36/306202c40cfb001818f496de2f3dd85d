'''
Created on Sep 28, 2018

@author: xingli
'''
import os,sys
sys.path.append('/home/pi/Desktop/xing/iot-device/apps')
from labs.common.ActuatorData import ActuatorData
from labs.module03.SenseHatLedActivator import SenseHatLedActivator
from labs.module03.SimpleLedActivator import SimpleLedActivator

class TempActuatorEmulator():
    actuatorData = None
    senseHatLedActivator = None
    simpleLedActivator = None

    #Constructor
    def __init__(self):
        self.actuatorData = ActuatorData()
        self.senseHatLedActivator = SenseHatLedActivator()
        self.simpleLedActivator = SimpleLedActivator()
        
    #generate a message and run the activator
    def processMessage(self, ActuatorData):
        #print('processMessage...')
        #self.actuatorData.updateData(ActuatorData)
        self.simpleLedActivator.setEnableLedFlag(True)
        if self.actuatorData.getCommand() == 0:
            print('create msg-------')
            msg = "Temperature is " + str(abs(self.actuatorData.getValue())) + " degree lower than nominal temperature, open the cool function" 
        if self.actuatorData.getCommand() == 1:
            print('create msg-+++++')
            msg = "Temperature is " + str(self.actuatorData.getValue()) + " degree higher than nominal temperature, open the heat function" 
        self.senseHatLedActivator.setEnableLedFlag(True)
        self.senseHatLedActivator.setDisplayMessage(ActuatorData)
        #print('before run')
        self.senseHatLedActivator.run()
        #print('after run')