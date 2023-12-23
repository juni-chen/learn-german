from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
import random


# Create your views here.



def quiz_index_template(request):
    return render(request, 'wordquiz/quiz_index.html')
