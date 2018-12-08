'''
Created on 2018年9月15日

@author: jrq
'''
#import sys
#sys.path.append('/home/pi/workspace/iot-device/apps')

SMTP = 'smtp'
MQTT = 'mqtt'
COAP = 'coap'

CLOUD = 'cloud'
GATEWAY = 'gateway'
DEVICE = 'device'

SECTION_SEPARATOR = '.'


SMTP_CLOUD_SECTION = SMTP + SECTION_SEPARATOR + CLOUD
MQTT_CLOUD_SECTION = MQTT + SECTION_SEPARATOR + CLOUD
COAP_GATEWAY_SECTION = COAP + SECTION_SEPARATOR + GATEWAY
DEVICE_SECTION = DEVICE


nominalTemp = 20
enableEmulator = True

#SMTP
HOST_KEY = 'smtp.163.com'
PORT_KEY = '587'
FROM_ADDRESS_KEY = 'private information@163.com'
TO_ADDRESS_KEY = 'private information@gmail.com'
USER_AUTH_TOKEN_KEY = 'private information'

#COAP
COAP_HOST = '192.168.0.199'
COAP_PORT = '5683'


DEFAULT_CONFIG_FILE_NAME = ""




