from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# def Home(request):
#     return HttpResponse('<h1>Hello World!!</h1> <br> <p>by Wintech</p>')
    
def Home(request):
    return render(request, 'company/home.html')