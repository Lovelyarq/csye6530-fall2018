'''
Created on 2018年12月4日

@author: jrq
'''
#!/usr/bin/env python

from coapthon.server.coap import CoAP
#from labs.common import ConfigUtil
#from labs.common import ConfigConst
from labs.module07.TestCoapResource import TestCoapResource


class CoapServerConnector(CoAP):


    config = None


    def __init__(self, ipAddr="0.0.0.0", port=5683, multicast=False):


        #self.config = ConfigUtil.ConfigUtil(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        #self.config.loadConfig()
        #print('Configuration data...\n' + str(self.config))
        CoAP.__init__(self, (ipAddr, port), multicast)
        if port >= 1024:
            self.port = port
        else:
            self.port = 5683
            
        self.ipAddr = ipAddr
        self.useMulticast = multicast
        self.initResources()


    def initResources(self):


        self.add_resource('test/', TestCoapResource())
        print("CoAP server initialized. Binding: " + self.ipAddr + ":" + str(self.port))
        print(self.root.dump())


def main():


    ipAddr = "0.0.0.0"
    port = 5683
    useMulticast = False
    coapServer = None
    try:
        coapServer = CoapServerConnector(ipAddr, port, useMulticast)
        try:
            coapServer.listen(10)
            print("Created CoAP server ref: " + str(coapServer))
        except Exception:
            print("Failed to create CoAP server reference bound to host: " + ipAddr)
            pass
    except KeyboardInterrupt:
        print("CoAP server shutting down due to keyboard interrupt...")
    if coapServer:
        coapServer.close()
    print("CoAP server app exiting.")
if __name__ == '__main__':
    main()
