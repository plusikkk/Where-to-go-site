from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'mainapp/main.html')

def listpage(request):
    return HttpResponse("hello from list page")