from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

def index(request):
    """
    URL: /polls/
    Uses: polls/templates/index.html
    """
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)

def detail(request, question_id):
    """
    URL: /polls/<id>/
    Uses: polls/templates/detail.html
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", {"question": question})

def hello_view(request):
    """
    URL: /polls/hello/
    Uses: polls/templates/hello.html
    """
    return render(request, 'hello.html')

def calc_view(request):
    """
    URL: /polls/calc/
    Uses: polls/templates/calc.html
    """
    result = None
    if request.method == "POST":
        val1 = int(request.POST.get('num1', 0))
        val2 = int(request.POST.get('num2', 0))
        result = val1 + val2
    
    return render(request, 'calc.html', {'result': result})

def results(request, question_id):
    """URL: /polls/<id>/results/"""
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """URL: /polls/<id>/vote/"""
    return HttpResponse("You're voting on question %s." % question_id)
