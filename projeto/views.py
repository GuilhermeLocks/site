from django.shortcuts import render
from django.http import HttpResponse

def ona_view(request):
    return render(request, 'template/ona.html')

def index_view(request):
    #return HttpResponse("Padrão Ona 2")
    return render(request, 'ona.html')

