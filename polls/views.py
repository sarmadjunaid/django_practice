from django.http import HttpResponse

# first view function that returns and HTTP Response 
def index(request):
    return HttpResponse('Hello world, your at the polls index.')