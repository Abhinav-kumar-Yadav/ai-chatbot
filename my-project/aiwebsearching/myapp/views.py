from django.http import HttpResponse

# Create your views here.


def signup(request):
    return HttpResponse("Signup view")


def login(request):
    return HttpResponse("Login view")


def chat(request):
    return HttpResponse("Chat view")
