from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
from django.shortcuts import render

def hello_view(request):
    return render(request, 'hello.html')

from django.shortcuts import render

def calc_view(request):
    result = None
    if request.method == "POST":
      
        val1 = int(request.POST.get('num1', 0))
        val2 = int(request.POST.get('num2', 0))
        result = val1 + val2
    
    return render(request, 'calc.html', {'result': result})



