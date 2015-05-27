from settingsWeiXin import Settings
import urllib,urllib2,time,hashlib  
class ValidWeiXin(object):  #valid the income message when received
    @classmethod
    def isRequestIsValid(cls,request):
        token=Settings.weixin_token
        signature = request.REQUEST.get('signature', '')
        timestamp = request.REQUEST.get('timestamp', '')
        nonce = request.REQUEST.get('nonce',  '')
        tmp_str = hashlib.sha1(''.join(sorted([token, timestamp, nonce]))).hexdigest()
        if tmp_str == signature:
            return True 
        return False