'''
Created on 2018年12月4日

@author: jrq
'''
import paho.mqtt.client as mqttClient

_userName = "A1E-hRhHhHVjakJvL8VNMxjLCzfNN7BOMJ"
_authToken = "null"
_pemFileName = "/Users/jrq/Documents/pem/ubidots.pem"
_host = "things.ubidots.com"
 
def on_connect(clientConn, _userName, _pemFileName, resultCode):
 
 
    print("Client connected to server. Result: " + str(resultCode))
    # NOTE: This subscribes to ALL topics (depending on broker implementation)
    clientConn.subscribe("/v1.6/devices/homeiotgateway/tempactuator")
 
 
def on_message(clientConn, data, msg):
 
 
    print("Received PUBLISH on topic {0}. Payload: {1}".format(str(msg.topic), str(msg.payload)))
     
     
mc = mqttClient.Client()
mc.on_connect = on_connect
mc.on_message = on_message
mc.connect(_host, 1883, 60)
mc.loop_forever()



