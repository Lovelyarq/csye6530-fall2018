#coding:utf-8   #强制使用utf-8编码格式
'''
Created on 2018年9月15日

@author: jrq
'''
      


import threading
import smtplib

from labs.common import ConfigUtil
from labs.common import ConfigConst

from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
#from labs.common import SensorData

#Sens = SensorData.SensorData()


class SmtpClientConnector (threading.Thread):
    def __init__(self):
        #Give address of .props file from data
        self.config = ConfigUtil.ConfigUtil('../../../data/ConnectedDevicesConfig.props') 
        #Read the .props file from the address above
        self.config.loadConfig()                                                          
        print('Configuration data...\n' + str(self.config)) 
        print('============= Setting Done! =============')
        
    #HOST_KEY,PORT_KEY,FROM_ADDRESS_KEY,TO_ADDRESS_KEY,USER_AUTH_TOKEN_KEY
    def publishMessage(self, topic, data):
        host = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.HOST_KEY)
        port = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.PORT_KEY)
        fromAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.FROM_ADDRESS_KEY)
        toAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.TO_ADDRESS_KEY)
        authToken = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.USER_AUTH_TOKEN_KEY)
        
        #mimeMultipart
        msg = MIMEMultipart()  
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic
        msgBody = str(data)
        #mimeText  
        msg.attach(MIMEText(msgBody))  
        msgText = msg.as_string()
        # send e-mail notification
        
        
        """  this is the code from professor
        smtpServer = smtplib.SMTP_SSL(host, port)
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken)
        smtpServer.sendmail(fromAddr, toAddr, msgText)
        smtpServer.close()
        """
   
        #My code added a check part enable to check if the mail is sent successfully or not.
        def mail():
            #checking variable
            ret=True
            try:
                print ('')
                print ('The content of msgText:')
                print ('-----------------------------')
                print (str(msgText))
                print ('-----------------------------')
                #The SMTP server in the sender's mailbox
                server=smtplib.SMTP_SSL(host,port) 
                #server.ehlo()  # Say hello to the SMTP server to check the connection status
                #server.starttls()  # The connection uses TLS encryption
                #sender's email account and email password.
                server.login(fromAddr,authToken)    
                #Another way: server.sendmail(fromAddr,[toAddr,],msgText)
                #Sender's email account, the recipient's email account, and the outgoing email.
                server.sendmail(fromAddr,toAddr,msgText)    
                #shut down the server
                server.quit()  
                server.close()
                
            except Exception:   
                #If the statement in try is not executed, the following ret=False will be executed.
                ret=False
            return ret
        
        
        
        ret=mail()
        if ret:
            print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print ("The Alert-Email has been sent!!") 
            #If the transmission is successful, it will return ok, wait for about 20 seconds to receive the mail.
            print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        else:
            print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print("Filed to send the Alert-Email!! Please call 911 or using your Personal Hotspot by your phone!")  
            #Return filed if the send fails
            print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        
            