from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def indexad(request):
    return render(request,'administrador/index.html')