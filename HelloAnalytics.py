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

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
DISCOVERY_URI = ('https://analyticsreporting.googleapis.com/$discovery/rest')
CLIENT_SECRETS_PATH = 'c:\\client_secrets.json'
# Path to client_secrets.json file.
VIEW_ID = '125411210'
M_ALL = '124911265'
PC_ALL= '125394249'
M_US = '125501241'
PC_US = '122769400'
M_FR = '125474948'
PC_FR = '124898271'
MPWES = '174280939'
MES = '125492845'

def get_report(analytics,startdate,enddate):
    
# Use the Analytics Service Object to query the Analytics Reporting API V4.

 return analytics.reports().batchGet(
      body={
         "reportRequests":
          [
            {
              "viewId": M_US,
              "dateRanges":
              [{"startDate": startdate,
                  "endDate": enddate}],
              "metrics":
              [{"expression": "ga:transactions"
                }],
              "dimensions":
              [{"name": "ga:eventAction"}],
              "dimensionFilterClauses": [{
              "filters": [{"dimensionName": "ga:eventAction",
              "expressions": ["Register - Other"]
              }]
          }]
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

    for row in rows:
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])
      
      #for header, dimension in zip(dimensionHeaders, dimensions):
         # print (header + ',' + dimension)

      for i, values in enumerate(dateRangeValues):
        #print ('Date range (' + str(i) + ')')
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          print (value)
          #print (metricHeader.get('name') +'\t'+ value)
          
    #return header,dimension,metricHeader.get('name'),value
    return metricHeader.get('name'),value

def antianshuchu():
    i=datetime.datetime(2018, 7, 30)
    a=datetime.datetime(2018, 8, 26)+datetime.timedelta(days =+1)
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
    print('enddate:'+i.strftime('%Y-%m-%d'))    
def buantian():
    startdate=datetime.datetime(2018, 7, 30)
    enddate=datetime.datetime(2018, 7, 30)
    analytics = initialize_analyticsreporting()
    response = get_report(analytics,startdate.strftime('%Y-%m-%d'),enddate.strftime('%Y-%m-%d'))
    print_response(response)

def main():
    antianshuchu()
    #buantian()
if __name__ == '__main__':
  main()
