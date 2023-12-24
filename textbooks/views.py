from django.shortcuts import render

# Create your views here.

def index_template(request):

    return render(request, 'textbooks/index.html')