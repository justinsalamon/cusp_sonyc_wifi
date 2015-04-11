import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sonyc_ingestion_project.settings')

import django
django.setup()

try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

from ingestion.models import WifiScan
import simplejson as json
def populate():
  f = open('b.txt', 'r')
  j = f.read()
  f.close()
  #scan = json.loads(f.read())

  scan = json.loads(j)

  #len(scan[mainkey])
  list_results = []
  for mainkey in scan:
      for i in range(0, 1):
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

if __name__ == '__main__':
  print "starting ingestion!"
  populate()
