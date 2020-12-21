from django.shortcuts import render
from .models import *


def index(request):
    main_menu = Menu.objects.all()
    context = {
        "main_menu_items": main_menu
    }
    return render(request, 'default/base.html', context)


def posts(request):
    return render(request, 'default/posts.html', {})


def post(request, pk):
    _post = Posts.objects.get(pk=pk)
    context = {
        "post": _post
    }
    return render(request, 'default/post.html', context)
