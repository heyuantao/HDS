#-*-coding:utf-8-*-
from django.http.response import HttpResponseRedirect,HttpResponse
def is_superuser(fun):
    def wrapped(self,request,*args,**kwargs):
        if request.user.is_authenticated() and request.user.is_superuser:
            print "success"
            return fun(self,request,*args,**kwargs)
        else:
            print "no login"
            return HttpResponseRedirect('/management/login/')
    return wrapped