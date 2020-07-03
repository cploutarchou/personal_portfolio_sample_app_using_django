import datetime

from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "default_template/index.html", {
        'current_year': datetime.datetime.now(),
    })


def category(request):
    return render(request, "default_template/category.html", {
        'current_year': datetime.datetime.now(),
    })


def single(request):
    return render(request, "default_template/single.html", {
        'current_year': datetime.datetime.now(),
    })


def about(request):
    return render(request, "default_template/about.html", {
        'current_year': datetime.datetime.now(),
    })
