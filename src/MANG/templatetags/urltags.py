#coding=utf-8
from django import template
register = template.Library()

@register.filter(name='urlPart') # freach the ith of url str, split with slash
def urlPart(value,arg):
    strArry=value.split('/')
    return strArry[int(arg)]