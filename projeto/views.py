from django.shortcuts import render
from django.http import HttpResponse

def ona_view(request):
    return HttpResponse("Padrão Ona 1")

def index_view(request):
    return render(request, 'template/home.html')

