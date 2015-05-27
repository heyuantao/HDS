#this file can be delete 
from django.utils.encoding import smart_str, smart_unicode
import xml.etree.ElementTree as Etree  
if __name__=="__main__":
    org='<xml><ToUserName><![CDATA[gh_7537b2d3ec4e]]></ToUserName>\
        <FromUserName><![CDATA[oyL4wt5FSgJ9Q2dvOErRv5_F6GzE]]></FromUserName>\
        <CreateTime>1427009853</CreateTime>\
        <MsgType><![CDATA[text]]></MsgType>\
        <Content><![CDATA[Ggg]]></Content>\
        <MsgId>6128960649910558188</MsgId>\
        </xml>'
    xmlstr=smart_str(org)
    xml = Etree.fromstring(xmlstr)
    print xml.find('FromUserName').text
    print xml.find('CreateTime').text
    print xml.find('MsgId').text
    #a=PassiveMessage('123','456')
    #test=a.responeWithText("hello")
    '''
    while True:
        result=basicWeiXinInterface.BasicInterface.getAccessToken()
        time.sleep(1)
        print result
    '''