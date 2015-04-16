from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ingestion.models import WifiScan
import json
import datetime
def index(request):
#     return HttpResponse("Hello. This is a test.")

#     scan_list = WifiScan.objects.filter(ssid='nyu').values()
    ss_id = request.GET.get('ssid', '')
    if (ss_id == ''):
        scan_dict = WifiScan.objects.all().values()
    else:
        scan_dict = WifiScan.objects.filter(ssid=ss_id).values()

        
    response_data = []
     
    i = 0
    for record in scan_dict:
        data = {}
        data['idx']=record['idx']
        data['lat']=record['lat']
        data['lng']=record['lng']
        data['acc']=record['acc']
        data['altitude']=record['altitude']       
        data['time']=(datetime.datetime.fromtimestamp(record['time']/1000)).strftime('%m-%d-%Y %H:%M:%S')
        data['device_mac']=record['device_mac']
        data['app_version']=record['app_version']
        data['droid_version']=record['droid_version']
        data['device_model']=record['device_model']
        data['ssid']=record['ssid']
        data['bssid']=record['bssid']
        data['caps']=record['caps']
        data['level']=record['level']
        data['freq']=record['freq']
 
#         i = 1 + i
#         if (i == 40000):
#             break
        response_data.append(data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")
#     return HttpResponse(scan_list)#, mimetype='application/json')
#     return HttpResponse(scan_list)
