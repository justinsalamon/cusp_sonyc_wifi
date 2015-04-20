from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ingestion.models import WifiScan
import json
import datetime
import time
def index(request):
#     return HttpResponse("Hello. This is a test.")

#     scan_list = WifiScan.objects.filter(ssid='nyu').values()
    batch = 10 #default
    offset = 0 #default
    b_size = request.GET.get('batch', '')
    off_size = request.GET.get('offset', '')
    if (b_size != ''):
        try:
            batch = int(b_size)
        except:
            pass
    if (off_size != ''):
        try:
            offset = int(off_size)
        except:
            pass    
    idx_start = offset
    idx_end = offset + batch
    is_full_size = True if (b_size==''and off_size=='') else False
    
    q_idx = request.GET.get('idx', '')
    q_lat = request.GET.get('lat', '')
    q_lng = request.GET.get('lng', '')
    q_radius = request.GET.get('radius', '')
    q_acc = request.GET.get('acc', '')
    q_alt = request.GET.get('altitude', '')
    q_startdate = request.GET.get('startdate', '')
    q_enddate = request.GET.get('enddate', '')
    q_dev_mac = request.GET.get('device_mac', '')
    q_app_v = request.GET.get('app_version', '')
    q_dro_v = request.GET.get('droid_version', '')
    q_dev_m = request.GET.get('device_model', '')
    q_ssid = request.GET.get('ssid', '')
    q_bssid = request.GET.get('bssid', '')
    q_caps = request.GET.get('caps', '')
    q_lvl = request.GET.get('level', '')
    q_frq = request.GET.get('freq', '')
    
    query_set = None
    try:
        query_set = WifiScan.objects.all()
    except:
        pass
    
    response_data = []
    if (query_set != None):
        if (q_idx != ''): # int
            try:
                query_set = query_set.filter(idx=q_idx)
            except:
                pass
        if (q_acc != ''): #float
            try:
                query_set = query_set.filter(acc__gte=q_acc)
            except:
                pass
        if (q_alt != ''): #double
            try:
                query_set = query_set.filter(altitude__gte=q_alt)
            except:
                pass
        if (q_startdate != ''):
            try:
                mth, day, year = q_startdate.split('/',2)
                dt = datetime.date(int(year), int(mth), int(day))
                t_stamp = time.mktime(dt.timetuple()) * 1000
                query_set = query_set.filter(time__gte=t_stamp)
            except:
                pass
        if(q_ssid != ''):
            try:
                list_ssid = q_ssid.split('/')
                multi_ssid = ''
                for id in list_ssid:
                    if (id != ''):
                        multi_ssid += "ssid="+"\'" + id + "\'" + " OR "
                query_set = query_set.extra(where=[multi_ssid[:-4]])
            except:
                pass
        if (q_bssid != ''):
            query_set = query_set.filter(bssid=q_bssid)
        if(q_caps != ''):
            query_set = query_set.filter(caps__contains=q_caps)
        if (q_lvl != ''):
            try:
                query_set = query_set.filter(level__gte=q_lvl)
            except:
                pass
        if (q_frq != ''):
            try:
                query_set = query_set.filter(freq=q_frq)
            except:
                pass
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if (is_full_size == False):
            query_set = query_set[idx_start:idx_end]
         
        for record in query_set:
            data = {}
            data['idx']=record.idx
            data['lat']=record.lat
            data['lng']=record.lng
            data['acc']=record.acc
            data['altitude']=record.altitude      
            data['time']=(datetime.datetime.fromtimestamp(record.time/1000)).strftime('%m-%d-%Y %H:%M:%S')
            data['device_mac']=record.device_mac
            data['app_version']=record.app_version
            data['droid_version']=record.droid_version
            data['device_model']=record.device_model
            data['ssid']=record.ssid
            data['bssid']=record.bssid
            data['caps']=record.caps
            data['level']=record.level
            data['freq']=record.freq
     
            response_data.append(data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")
#     return HttpResponse(scan_list)#, mimetype='application/json')
#     return HttpResponse(scan_list)
