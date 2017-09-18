
from django.shortcuts import render
import datetime

def homepage(request):
    return render(request, 'home.html')

def current_datetime(request):
    time_now = datetime.datetime.now()
    return render(request, 'date_time.html', {'time_now': time_now})
