# coding=utf-8
#from numpy import xrange

      body={
         "reportRequests":
          [
            {
              "viewId": PC_ALL,#id
              "dateRanges":#日期
              [{"startDate": startdate,
                  "endDate": enddate}],
              "metrics":#指标
              [{"expression": "ga:users"}],
              "dimensions":#维度
              [{"name": "ga:segment"},#有无细分
               {"name": "ga:eventAction"}],
              "dimensionFilterClauses": #过滤器
              [{"filters": #过滤器
              [{"dimensionName": "ga:eventAction",#过滤维度
              "operator": "EXACT",#方式
              "expressions": ["Register - Other"]#值
              }]
              }],"segments": #细分
              [{"segmentId": "gaid::g57Gjow1TMioHexefYLKmA"}]
            }
          ]

      }
      
            body={
         "reportRequests":
          [
            {
              "viewId": M_ALL,
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
              "expressions": ["Register - Login"]
              }]
          }]
            }
          ]

      }