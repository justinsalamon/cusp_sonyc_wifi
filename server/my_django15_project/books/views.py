from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from books.models import Books
from django.template import Context, loader

import json


response_data = []
# response_data['result'] = 'keep up'
# response_data['message'] = 'You messed up'

tlt = ''
auth = ''
def index(request):
    response_data = []
#     return HttpResponse(json.dumps(response_data), content_type="application/json")
    
#     return HttpResponse("Hello. This is a test.")
    tlt = request.GET.get('title', '')
    auth = request.GET.get('author', '')
#     tlt = request.GET['title']
#     books_list = Books.objects.all()
    
#     t_name = tlt
    if (tlt == '' and auth == ''):
        books_list = Books.objects.all()
    elif (tlt != '' and auth == ''):
        books_list = Books.objects.filter(title=tlt)
    elif (tlt == '' and auth != ''):
        books_list = Books.objects.filter(author=auth)
    elif (tlt != '' and auth != ''):
        books_list = Books.objects.filter(title=tlt,author=auth)
#     books_list = Books.objects.filter(title=tlt,author=auth)
#     books_list = Books.objects.all()   

    for p in books_list:
        data = {}
        data['title'] = str(p.title)
        data['author']=str(p.author)
        data['read']=str(p.read)
#         data['parm']=tlt
        response_data.append(data)

    return HttpResponse(json.dumps(response_data), content_type="application/json")
#     return HttpResponse(json.serialize(books_list, content_type="application/json")
    