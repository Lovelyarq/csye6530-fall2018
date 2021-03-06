'''
Created on 2018年9月22日

@author: jrq
'''
import sys
sys.path.append('/home/pi/workspace/iot-device/apps')

from time import sleep
from sense_hat import SenseHat
import threading

class SenseHatLedActivator(threading.Thread):
    enableLed = False
    rateInSec = 1
    rotateDeg = 270
    sh = None
    displayMsg = None
    
    def __init__(self, rotateDeg = 270, rateInSec = 1):
        super(SenseHatLedActivator, self).__init__()
        if rateInSec > 0:
            self.rateInSec = rateInSec
        if rotateDeg >= 0:
            self.rotateDeg = rotateDeg
        self.sh = SenseHat()
        self.sh.set_rotation(self.rotateDeg)
        
    def run(self):
        while True:
            if self.enableLed:
                if self.displayMsg != None:
                    if self.getLedValue() == 1:
                        self.sh.set_pixel_list = ()
                        self.sh.show_message(str(self.displayMsg))
                    if self.getLedValue() == 0:   
                        self.sh.show_message(str(self.displayMsg))
                else:
                    self.sh.show_letter(str('R'))
                sleep(self.rateInSec)
                self.sh.clear()
            sleep(self.rateInSec)
            
    def getRateInSeconds(self):
        return self.rateInSec
    
    def setEnableLedFlag(self, enable):
        self.sh.clear()
        self.enableLed = enable
        
    def setDisplayMessage(self, msg):
        self.displayMsg = msg + " |got msg!|"
    
    def setLedValue(self,value):
        self.value = value
        
    def getLedValue(self):
        return self.value
    
    
        
        
        
        