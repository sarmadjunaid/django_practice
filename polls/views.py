from django.shortcuts import get_object_or_404, render

from .models import Question

# first view function that returns and HTTP Response 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }    
    return render(request, 'polls/index.html', context)

# displays the detail of a question
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", { 'question': question })

# displays the result of the question
def results(request, question_id):
    response = "You're looking at the result of question %s"
    return HttpResponse(response % question_id)

# lets you vote on the question 
def vote(request, question_id):
    return HttpResponse("You're voting on the question %s" % question_id)

