from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'mainapp/main.html')

def listpage(request):
    return render(request, 'mainapp/listpage.html')

def addplace(request):
    return render(request, 'mainapp/addplace.html')