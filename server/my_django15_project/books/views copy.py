from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from books.models import Books
from django.template import Context, loader

import json

response_data = []
# response_data['result'] = 'keep up'
# response_data['message'] = 'You messed up'


def index(request):
#     return HttpResponse(json.dumps(response_data), content_type="application/json")
    
#     return HttpResponse("Hello. This is a test.")

    books_list = Books.objects.all()

    for p in books_list:
        data = {}
        data['title'] = str(p.title)
        data['author']=str(p.author)
        data['read']=str(p.read)
        response_data.append(data)


    return HttpResponse(json.dumps(response_data), content_type="application/json")
    
#     
#     books_list = Books.objects.all()
#     t = loader.get_template('books/index.html')
#     c = Context({'books_list': books_list,})
#     return HttpResponse(t.render(c))

#     context_dict = {'boldmessage': "I am bold font from the context"}
#     return render(request, 'books/index.html', context_dict)