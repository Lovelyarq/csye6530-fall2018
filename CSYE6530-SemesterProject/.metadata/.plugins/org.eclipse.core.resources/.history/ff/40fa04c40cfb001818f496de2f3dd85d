'''
Created on Dec 4, 2018

@author: xingli
'''
import os,sys
from coapthon.messages import response
sys.path.append('/home/pi/Desktop/xing/iot-device/apps')
from coapthon.client.helperclient import HelperClient
from labs.common import ConfigUtil 
from labs.common import ConfigConst


class CoapSimpleClientConnector(object):
    config = None
    serverAddr = None
    host = "192.168.1.14" 
    port = 5683
    
    
    def __init__(self):
#             self.config = ConfigUtil.ConfigUtil(ConfigConst.DEFAULT_CONFIG_FILE_NAME) 
#             self.config.loadConfig()
#             self.host = self.config.getProperty(ConfigConst.COAP_CLOUD_SECTION, ConfigConst.HOST_KEY) 
#             self.port = int(self.config.getProperty(ConfigConst.COAP_CLOUD_SECTION, ConfigConst.PORT_KEY))
            print('\tHost: ' + self.host) 
            print('\tPort: ' + str(self.port))
#             if not self.host or self.host.isspace(): 
#                 print("Using default host: " + self.host)
#             if self.port < 1024 or self.port > 65535: 
#                 print("Using default port: " + self.port)
            self.serverAddr = (self.host, self.port)
            self.url = "coap://" + self.host + ":" + str(self.port) + "/temp"
            
    
    def initClient(self): 
        try:
            self.client = HelperClient(server=(self.host, self.port))

           # self.observer = self.client.observe(self.url, callback=self.cb(response), timeout=None)
            print("Created CoAP client ref: " + str(self.client))
            print(" coap://" + self.host + ":" + str(self.port)) 
        except Exception:
            print("Failed to create CoAP helper client reference using host: " + self.host) 
            pass
    
    def handleGetTest(self, resource):
        print("Testing GET for resource: " + resource)
        self.initClient()
        print("initclient successful")
        print(self.url)
        response = self.client.get(resource)

        print("get response--")
        if response: 
            print(response.pretty_print())
        else:
            print("No response received for GET using resource: " + resource)
        self.client.stop()
        
    def handlePostTest(self, resource, payload):
        print("Testing POST for resource: " + resource + ", payload: " + str(payload))
        self.initClient()
        response = self.client.post(resource, payload)
        if response: 
            print(response.pretty_print())
        else:
            print("No response received for POST using resource: " + resource)
        self.client.stop()
        
    def cb(self, response):
        print("here is the response from coap server!!")
        print(response.Response)
