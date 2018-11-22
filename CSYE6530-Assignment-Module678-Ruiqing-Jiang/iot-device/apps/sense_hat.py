'''
Created on 2018年9月22日

@author: jrq
'''
class SenseHat():
    rotateDeg = 270
    clearFlag = False
    def __init__(self):
        self.set_rotation(self.rotateDeg)
    def clear(self):
        self.clearFlag = True
    def get_humidity(self):
    # NOTE: This is just a sample
        return 48.5
    def get_temperature(self):
        return self.get_temperature_from_humidity()
    def get_temperature_from_humidity(self):
    # NOTE: This is just a sample
        return 21.4
    def get_temperature_from_pressure(self):
        return self.get_temperature_from_humidity()
    def get_pressure(self):
    # NOTE: This is just a sample
        return 31.5
    def set_rotation(self, rotateDeg):
        self.rotateDeg = rotateDeg
    def show_letter(self, val):
        print(val)
    def show_message(self, msg):
        print(msg)