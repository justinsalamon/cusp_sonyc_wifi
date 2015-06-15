from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ingestion.models import WifiScan
import simplejson as json
import datetime
import time

col_name = {'idx':1, 'lat':1, 'lng':1, 'acc':1, 'altitude':1, 'time':1, 'device_mac':1, 'app_version':1, 'droid_version':1, 'device_model':1, 'ssid':1, 'bssid':1, 'caps':1, 'level':1, 'freq':1}

def index(request):

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
    q_colname = request.GET.get('columns', '')
    
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
        if (q_enddate != ''):
            try:
                mth, day, year = q_enddate.split('/',2)
                dt = datetime.date(int(year), int(mth), int(day))
                t_stamp = time.mktime(dt.timetuple()) * 1000
                query_set = query_set.filter(time__lt=t_stamp)
            except:
                pass
        if (q_dev_mac != ''):
            query_set = query_set.filter(device_mac=q_dev_mac)
        if(q_app_v != ''):
            query_set = query_set.filter(app_version=q_app_v)
        if (q_dro_v != ''):
            query_set = query_set.filter(droid_version=q_dro_v)
        if (q_dev_m != ''):
            query_set = query_set.filter(device_model=q_dev_m)
        if (q_ssid != ''):
            try:
                list_ssid = q_ssid.split('|')
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
        human_readable = 0
        q_timeformat = request.GET.get('timeformat', '')
        try:
            human_readable = int(q_timeformat)
        except:
            pass
        
        is_distinct = 0
        q_distinct = request.GET.get('distinct', '')
        try:
            is_distinct = int(q_distinct)
        except:
            pass
        
        tem=[]
        list_name=[]
        if (q_colname == ''):
            if (is_distinct == 1):
                tem=query_set.values().distinct()
            else:
                tem=query_set.values()
        else:
            list_name = q_colname.split('|')
            args = []
            for name in list_name:
                if name in col_name:
                    args.append(name)
            if (is_distinct == 1):
                tem=query_set.values(*args).distinct()
            else:
                tem=query_set.values(*args)
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if (is_full_size == False):
            tem = tem[idx_start:idx_end]
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        key = 'time'
        if (q_colname == '' or key in list_name):
            if (human_readable == 1):
                for item in tem:
                    item[key]=(datetime.datetime.fromtimestamp(item[key]/1000)).strftime('%m-%d-%Y %H:%M:%S')
            elif(human_readable == 2):
                for item in tem:
                    item['time2']=(datetime.datetime.fromtimestamp(item[key]/1000)).strftime('%m-%d-%Y %H:%M:%S')

        response_data = list(tem)
            
            
    return HttpResponse(json.dumps(response_data), content_type="application/json")

