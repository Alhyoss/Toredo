from django.shortcuts import render
from datetime import datetime

# Create your views here.

def date(request):
    return render(request, 'tests/date.html', {'date': datetime.now()})

def add(request, n1, n2):
    total = n1 + n2;
    return render(request, 'tests/add.html', locals())

def sub(request, n1, n2):
    total = n1-n2
    return render(request, 'tests/sub.html', { 'sub': total })