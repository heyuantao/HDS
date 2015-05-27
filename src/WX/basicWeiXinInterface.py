import settingsWeiXin 
import redis
import urllib
import pickle
import pycurl
import json
from datetime import datetime
from StringIO import StringIO

class BasicInterface(object):
    url='https://api.weixin.qq.com/cgi-bin/token?'
    data={'grant_type':'client_credential','appid':settingsWeiXin.Settings.appID,'secret':settingsWeiXin.Settings.appSecret}
    requestUrl=url+urllib.urlencode(data)
    @classmethod
    def getAccessToken(cls):
        db=redis.StrictRedis(host=settingsWeiXin.Settings.redisServerAddress,port=settingsWeiXin.Settings.redisServerPort,db=0)
        if db.exists('accessToken'): #accessToken exist ,do not expire
            token=db.get('accessToken')
            return token
        else:  #accessToken do not exist or accessToken expire,Redis will delete the token when expire
            try:
                newToken=cls.requestAccessToken()
            except Exception:
                raise Exception('Exception in getAcessToken!')
            db.set('accessToken',newToken) #create new key in db and set expire time
            db.expire('accessToken',settingsWeiXin.Settings.accessTokenExpireTime-200) #-200 for safe reasion
            return newToken
    @classmethod
    def updateAccessTokenAndUpdateTime(cls):
        pass
    @classmethod
    def requestAccessToken(cls): 
        #if success return {'status':'success','accessToken':%s} and raise exception
        #if error return {'status':'error'}
        try:
            buffer=StringIO()
            c=pycurl.Curl()
            c.setopt(pycurl.URL, cls.requestUrl)
            c.setopt(pycurl.WRITEDATA,buffer)
            c.perform()
            c.close()
        except Exception:
            raise Exception('error in requestAccessToken')
            return {'status':'error'}
        htmlStr=buffer.getvalue()
        htmlJson=json.loads(htmlStr)
        return {'status':'success','accessToken':htmlJson['access_token']}