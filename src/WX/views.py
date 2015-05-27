#coding=utf-8
from django.shortcuts import render,render_to_response
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.http import Http404


from django.utils.encoding import smart_str, smart_unicode
import xml.etree.ElementTree as Etree  

from receivedWeiXin import BaseWeiXinMessage
from receivedWeiXinMsg import NormalWeiXinMessage
from receivedWeiXinMsg import TextWeiXinMessage,ImageWeiXinMessage,VoiceWeiXinMessage,VideoWeiXinMessage,GeogWeiXinMessage,LinkWeiXinMessage
from receivedWeiXinEvent import BaseWeiXinEvent
from receivedWeiXinEvent import FollowOrUndoWeiXinEvent,ScanQRCodeWithArgument,UploadGeogWeiXinEvent,UserDefMenuWeiXinEvent
from receivedWeiXinVaild import ValidWeiXin
from sendPassiveWeiXinMsg import PassiveMessage
# Create your views here.
class Process(View):  # this is the main router for weixin      
    def post(self, request):  
        rev=BaseWeiXinMessage(request)    
        if not ValidWeiXin.isRequestIsValid(request):    
            raise Http404 
        print rev.getToUser()
        print rev.getFromUser()
        print rev.getMessageType()
        if  rev.getMessageType()=='text':
            rece=TextWeiXinMessage(request)
            print rece.getContent()
            send=PassiveMessage(rece.getToUser(),rece.getFromUser())
            return send.responseWithText(u"你输入了"+rece.getContent())
        if rev.getMessageType()=='voice':
            rece=VoiceWeiXinMessage(request)
            send=PassiveMessage(rece.getToUser(),rece.getFromUser())
            print rece.getMediaId()
            return send.responseWithVoice(rece.getMediaId())
        else:
            rece=BaseWeiXinMessage(request)
            send=PassiveMessage(rece.getToUser(),rece.getFromUser())
            return send.responseWithText("不知道你输入了什么！")
        raise Http404 
        