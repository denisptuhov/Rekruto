from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello {name}! {message}!".format(name=request.GET.get('name',''),
                                                          message=request.GET.get('message','')))
