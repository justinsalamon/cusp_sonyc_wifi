from django.shortcuts import render
from django.http import HttpResponse
from ingestion.models import WifiScan
import simplejson as json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == 'POST':
        print request.body
        populate(request.body)
    # return HttpResponse("ingestion says hello!")


def populate(info):
  #f = open('C:\Users\Nick\Documents\sonyc_wifi\server\sonyc_ingestion_project\b.txt', 'r')
  #j = f.read()
  #f.close()
  #scan = json.loads(f.read())

  scan = json.loads(info)

  #len(scan[mainkey])
  list_results = []
  for mainkey in scan:
      for i in range(0, len(scan[mainkey])):
          single = []
          for key in scan[mainkey][i]:
              if isinstance(scan[mainkey][i][key],list):
                  readings = []
                  for j in range(0,len(scan[mainkey][i][key])):
                      items = []
                      for readkey in scan[mainkey][i][key][j]:
                          items.append((readkey,scan[mainkey][i][key][j][readkey]))
                          #print readkey, scan[mainkey][i][key][j][readkey]
                      readings.append(items)
              else:
                  single.append((key, scan[mainkey][i][key]))
                  #print key, scan[mainkey][i][key]
          final = []
          for k in range(0, len(readings)):
              #subfinal = []
              subfinal = {}
              for tup in readings[k]:
                  a = tup[0]
                  b = tup[1]
                  if isinstance(tup[0], unicode):
                      a = str(tup[0]).lower()
                  if isinstance(tup[1], unicode):
                      b = str(tup[1]).lower()
                  subfinal[a] = b
                  #subfinal.append((tup[0], tup[1]))
                  #print str(tup[0]) + ": " + str(tup[1])
              for tup2 in single:
                  a = tup2[0]
                  b = tup2[1]
                  if isinstance(tup2[0], unicode):
                      a = str(tup2[0])
                  if isinstance(tup2[1], unicode):
                      b = str(tup2[1])
                  subfinal[a] = b
                  #subfinal.append((tup2[0],tup2[1]))
                  #print str(tup2[0]) + ": " + str(tup2[1])
              final.append(subfinal)
          for ap in final:
              list_results.append(WifiScan(**ap))

  WifiScan.objects.bulk_create(list_results)
  return 1