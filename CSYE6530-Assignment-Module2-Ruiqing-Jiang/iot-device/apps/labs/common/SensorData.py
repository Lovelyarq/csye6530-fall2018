'''
Created on 2018年9月15日

@author: jrq
'''
import os

from datetime import datetime

class SensorData:
    timeStamp = None
    name = 'Not set'
    #newVal = 0
    curValue = 0
    avgValue = 0
    minValue = 0
    maxValue = 0
    totValue = 0
    sampleCount = 0
    
    def __init__(self):
        self.timeStamp = str(datetime.now())
    def addValue(self, newVal):
        #self.newVal = newVal
        #Count the number so that we can calculate the avgValue by totValue/sampleCount
        self.sampleCount += 1
        self.timeStamp = str(datetime.now())
        
        self.totValue = self.totValue + newVal
        self.curValue = newVal
        
        if (self.curValue < self.minValue):
            self.minValue = self.curValue
        if (self.curValue > self.maxValue):
            self.maxValue = self.curValue
        if (self.totValue != 0 and self.sampleCount > 0):
            self.avgValue = self.totValue / self.sampleCount
    def getAvgValue(self):
        return self.avgValue
    def getMaxValue(self):
        return self.maxValue
    def getMinValue(self):
        return self.minValue
    def getValue(self):
        return self.curValue
    def gettotvalue(self):
        return self.totValue
    def setName(self, name):
        self.name = name
    def __str__(self):
        customStr = \
            str(self.name + ':'        + \
            os.linesep + '\tTime: '    + self.timeStamp + \
            os.linesep + '\tCurrent: ' + str(self.curValue) + \
            os.linesep + '\tAverage: ' + str(self.avgValue) + \
            os.linesep + '\tSamples: ' + str(self.sampleCount) + \
            os.linesep + '\tMin: '     + str(self.minValue) + \
            os.linesep + '\tMax: '     + str(self.maxValue))
        return customStr










