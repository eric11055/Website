from django.shortcuts import render
import os
# Create your views here.
def home(request):
    return render(request,'base/website.html')

def page2(request):
    return render(request,'base/website2.html')