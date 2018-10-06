'''
Created on 2018年9月22日

@author: jrq
'''

from labs.common import SensorData

ss = SensorData.SensorData()
a = ss.getAvgValue()
b = ss.__str__()


class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        