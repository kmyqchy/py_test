#Filename:ttest.py
# coding=utf-8
import datetime
''''j=time("2018-07-30")
i=time.strftime("2018-07-30", time.localtime())
a="2018-08-26"
print(j) 
while i==a :
    i=i+86400
    print(i)
#i=(datetime.datetime.now() + datetime.timedelta(days=+1)).strftime('%Y-%m-%d')
'''
def main():
    i=datetime.datetime(2018, 7, 30)
    a=datetime.datetime(2018, 8, 26) 
    while i!=a :
        j=i+datetime.timedelta(days =+1) 
        
        print(j.strftime('%Y-%m-%d'))
              
main()