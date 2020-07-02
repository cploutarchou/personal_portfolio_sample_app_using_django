import datetime

from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    return render(request, "default_template/index.html", {
        'current_year': datetime.datetime.now(),
    })


def category(request):
    return render(request, "default_template/category.html", {
        'current_year': datetime.datetime.now(),
    })
