from django.shortcuts import render
from django.http import HttpResponse

def index(request,id ,nickname):
    result = str(id) + ':' + nickname
    return HttpResponse(result)