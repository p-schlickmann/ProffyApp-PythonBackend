from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "server/index.html")


def study(request):
    return render(request, "server/study.html")


def teach(request):
    return render(request, "server/give-classes.html")
