from time import time
from django.shortcuts import render_to_response
class PassiveMessage(object):
    def __init__(self,fromUser,toUser):
        self.fromUser=fromUser
        self.toUser=toUser
        self.createTime=int(time())
        self.contextDic={'fromUser':self.fromUser,'toUser':self.toUser,'createTime':self.createTime}
    def responseWithText(self,content):
        template='textMessage.html'
        dic=self.contextDic.copy()
        dic['content']=content
        return render_to_response(template,dic)
    def responseWithImage(self,mediaId):
        template='imageMessage.html'
        dic=self.contextDic.copy()
        dic['mediaId']=mediaId
        return render_to_response(template,dic)
    def responseWithVoice(self,mediaId):
        template='voiceMessage.html'
        dic=self.contextDic.copy()
        dic['mediaId']=mediaId
        return render_to_response(template,dic)
    def responseWithMusic(self,mediaId,title,description,musicUrl,hqMusicUrl):
        template='musicMessage.html'
        dic=self.contextDic.copy()
        dic['mediaId']=mediaId
        dic['title']=title
        dic['description']=description
        dic['musicUrl']=musicUrl
        dic['hqMusicUrl']=hqMusicUrl
        return render_to_response(template,dic)
    def responseWithTextAndImage(self,articles): #article is array ,
        template='imageAndTextMessage.html'
        dic=self.contextDic.copy()
        dic['articles']=articles
        return render_to_response(template,dic)