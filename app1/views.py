from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def homepage(req):
    return render(req,'home.html')
def firstpage(req):
    return render(req,'first.html')