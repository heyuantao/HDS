#coding=utf-8
from django.utils.encoding import smart_str
import xml.etree.ElementTree as Etree
from receivedWeiXin import BaseWeiXinMessage

class NormalWeiXinMessage(BaseWeiXinMessage):  #普通消息    消息类的父类
    #normalMsgTypeList=['text','image','voice','video','location']
    def __init_(self,request):
        super(self,NormalWeiXinMessage).__init__(self,request)
    def getMsgId(self):
        msgId=self.xml.find('MsgId').text
        return msgId
    
class TextWeiXinMessage(NormalWeiXinMessage):
    def __init_(self,request):
        super(self,TextWeiXinMessage).__init__(self,request)
    def getContent(self):
        requestMsgType=self.xml.find('Content').text
        return requestMsgType
    
class ImageWeiXinMessage(NormalWeiXinMessage):
    def __init_(self,request):
        super(self,ImageWeiXinMessage).__init__(self,request)
    def getPicUrl(self):
        picUrl=self.xml.find('PicUrl').text
        return picUrl
    def getMediaId(self):
        mediaId=self.xml.find('MediaId').text
        return mediaId
    
class VoiceWeiXinMessage(NormalWeiXinMessage):
    def __init_(self,request):
        super(self,VoiceWeiXinMessage).__init__(self,request)
    def getMediaId(self):
        mediaId=self.xml.find('MediaId').text
        return mediaId
    def getFormat(self):
        format=self.xml.find('Format').text
        return format
    
class VideoWeiXinMessage(NormalWeiXinMessage):
    def __init_(self,request):
        super(self,VideoWeiXinMessage).__init__(self,request)
    def getMediaId(self):
        mediaId=self.xml.find('MediaId').text
        return mediaId
    def getThumbMediaId(self):
        thumbMediaId=self.xml.find('ThumbMediaId').text
        return thumbMediaId

class GeogWeiXinMessage(NormalWeiXinMessage):
    def __init_(self,request):
        super(self,GeogWeiXinMessage).__init__(self,request)
    def getLocation(self):
        Location_X=self.xml.find('Location_X').text
        Location_Y=self.xml.find('Location_Y').text
        return (Location_X,Location_Y)
    def getScale(self):
        scale=self.xml.find('Scale').text
        return scale
    def getLabel(self):
        label=self.xml.find('Label').text
        return label

class LinkWeiXinMessage(NormalWeiXinMessage):
    def __init_(self,request):
        super(self,LinkWeiXinMessage).__init__(self,request)
    def getTitle(self):
        title=self.xml.find('Title').text
        return title
    def getDescription(self):
        description=self.xml.find('Description').text
        return description
    def getUrl(self):
        url=self.xml.find('Url').text
        return url