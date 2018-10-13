'''
Created on 2018年9月14日

@author: jrq
'''

 


from time import sleep
from labs.module01 import SystemPerformanceAdaptor

sysPerfAdaptor = SystemPerformanceAdaptor.SystemPerformanceAdaptor()
#sysPerfAdaptor.daemon = True
#SystemPerformanceAdaptor.SystemPerformanceAdaptor().daemon = True
print("Starting system performance app daemon thread...")

sysPerfAdaptor.enableAdaptor = True
sysPerfAdaptor.start()
#SystemPerformanceAdaptor.SystemPerformanceAdaptor().enableAdaptor = True
#SystemPerformanceAdaptor.SystemPerformanceAdaptor().start()


while (True):
    sleep(5)
    pass





