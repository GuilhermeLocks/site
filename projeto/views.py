from django.shortcuts import render
from django.http import HttpResponse

def ona_view(request):
    return render(request, 'ona.html')

def ona2_view(request):
    return render(request, 'ona2.html')

def index_view(request):
    return render(request, 'index.html')

