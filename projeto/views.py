from django.http import HttpResponse

def ona_view(request):
    return HttpResponse("Padrão Ona")

def index_view(request):
    return HttpResponse('Padrão Ona')