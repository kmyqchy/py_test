"""Hello Analytics Reporting API V4."""
# -- coding: utf-8 --
import argparse
import datetime
from apiclient.discovery import build
import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools
from _datetime import date
from wsgiref import headers


SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
DISCOVERY_URI = ('https://analyticsreporting.googleapis.com/$discovery/rest')
CLIENT_SECRETS_PATH = 'c:\\client_secrets.json'
# Path to client_secrets.json file.
VIEW_ID = '125411210'
M_ALL = '124911265'
PC_ALL= '125394249'
M_US = '125501241'
PC_US = '122769400'
PC_UK = '136745014'
M_FR = '125474948'
PC_FR = '124898271'
PW_ES = '174280939'
M_ES = '125492845'
TANC = 'gaid::7RC_e4cnRuyhTrTJRBopXg' #弹窗注册
ZHENGC = 'gaid::6GlytQQvTB6VP1Qw7OgcvQ' #正常注册
GOUM = 'gaid::aHA4Dhz8TjW97dcSk7-eNA' #购买中注册
QIT = 'gaid::g57Gjow1TMioHexefYLKmA' #其他注册
GGS = 'gaid::jUgegKH6SR-1PGu9w7GESQ'#谷歌登陆
FBS = 'gaid::_T7Ut9X7SF-XJgBKj4Xfjw' #fb登陆
shuruci = 'gaid::cU_XCtnWSpenNUYD87MR0g' #输入词
resouci = 'gaid::XWaZvGZTQ_yodARgHMkZJQ' #热搜词
lishisousuoci = 'gaid::OaHR1qFYTdS9XZREDdKHeA' #历史搜索词
lianxiangci = 'gaid::3nmSsA_AS7yrdQlnHDwHFQ'#联想词
morenci = 'gaid::lp8skz-RTzWANDjZOfL7PQ' #默认词
antc = 'gaid::QtfKkXmZSyCbkYkXgK9HeQ'
anzc = 'gaid::0KlYjHNjQle-t4Khm3928w'
anot = 'gaid::-aK4C58IRt6r6iD2Qd71RA'
angm = 'gaid::LOE7dvecSHKZlKdDIWXoxw'
ango = 'gaid::ZlbfQj5FS26aKFzD1Ovbjw'
anfb = 'gaid::aKXOLA9TTaSE-nyRvpXAPg'

def get_report(analytics,startdate,enddate):
    
# Use the Analytics Service Object to query the Analytics Reporting API V4.

 return analytics.reports().batchGet(
      body={
         "reportRequests":
          [
            {
              "viewId": M_ES,#id
              "dateRanges":#日期
              [{"startDate": startdate,
                  "endDate": enddate}],
              "metrics":#指标
              [{"expression": "ga:users"}],
              "dimensions":#维度
              [{"name": "ga:segment"},#有无细分
               {"name": "ga:date"}],
              
             "segments": #细分
              [{"segmentId": FBS}]
            }
          ]

      }
  ).execute()  

def initialize_analyticsreporting():

# Parse command-line arguments.
  parser = argparse.ArgumentParser(
      formatter_class=argparse.RawDescriptionHelpFormatter,
      parents=[tools.argparser])
  flags = parser.parse_args([])

# Set up a Flow object to be used if we need to authenticate.
  flow = client.flow_from_clientsecrets(
      CLIENT_SECRETS_PATH, scope=SCOPES,
      message=tools.message_if_missing(CLIENT_SECRETS_PATH))

# Prepare credentials, and authorize HTTP object with them.
# If the credentials don't exist or are invalid run through the native client
# flow. The Storage object will ensure that if successful the good
# credentials will get written back to a file.
  storage = file.Storage('analyticsreporting.dat')
  credentials = storage.get()
  if credentials is None or credentials.invalid:
    credentials = tools.run_flow(flow, storage, flags)
  http = credentials.authorize(http=httplib2.Http())

# Build the service object.
  analytics = build('analytics', 'v4', http=http, discoveryServiceUrl=DISCOVERY_URI)

  return analytics


def print_response(response):
  """Parses and prints the Analytics Reporting API V4 response"""

  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    rows = report.get('data', {}).get('rows', [])
    #print(rows)
    
    for row in rows:       
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])
      #print(row)

      headers = []
      for header, dimension in zip(dimensionHeaders, dimensions):
         headers.append(header)
         
      #print ('数组：'+headers[1]) 

      for i, values in enumerate(dateRangeValues):
        #print ('Date range (' + str(i) + ')')
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          #print (value)
             print (metricHeader.get('name') +'\t'+ value)
          
   
          
    return headers,dimension,metricHeader.get('name'),value
   # return metricHeader.get('name'),value


def antianshuchu():
    i=datetime.datetime(2018, 8, 26)
    a=datetime.datetime(2018, 9, 5)+datetime.timedelta(days =+1)
    j=i
    print('startdate:'+i.strftime('%Y-%m-%d'))
    
    while i!=a :
        startdate=j
        enddate=j
        analytics = initialize_analyticsreporting()
        response = get_report(analytics,startdate.strftime('%Y-%m-%d'),enddate.strftime('%Y-%m-%d'))
        j=i+datetime.timedelta(days =+1) 
        i=j
        #print(j)
        print_response(response)
    print('enddate:'+(i+datetime.timedelta(days =-1)).strftime('%Y-%m-%d'))    

def buantian():
    startdate=datetime.datetime(2018, 8, 30)
    enddate=datetime.datetime(2018, 9, 5)
    analytics = initialize_analyticsreporting()
    response = get_report(analytics,startdate.strftime('%Y-%m-%d'),enddate.strftime('%Y-%m-%d'))
    print_response(response)
    

def main():
    #antianshuchu()
    buantian()
if __name__ == '__main__':
  main()
