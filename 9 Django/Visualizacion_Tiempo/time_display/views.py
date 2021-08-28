from django.shortcuts import render, HttpResponse
from time import gmtime, localtime, strftime
import datetime

# Create your views here.

def index(request):
    
    context = {
        "date": strftime("%Y-%m-%d", gmtime()),
        "time": strftime("%H:%M %p", gmtime()),
        "date2": strftime("%a, %d %b %Y", localtime()),
        "time2": strftime("%H:%M:%S %p", localtime()),
        #"datetime":datetime.datetime.now(),
    }
    return render(request,"index.html",context)
