'''
Created on 2018年9月22日

@author: jrq
'''


'''

import sense_hat
from labs.common import ActuatorData

from labs.module03 import SimpleLedActivator
from labs.module03 import SenseHatLedActivator

sensh = sense_hat.SenseHat()
SimpLedAct = SimpleLedActivator.SimpleLedActivator()
SensHatAct = SenseHatLedActivator.SenseHatLedActivator()
'''

from labs.common import ActuatorData
from labs.module03 import SenseHatLedActivator
from labs.module03 import SimpleLedActivator

from labs.common import ConfigUtil
from labs.common import ConfigConst

AcData = ActuatorData.ActuatorData()
SensHat = SenseHatLedActivator.SenseHatLedActivator()
SimpLed = SimpleLedActivator.SimpleLedActivator()
config = ConfigUtil.ConfigUtil

class TempActuatorEmulator(): 
    AData = AcData
    AData.setCommand(0)
    AData.setErrorCode(0)
    AData.setStateData(None)
    AData.setStatusCode(0)
    


    def __init__(self):
        self.config = ConfigUtil.ConfigUtil('../../../data/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        self.nomalTemp = self.config.getProperty(ConfigConst.DEVICE_SECTION, ConfigConst.nominalTemp)
        self.botton = self.config.getProperty(ConfigConst.DEVICE_SECTION, ConfigConst.enableEmulator)
        print("The nomalTemp is = " + str(self.nomalTemp))
        print("The botton is :" + str(self.botton))
        
        SensHat.daemon = True
        SensHat.start()
        
    def processMessage(self, Data):
        self.Data = Data
        AcData.updateData(self.Data)
        SensHat.setEnableLedFlag(True)
        #SimpLed.setEnableLedFlag(True)
        message = "Actuator mmmmmmmmmesg::" + AcData.getStateData()
        SensHat.setDisplayMessage(message)
    
    def setMessage(self,AData,command,errCode,stateData,statusCode):
        AData.setCommand(command)
        AData.setErrorCode(errCode)
        AData.setStateData(stateData)
        AData.setStatusCode(statusCode)
        
    def Check(self,curTemp):
        self.curTemp = curTemp
        self.dif = self.curTemp - self.nomalTemp
        dif = self.dif
        return dif
    
        
    
        
        
        
    
   


















'''
    AcData = None    
    SimpLedAct = None
    SensHatAct = None

    def __init__(self):
        
        SimpLedAct.daemon = True
        SimpLedAct.enableLed = True
        SimpLedAct.start() 
        
        SensHatAct.daemon = True
        SensHatAct.enableLed = True
        SensHatAct.start()
        
    def processMessage(self,command,name,errCode,stateData,statusCode):
        
        
        self.updcom = AcData.setCommand(command)
        self.updname = AcData.setName(name)
        self.updeerC = AcData.setErrorCode(errCode)
        self.updstateD = AcData.setStateData(stateData)
        self.updstateC = AcData.setStatusCode(statusCode)
    
    def process_message(self, Data):
        AcData.updateData(Data)
        SimpLedAct.setEnableLedFlag(True)
        self.Led()

    def Led(self):
                
        if (AcData.getCommand() == 0):
            SensHatAct.setEnableLedFlag(True)
            m = "Temperature is lowered "
            print(m)
            SensHatAct.setDisplayMessage(m)
            
        elif (AcData.getCommand() == 1):
            SensHatAct.setEnableLedFlag(False)
            m = "Temperature is high "
            print(m)
            SensHatAct.setDisplayMessage(m)
            
        else:
            print('nothing happen')
    
   '''