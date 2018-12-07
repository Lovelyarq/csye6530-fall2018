'''
Created on 2018年12月1日

@author: jrq
'''

#import sys
#sys.path.append('/home/pi/workspace/iot-device/apps')

from coapthon.client.helperclient import HelperClient
from labs.common import ConfigUtil
from labs.common import ConfigConst
#import socket


client = None

class CoapClientConnector():


    config = None
    serverAddr = None
    host = "127.0.0.1"
    port = 5683
    
    
    def __init__(self):
    
    
        #self.config = ConfigUtil.ConfigUtil(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        #self.config.loadConfig()
        
        self.config = ConfigUtil.ConfigUtil('../../../data/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config)) 
        print('============= Setting Done! =============')
        
        
        self.host = self.config.getProperty(ConfigConst.COAP_GATEWAY_SECTION, ConfigConst.COAP_HOST)
        self.port = int(self.config.getProperty(ConfigConst.COAP_GATEWAY_SECTION, ConfigConst.COAP_PORT))
        print('\tHost: ' + self.host)
        print('\tPort: ' + str(self.port))
        
        if not self.host or self.host.isspace():
            print("Using default host: " + self.host)
        if self.port < 1024 or self.port > 65535:
            print("Using default port: " + self.port)
            
        self.serverAddr = (self.host, self.port)
        print('dddddddddddddddd' + str(self.serverAddr))
        
        self.url = "coap://" + self.host + ":" + str(self.port) + "/temp"
    
    
    def initClient(self):
        """
        try:
            tmp = socket.gethostbyname(self.host)
            host = tmp

        except socket.gaierror:
            pass
        """
        try:
            self.client = HelperClient(server=(self.host, self.port))
            print("Created CoAP client ref: " + str(self.client))
            print(" coap://" + self.host + ":" + str(self.port))
        except Exception:
            print("Failed to create CoAP helper client reference using host: " + self.host)
            pass
    
    
    def handleGetTest(self,resource):
    
        print("Testing GET for resource: " + str(resource))
        self.initClient()
        response = self.client.get(resource)
        if response:
            print(response.pretty_print())
        else:
            print("No response received for GET using resource: " + resource)
        self.client.stop()
    
    
    def handlePostTest(self, resource, payload):
    
        print("Testing POST for resource: " + resource + ", payload: " + payload)
        self.initClient()
        response = self.client.post(resource, payload)
        if response:
            print(response.pretty_print())
            print("wohahahahahah:POST COMPLETE!!!")
        else:
            print("No response received for POST using resource: " + resource)
        self.client.stop()
        
        
    def handlePutTest(self, resource, payload):
    
        print("Testing PUT for resource: " + resource + ", payload: " + payload)
        self.initClient()
        response = self.client.put(resource, payload)
        if response:
            print(response.pretty_print())
        else:
            print("No response received for put using resource: " + resource)
        self.client.stop()
        
    def handleDeleteTest(self, resource, payload):
    
    
        print("Testing delete for resource: " + resource + ", payload: " + payload)
        self.initClient()
        response = self.client.delete(resource, payload)
        if response:
            print(response.pretty_print())
        else:
            print("No response received for delete using resource: " + resource)
        self.client.stop()

#         
# def main():  # pragma: no cover
#  
#     # url = "coap://localhost:5683/temp"
#     CoapClientConnector().handleGetTest("temp")
#     #CoapClientConnector().handlePostTest("temp", "23")
#     
#      
#      
# if __name__ == '__main__':  # pragma: no cover
#     main()
    
