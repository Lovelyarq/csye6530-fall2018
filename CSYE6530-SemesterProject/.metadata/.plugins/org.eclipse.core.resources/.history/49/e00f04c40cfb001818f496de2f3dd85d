'''
Created on Sep 28, 2018

@author: xingli
'''
from time import sleep
from sense_hat import SenseHat
import threading

class SenseHatLedActivator(threading.Thread):
    enableLed = False
    rateInSec = 1
    rotateDeg = 270
    sh = None
    displayMsg = None
    
    #Constructor
    def __init__(self, rotateDeg = 270, rateInSec = 1):
        super(SenseHatLedActivator, self).__init__()
        if rateInSec > 0:
            self.rateInSec = rateInSec
        if rotateDeg >= 0:
            self.rotateDeg = rotateDeg
        self.sh = SenseHat()
        self.sh.set_rotation(self.rotateDeg)
        
    def run(self):
        once = True
        while once:
            print('in run' + str(self.enableLed))
            if self.enableLed:
                print('in self.enableled')
                if self.displayMsg != None:
                    print('in self.displaymsg')
                    self.sh.show_message(str(self.displayMsg))#show message in the sensorHat
                    once = False
                else:
                    self.sh.show_letter(str('R'))
                    sleep(self.rateInSec)
                    self.sh.clear()
                    once = False
            sleep(self.rateInSec)
            
    def getRateInSeconds(self):
        return self.rateInSec
    
    def setEnableLedFlag(self, enable):
        self.sh.clear()
        self.enableLed = enable
        
    def setDisplayMessage(self, msg):
        self.displayMsg = msg