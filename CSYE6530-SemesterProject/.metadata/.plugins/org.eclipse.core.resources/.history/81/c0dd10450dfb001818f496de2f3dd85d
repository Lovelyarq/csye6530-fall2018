'''
Created on Dec 7, 2018

@author: xingli
'''
import os,sys
sys.path.append('/home/pi/Desktop/xing/iot-device/apps')
import paho.mqtt.client as mqttClient
import RPi.GPIO as GPIO
pins = [17]


from time           import sleep
from labs.module03 import TempSensorAdaptor
from labs.module03 import mqttSimpleClient
sysPerfAdaptor = TempSensorAdaptor.TempSensorAdaptor()

print("Starting system performance app daemon thread...")
sysPerfAdaptor.setEnableAdaptorFlag(True)#set enableAdaptor to true
sysPerfAdaptor.start()#start the run function in TempSensorAdaptor
def gpio_setup():
    GPIO.setmode(GPIO.BCM)
    for pin  in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.IN)
        
def on_connect(clientConn, data, flags, resultCode):
    print("Client connected to server. Result: " + str(resultCode))

# NOTE: This subscribes to ALL topics (depending on broker implementation)

    clientConn.subscribe("myActuatorData") 
def on_message(clientConn, data, msg):

    print("Received PUBLISH on topic {0}. Payload: {1}".format(str(msg.topic), str(msg.payload)))
    sysPerfAdaptor.tragerActuator(msg.payload)
         

    
    

mc = mqttClient.Client()

mc.on_connect = on_connect

mc.on_message = on_message
gpio_setup()
mc.connect("test.mosquitto.org", 1883, 60)

mc.loop_forever()

#--------------------

 
# 消息推送回调函数
# def on_message(client, userdata, msg):
#     print(msg.topic+" "+str(msg.payload))
#     # 获得负载中的pin 和 value
#     gpio =str(msg.payload)
#     
# #     if gpio > 23:
# #         GPIO.output(pins, GPIO.HIGH)
# #     else:
# #         GPIO.output(pins, GPIO.LOW)
 

