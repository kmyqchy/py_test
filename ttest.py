#Filename:ttest.py
# coding=utf-8

from urllib import request,parse
#import re
#import http

'''
a='adfwqepzz,msfkwew123dfws35%^*'
print(a)
print(re.match('www', 'www.runoob.com').span()) 
b=re.search('sf',a).span()
print(b)
'''
class conrequest:
    def __init__(self,url):
        self.url=url       
    #这是注释
    def con(self):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0;WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
        
        #进行请求，吧request对象传入urlopen参数中
        requests = request.Request(self.url,headers=headers)
        response = request.urlopen(requests)
        print(response.read().decode('utf-8'))
        
        print(response.status)
        
        print(response.getheaders())
        
        for k,v in response.getheaders():
            print(k,'=',v)
    def login(self):
        data = {'source':'None','redir':self.url,'form_email':'user','form_password':'passwd',''}
'''X=conrequest('https://www.google.com')
X.con()
'''
    



