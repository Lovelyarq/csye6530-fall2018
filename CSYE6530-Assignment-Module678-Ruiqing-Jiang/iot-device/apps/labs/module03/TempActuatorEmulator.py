'''
Created on 2018年9月22日

@author: jrq
'''
#import sys
#sys.path.append('/home/pi/workspace/iot-device/apps')

from labs.common import ActuatorData
from labs.module03 import SenseHatLedActivator

from labs.common import ConfigUtil
from labs.common import ConfigConst

AcData = ActuatorData.ActuatorData()
SensHat = SenseHatLedActivator.SenseHatLedActivator()
config = ConfigUtil.ConfigUtil

class TempActuatorEmulator(): 
    def __init__(self):
        self.config = ConfigUtil.ConfigUtil('../../../data/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        #Read the config and get the data of nominalTemp
        self.nomalTemp = self.config.getProperty(ConfigConst.DEVICE_SECTION, ConfigConst.nominalTemp)
        print("The nomalTemp is = " + str(self.nomalTemp))
        
        SensHat.daemon = True
        SensHat.start()
        
    def processMessage(self, Data):
        self.Data = Data
        AcData.updateData(self.Data)
        #Set msg to cold
        if (AcData.getCommand() == 1):
            msg = "|Up| Be cold!"
            AcData.setStateData(msg)
        #Set msg to warm
        if (AcData.getCommand() == 0):
            msg = "|Down| Be warm"
            AcData.setStateData(msg)
        #Enable sense_hat run()
        SensHat.setEnableLedFlag(True)
        #Send the msg to sense_hat
        message = "ActuatorMsg::" + AcData.getStateData()
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
    
        
    
        
        
    