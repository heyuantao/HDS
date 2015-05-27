#coding=utf-8
from django.utils.encoding import smart_str
import xml.etree.ElementTree as Etree
from receivedWeiXin import BaseWeiXinMessage


class BaseWeiXinEvent(BaseWeiXinMessage):    #接受事件类的父类
    
    def __init_(self,request):
        super(self,BaseWeiXinEvent).__init__(self,request)
    def getEvent(self):
        event = self.xml.find('Event').text
        return event
    
class FollowOrUndoWeiXinEvent(BaseWeiXinEvent):  #关注取消关注事件
    def __init_(self,request):
        super(self,FollowOrUndoWeiXinEvent).__init__(self,request)   

class ScanQRCodeWithArgument(BaseWeiXinEvent):  #扫描带参数的二维码事件
    def __init_(self,request):
        super(self,ScanQRCodeWithArgument).__init__(self,request)  
    def getEventKey(self):
        eventKey = self.xml.find('EventKey').text
        return eventKey
    def getTicket(self):
        ticket = self.xml.find('Ticket').text
        return ticket
    

class UploadGeogWeiXinEvent(BaseWeiXinEvent):  #上报地理位置事件
    def __init_(self,request):
        super(self,UploadGeogWeiXinEvent).__init__(self,request)   
    def getLatitude(self):
        latitude = self.xml.find('Latitude').text
        return latitude
    def getLongitude(self):
        longitude = self.xml.find('Longitude').text
        return longitude
    def getPrecision(self):
        precision = self.xml.find('Precision').text
        return precision

class UserDefMenuWeiXinEvent(BaseWeiXinEvent):  #用户自定义菜单事件
    def __init_(self,request):
        super(self,UserDefMenuWeiXinEvent).__init__(self,request)   
    
