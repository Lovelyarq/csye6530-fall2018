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
from labs.module03 import SimpleLedActivator

AcData = ActuatorData.ActuatorData()
SimpLed = SimpleLedActivator.SimpleLedActivator()

class TempActuatorEmulator(): 
    

    
    def __init__(self):
        '''
        nothing
        '''

        
    def processMessage(self, Data):
        self.Data = Data
        AcData.updateData(self.Data)
    
    def StartLed(self):
        SimpLed.enableLed = True
        SimpLed.daemon = True
        SimpLed.start()
    
    def CloseLed(self):
        SimpLed.enableLed = False
        
    
        
        
        
    
   


















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