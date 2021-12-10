# # Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    task = Task.objects.all()

    context= {'tasks':task}
    return render(request,"list.html",context)