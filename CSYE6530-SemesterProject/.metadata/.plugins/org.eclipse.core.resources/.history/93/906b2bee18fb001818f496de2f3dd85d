'''
Created on Sep 28, 2018

@author: xingli
'''
import os,sys
sys.path.append('/home/pi/Desktop/xing/iot-device/apps')
from time import sleep

import threading
import RPi.GPIO as GPIO

# This next import is why we need the RPi.GPIO proxy class import RPi.GPIO as GPIO
class SimpleLedActivator(threading.Thread):
    enableLed = False
    rateInSec = 1
    
    #Constructor
    def __init__(self, rateInSec = 1):
        super(SimpleLedActivator, self).__init__()
        if rateInSec > 0:
            self.rateInSec = rateInSec
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(17, GPIO.OUT)
    
    def run(self):
        while True:
            if self.enableLed:
                GPIO.output(17, GPIO.HIGH)
                sleep(self.rateInSec)
                GPIO.output(17, GPIO.LOW)
            sleep(self.rateInSec)
            
    def getRateInSeconds(self):
        return self.rateInSec
    
    def setEnableLedFlag(self, enable):
        GPIO.setup(17, GPIO.LOW)
        self.enableLed = enable
        
    