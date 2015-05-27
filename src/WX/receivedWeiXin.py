#coding=utf-8
from django.utils.encoding import smart_str
import xml.etree.ElementTree as Etree

class BaseWeiXinMessage(object):    
    def __init__(self,request):
        try:
            self.xmlstr=smart_str(request.body)
            self.xml = Etree.fromstring(self.xmlstr)
        except Exception:
            print "error in BaseWeiXinMessage init"
    def getMessageType(self):
        requestMsgType=self.xml.find('MsgType').text
        return requestMsgType
    def getFromUser(self):
        fromUser = self.xml.find('FromUserName').text
        return fromUser
    def getToUser(self):
        toUser = self.xml.find('ToUserName').text
        return toUser
    def getFromAndToUser(self):
        toUser = self.xml.find('ToUserName').text
        fromUser = self.xml.find('FromUserName').text
        return (fromUser,toUser)
    def getCreateTime(self):
        createTime = self.xml.find('CreateTime').text
        return createTime
    
            