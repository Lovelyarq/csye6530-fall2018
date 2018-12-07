'''
Created on 2018年12月4日

@author: jrq
'''
from coapthon.server.coap import CoAP
from labs.common import ConfigUtil
#from labs.common import ConfigConst
from labs.module07.TestCoapResource import TestCoapResource


class CoapServerConnector(CoAP):
    #config = None
    def __init__(self, ipAddr="0.0.0.0", port=5683, multicast=False):

    
    
        #self.config = ConfigUtil.ConfigUtil(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        #self.config.loadConfig()
        
        self.config = ConfigUtil.ConfigUtil('../../../data/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config)) 
        print('============= Setting Done! =============')
        #print('Configuration data...\n' + str(self.config))
        CoAP.__init__(self, (ipAddr, port), multicast)
        
        #self.add_resource('TestCoapResource/', TestCoapResource())
        
        print('PPPPPPPPPPPotttttt::::' + str(port) + '  ' + str(ipAddr))
        if port >= 1024:
            self.port = port
        else:
            self.port = 5683
        self.ipAddr = ipAddr
        self.useMulticast = multicast
        self.add_resource('test/', TestCoapResource())
        self.initResources()
    
    
    def initResources(self):
    
    
        
        a = self.add_resource('test/', TestCoapResource())
        print (str(a))
        print("CoAP server initialized. Binding: " + self.ipAddr + ":" + str(self.port))
        print(self.root.dump())
    
    
def main():
    host = "0.0.0.0"
    port = 5683
    useMulticast = False
    try:
        coapServer = CoapServerConnector(host, port, useMulticast)
        try:
            coapServer.listen(10)
            print("Created CoAP server ref: " + str(coapServer))
        except Exception:
            print("Failed to create CoAP server reference bound to host: " + host)
            pass
    except KeyboardInterrupt:
        print("CoAP server shutting down due to keyboard interrupt...")
        if coapServer:
            coapServer.close()
            print("CoAP server app exiting.")
    
if __name__ == '__main__':
        main()
