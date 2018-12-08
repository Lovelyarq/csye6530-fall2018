'''
Created on 2018年12月2日

@author: jrq
'''

import sys
sys.path.append('/home/pi/workspace/iot-device/apps')


import paho.mqtt.client as mqttClient
from labs.semesterProject import SenseHatLedActivator



 
SensHat = SenseHatLedActivator.SenseHatLedActivator()
buttonn = "enable"
 
def on_connect(clientConn, _userName, _pemFileName, resultCode):
 
 
    print("Client connected to server. Result: " + str(resultCode))
    # NOTE: This subscribes to ALL topics (depending on broker implementation)
    clientConn.subscribe("ActuatorData")
 
 
def on_message(clientConn, data, msg):
 
 
    print("Received PUBLISH on topic {0}. Payload: {1}".format(str(msg.topic), str(msg.payload)))
    strr = str(msg.payload)
    #split the spring: example:{"timestamp": 1544219224392, "context": {}, "value": 38.0, "id": "5c0aea585916363eb0eaaf68"}
    #this code is to get the "value" of the msg.payload, which is 38 in the example
    print ("Request from the cloud: Set temp to" + str( strr.split(',')[-2].split(':')[1]) )
    tempData = str( strr.split(',')[-2].split(':')[1])
     
    message ="Set temp to" + tempData
    print(message)
    if buttonn == "enable" :
        print("Sense Hat start showing!")
        SensHat.setEnableLedFlag(True)
        SensHat.setDisplayMessage(message)
    else:
        print("Please enable the button for this actuator.")

def run():
    mc = mqttClient.Client()
    mc.on_connect = on_connect
    #Start senHat
    SensHat.daemon = True
    SensHat.start()
    mc.on_message = on_message
    mc.connect("test.mosquitto.org", 1883, 60)
    mc.loop_forever()



